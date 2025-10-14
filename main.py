import discord
from discord import app_commands
import json
import os
from discord.ext import commands
import asyncio
from keep_alive import keep_alive
from random import random
from operator import itemgetter
from discord.ui import View, Button
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import urllib.parse
import re


from config import *

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
keep_alive()
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

# Configuration is now imported from config.py
# You can edit ROLE_ODMENY, AUTA, CENY_ZBRANI, etc. in config.py
    # All configuration moved to config.py

# MongoDB connection setup
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set")

# Parse and properly encode MongoDB URI
def encode_mongo_uri(uri):
    """Properly encode username and password in MongoDB URI"""
    try:
        # Pattern to extract mongodb://username:password@host or mongodb+srv://username:password@host
        pattern = r'^(mongodb(?:\+srv)?://)([^:]+):([^@]+)@(.+)$'
        match = re.match(pattern, uri)

        if match:
            protocol, username, password, rest = match.groups()
            # URL encode username and password
            encoded_username = urllib.parse.quote_plus(username)
            encoded_password = urllib.parse.quote_plus(password)
            encoded_uri = f"{protocol}{encoded_username}:{encoded_password}@{rest}"
            print(f"🔧 Encoded MongoDB URI (username: {username}, host: {rest.split('?')[0].split('/')[0]})")
            return encoded_uri
        else:
            # If no credentials in URI, return as is
            print(f"⚠️ Could not parse MongoDB URI pattern, using as-is")
            return uri
    except Exception as e:
        print(f"Warning: Could not parse MongoDB URI: {e}")
        return uri

MONGO_URI_ENCODED = encode_mongo_uri(MONGO_URI)

try:
    client = MongoClient(MONGO_URI_ENCODED, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
    db = client["miamirpbot"]
    hraci = db["hraci"]
except Exception as e:
    print(f"❌ MongoDB connection error: {e}")
    print("Please ensure your MONGO_URI is properly formatted.")
    print("Format: mongodb+srv://username:password@cluster.mongodb.net/database")
    raise

def get_or_create_user(user_id):
    user_id = str(user_id)
    user = hraci.find_one({"_id": user_id})

    if not user:
        new_user = {
            "_id": user_id,
            "auta": {},
            "zbrane": {},
            "penize": 0,
            "hotovost": 0,
            "bank": 0,
            "last_collect": None,
            "collect_timestamps": {},
            "veci": {},
            "drogy": {} # Inicializace drog
        }
        hraci.insert_one(new_user)
        return new_user

    update_fields = {}

    # Doplnění chybějících polí
    for key, default in {
        "auta": {},
        "zbrane": {},
        "penize": 0,
        "hotovost": 0,
        "bank": 0,
        "veci": {},
        "collect_timestamps": {},
        "last_collect": None,
        "drogy": {} # Doplnění drog
    }.items():
        if key not in user:
            update_fields[key] = default
            user[key] = default

    # Konverze starých seznamů na dict
    if isinstance(user.get("auta"), list):
        auta_dict = {}
        for auto in user["auta"]:
            auta_dict[auto] = auta_dict.get(auto, 0) + 1
        update_fields["auta"] = auta_dict
        user["auta"] = auta_dict

    if isinstance(user.get("zbrane"), list):
        zbrane_dict = {}
        for zbran in user["zbrane"]:
            zbrane_dict[zbran] = zbrane_dict.get(zbran, 0) + 1
        update_fields["zbrane"] = zbrane_dict
        user["zbrane"] = zbrane_dict

    # Přepočítání peněz
    user["penize"] = user.get("hotovost", 0) + user.get("bank", 0)
    update_fields["penize"] = user["penize"]

    # Pokud byly změny, aktualizuj dokument v DB
    if update_fields:
        hraci.update_one({"_id": user_id}, {"$set": update_fields})

    return user
# 📦 Seznam věcí pro autocomplete (z cen)
VECI_SEZNAM = list(CENY_VECI.keys())

# 📋 Seznam drog (přizpůsob podle svých receptů)
DROGY_SEZNAM = ["Marihuana", "Kokain", "Metamfetamin", "Pervitin", "Extáze", "Heroin"]

# Autocomplete pro věci
async def autocomplete_veci(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=vec, value=vec)
        for vec in VECI_SEZNAM if current.lower() in vec.lower()
    ][:25]

# Autocomplete pro drogy
async def autocomplete_drogy(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=drug, value=drug)
        for drug in DROGY_SEZNAM if current.lower() in drug.lower()
    ][:25]

# Autocomplete pro věci a drogy dohromady (pro prodej-veci)
async def autocomplete_veci_drogy(interaction: discord.Interaction, current: str):
    user_data = get_or_create_user(interaction.user.id)
    veci = user_data.get("veci", {})
    drogy = user_data.get("drogy", {})

    # Kombinuj věci a drogy z inventáře uživatele
    dostupne_polozky = list(veci.keys()) + list(drogy.keys())

    return [
        app_commands.Choice(name=item, value=item)
        for item in dostupne_polozky if current.lower() in item.lower()
    ][:25]

async def log_action(bot, guild: discord.Guild, message: str):
    log_channel = guild.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(
            description=message,
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        embed.set_footer(text="Bot Action Log")
        await log_channel.send(embed=embed)


class ConfirmationView(discord.ui.View):
    def __init__(self, prodavajici, kupec, item, item_type, cena):
        super().__init__(timeout=60.0)
        self.prodavajici = prodavajici
        self.kupec = kupec
        self.item = item
        self.item_type = item_type
        self.cena = cena
        self.result = None

    @discord.ui.button(label='✅ Potvrdit nákup', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.kupec.id:
            await interaction.response.send_message("❌ Pouze kupující může potvrdit nákup.", ephemeral=True)
            return

        self.result = True
        self.stop()
        await interaction.response.edit_message(content=f"✅ {self.kupec.display_name} potvrdil nákup!", view=None)

    @discord.ui.button(label='❌ Zrušit', style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id not in [self.kupec.id, self.prodavajici.id]:
            await interaction.response.send_message("❌ Pouze kupující nebo prodávající může zrušit obchod.", ephemeral=True)
            return

        self.result = False
        self.stop()
        await interaction.response.edit_message(content=f"❌ Obchod byl zrušen.", view=None)

    async def on_timeout(self):
        self.result = False



def get_total_money(data):
    return data.get("hotovost", 0) + data.get("bank", 0)


# === PŘIPOJENÍ ===


@bot.event
async def on_ready():
    await tree.sync()
    print(f"✅ Bot je online jako {bot.user}")

# ===INVENTORY PŘÍKAZY ===

#pridej zbran command
@tree.command(name="pridej-zbran", description="Přidá zbraň hráči (admin)")
@app_commands.describe(uzivatel="Uživatel, kterému přidáš zbraň",
                           zbran="Zbraň, kterou chceš přidat",
                           pocet="Počet kusů")
async def pridej_zbran(interaction: discord.Interaction,
                           uzivatel: discord.Member,
                           zbran: str,
                           pocet: int = 1):
        if not any(role.id == ADMIN_ROLE_ID for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
            await log_action(bot, interaction.guild, f"❌ {interaction.user.mention} pokusil se použít /pridej-zbran bez oprávnění")
            return
        if zbran not in DOSTUPNE_ZBRANE:
            await interaction.response.send_message(
                f"❌ Zbraň `{zbran}` není v seznamu dostupných zbraní.",
                ephemeral=True)
            return
        data = get_or_create_user(uzivatel.id)
        if zbran in data["zbrane"]:
            data["zbrane"][zbran] += pocet
        else:
            data["zbrane"][zbran] = pocet
        hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})

        await interaction.response.send_message(
            f"✅ Přidáno {pocet}x `{zbran}` hráči {uzivatel.display_name}.")
        await log_action(bot, interaction.guild, f"{interaction.user.mention} přidal {pocet}x {zbran} hráči {uzivatel.mention}")




@pridej_zbran.autocomplete("zbran")
async def autocomplete_zbran_pridat(interaction: discord.Interaction,
                                        current: str):
        return [
            app_commands.Choice(name=z, value=z) for z in DOSTUPNE_ZBRANE
            if current.lower() in z.lower()
        ][:25]
#odeber zbran command
@tree.command(name="odeber-zbran", description="Odebere zbraň hráči (admin)")
@app_commands.describe(uzivatel="Uživatel, kterému odebereš zbraň",
                           zbran="Zbraň, kterou chceš odebrat",
                           pocet="Počet kusů")
async def odeber_zbran(interaction: discord.Interaction,
                           uzivatel: discord.Member,
                           zbran: str,
                           pocet: int = 1):
        if not any(role.id == ADMIN_ROLE_ID for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
            await log_action(bot, interaction.guild, f"❌ {interaction.user.mention} pokusil se použít /odeber-zbran bez oprávnění")
            return
        data = get_or_create_user(uzivatel.id)
        if zbran in data["zbrane"]:
            data["zbrane"][zbran] -= pocet
            if data["zbrane"][zbran] <= 0:
                del data["zbrane"][zbran]
            hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})

            await interaction.response.send_message(
                f"✅ Odebráno {pocet}x `{zbran}` hráči {uzivatel.display_name}."
            )
            await log_action(bot, interaction.guild, f"{interaction.user.mention} odebral {pocet}x {zbran} hráči {uzivatel.mention}")
        else:
            await interaction.response.send_message(
                f"❌ Zbraň `{zbran}` nebyla nalezena u {uzivatel.display_name}."
            )

@odeber_zbran.autocomplete("zbran")
async def autocomplete_zbran_odebrat(interaction: discord.Interaction,
                                         current: str):
        uzivatel = interaction.namespace.uzivatel
        if not uzivatel:
            return []
        data = get_or_create_user(uzivatel.id)
        return [
            app_commands.Choice(name=z, value=z) for z in data["zbrane"]
            if current.lower() in z.lower()
        ][:25]

    # Pridej auto command
@tree.command(name="pridej-auto", description="Přidá auto hráči (admin)")
@app_commands.describe(uzivatel="Uživatel, kterému přidáš auto",
                           auto="Auto, které chceš přidat",
                           pocet="Počet kusů")
async def pridej_auto(interaction: discord.Interaction,
                          uzivatel: discord.Member,
                          auto: str,
                          pocet: int = 1):
        if not any(role.id == ADMIN_ROLE_ID for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
            await log_action(bot, interaction.guild, f"❌ {interaction.user.mention} pokusil se použít /pridej-auto bez oprávnění")
            return
        if auto not in DOSTUPNA_AUTA:
            await interaction.response.send_message(
                f"❌ Auto `{auto}` není v seznamu dostupných aut.", ephemeral=True)
            return
        data = get_or_create_user(uzivatel.id)
        if auto in data["auta"]:
            data["auta"][auto] += pocet
        else:
            data["auta"][auto] = pocet
        hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})

        await interaction.response.send_message(
            f"✅ Přidáno {pocet}x `{auto}` hráči {uzivatel.display_name}.")
        await log_action(bot, interaction.guild, f"{interaction.user.mention} přidal {pocet}x {auto} hráči {uzivatel.mention}")

@pridej_auto.autocomplete("auto")
async def autocomplete_auto_pridat(interaction: discord.Interaction,
                                       current: str):
        return [
            app_commands.Choice(name=a, value=a) for a in DOSTUPNA_AUTA
            if current.lower() in a.lower()
        ][:25]

    # Odeber auto command
@tree.command(name="odeber-auto", description="Odebere auto hráči (admin)")
@app_commands.describe(uzivatel="Uživatel, kterému odebereš auto",
                           auto="Auto, které chceš odebrat",
                           pocet="Počet kusů")
async def odeber_auto(interaction: discord.Interaction,
                          uzivatel: discord.Member,
                          auto: str,
                          pocet: int = 1):
        if not any(role.id == ADMIN_ROLE_ID for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
            await log_action(bot, interaction.guild, f"❌ {interaction.user.mention} pokusil se použít /odeber-auto bez oprávnění")
            return
        data = get_or_create_user(uzivatel.id)
        if auto in data["auta"]:
            data["auta"][auto] -= pocet
            if data["auta"][auto] <= 0:
                del data["auta"][auto]
            hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})

            await interaction.response.send_message(
                f"✅ Odebráno {pocet}x `{auto}` hráči {uzivatel.display_name}.")
            await log_action(bot, interaction.guild, f"{interaction.user.mention} odebral {pocet}x {auto} hráči {uzivatel.mention}")
        else:
            await interaction.response.send_message(
                f"❌ Auto `{auto}` nebylo nalezeno u {uzivatel.display_name}.")

@odeber_auto.autocomplete("auto")
async def autocomplete_auto_odebrat(interaction: discord.Interaction,
                                        current: str):
        uzivatel = interaction.namespace.uzivatel
        if not uzivatel:
            return []
        data = get_or_create_user(uzivatel.id)
        return [
            app_commands.Choice(name=a, value=a) for a in data["auta"]
            if current.lower() in a.lower()
        ][:25]

    # Inventory command
@tree.command(name="inventory", description="Zobrazí inventář hráče")
@app_commands.describe(uzivatel="Uživatel, jehož inventář chceš zobrazit")
async def inventory(interaction: discord.Interaction, uzivatel: discord.Member = None):
        uzivatel = uzivatel or interaction.user
        data = get_or_create_user(uzivatel.id)

        auta = data.get("auta", {})
        zbrane = data.get("zbrane", {})
        veci = data.get("veci", {})
        drogy = data.get("drogy", {})

        auta_text = "\n".join(f"🚗 {auto} ×{pocet}" for auto, pocet in auta.items()) or "Žádná"
        zbrane_text = "\n".join(f"🔫 {zbran} ×{pocet}" for zbran, pocet in zbrane.items()) or "Žádné"
        veci_text = "\n".join(f"📦 {nazev} ×{pocet}" for nazev, pocet in veci.items()) or "Žádné"
        drogy_text = "\n".join(f"💊 {nazev} ×{gramy:.2f}g" for nazev, gramy in drogy.items()) # Formátování na 2 desetinná místa

        embed = discord.Embed(
            title=f"📋 Inventář uživatele {uzivatel.display_name}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Auta", value=auta_text, inline=False)
        embed.add_field(name="Zbraně", value=zbrane_text, inline=False)
        embed.add_field(name="Věci", value=veci_text, inline=False)

        if drogy:  # ✅ Přidá se pouze pokud nějaké drogy existují
            embed.add_field(name="Drogy", value=drogy_text, inline=False)

        await interaction.response.send_message(embed=embed)


# Reset inventory command
@tree.command(name="reset-inventory", description="Resetuje celý inventář hráče (admin)")
@app_commands.describe(uzivatel="Uživatel, jehož inventář chceš vymazat")
async def reset_inventory(interaction: discord.Interaction, uzivatel: discord.Member):
        if not any(role.id == ADMIN_ROLE_ID for role in interaction.user.roles):
            await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
            return
        data = get_or_create_user(uzivatel.id)
        data["auta"] = {}
        data["zbrane"] = {}
        data["veci"] = {}
        data["drogy"] = {}
        hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})

        await interaction.response.send_message(f"♻️ Inventář hráče {uzivatel.display_name} byl úspěšně resetován.")
        await log_action(bot, interaction.guild, f"{interaction.user.mention} resetoval inventář hráče {uzivatel.mention}")


# === PŘÍKAZY NA PENÍZE ===


# Balance command

@tree.command(name="balance", description="Zobrazí finanční stav")
@app_commands.describe(uzivatel="(Volitelné) Uživatel, jehož stav chceš zobrazit")
async def balance(interaction: discord.Interaction, uzivatel: discord.Member = None):
    uzivatel = uzivatel or interaction.user
    data = get_or_create_user(uzivatel.id)

    penize = data.get("penize", 0)
    hotovost = data.get("hotovost", 0)
    bank = data.get("bank", 0)

    embed = discord.Embed(
        title=f"💰 Finanční přehled pro {uzivatel.display_name}",
        color=discord.Color.gold()
    )
    embed.add_field(name="💵 Celkem", value=f"{penize:,} $", inline=False)
    embed.add_field(name="💳 Hotovost", value=f"{hotovost:,} $", inline=True)
    embed.add_field(name="🏦 Banka", value=f"{bank:,} $", inline=True)

    await interaction.response.send_message(embed=embed)

# Pridej penize command
@tree.command(name="pridej-penize", description="Přidá peníze hráči (admin)")
@app_commands.describe(uzivatel="Uživatel, kterému chceš přidat peníze", castka="Kolik peněz chceš přidat")
async def pridej_penize(interaction: discord.Interaction, uzivatel: discord.Member, castka: int):
    if not any(role.id == ADMIN_ROLE_ID for role in interaction.user.roles):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
        await log_action(bot, interaction.guild, f"❌ {interaction.user.mention} pokusil se použít /pridej-penize bez oprávnění")
        return
    data = get_or_create_user(uzivatel.id)
    data["hotovost"] += castka # Automatically adds to hotovost
    data["penize"] = data["hotovost"] + data["bank"]  # Update total money
    hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})

    await interaction.response.send_message(f"✅ Přidáno {castka}$ hráči {uzivatel.display_name}.")
    await log_action(bot, interaction.guild, f"{interaction.user.mention} přidal {castka}$ hráči {uzivatel.mention}")

# Odeber penize command
@tree.command(name="odeber-penize", description="Odebere peníze hráči (admin)")
@app_commands.describe(uzivatel="Uživatel, kterému chceš odebrat peníze", castka="Kolik peněz chceš odebrat (nebo 'all' pro všechny)")
async def odeber_penize(interaction: discord.Interaction, uzivatel: discord.Member, castka: str):
    if not any(role.id == ADMIN_ROLE_ID for role in interaction.user.roles):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
        await log_action(bot, interaction.guild, f"❌ {interaction.user.mention} pokusil se použít /odeber-penize bez oprávnění")
        return
    data = get_or_create_user(uzivatel.id)

    if castka.lower() == "all":
        actual_castka = data["hotovost"] + data["bank"]
        data["hotovost"] = 0
        data["bank"] = 0
    else:
        try:
            actual_castka = int(castka)
            if actual_castka <= 0:
                await interaction.response.send_message("❌ Částka musí být větší než 0.", ephemeral=True)
                return
        except ValueError:
            await interaction.response.send_message("❌ Neplatná částka. Použij číslo nebo 'all'.", ephemeral=True)
            return

        # Remove from hotovost first, then bank
        if data["hotovost"] >= actual_castka:
            data["hotovost"] -= actual_castka
        else:
            remaining = actual_castka - data["hotovost"]
            data["hotovost"] = 0
            data["bank"] -= remaining
            if data["bank"] < 0:
                data["bank"] = 0

    data["penize"] = data["hotovost"] + data["bank"]
    hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})

    await interaction.response.send_message(f"✅ Odebráno {actual_castka}$ hráči {uzivatel.display_name}.")
    await log_action(bot, interaction.guild, f"{interaction.user.mention} odebral {actual_castka}$ hráči {uzivatel.mention}")

# Reset penize command

@tree.command(name="reset-penize", description="Resetuje peníze hráče (admin)")
@app_commands.describe(uzivatel="Uživatel, jehož peníze chceš vynulovat")
async def reset_penize(interaction: discord.Interaction, uzivatel: discord.Member):
        if not any(role.id == ADMIN_ROLE_ID for role in interaction.user.roles):
            await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
            await log_action(bot, interaction.guild, f"❌ {interaction.user.mention} pokusil se použít /reset-penize bez oprávnění")
            return
        data = get_or_create_user(uzivatel.id)
        data["hotovost"] = 0
        data["bank"] = 0
        data["penize"] = 0
        hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})

        await interaction.response.send_message(f"♻️ Peníze hráče {uzivatel.display_name} byly vynulovány.")
        await log_action(bot, interaction.guild, f"{interaction.user.mention} resetoval peníze hráče {uzivatel.mention}")

# Pay command

@tree.command(name="pay", description="Pošle peníze jinému hráči")
@app_commands.describe(cil="Komu chceš poslat peníze", castka="Kolik peněz chceš poslat")
async def posli_penize(interaction: discord.Interaction, cil: discord.Member, castka: int):
    if castka <= 0:
        await interaction.response.send_message("❌ Částka musí být větší než 0.", ephemeral=True)
        return
    odesilatel_data = get_or_create_user(interaction.user.id)
    prijemce_data = get_or_create_user(cil.id)

    total_money_odesilatel = get_total_money(odesilatel_data)
    if total_money_odesilatel < castka:
        await interaction.response.send_message("❌ Nemáš dostatek peněz.", ephemeral=True)
        return

    # Remove money from sender (hotovost first, then bank)
    remaining_to_remove = castka
    if odesilatel_data["hotovost"] >= remaining_to_remove:
        odesilatel_data["hotovost"] -= remaining_to_remove
    else:
        remaining_to_remove -= odesilatel_data["hotovost"]
        odesilatel_data["hotovost"] = 0
        odesilatel_data["bank"] -= remaining_to_remove

    # Add money to receiver's hotovost
    prijemce_data["hotovost"] += castka

    # Update total money for both users
    odesilatel_data["penize"] = odesilatel_data["hotovost"] + odesilatel_data["bank"]
    prijemce_data["penize"] = prijemce_data["hotovost"] + prijemce_data["bank"]

    hraci.update_one({"_id": str(interaction.user.id)}, {"$set": odesilatel_data})
    hraci.update_one({"_id": str(cil.id)}, {"$set": prijemce_data})

    await interaction.response.send_message(f"💸 Poslal jsi {castka}$ hráči {cil.display_name}.")
    await log_action(bot, interaction.guild, f"{interaction.user.mention} poslal {castka}$ hráči {cil.mention}")
# Kup auto command

@tree.command(name="koupit-auto", description="Koupí auto, pokud máš dost peněz a případnou roli")
@app_commands.describe(auto="Auto, které chceš koupit")
async def koupit_auto(interaction: discord.Interaction, auto: str):
    user = interaction.user
    data = get_or_create_user(user.id)

    if auto not in AUTA:
        await interaction.response.send_message("❌ Takové auto neexistuje.", ephemeral=True)
        return

    info = AUTA[auto]
    cena = info["cena"]
    pozadovana_role = info["role"]

    # Check if specific role is required and user has it
    if pozadovana_role:
        required_role_ids = [int(role_id.strip()) for role_id in pozadovana_role.split("||")]
        user_role_ids = [role.id for role in user.roles]

        if not any(role_id in user_role_ids for role_id in required_role_ids):
            await interaction.response.send_message(
                f"❌ Toto auto vyžaduje specifickou roli.", ephemeral=True)
            return

    total_money = get_total_money(data)
    if total_money < cena:
        await interaction.response.send_message("❌ Nemáš dostatek peněz.", ephemeral=True)
        return

    # Remove money from user (hotovost first, then bank)
    remaining_to_remove = cena
    if data["hotovost"] >= remaining_to_remove:
        data["hotovost"] -= remaining_to_remove
    else:
        remaining_to_remove -= data["hotovost"]
        data["hotovost"] = 0
        data["bank"] -= remaining_to_remove

    # Add car to inventory
    if auto in data["auta"]:
        data["auta"][auto] += 1
    else:
        data["auta"][auto] = 1

    # Update total money
    data["penize"] = data["hotovost"] + data["bank"]
    hraci.update_one({"_id": str(user.id)}, {"$set": data})


    await interaction.response.send_message(
        f"✅ Úspěšně jsi koupil **{auto}** za **{cena:,} $**."
    )
    await log_action(bot, interaction.guild, f"{user.mention} koupil {auto} za {cena:,}$")

@koupit_auto.autocomplete("auto")
async def autocomplete_kup_auto(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=a, value=a)
        for a in AUTA.keys() if current.lower() in a.lower()
    ][:25]

# Kup zbran command

@tree.command(name="koupit-zbran", description="Koupit zbraň z nabídky")
@app_commands.describe(zbran="Zbraň, kterou chceš koupit", pocet="Počet kusů")
async def koupit_zbran(interaction: discord.Interaction, zbran: str, pocet: int = 1):
    role_id = 1293617188988784667  # Změň na ID role, která má povolený nákup zbraní
    if not any(role.id == role_id for role in interaction.user.roles):
        await interaction.response.send_message("❌ Nemáš oprávnění koupit zbraně.", ephemeral=True)
        return

    uzivatel = interaction.user
    data = get_or_create_user(uzivatel.id)

    if zbran not in CENY_ZBRANI:
        await interaction.response.send_message(f"❌ Zbraň `{zbran}` není v nabídce k prodeji.", ephemeral=True)
        return

    cena_za_kus = CENY_ZBRANI[zbran]
    celkova_cena = cena_za_kus * pocet

    total_money = get_total_money(data)
    if total_money < celkova_cena:
        await interaction.response.send_message(
            f"❌ Nemáš dostatek peněz ({total_money:,}$) na koupi {pocet}x `{zbran}` (potřebuješ {celkova_cena:,}$).",
            ephemeral=True
        )
        return
    # Remove money from buyer (hotovost first, then bank)
    remaining_to_remove = celkova_cena
    if data["hotovost"] >= remaining_to_remove:
        data["hotovost"] -= remaining_to_remove
    else:
        remaining_to_remove -= data["hotovost"]
        data["hotovost"] = 0
        data["bank"] -= remaining_to_remove

    data["penize"] = data["hotovost"] + data["bank"]

    # Přidej zbraň
    if zbran in data["zbrane"]:
        data["zbrane"][zbran] += pocet
    else:
        data["zbrane"][zbran] = pocet
    hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})


    await interaction.response.send_message(f"✅ Koupil jsi {pocet}x `{zbran}` za {celkova_cena:,}$. Zůstatek: {data['penize']:,}$.")
    await log_action(bot, interaction.guild, f"{uzivatel.mention} koupil {pocet}x {zbran} za {celkova_cena:,}$")

@koupit_zbran.autocomplete("zbran")
async def autocomplete_koupit_zbran(interaction: discord.Interaction, current: str):
    return [app_commands.Choice(name=z, value=z) for z in CENY_ZBRANI if current.lower() in z.lower()][:25]

@tree.command(name="prodej-auto", description="Prodá auto jinému hráči")
@app_commands.describe(kupec="Komu prodáváš auto", auto="Jaké auto prodáváš", cena="Cena za auto")
async def prodej_auto(interaction: discord.Interaction, kupec: discord.Member, auto: str, cena: int):
    prodavajici_data = get_or_create_user(interaction.user.id)
    kupec_data = get_or_create_user(kupec.id)

    if auto not in prodavajici_data["auta"]:
        await interaction.response.send_message("❌ Nemáš toto auto v inventáři.", ephemeral=True)
        return
    if prodavajici_data["auta"][auto] <= 0:
        await interaction.response.send_message("❌ Nemáš žádné kusy tohoto auta.", ephemeral=True)
        return
    total_money_kupec = get_total_money(kupec_data)
    if total_money_kupec < cena:
        await interaction.response.send_message("❌ Kupující nemá dostatek peněz.", ephemeral=True)
        return

    # Create confirmation view
    view = ConfirmationView(interaction.user, kupec, auto, "auto", cena)

    embed = discord.Embed(
        title="🚗 Potvrzení nákupu auta",
        description=f"**Prodávající:** {interaction.user.display_name}\n**Kupující:** {kupec.display_name}\n**Auto:** {auto}\n**Cena:** {cena:,}$",
        color=discord.Color.orange()
    )
    embed.add_field(name="⏰ Čekám na potvrzení", value=f"{kupec.mention}, potvrď prosím nákup kliknutím na tlačítko níže.", inline=False)

    await interaction.response.send_message(embed=embed, view=view)

    # Wait for confirmation
    await view.wait()

    if view.result is True:
        # Proceed with the sale
        prodavajici_data["auta"][auto] -= 1
        if prodavajici_data["auta"][auto] == 0:
            del prodavajici_data["auta"][auto]
        kupec_data["auta"][auto] = kupec_data["auta"].get(auto, 0) + 1

        # Remove money from buyer (hotovost first, then bank)
        remaining_to_remove = cena
        if kupec_data["hotovost"] >= remaining_to_remove:
            kupec_data["hotovost"] -= remaining_to_remove
        else:
            remaining_to_remove -= kupec_data["hotovost"]
            kupec_data["hotovost"] = 0
            kupec_data["bank"] -= remaining_to_remove

        # Add money to seller's hotovost
        prodavajici_data["hotovost"] += cena

        # Update total money
        kupec_data["penize"] = kupec_data["hotovost"] + kupec_data["bank"]
        prodavajici_data["penize"] = prodavajici_data["hotovost"] + prodavajici_data["bank"]

        # Save to database
        hraci.update_one({"_id": str(kupec.id)}, {"$set": kupec_data})
        hraci.update_one({"_id": str(interaction.user.id)}, {"$set": prodavajici_data})

        success_embed = discord.Embed(
            title="✅ Obchod dokončen!",
            description=f"Auto `{auto}` bylo úspěšně prodáno {kupec.display_name} za {cena:,}$.",
            color=discord.Color.green()
        )
        await interaction.followup.send(embed=success_embed)
        await log_action(bot, interaction.guild, f"{interaction.user.mention} prodal {auto} hráči {kupec.mention} za {cena:,}$")
    elif view.result is False:
        fail_embed = discord.Embed(
            title="❌ Obchod zrušen",
            description="Obchod byl zrušen nebo vypršel čas na potvrzení.",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=fail_embed)

@prodej_auto.autocomplete("auto")
async def autocomplete_prodej_auto(interaction: discord.Interaction, current: str):
    data = get_or_create_user(interaction.user.id)
    auta = data.get("auta", {})
    return [app_commands.Choice(name=a, value=a) for a in auta if current.lower() in a.lower()][:25]

@tree.command(name="prodej-zbran", description="Prodá zbraň jinému hráči")
@app_commands.describe(kupec="Komu prodáváš zbraň", zbran="Jakou zbraň prodáváš", cena="Cena za zbraň")
async def prodej_zbran(interaction: discord.Interaction, kupec: discord.Member, zbran: str, cena: int):
    prodavajici_data = get_or_create_user(interaction.user.id)
    kupec_data = get_or_create_user(kupec.id)

    if zbran not in prodavajici_data["zbrane"]:
        await interaction.response.send_message("❌ Nemáš tuto zbraň v inventáři.", ephemeral=True)
        return
    if prodavajici_data["zbrane"][zbran] <= 0:
        await interaction.response.send_message("❌ Nemáš žádné kusy této zbraně.", ephemeral=True)
        return
    total_money_kupec = get_total_money(kupec_data)
    if total_money_kupec < cena:
        await interaction.response.send_message("❌ Kupující nemá dostatek peněz.", ephemeral=True)
        return

    # Create confirmation view
    view = ConfirmationView(interaction.user, kupec, zbran, "zbran", cena)

    embed = discord.Embed(
        title="🔫 Potvrzení nákupu zbraně",
        description=f"**Prodávající:** {interaction.user.display_name}\n**Kupující:** {kupec.display_name}\n**Zbraň:** {zbran}\n**Cena:** {cena:,}$",
        color=discord.Color.orange()
    )
    embed.add_field(name="⏰ Čekám na potvrzení", value=f"{kupec.mention}, potvrď prosím nákup kliknutím na tlačítko níže.", inline=False)

    await interaction.response.send_message(embed=embed, view=view)

    # Wait for confirmation
    await view.wait()

    if view.result is True:
        # Proceed with the sale
        prodavajici_data["zbrane"][zbran] -= 1
        if prodavajici_data["zbrane"][zbran] == 0:
            del prodavajici_data["zbrane"][zbran]
        kupec_data["zbrane"][zbran] = kupec_data["zbrane"].get(zbran, 0) + 1

        # Remove money from buyer (hotovost first, then bank)
        remaining_to_remove = cena
        if kupec_data["hotovost"] >= remaining_to_remove:
            kupec_data["hotovost"] -= remaining_to_remove
        else:
            remaining_to_remove -= kupec_data["hotovost"]
            kupec_data["hotovost"] = 0
            kupec_data["bank"] -= remaining_to_remove

        # Add money to seller's hotovost
        prodavajici_data["hotovost"] += cena

        # Update total money
        kupec_data["penize"] = kupec_data["hotovost"] + kupec_data["bank"]
        prodavajici_data["penize"] = prodavajici_data["hotovost"] + prodavajici_data["bank"]

        # Save to database
        hraci.update_one({"_id": str(kupec.id)}, {"$set": kupec_data})
        hraci.update_one({"_id": str(interaction.user.id)}, {"$set": prodavajici_data})


        success_embed = discord.Embed(
            title="✅ Obchod dokončen!",
            description=f"Zbraň `{zbran}` byla úspěšně prodána {kupec.display_name} za {cena:,}$.",
            color=discord.Color.green()
        )
        await interaction.followup.send(embed=success_embed)
        await log_action(bot, interaction.guild, f"{interaction.user.mention} prodal {zbran} hráči {kupec.mention} za {cena:,}$")
    elif view.result is False:
        fail_embed = discord.Embed(
            title="❌ Obchod zrušen",
            description="Obchod byl zrušen nebo vypršel čas na potvrzení.",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=fail_embed)

@prodej_zbran.autocomplete("zbran")
async def autocomplete_prodej_zbran(interaction: discord.Interaction, current: str):
    data = get_or_create_user(interaction.user.id)
    zbrane = data.get("zbrane", {})
    return [app_commands.Choice(name=z, value=z) for z in zbrane if current.lower() in z.lower()][:25]

@tree.command(name="vybrat", description="Vybere peníze z banky do peněženky")
@app_commands.describe(castka="Částka, kterou chceš vybrat (nebo 'all' pro všechny)")
async def vybrat(interaction: discord.Interaction, castka: str):
    data = get_or_create_user(interaction.user.id)

    if castka.lower() == "all":
        actual_castka = data.get("bank", 0)
        if actual_castka <= 0:
            await interaction.response.send_message("❌ Nemáš žádné peníze v bance.", ephemeral=True)
            return
        data["bank"] = 0
        data["hotovost"] += actual_castka
    else:
        try:
            actual_castka = int(castka)
            if actual_castka <= 0:
                await interaction.response.send_message("❌ Částka musí být větší než 0.", ephemeral=True)
                return
        except ValueError:
            await interaction.response.send_message("❌ Neplatná částka. Použij číslo nebo 'all'.", ephemeral=True)
            return

        if data["bank"] < actual_castka:
            await interaction.response.send_message("❌ Nemáš dostatek peněz v bance.", ephemeral=True)
            return

        data["bank"] -= actual_castka
        data["hotovost"] += actual_castka

    data["penize"] = data["hotovost"] + data["bank"]
    hraci.update_one({"_id": str(interaction.user.id)}, {"$set": data})


    await interaction.response.send_message(f"✅ Vybral jsi {actual_castka:,}$ z banky.")


@tree.command(name="vlozit", description="Vloží peníze z peněženky do banky")
@app_commands.describe(castka="Částka, kterou chceš vložit (nebo 'all' pro všechny)")
async def vlozit(interaction: discord.Interaction, castka: str):
    data = get_or_create_user(interaction.user.id)

    if castka.lower() == "all":
        actual_castka = data.get("hotovost", 0)
        if actual_castka <= 0:
            await interaction.response.send_message("❌ Nemáš žádné peníze v peněžence.", ephemeral=True)
            return
        data["hotovost"] = 0
        data["bank"] += actual_castka
    else:
        try:
            actual_castka = int(castka)
            if actual_castka <= 0:
                await interaction.response.send_message("❌ Částka musí být větší než 0.", ephemeral=True)
                return
        except ValueError:
            await interaction.response.send_message("❌ Neplatná částka. Použij číslo nebo 'all'.", ephemeral=True)
            return

        if data.get("hotovost", 0) < actual_castka:
            await interaction.response.send_message("❌ Nemáš dostatek peněz v peněžence.", ephemeral=True)
            return

        data["hotovost"] -= actual_castka
        data["bank"] += actual_castka

    data["penize"] = data["hotovost"] + data["bank"]
    hraci.update_one({"_id": str(interaction.user.id)}, {"$set": data})


    await interaction.response.send_message(f"✅ Vložil jsi {actual_castka:,} $ z peněženky do banky.")

@tree.command(name="collect", description="Vybereš si týdenní výplatu podle svých rolí (každá má vlastní cooldown).")
async def collect(interaction: discord.Interaction):
    now = datetime.utcnow()
    data = get_or_create_user(interaction.user.id)

    if "collect_timestamps" not in data:
        data["collect_timestamps"] = {}

    user_role_ids = [role.id for role in interaction.user.roles]

    vyplaceno = 0
    vyplacene_role = []
    cekajici_role = []

    for role_id, castka in ROLE_ODMENY.items():
        if role_id not in user_role_ids:
            continue

        posledni = data["collect_timestamps"].get(str(role_id))
        if posledni:
            posledni_cas = datetime.fromisoformat(posledni)
            rozdil = now - posledni_cas
            if rozdil < timedelta(days=7):
                zbývá = timedelta(days=7) - rozdil
                hodiny, zbytek = divmod(zbývá.total_seconds(), 3600)
                minuty = int((zbytek % 3600) // 60)
                cekajici_role.append((role_id, hodiny, minuty))
                continue

        vyplaceno += castka
        vyplacene_role.append((role_id, castka))
        data["collect_timestamps"][str(role_id)] = now.isoformat()

    data["hotovost"] = data.get("hotovost", 0) + vyplaceno
    data["penize"] = data["hotovost"] + data.get("bank", 0) # Aktualizace celkových peněz
    hraci.update_one({"_id": str(interaction.user.id)}, {"$set": data})


    embed = discord.Embed(
        title="💰 Týdenní výplata",
        color=discord.Color.green()
    )
    if vyplacene_role:
        popis = ""
        for role_id, castka in vyplacene_role:
            role_obj = discord.utils.get(interaction.guild.roles, id=role_id)
            nazev = role_obj.name if role_obj else f"Role ID {role_id}"
            popis += f"✅ **{nazev}**: +{castka:,} $\n"
        embed.add_field(name="💸 Vyplaceno", value=popis, inline=False)

    if cekajici_role:
        cekani = ""
        for role_id, h, m in cekajici_role:
            role_obj = discord.utils.get(interaction.guild.roles, id=role_id)
            nazev = role_obj.name if role_obj else f"Role ID {role_id}"
            cekani += f"⏳ **{nazev}** – za {int(h)}h {int(m)}m\n"
        embed.add_field(name="<!--- Timer --->", value=cekani, inline=False)

    if not vyplacene_role and not cekajici_role:
        embed.description = "ℹ️ Nemáš žádné role s týdenní výplatou."
    elif not vyplacene_role and cekajici_role:
         embed.description = "❌ Tento týden sis už vybral odměnu za všechny své role."


    await interaction.response.send_message(embed=embed, ephemeral=True)
@tree.command(name="leaderboard", description="Zobrazí žebříček nejbohatších hráčů")
@app_commands.describe(stranka="Číslo stránky leaderboardu")
async def leaderboard(interaction: discord.Interaction, stranka: int = 1):
    all_users = list(hraci.find())

    if not all_users:
        await interaction.response.send_message("❌ Žádná data k zobrazení.", ephemeral=True)
        return

    leaderboard_data = []
    for user in all_users:
        user_id = str(user["_id"])  # Keep as string, MongoDB stores as string
        total = user.get("hotovost", 0) + user.get("bank", 0)
        leaderboard_data.append((user_id, total))

    leaderboard_data.sort(key=lambda x: x[1], reverse=True)

    stranka -= 1
    zaznamu_na_stranku = 10
    zacatek = stranka * zaznamu_na_stranku
    konec = zacatek + zaznamu_na_stranku
    strankovany = leaderboard_data[zacatek:konec]

    if not strankovany:
        await interaction.response.send_message("❌ Tato stránka neexistuje.", ephemeral=True)
        return

    embed = discord.Embed(
        title="💰 Leaderboard – Nejbohatší hráči",
        description=f"Stránka {stranka + 1}/{(len(leaderboard_data) + 9) // 10}",
        color=discord.Color.gold()
    )

    for index, (user_id, total) in enumerate(strankovany, start=zacatek + 1):
        user = interaction.guild.get_member(int(user_id))  # Convert to int for Discord API
        jmeno = user.display_name if user else f"<@{user_id}>"
        embed.add_field(
            name=f"#{index} – {jmeno}",
            value=f"💵 {total:,} $",
            inline=False
        )

    await interaction.response.send_message(embed=embed)

@tree.command(name="prodej-veci", description="Prodej věc nebo drogu jinému hráči")
@app_commands.describe(
    cil="Komu chceš věc nebo drogu prodat",
    vec="Název věci nebo drogy",
    mnozstvi="Kolik kusů/gramů chceš prodat",
    cena="Cena za vše v $"
)
@app_commands.autocomplete(vec=autocomplete_veci_drogy)
async def prodej_veci(interaction: discord.Interaction, cil: discord.Member, vec: str, mnozstvi: int, cena: int):
    prodavajici = interaction.user
    if prodavajici.id == cil.id:
        await interaction.response.send_message("❌ Nemůžeš prodávat sám sobě.", ephemeral=True)
        return

    data_prodejce = get_or_create_user(prodavajici.id)
    data_kupce = get_or_create_user(cil.id)

    # Inventář
    inventar = data_prodejce.get("veci", {}) | data_prodejce.get("drogy", {})
    if vec not in inventar or inventar[vec] < mnozstvi:
        await interaction.response.send_message("❌ Nemáš dostatek tohoto předmětu nebo drogy.", ephemeral=True)
        return

    embed = discord.Embed(
        title="💸 Nabídka k prodeji",
        description=f"{prodavajici.mention} nabízí `{mnozstvi}x {vec}` za `{cena:,}$` {cil.mention}.",
        color=discord.Color.green()
    )

    # Tlačítka
    class Potvrzeni(discord.ui.View):
        def __init__(self, timeout=60):
            super().__init__(timeout=timeout)
            self.prodej_potvrzen = None

        @discord.ui.button(label="✅ Přijmout", style=discord.ButtonStyle.success)
        async def prijmout(self, interaction_button: discord.Interaction, button: discord.ui.Button):
            if interaction_button.user.id != cil.id:
                await interaction_button.response.send_message("❌ Tohle není tvoje nabídka.", ephemeral=True)
                return
            self.prodej_potvrzen = True
            self.stop()
            await interaction_button.response.defer()

        @discord.ui.button(label="❌ Odmítnout", style=discord.ButtonStyle.danger)
        async def odmitnout(self, interaction_button: discord.Interaction, button: discord.ui.Button):
            if interaction_button.user.id != cil.id:
                await interaction_button.response.send_message("❌ Tohle není tvoje nabídka.", ephemeral=True)
                return
            self.prodej_potvrzen = False
            self.stop()
            await interaction_button.response.defer()

    view = Potvrzeni()
    await interaction.response.send_message(embed=embed, view=view)

    await view.wait()

    if view.prodej_potvrzen is None:
        await interaction.edit_original_response(content="⏳ Čas na odpověď vypršel.", embed=None, view=None)
        return

    if not view.prodej_potvrzen:
        await interaction.edit_original_response(content="❌ Kupující odmítl nabídku.", embed=None, view=None)
        return

    total_money_kupce = get_total_money(data_kupce)
    if total_money_kupce < cena:
        await interaction.edit_original_response(content="❌ Kupující nemá dost peněz.", embed=None, view=None)
        return

    # Odeber prodejci
    if vec in data_prodejce.get("veci", {}):
        data_prodejce["veci"][vec] -= mnozstvi
        if data_prodejce["veci"][vec] <= 0:
            del data_prodejce["veci"][vec]
        data_kupce.setdefault("veci", {})[vec] = data_kupce["veci"].get(vec, 0) + mnozstvi
    else:
        data_prodejce["drogy"][vec] -= mnozstvi
        if data_prodejce["drogy"][vec] <= 0:
            del data_prodejce["drogy"][vec]
        data_kupce.setdefault("drogy", {})[vec] = data_kupce["drogy"].get(vec, 0) + mnozstvi

    # Převod peněz
    data_prodejce["hotovost"] += cena

    # Remove money from buyer (hotovost first, then bank)
    remaining_to_remove = cena
    if data_kupce["hotovost"] >= remaining_to_remove:
        data_kupce["hotovost"] -= remaining_to_remove
    else:
        remaining_to_remove -= data_kupce["hotovost"]
        data_kupce["hotovost"] = 0
        data_kupce["bank"] -= remaining_to_remove

    # Update total money for both users
    data_prodejce["penize"] = data_prodejce["hotovost"] + data_prodejce["bank"]
    data_kupce["penize"] = data_kupce["hotovost"] + data_kupce["bank"]

    hraci.update_one({"_id": str(prodavajici.id)}, {"$set": data_prodejce})
    hraci.update_one({"_id": str(cil.id)}, {"$set": data_kupce})


    await interaction.edit_original_response(
        content=f"✅ {cil.mention} koupil {mnozstvi}x `{vec}` za {cena:,}$ od {prodavajici.mention}.",
        embed=None,
        view=None
    )
    await log_action(bot, interaction.guild, f"{prodavajici.mention} prodal {mnozstvi}x {vec} hráči {cil.mention} za {cena:,}$")


@tree.command(name="kup-veci", description="Kup si suroviny nebo nástroje")
@app_commands.describe(veci="Název věci, kterou chceš koupit", pocet="Počet kusů")
@app_commands.autocomplete(veci=autocomplete_veci)
async def kup_veci(interaction: discord.Interaction, veci: str, pocet: int = 1):
    user = interaction.user
    data = get_or_create_user(user.id)

    if veci not in CENY_VECI:
        await interaction.response.send_message("❌ Tato věc není dostupná k prodeji.", ephemeral=True)
        return

    cena = CENY_VECI[veci] * pocet
    if data["hotovost"] < cena:
        await interaction.response.send_message(f"❌ Nemáš dostatek peněz (potřebuješ {cena:,}$).", ephemeral=True)
        return

    data["hotovost"] -= cena
    data["penize"] = data["hotovost"] + data["bank"]

    if veci in data["veci"]:
        data["veci"][veci] += pocet
    else:
        data["veci"][veci] = pocet
    hraci.update_one({"_id": str(user.id)}, {"$set": data})


    await interaction.response.send_message(f"✅ Koupil jsi {pocet}x `{veci}` za {cena:,}$.")

    await log_action(bot, interaction.guild, f"{user.mention} koupil {pocet}x {veci} za {cena:,}$")

@tree.command(name="vyrob", description="Vyrob nelegální látku")
@app_commands.describe(droga="Druh drogy", mnozstvi="Kolik gramů chceš vyrobit")
@app_commands.autocomplete(droga=autocomplete_drogy)
async def vyrob(interaction: discord.Interaction, droga: str, mnozstvi: int = 10):
    uzivatel = interaction.user
    data = get_or_create_user(uzivatel.id)

    if mnozstvi % 10 != 0 or mnozstvi <= 0:
        return await interaction.response.send_message("❌ Výroba je možná pouze po 10g dávkách (např. 10, 20, 30...).", ephemeral=True)

    recept = RECEPTY.get(droga)
    if not recept:
        return await interaction.response.send_message("❌ Tato droga neexistuje.", ephemeral=True)

    nyni = datetime.utcnow()
    posledni = data.get("last_vyroba")
    if posledni:
        rozdil = (nyni - datetime.fromisoformat(posledni)).total_seconds()
        if rozdil < VYROBA_COOLDOWN * 60:
            zbyva = int((VYROBA_COOLDOWN * 60 - rozdil) / 60)
            return await interaction.response.send_message(f"⏳ Musíš počkat {zbyva} minut před další výrobou.", ephemeral=True)

    veci = data.get("veci", {})
    drogy = data.get("drogy", {})

    davky = mnozstvi // 10

    # Zkontroluj všechny chybějící položky najednou
    chybejici = []
    
    # Zkontroluj suroviny
    for surovina, pocet in recept["suroviny"].items():
        potrebne = pocet * davky
        mam = veci.get(surovina, 0)
        if mam < potrebne:
            chybejici.append(f"🧂 `{surovina}`: chybí {potrebne - mam}× (máš {mam}×, potřebuješ {potrebne}×)")

    # Zkontroluj nástroje
    for nastroj, pocet in recept["nastroje"].items():
        mam = veci.get(nastroj, 0)
        if mam < pocet:
            chybejici.append(f"🛠️ `{nastroj}`: chybí {pocet - mam}× (máš {mam}×, potřebuješ {pocet}×)")
    
    # Pokud něco chybí, zobraz všechno najednou
    if chybejici:
        embed = discord.Embed(
            title=f"❌ Chybějící položky pro výrobu {mnozstvi}g `{droga}`",
            description="\n".join(chybejici),
            color=discord.Color.red()
        )
        return await interaction.response.send_message(embed=embed, ephemeral=True)

    # Odečti suroviny
    for surovina, pocet in recept["suroviny"].items():
        veci[surovina] -= pocet * davky
        if veci[surovina] <= 0:
            veci.pop(surovina)

    data["last_vyroba"] = nyni.isoformat()
    celkovy_cas = recept["cas"] * davky


    await interaction.response.send_message(
        f"🧪 Začal jsi vyrábět {mnozstvi}g `{droga}`.\n⏳ Dokončení za {celkovy_cas} minut...", ephemeral=True)
    await log_action(bot, interaction.guild, f"{uzivatel.mention} začal vyrábět {mnozstvi}g {droga}")

    # ASYNC VÝROBA
    async def dokonci_vyrobu():
        await asyncio.sleep(celkovy_cas * 60)

        # Šance na selhání
        if random() < recept["selhani"]:
            for nastroj, pocet in recept["nastroje"].items():
                if nastroj in veci:
                    veci[nastroj] -= pocet
                    if veci[nastroj] <= 0:
                        veci.pop(nastroj)

            try:
                await uzivatel.send(f"❌ Výroba {mnozstvi}g `{droga}` selhala. Přišel jsi o suroviny i nástroje.")
            except:
                pass
            return

        # Výroba úspěšná
        drogy[droga] = drogy.get(droga, 0) + mnozstvi
        data["drogy"] = drogy
        hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})

        try:
            await uzivatel.send(f"✅ Výroba dokončena: {mnozstvi}g `{droga}` bylo přidáno do inventáře.")
        except:
            pass

    asyncio.create_task(dokonci_vyrobu())

async def autocomplete_drogy_ve_inventari(interaction: discord.Interaction, current: str):
    data = get_or_create_user(interaction.user.id)
    drogy = data.get("drogy", {})
    # Filtruj drogy podle aktuálního textu, vracej max 25 položek
    options = [
        app_commands.Choice(name=droga, value=droga)
        for droga in drogy.keys()
        if current.lower() in droga.lower()
    ][:25]
    return options

@tree.command(name="pozij-drogu", description="Požij drogu z inventáře a získej dočasné účinky")
@app_commands.describe(
    droga="Droga, kterou chceš použít",
    mnozstvi="Kolik chceš požít (např. 0.5g, 500mg, all)"
)
@app_commands.autocomplete(droga=autocomplete_drogy_ve_inventari)
async def pozij_drogu(interaction: discord.Interaction, droga: str, mnozstvi: str):
    uzivatel = interaction.user
    data = get_or_create_user(uzivatel.id)
    drogy = data.get("drogy", {})

    if droga not in drogy:
        await interaction.response.send_message("❌ Tuto drogu nemáš v inventáři.", ephemeral=True)
        return

    inventar_mnozstvi = drogy[droga]  # v gramech

    mnozstvi = mnozstvi.strip().lower()
    try:
        if mnozstvi == "all":
            mnozstvi_g = inventar_mnozstvi
        elif mnozstvi.endswith("mg"):
            mnozstvi_g = float(mnozstvi[:-2].strip()) / 1000
        elif mnozstvi.endswith("g"):
            mnozstvi_g = float(mnozstvi[:-1].strip())
        else:
            mnozstvi_g = float(mnozstvi)  # default = g
    except ValueError:
        await interaction.response.send_message("❌ Neplatný formát. Zadej třeba `0.5g`, `500mg`, nebo `all`.", ephemeral=True)
        return

    if mnozstvi_g <= 0:
        await interaction.response.send_message("❌ Množství musí být větší než 0.", ephemeral=True)
        return

    if mnozstvi_g > inventar_mnozstvi:
        await interaction.response.send_message(f"❌ Máš pouze {inventar_mnozstvi:.2f}g `{droga}`.", ephemeral=True)
        return
    UCINKY_DROG = {
        "Marihuana": {
            "base": "🧘 Uklidnění a zpomalení reakcí",
            "priznaky": [
                "👁️‍🗨️ Zarudlé oči",
                "🍔 Zvýšená chuť k jídlu",
                "😶 Zpomalená řeč"
            ],
            "trvani": 5
        },
        "Kokain": {
            "base": "⚡ Zvýšená energie a euforie",
            "priznaky": [
                "👃 Časté čichání",
                "👁️ Rozšířené zornice",
                "💦 Pocení"
            ],
            "trvani": 8
        },
        "Metamfetamin": {
            "base": "🔥 Extrémní bdělost a hyperaktivita",
            "priznaky": [
                "💢 Paranoia",
                "👄 Rychlé mluvení",
                "💦 Pocení"
            ],
            "trvani": 10
        },
        "Pervitin": {
            "base": "🌀 Silná euforie a soustředění",
            "priznaky": [
                "😬 Skřípání zubů",
                "💧 Sucho v ústech",
                "👁️ Rozšířené zornice"
            ],
            "trvani": 10
        },
        "Extáze": {
            "base": "💖 Emoční propojení a euforie",
            "priznaky": [
                "👁️ Velké zornice",
                "💦 Pocení",
                "🤗 Přehnaná empatie"
            ],
            "trvani": 7
        },
        "Heroin": {
            "base": "😴 Uklidnění a utlumení bolesti",
            "priznaky": [
                "😵 Zúžené zornice",
                "🛌 Malátnost",
                "🩸 Pomalejší dýchání"
            ],
            "trvani": 12
        },
    }

    # Výpočet účinku a příznaků
    ucinky = UCINKY_DROG.get(droga, None)
    if not ucinky:
        ucinek_text = "❓ Neznámé účinky"
        priznaky = []
        trvani = 5
    else:
        ucinek_text = ucinky["base"]
        priznaky = ucinky["priznaky"]
        trvani = ucinky["trvani"]

    # Příznaky podle síly dávky
    if mnozstvi_g >= 2.5:
        extra = "🚨 **Silná dávka! Možné záchvaty, halucinace, nebo smrtelné riziko.**"
        priznaky += ["💀 Dezorientace", "🤢 Nevolnost", "💤 Kolaps"]
    elif mnozstvi_g >= 1.0:
        extra = "⚠️ **Silnější účinky. Výrazné změny chování.**"
        priznaky += ["😵 Ztráta rovnováhy", "💬 Zmatečný projev"]
    else:
        extra = ""

    # Odečtení drogy
    drogy[droga] -= mnozstvi_g
    if drogy[droga] <= 0:
        del drogy[droga]
    data["drogy"] = drogy
    hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})


    # Embed
    embed = discord.Embed(
        title=f"💊 {droga} použita",
        description=(
            f"**{interaction.user.display_name}** právě požil {mnozstvi_g:.2f}g `{droga}`.\n\n"
            f"🧠 **Účinek:** {ucinek_text}\n"
            f"⏳ **Doba trvání:** {trvani * mnozstvi_g:.1f} minut (OOC)\n"
            f"{extra}\n\n"
            f"🩺 **Příznaky:**\n" + "\n".join(f"- {p}" for p in priznaky)
        ),
        color=discord.Color.purple()
    )
    await interaction.response.send_message(embed=embed)
    await log_action(bot, interaction.guild, f"{uzivatel.mention} požil {mnozstvi_g:.2f}g {droga}")





@tree.command(name="recepty", description="Zobrazí seznam receptů pro výrobu drog")
async def recepty(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🧪 Recepty na výrobu drog",
        description="Zde je seznam všech dostupných drog, jejich požadavků a šancí na selhání.",
        color=discord.Color.dark_red()
    )

    for droga, info in RECEPTY.items():
        suroviny = "\n".join(f"- {nazev} ×{pocet}" for nazev, pocet in info["suroviny"].items())
        nastroje = "\n".join(f"- {nazev} ×{pocet}" for nazev, pocet in info["nastroje"].items())
        cas = info["cas"]
        selhani = int(info["selhani"] * 100)

        embed.add_field(
            name=f"💊 {droga}",
            value=(
                f"**🧂 Suroviny:**\n{suroviny}\n"
                f"**🛠️ Nástroje:**\n{nastroje}\n"
                f"⏳ **Čas výroby:** {cas} minut / 10g\n"
                f"⚠️ **Šance na selhání:** {selhani}%"
            ),
            inline=False
        )

    await interaction.response.send_message(embed=embed)

def is_admin(user: discord.User):
    return any(role.id == ADMIN_ROLE_ID for role in user.roles)

@tree.command(name="pridej-veci", description="Přidej věci do inventáře uživatele (admin)")
@app_commands.describe(uzivatel="Uživatel, kterému přidáš věci", vec="Název věci", mnozstvi="Počet kusů")
@app_commands.autocomplete(vec=autocomplete_veci)  # Pokud máš autocomplete věcí
async def pridej_veci(interaction: discord.Interaction, uzivatel: discord.Member, vec: str, mnozstvi: int):
    if not is_admin(interaction.user):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
        return

    data = get_or_create_user(uzivatel.id)
    veci = data.get("veci", {})
    veci[vec] = veci.get(vec, 0) + mnozstvi
    data["veci"] = veci
    hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})


    await interaction.response.send_message(f"✅ Přidáno {mnozstvi}× `{vec}` uživateli {uzivatel.display_name}.", ephemeral=True)
    await log_action(bot, interaction.guild, f"{interaction.user.mention} přidal {mnozstvi}× {vec} hráči {uzivatel.mention}")


@tree.command(name="pridej-drogy", description="Přidá drogy do inventáře uživatele (admin)")
@app_commands.describe(uzivatel="Uživatel, kterému přidáš drogy", droga="Název drogy", mnozstvi="Počet gramů")
@app_commands.autocomplete(droga=autocomplete_drogy)  # Pokud máš autocomplete drog
async def pridej_drogy(interaction: discord.Interaction, uzivatel: discord.Member, droga: str, mnozstvi: int):
    if not is_admin(interaction.user):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
        return

    data = get_or_create_user(uzivatel.id)
    drogy = data.get("drogy", {})
    drogy[droga] = drogy.get(droga, 0) + mnozstvi
    data["drogy"] = drogy
    hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})


    await interaction.response.send_message(f"✅ Přidáno {mnozstvi}g `{droga}` uživateli {uzivatel.display_name}.", ephemeral=True)
    await log_action(bot, interaction.guild, f"{interaction.user.mention} přidal {mnozstvi}g {droga} hráči {uzivatel.mention}")

def has_permission(user: discord.User):
    return any(role.id == ADMIN_ROLE_ID for role in user.roles)

# Autocomplete pro odeber-veci podle inventáře cílového uživatele
async def autocomplete_odeber_veci(interaction: discord.Interaction, current: str):
    # Zkus získat cílového uživatele z argumentů příkazu
    uzivatel = None
    for option in interaction.data.get("options", []):
        if option["name"] == "uzivatel":
            try:
                uzivatel = await interaction.guild.fetch_member(option["value"])
            except:
                pass
            break
    if not uzivatel:
        return []

    data = get_or_create_user(uzivatel.id)
    veci = data.get("veci", {})
    # Filtruj podle aktuálního textu
    return [
        app_commands.Choice(name=vec, value=vec)
        for vec in veci.keys() if current.lower() in vec.lower()
    ][:25]

# Autocomplete pro odeber-drogy podle inventáře cílového uživatele
async def autocomplete_odeber_drogy(interaction: discord.Interaction, current: str):
    uzivatel = None
    for option in interaction.data.get("options", []):
        if option["name"] == "uzivatel":
            try:
                uzivatel = await interaction.guild.fetch_member(option["value"])
            except:
                pass
            break
    if not uzivatel:
        return []

    data = get_or_create_user(uzivatel.id)
    drogy = data.get("drogy", {})
    return [
        app_commands.Choice(name=droga, value=droga)
        for droga in drogy.keys() if current.lower() in droga.lower()
    ][:25]

@tree.command(name="odeber-veci", description="Odeber věci z inventáře uživatele (admin/policie)")
@app_commands.describe(uzivatel="Uživatel, kterému odebereš věci", vec="Název věci", mnozstvi="Počet kusů")
@app_commands.autocomplete(vec=autocomplete_odeber_veci)
async def odeber_veci(interaction: discord.Interaction, uzivatel: discord.Member, vec: str, mnozstvi: int):
    if not has_permission(interaction.user):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
        return

    data = get_or_create_user(uzivatel.id)
    veci = data.get("veci", {})
    if vec not in veci or veci[vec] < mnozstvi:
        await interaction.response.send_message(f"❌ Uživateli {uzivatel.display_name} chybí {mnozstvi}× `{vec}`.", ephemeral=True)
        return

    veci[vec] -= mnozstvi
    if veci[vec] <= 0:
        del veci[vec]
    data["veci"] = veci
    hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})


    await interaction.response.send_message(f"✅ Odebráno {mnozstvi}× `{vec}` uživateli {uzivatel.display_name}.", ephemeral=True)
    await log_action(bot, interaction.guild, f"{interaction.user.mention} odebral {mnozstvi}× {vec} hráči {uzivatel.mention}")


@tree.command(name="odeber-drogy", description="Odeber drogy z inventáře uživatele (admin/policie)")
@app_commands.describe(uzivatel="Uživatel, kterému odebereš drogy", droga="Název drogy", mnozstvi="Počet gramů")
@app_commands.autocomplete(droga=autocomplete_odeber_drogy)
async def odeber_drogy(interaction: discord.Interaction, uzivatel: discord.Member, droga: str, mnozstvi: int):
    if not has_permission(interaction.user):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
        return

    data = get_or_create_user(uzivatel.id)
    drogy = data.get("drogy", {})
    if droga not in drogy or drogy[droga] < mnozstvi:
        await interaction.response.send_message(f"❌ Uživateli {uzivatel.display_name} chybí {mnozstvi}g `{droga}`.", ephemeral=True)
        return

    drogy[droga] -= mnozstvi
    if drogy[droga] <= 0:
        del drogy[droga]
    data["drogy"] = drogy
    hraci.update_one({"_id": str(uzivatel.id)}, {"$set": data})


    await interaction.response.send_message(f"✅ Odebráno {mnozstvi}g `{droga}` uživateli {uzivatel.display_name}.", ephemeral=True)
    await log_action(bot, interaction.guild, f"{interaction.user.mention} odebral {mnozstvi}g {droga} hráči {uzivatel.mention}")

@tree.command(name="auto-info", description="Zobrazí detailní informace o autě")
@app_commands.describe(auto="Auto, o kterém chceš získat informace")
@app_commands.autocomplete(auto=autocomplete_kup_auto)
async def car_info(interaction: discord.Interaction, auto: str):
    if auto not in AUTA:
        await interaction.response.send_message("❌ Takové auto neexistuje.", ephemeral=True)
        return

    info = AUTA[auto]
    cena = info.get("cena", 0)
    top_speed = info.get("top_speed", "N/A")
    car_class = info.get("class", "N/A")
    car_type = info.get("type", "N/A")
    fuel = info.get("fuel", "N/A")
    pozadovana_role = info.get("role")

    # Role requirement text
    if pozadovana_role:
        role_text = "🔒 Vyžaduje specifickou roli (FHP/MPD/FBI/MFD/EMS/FDOT)"
    else:
        role_text = "✅ Dostupné pro všechny"

    # Price text
    if cena == 0:
        price_text = "ZDARMA (pro oprávněné role)"
    else:
        price_text = f"{cena:,} $"

    # Fuel emoji
    fuel_emoji = {
        "Petrol": "⛽",
        "Diesel": "🛢️",
        "Electric": "🔋",
        "Hybrid": "🔋⛽"
    }.get(fuel, "⚙️")

    embed = discord.Embed(
        title=f"🚗 {auto}",
        color=discord.Color.blue()
    )
    embed.add_field(name="💰 Cena", value=price_text, inline=True)
    embed.add_field(name="🏁 Maximální rychlost", value=f"{top_speed} mph" if top_speed != "N/A" else "N/A", inline=True)
    embed.add_field(name="📊 Třída", value=car_class, inline=True)
    embed.add_field(name="🚙 Typ vozidla", value=car_type, inline=True)
    embed.add_field(name=f"{fuel_emoji} Palivo", value=fuel, inline=True)
    embed.add_field(name="🔐 Dostupnost", value=role_text, inline=True)

    await interaction.response.send_message(embed=embed)

@tree.command(name="prikazy", description="Zobrazí seznam všech dostupných příkazů a jejich popis")
async def prikazy(interaction: discord.Interaction):
    embed = discord.Embed(title="📜 Seznam příkazů", color=discord.Color.green())

    embed.add_field(name="/inventory [uživatel]", value="Zobrazí inventář hráče (auta, zbraně, věci, drogy).", inline=False)
    embed.add_field(name="/koupit-zbran [zbraň] [počet]", value="Koupíš zbraň z nabídky, pokud máš oprávnění a peníze.", inline=False)
    embed.add_field(name="/prodej-zbran [uživatel] [zbraň] [cena]", value="Prodáš zbraň jinému hráči, s potvrzením od kupujícího.", inline=False)
    embed.add_field(name="/koupit-auto [auto]", value="Koupíš auto z nabídky.", inline=False)
    embed.add_field(name="/prodej-auto [uživatel] [auto] [cena]", value="Prodáš auto jinému hráči, s potvrzením od kupujícího.", inline=False)
    embed.add_field(name="/car-info [auto]", value="Zobrazí detailní informace o autě (rychlost, třída, palivo, atd.).", inline=False)
    embed.add_field(name="/kup-veci [věc] [počet]", value="Koupíš věci potřebné pro výrobu nelegálních látek.", inline=False)
    embed.add_field(name="/prodej-veci [uživatel] [věc] [počet] [cena]", value="Prodáš věci jinému hráči za určenou cenu.", inline=False)
    embed.add_field(name="/vyrob [droga] [gramy]", value="Vyrobíš nelegální látku (vyžaduje nástroje a suroviny).", inline=False)
    embed.add_field(name="/vyrob [droga] [gramy]", value="Začne výrobu drogy, trvá určitou dobu, může selhat.", inline=False)
    embed.add_field(name="/pozij-drogu [droga] [gramy]", value="Použiješ drogu ze svého inventáře, aktivují se efekty.", inline=False)
    embed.add_field(name="/balance", value="Zobrazí stav peněženky a bankovního účtu.", inline=False)
    embed.add_field(name="/vyber [částka]", value="Vybereš peníze z banky do peněženky.", inline=False)
    embed.add_field(name="/vloz [částka]", value="Vložíš peníze z peněženky na bankovní účet.", inline=False)
    embed.add_field(name="/collect", value="Vybereš týdenní odměnu podle rolí.", inline=False)
    embed.add_field(name="/leaderboard", value="Zobrazí žebříček hráčů podle jejich peněz.", inline=False)
    embed.add_field(name="/odeber-veci [uživatel] [věc] [počet]", value="Odebere věci z inventáře hráče (pouze policie/admin).", inline=False)
    embed.add_field(name="/odeber-drogy [uživatel] [droga] [gramy]", value="Odebere drogy z inventáře hráče (pouze policie/admin).", inline=False)
    embed.add_field(name="/reset-inventory [uživatel]", value="Resetuje celý inventář hráče (pouze policie/admin).", inline=False)
    embed.add_field(name="/prikazy", value="Zobrazí tento seznam příkazů.", inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=True)

bot.run(TOKEN)