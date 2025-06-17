# 📘 Popis souboru `main.py` (Discord bot pro Miami RP)

Tento Python skript je jádrem Discord bota pro roleplay server **Miami RP**, který umožňuje správu herních inventářů, ekonomiky a obchodů mezi hráči. Využívá `discord.py`, MongoDB a řadu vlastních příkazů.  

---

## 🧩 Klíčové funkce

### 🔧 Základní nastavení
- Připojení k Discordu přes token z prostředí
- Aktivace keep_alive serveru
- Nastavení `discord.Intents` a `commands.Bot`

### 🗃️ Práce s MongoDB
- Každý hráč je uložen podle ID v kolekci `hraci`
- Obsah inventáře: auta, zbraně, věci, drogy, peníze
- Funkce `get_or_create_user()` zajišťuje inicializaci záznamu

---

## 💰 Ekonomika

- **Peněženka (`hotovost`)** + **Banka (`bank`)** = `penize`
- Příkazy:
  - `/balance`: zobrazí stav účtu
  - `/pay`: převod mezi hráči
  - `/vlozit`, `/vybrat`: práce s bankou
  - `/pridej-penize`, `/odeber-penize`, `/reset-penize` (admin)

---

## 📦 Inventář

- Správa pomocí MongoDB
- Systém příkazů pro:
  - `/inventory`: zobrazení
  - `/reset-inventory` (admin)
  - `/pridej-zbran`, `/odeber-zbran`
  - `/pridej-auto`, `/odeber-auto`
- Autocomplete pro zbraně, auta, věci i drogy

---

## 🚗 Auta

- `DOSTUPNA_AUTA`: seznam všech vozidel
- `AUTA`: ceník a role potřebné pro zakoupení
- Speciální vozidla pro PD/EMS mají určené `role` a jsou zdarma

### Příkazy:
- `/koupit-auto`: nákup vozidla
- `/prodej-auto`: prodej hráči (s potvrzením)
- `/pridej-auto`, `/odeber-auto` (admin)

---

## 🔫 Zbraně

- `DOSTUPNE_ZBRANE`: seznam zbraní
- `CENY_ZBRANI`: ceny zbraní podle typu (A–D)

### Příkazy:
- `/koupit-zbran`: nákup
- `/prodej-zbran`: prodej mezi hráči
- `/pridej-zbran`, `/odeber-zbran` (admin)

---

## 💊 Drogy a výroba

- Seznam drog: Marihuana, Kokain, Metamfetamin, Pervitin, Extáze, Heroin
- `RECEPTY`: výrobní recepty (suroviny, nástroje, čas, šance na selhání)
- `DOSTUPNE_VECI`: materiály a nástroje
- `CENY_VECI`: ceny jednotlivých položek

---

## 🔄 Potvrzení obchodů

- Využívá `discord.ui.View` s tlačítky pro schválení/odmítnutí
- Používá se u prodeje zbraní/aut jinému hráči

---

## 🧠 Autocomplete systém

- Pro věci, drogy, zbraně, auta v rámci interakcí
- Dynamicky načítá dostupné položky z databáze nebo seznamů

---

## 🗂️ Použité knihovny

- `discord`, `discord.ext.commands`, `discord.ui`
- `pymongo`, `bson`
- `os`, `json`, `datetime`, `asyncio`, `random`

---

## 🛡️ Přístupová práva

- Administrátorské příkazy kontrolují roli podle ID
- Některé funkce (např. nákup zbraní) jsou omezeny na role

---

## 📁 Poznámky

- Bot není kompletní bez souboru `keep_alive.py`
- `DATA_FILE` je používán, ale není definován v ukázce – pravděpodobně globální proměnná
