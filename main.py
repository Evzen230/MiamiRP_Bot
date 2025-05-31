import datetime
import discord
from discord import app_commands
import json
import os
from discord.ext import commands
import asyncio
from keep_alive import keep_alive 

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
keep_alive()
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

# === Seznamy dostupných aut a zbraní ===


# Role ID a týdenní odměna (v dolarech)
ROLE_ODMENY = {
    1378320035277307914: 30,   # Např. Policista
    1378319995250937906: 20,   # Např. Starosta
    1378319956512473109: 10    # Např. Občan
}

# V datovém modelu musíš mít poslední čas vyzvednutí
# Např.: data["last_collect"] = "2024-05-30T12:00:00"

DOSTUPNA_AUTA = [
    "Falcon Stallion 350 1969", "Bullhorn Prancer 1969",
    "Falcon Advance 100 Holiday Edition 1956", "Chevlon Corbeta C2 1967",
    "Sentinel Platinum 1968", "Bullhorn Foreman 1988",
    "Arrow Phoenix Nationals 1977", "Vellfire Runabout 1984",
    "Chevlon L/35 Extended 1981", "Chevlon Inferno 1981", "Chevlon L/15 1981",
    "Falcon Traveller 2003", "Chevlon Camion 2002", "Falcon Prime Eques 2003",
    "Vellfire Evertt 1995", "Overland Apache 1995", "Vellfire Prima 2009",
    "Overland Apache 2011", "Overland Buckaroo 2018", "Falcon Scavenger 2016",
    "Falcon Fission 2015", "Chevlon Captain 2009", "Vellfire Riptide 2020",
    "Bullhorn BH15 2009", "Elysion Slick 2014", "Chevlon Commuter Van 2006",
    "Chevlon Amigo LZR 2016", "Chevlon Landslide 2007",
    "Falcon Traveller 2022", "Navara Boundary 2022",
    "Bullhorn Determinator 2008", "Chevlon Camion 2021", "Chevlon Camion 2008",
    "Chevlon Revver 2005", "Falcon Rampage Bigfoot 2-Door 2021",
    "Bullhorn Prancer 2011", "Navara Imperium 2020", "Falcon Advance 2018",
    "Falcon Advance Beast 2017", "Falcon Rampage Beast 2021",
    "Falcon Advance 2022", "Bullhorn Prancer Widebody 2020",
    "Bullhorn Determinator SFP Fury 2022", "Vellfire Prairie 2022",
    "Bullhorn Pueblo 2018", "Navara Horizon 2013", "Chevlon Antilope 1994",
    "Leland LTS 2010", "Overland Apache SFP 2020", "Stuttgart Landschaft 2022",
    "Vellfire Pioneer 2019", "Falcon Stalion 350", "Chevlon Amigo S 2011",
    "Chevlon Amigo S 2016", "Amigo LZR 2011", "Averon S5 2010",
    "Leland Vault 2020", "Averon RS3 2020", "Stuttgart Executive 2021",
    "Terrain Traveller 2022", "Averon Q8 2022", "BKM Munich 2020",
    "Stuttgart Vierturig 2021", "Takeo Experience 2021", "Averon R8 2017",
    "Strugatti Ettore 2020", "Surrey 650S 2016", "LTS5-V Blackwing 2023",
    "Falcon Heritage 2021", "Ferdinand Jalapeno Turbo 2022",
    "Falcon Traveller 2022", "Chevlon Corbeta TZ 2014",
    "Chevlon Corbeta 8 2023", "Falcon Advance Bolt 2024", "Averon Anodic 2024",
    "Celestial Truckatron 2024", "BKM Risen Roadster 2020"
]
CENY_AUT = {
    # Classic
    "Falcon Stallion 350 1969": 260000,
    "Bullhorn Prancer 1969": 245000,
    "Falcon Advance 100 Holiday Edition 1956": 95000,
    "Chevlon Corbeta C2 1967": 185000,
    "Sentinel Platinum 1968": 115000,
    "Bullhorn Foreman 1988": 105000,
    "Arrow Phoenix Nationals 1977": 240000,
    "Vellfire Runabout 1984": 95000,
    "Chevlon L/35 Extended 1981": 105000,
    "Chevlon Inferno 1981": 97500,
    "Chevlon L/15 1981": 92000,

    # Regular
    "Falcon Traveller 2003": 15000,
    "Chevlon Camion 2002": 10000,
    "Falcon Prime Eques 2003": 9000,
    "Vellfire Evertt 1995": 20000,
    "Overland Apache 1995": 12000,
    "Vellfire Prima 2009": 10000,
    "Overland Apache 2011": 40000,
    "Overland Buckaroo 2018": 45000,
    "Falcon Scavenger 2016": 40000,
    "Falcon Fission 2015": 35000,
    "Chevlon Captain 2009": 20000,
    "Vellfire Riptide 2020": 55000,
    "Bullhorn BH15 2009": 30000,
    "Elysion Slick 2014": 20000,
    "Chevlon Commuter Van 2006": 30000,
    "Chevlon Amigo LZR 2016": 100000,
    "Chevlon Landslide 2007": 26000,
    "Falcon Traveller 2022": 90000,
    "Navara Boundary 2022": 65000,
    "Bullhorn Determinator 2008": 70000,
    "Chevlon Camion 2021": 75000,
    "Chevlon Camion 2008": 30000,
    "Chevlon Revver 2005": 50000,
    "Falcon Rampage Bigfoot 2-Door 2021": 70000,
    "Bullhorn Prancer 2011": 50000,
    "Navara Imperium 2020": 30000,
    "Falcon Advance 2018": 70000,
    "Falcon Advance Beast 2017": 100000,
    "Falcon Rampage Beast 2021": 130000,
    "Falcon Advance 2022": 140000,
    "Bullhorn Prancer Widebody 2020": 170000,
    "Bullhorn Determinator SFP Fury 2022": 185000,
    "Vellfire Prairie 2022": 80000,
    "Bullhorn Pueblo 2018": 100000,
    "Navara Horizon 2013": 250000,
    "Chevlon Antilope 1994": 7000,
    "Leland LTS 2010": 42000,
    "Overland Apache SFP 2020": 150000,
    "Stuttgart Landschaft 2022": 200000,
    "Vellfire Pioneer 2019": 125000,
    "Falcon Stalion 350": 100000,
    "Chevlon Amigo S 2011": 85000,
    "Chevlon Amigo S 2016": 96000,
    "Chevlon Amigo LZR 2011": 90000,

    # Prestige
    "Averon S5 2010": 140000,
    "Leland Vault 2020": 130000,
    "Averon RS3 2020": 180000,
    "Stuttgart Executive: 2021": 240000,
    "Terrain Traveller 2022": 180000,
    "Averon Q8 2022": 220000,
    "BKM Munich 2020": 185000,
    "Stuttgart Vierturig: 2021": 250000,  # Neurčena cena
    "Takeo Experience 2021": 550000,
    "Averon R8 2017": 800000,
    "Strugatti Ettore 2020": 1200000,
    "Surrey 650S 2016": 900000,
    "Leland LTS5-V Blackwing 2023": 280000,
    "Falcon Heritage 2021": 720000,
    "Ferdinand Jalapeno Turbo: 2022": 200000,
    "Falcon Traveller 2022": 100000,
    "Chevlon Corbeta TZ 2014": 450000,
    "Chevlon Corbeta 8 2023": 600000,

    # Electric
    "Falcon Advance Bolt 2024": 350000,
    "Averon Anodic 2024": 500000,
    "Celestial Truckatron 2024": 800000,
    "BKM Risen Roadster 2020": 650000
}
CENY_ZBRANI = {
    # Zbraně typu A:
    "Beretta M9": 700, 
    "Desert Eagle": 900, 
    "Colt M1911": 750, 
    "Colt Python": 1000,
    "Lemat Revolver": 1200,

    # Zbraně typu B:
    "TEC-9": 1000,
    "Skorpion": 1100,
    "Kriss Vector": 1500, 

    #Zbraně typu C:
    "M14": 2000,
    "AK47": 2500, 
    "PPSH 41": 2300, 
    "LMT L129A1": 2600, 
    "Remington 870": 2000, 

    #Zbraně typu D:
    "Remington MSR": 15000, 
    "M249":  12000 
}
DOSTUPNE_ZBRANE = [
    "Beretta M9", "M249", "Remington MSR", "M14", "AK47", "PPSH 41",
    "Desert Eagle", "Colt M1911", "Kriss Vector", "LMT L129A1", "Skorpion",
    "Colt Python", "TEC-9", "Remington 870", "Lemat Revolver"
]
# === Databáze ===

DATA_FILE = "data.json"

# Načti data
try:
    with open(DATA_FILE, "r") as f:
        databaze = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    databaze = {}




def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(databaze, f, indent=4)


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

def get_or_create_user(user_id):
    user_id = str(user_id)
    if user_id not in databaze:
        databaze[user_id] = {"auta": {}, "zbrane": {}, "penize": 0, "hotovost": 0, "bank": 0}
    else:
        # Convert old list format to new dict format and ensure all money fields exist
        data = databaze[user_id]

        # Ensure all money fields exist
        if "penize" not in data:
            data["penize"] = 0
        if "hotovost" not in data:
            data["hotovost"] = 0
        if "bank" not in data:
            data["bank"] = 0

        if isinstance(data.get("auta"), list):
            # Convert list to dict with counts
            auta_dict = {}
            for auto in data["auta"]:
                if auto in auta_dict:
                    auta_dict[auto] += 1
                else:
                    auta_dict[auto] = 1
            data["auta"] = auta_dict

        if isinstance(data.get("zbrane"), list):
            # Convert list to dict with counts
            zbrane_dict = {}
            for zbran in data["zbrane"]:
                if zbran in zbrane_dict:
                    zbrane_dict[zbran] += 1
                else:
                    zbrane_dict[zbran] = 1
            data["zbrane"] = zbrane_dict

    # Update total money
    data["penize"] = data["hotovost"] + data["bank"]

    return databaze[user_id]

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
        role_id = 1378111107780313209  # Změň na skutečné ID role
        if not any(role.id == role_id for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
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
        save_data()
        await interaction.response.send_message(
            f"✅ Přidáno {pocet}x `{zbran}` hráči {uzivatel.display_name}.")

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
        role_id = 1378111107780313209  # Změň na skutečné ID role
        if not any(role.id == role_id for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
            return
        data = get_or_create_user(uzivatel.id)
        if zbran in data["zbrane"]:
            data["zbrane"][zbran] -= pocet
            if data["zbrane"][zbran] <= 0:
                del data["zbrane"][zbran]
            save_data()
            await interaction.response.send_message(
                f"✅ Odebráno {pocet}x `{zbran}` hráči {uzivatel.display_name}."
            )
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
        role_id = 1378111107780313209  # Změň na skutečné ID role
        if not any(role.id == role_id for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
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
        save_data()
        await interaction.response.send_message(
            f"✅ Přidáno {pocet}x `{auto}` hráči {uzivatel.display_name}.")

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
        role_id = 1378111107780313209  # Změň na skutečné ID role
        if not any(role.id == role_id for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
            return
        data = get_or_create_user(uzivatel.id)
        if auto in data["auta"]:
            data["auta"][auto] -= pocet
            if data["auta"][auto] <= 0:
                del data["auta"][auto]
            save_data()
            await interaction.response.send_message(
                f"✅ Odebráno {pocet}x `{auto}` hráči {uzivatel.display_name}.")
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
async def inventory(interaction: discord.Interaction,
                        uzivatel: discord.Member = None):
        uzivatel = uzivatel or interaction.user
        data = get_or_create_user(uzivatel.id)

        auta = data.get("auta", {})
        zbrane = data.get("zbrane", {})

        auta_text = "\n".join(f"🚗 {auto} ×{pocet}"
                              for auto, pocet in auta.items()) or "Žádná"
        zbrane_text = "\n".join(f"🔫 {zbran} ×{pocet}"
                                for zbran, pocet in zbrane.items()) or "Žádné"

        embed = discord.Embed(
            title=f"📋 Inventář uživatele {uzivatel.display_name}",
            color=discord.Color.blue())
        embed.add_field(name="Auta", value=auta_text, inline=False)
        embed.add_field(name="Zbraně", value=zbrane_text, inline=False)

        await interaction.response.send_message(embed=embed)

# Reset inventory command
@tree.command(name="reset-inventory", description="Resetuje celý inventář hráče (admin)")
@app_commands.describe(uzivatel="Uživatel, jehož inventář chceš vymazat")
async def reset_inventory(interaction: discord.Interaction, uzivatel: discord.Member):
    role_id = 1378111107780313209  # Změň na skutečné ID role
    if not any(role.id == role_id for role in interaction.user.roles):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
        return
    data = get_or_create_user(uzivatel.id)
    data["auta"] = {}
    data["zbrane"] = {}
    save_data()
    await interaction.response.send_message(f"♻️ Inventář hráče {uzivatel.display_name} byl úspěšně resetován.")

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
    role_id = 1378111107780313209  # Změň na ID role s oprávněním
    if not any(role.id == role_id for role in interaction.user.roles):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
        return
    data = get_or_create_user(uzivatel.id)
    data["hotovost"] += castka # Automatically adds to hotovost
    data["penize"] = data["hotovost"] + data["bank"]  # Update total money
    save_data()
    await interaction.response.send_message(f"✅ Přidáno {castka}$ hráči {uzivatel.display_name}.")

# Odeber penize command
@tree.command(name="odeber-penize", description="Odebere peníze hráči (admin)")
@app_commands.describe(uzivatel="Uživatel, kterému chceš odebrat peníze", castka="Kolik peněz chceš odebrat (nebo 'all' pro všechny)")
async def odeber_penize(interaction: discord.Interaction, uzivatel: discord.Member, castka: str):
    role_id = 1378111107780313209  # Změň na ID role s oprávněním
    if not any(role.id == role_id for role in interaction.user.roles):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
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
    save_data()
    await interaction.response.send_message(f"✅ Odebráno {actual_castka}$ hráči {uzivatel.display_name}.")

# Reset penize command

@tree.command(name="reset-penize", description="Resetuje peníze hráče (admin)")
@app_commands.describe(uzivatel="Uživatel, jehož peníze chceš vynulovat")
async def reset_penize(interaction: discord.Interaction, uzivatel: discord.Member):
    role_id = 1378111107780313209  # Změň na ID role s oprávněním
    if not any(role.id == role_id for role in interaction.user.roles):
        await interaction.response.send_message("❌ Nemáš oprávnění použít tento příkaz.", ephemeral=True)
        return
    data = get_or_create_user(uzivatel.id)
    data["hotovost"] = 0
    data["bank"] = 0
    data["penize"] = 0
    save_data()
    await interaction.response.send_message(f"♻️ Peníze hráče {uzivatel.display_name} byly vynulovány.")

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

    save_data()
    await interaction.response.send_message(f"💸 Poslal jsi {castka}$ hráči {cil.display_name}.")
# Kup auto command

@tree.command(name="kup-auto", description="Koupí auto za peníze")
@app_commands.describe(auto="Auto, které chceš koupit", pocet="Kolik kusů chceš koupit")
async def kup_auto(interaction: discord.Interaction, auto: str, pocet: int = 1):
        user = interaction.user
        data = get_or_create_user(user.id)

        if auto not in CENY_AUT:
            await interaction.response.send_message(f"❌ Auto `{auto}` není dostupné k nákupu.", ephemeral=True)
            return

        cena = CENY_AUT[auto] * pocet
        total_money = get_total_money(data)
        if total_money < cena:
            await interaction.response.send_message(f"❌ Nemáš dostatek peněz. Potřebuješ {cena}$.", ephemeral=True)
            return

         # Remove money from buyer (hotovost first, then bank)
        remaining_to_remove = cena
        if data["hotovost"] >= remaining_to_remove:
            data["hotovost"] -= remaining_to_remove
        else:
            remaining_to_remove -= data["hotovost"]
            data["hotovost"] = 0
            data["bank"] -= remaining_to_remove
        
        data["penize"] = data["hotovost"] + data["bank"]

        if auto in data["auta"]:
            data["auta"][auto] += pocet
        else:
            data["auta"][auto] = pocet

        save_data()
        await interaction.response.send_message(f"✅ Koupil jsi {pocet}x `{auto}` za {cena}$.")

@kup_auto.autocomplete("auto")
async def autocomplete_kup_auto(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=a, value=a)
        for a in CENY_AUT.keys() if current.lower() in a.lower()
    ][:25]

# Kup zbran command


@tree.command(name="koupit-zbran", description="Koupit zbraň z nabídky")
@app_commands.describe(zbran="Zbraň, kterou chceš koupit", pocet="Počet kusů")
async def koupit_zbran(interaction: discord.Interaction, zbran: str, pocet: int = 1):
    uzivatel = interaction.user
    data = get_or_create_user(uzivatel.id)

    if zbran not in CENY_ZBRANI:
        await interaction.response.send_message(f"❌ Zbraň `{zbran}` není v nabídce k prodeji.", ephemeral=True)
        return

    cena_za_kus = CENY_ZBRANI[zbran]
    celkova_cena = cena_za_kus * pocet

    total_money = get_total_money(data)
    if total_money < celkova_cena:
        await interaction.response.send_message(f"❌ Nemáš dostatek peněz ({total_money:,}$) na koupi {pocet}x `{zbran}` (potřebuješ {celkova_cena:,}$).", ephemeral=True)
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

    save_data()
    await interaction.response.send_message(f"✅ Koupil jsi {pocet}x `{zbran}` za {celkova_cena:,}$. Zůstatek: {data['penize']:,}$.")

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

        save_data()

        success_embed = discord.Embed(
            title="✅ Obchod dokončen!",
            description=f"Auto `{auto}` bylo úspěšně prodáno {kupec.display_name} za {cena:,}$.",
            color=discord.Color.green()
        )
        await interaction.followup.send(embed=success_embed)
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

        save_data()

        success_embed = discord.Embed(
            title="✅ Obchod dokončen!",
            description=f"Zbraň `{zbran}` byla úspěšně prodána {kupec.display_name} za {cena:,}$.",
            color=discord.Color.green()
        )
        await interaction.followup.send(embed=success_embed)
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

        if data.get("bank", 0) < actual_castka:
            await interaction.response.send_message("❌ Nemáš dostatek peněz v bance.", ephemeral=True)
            return

        data["bank"] -= actual_castka
        data["hotovost"] += actual_castka

    data["penize"] = data["hotovost"] + data["bank"]
    save_data()

    await interaction.response.send_message(f"✅ Vybral jsi {actual_castka:,} $ z banky do peněženky.")


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
    save_data()

    await interaction.response.send_message(f"✅ Vložil jsi {actual_castka:,} $ z peněženky do banky.")

@tree.command(name="collect", description="Vybereš si týdenní výplatu podle svých rolí (každá má vlastní cooldown).")
async def collect(interaction: discord.Interaction):
    now = datetime.datetime.utcnow()
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
            posledni_cas = datetime.datetime.fromisoformat(posledni)
            rozdil = now - posledni_cas
            if rozdil < datetime.timedelta(days=7):
                zbývá = datetime.timedelta(days=7) - rozdil
                hodiny, zbytek = divmod(zbývá.total_seconds(), 3600)
                minuty = int((zbytek % 3600) // 60)
                cekajici_role.append((role_id, hodiny, minuty))
                continue

        vyplaceno += castka
        vyplacene_role.append((role_id, castka))
        data["collect_timestamps"][str(role_id)] = now.isoformat()

    data["hotovost"] = data.get("hotovost", 0) + vyplaceno
    save_data()

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
        embed.add_field(name="🕒 Nelze vybrat (ještě cooldown)", value=cekani, inline=False)

    if not vyplacene_role:
        embed.description = "❌ Tento týden už sis vybral odměnu za všechny své role."

    await interaction.response.send_message(embed=embed, ephemeral=True)


bot.run(TOKEN)