
# === KONFIGURACE PRO MIAMI RP BOT ===

# === ADMIN A POLICIE ROLE ===
ADMIN_ROLE_ID = 1356305712531243048 
POLICE_ROLE_ID = 1378711315119607808 
LOG_CHANNEL_ID = 1293617189055758433 

# === TÝDENNÍ ODMĚNY PODLE ROLÍ ===
ROLE_ODMENY = {
    1293617189005557873: 3000,      # Občan
    1293617189005557870: 25000,     # Ředitel: FHP
    1293617189005557868: 25000,     # Ředitel: MPD
    1293617189005557867: 10000,     # Ředitel: MFD
    1293617189005557865: 10000,     # Ředitel: FDOT
    1293617189005557864: 25000,     # Ředitel: FBI
    1293617189005557866: 10000,     # Ředitel: EMS
    1293617189005557869: 9500,      # Ředitel: MGMC
    1346163519070146681: 9500,      # Ředitel: IRS
    1330524261030301707: 9500,      # Ředitel: DMV
}

# === CENÍK AUT ===
# Format: "Název auta": {"cena": částka, "role": None nebo "role_id || role_id", "top_speed": km/h, "class": kategorie, "type": typ, "fuel": palivo}
AUTA = {
    # Classic
    "Falcon Stallion 350 1969": {"cena": 260000, "role": None, "top_speed": 114, "class": "Classic", "type": "Coupe", "fuel": "Benzín"},
    "Bullhorn Prancer 1969": {"cena": 245000, "role": None, "top_speed": 112, "class": "Classic", "type": "Coupe", "fuel": "Benzín"},
    "Falcon Advance 100 Holiday Edition 1956": {"cena": 95000, "role": None, "top_speed": 115, "class": "Classic", "type": "Truck", "fuel": "Benzín"},
    "Chevlon Corbeta C2 1967": {"cena": 185000, "role": None, "top_speed": 140, "class": "Classic", "type": "Coupe", "fuel": "Benzín"},
    "Sentinel Platinum 1968": {"cena": 115000, "role": None, "top_speed": 107, "class": "Classic", "type": "Sedan", "fuel": "Benzín"},
    "Bullhorn Foreman 1988": {"cena": 105000, "role": None, "top_speed": 119, "class": "Classic", "type": "Sedan", "fuel": "Benzín"},
    "Arrow Phoenix Nationals 1977": {"cena": 240000, "role": None, "top_speed": 123, "class": "Classic", "type": "Coupe", "fuel": "Benzín"},
    "Vellfire Runabout 1984": {"cena": 95000, "role": None, "top_speed": 107, "class": "Classic", "type": "Coupe", "fuel": "Benzín"},
    "Chevlon L/35 Extended 1981": {"cena": 105000, "role": None, "top_speed": 121, "class": "Classic", "type": "Truck", "fuel": "Benzín"},
    "Chevlon Inferno 1981": {"cena": 97500, "role": None, "top_speed": 135, "class": "Classic", "type": "Truck", "fuel": "Benzín"},
    "Chevlon L/15 1981": {"cena": 92000, "role": None, "top_speed": 121, "class": "Classic", "type": "Truck", "fuel": "Benzín"},
    "Falcon Coupe Hotrod 1934": {"cena": 0, "role": None, "top_speed": 129, "class": "Classic", "type": "Coupe", "fuel": "Benzín"},  # ⚠️ chybí cena v ceníku
    "Leland Birchwood Hearse 1995": {"cena": 0, "role": None, "top_speed": 126, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},  # ⚠️ chybí cena v ceníku

    # Regular
    "Falcon Traveller 2003": {"cena": 15000, "role": None, "top_speed": 128, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Chevlon Camion 2002": {"cena": 10000, "role": None, "top_speed": 98, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Falcon Prime Eques 2003": {"cena": 9000, "role": None, "top_speed": 155, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Vellfire Evertt 1995": {"cena": 20000, "role": None, "top_speed": 124, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Overland Apache 1995": {"cena": 12000, "role": None, "top_speed": 110, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Vellfire Prima 2009": {"cena": 10000, "role": None, "top_speed": 66, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Overland Apache 2011": {"cena": 40000, "role": None, "top_speed": 128, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Overland Buckaroo 2018": {"cena": 45000, "role": None, "top_speed": 131, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Falcon Scavenger 2016": {"cena": 40000, "role": None, "top_speed": 127, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Falcon Fission 2015": {"cena": 35000, "role": None, "top_speed": 165, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Chevlon Captain 2009": {"cena": 20000, "role": None, "top_speed": 126, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Vellfire Riptide 2020": {"cena": 55000, "role": None, "top_speed": 136, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Bullhorn BH15 2009": {"cena": 30000, "role": None, "top_speed": 127, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Elysion Slick 2014": {"cena": 20000, "role": None, "top_speed": 107, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Chevlon Commuter Van 2006": {"cena": 30000, "role": None, "top_speed": 84, "class": "Regular", "type": "Industrial", "fuel": "Benzín"},
    "Chevlon Amigo LZR 2016": {"cena": 100000, "role": None, "top_speed": 121, "class": "Regular", "type": "Coupe", "fuel": "Benzín"},
    "Chevlon Landslide 2007": {"cena": 26000, "role": None, "top_speed": 128, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Falcon Traveller 2022": {"cena": 90000, "role": None, "top_speed": 185, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Navara Boundary 2022": {"cena": 65000, "role": None, "top_speed": 140, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Bullhorn Determinator 2008": {"cena": 70000, "role": None, "top_speed": 125, "class": "Regular", "type": "Coupe", "fuel": "Benzín"},
    "Chevlon Camion 2021": {"cena": 75000, "role": None, "top_speed": 128, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Chevlon Camion 2008": {"cena": 30000, "role": None, "top_speed": 126, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Chevlon Revver 2005": {"cena": 50000, "role": None, "top_speed": 132, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Falcon Rampage Bigfoot 2-Door 2021": {"cena": 70000, "role": None, "top_speed": 99, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Bullhorn Prancer 2011": {"cena": 50000, "role": None, "top_speed": 126, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Navara Imperium 2020": {"cena": 30000, "role": None, "top_speed": 110, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Falcon Advance 2018": {"cena": 70000, "role": None, "top_speed": 175, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Falcon Advance Beast 2017": {"cena": 100000, "role": None, "top_speed": 185, "class": "Regular", "type": "Performance SUV", "fuel": "Benzín"},
    "Falcon Rampage Beast 2021": {"cena": 130000, "role": None, "top_speed": 99, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Falcon Advance 2022": {"cena": 140000, "role": None, "top_speed": 195, "class": "Regular", "type": "Performance SUV", "fuel": "Benzín"},
    "Bullhorn Prancer Widebody 2020": {"cena": 170000, "role": None, "top_speed": 136, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Bullhorn Determinator SFP Fury 2022": {"cena": 185000, "role": None, "top_speed": 162, "class": "Regular", "type": "Coupe", "fuel": "Benzín"},
    "Bullhorn Determinator SFP Blackjack Widebody 2022": {"cena": 124999, "role": None, "top_speed": 162, "class": "Regular", "type": "Coupe", "fuel": "Benzín"},  # ⚠️ chybí v ceníku
    "Vellfire Prairie 2022": {"cena": 80000, "role": None, "top_speed": 131, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Bullhorn Pueblo 2018": {"cena": 100000, "role": None, "top_speed": 125, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Navara Horizon 2013": {"cena": 250000, "role": None, "top_speed": 157, "class": "Regular", "type": "Coupe", "fuel": "Benzín"},
    "Chevlon Antilope 1994": {"cena": 7000, "role": None, "top_speed": 74, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Leland LTS 2010": {"cena": 42000, "role": None, "top_speed": 122, "class": "Regular", "type": "Sedan", "fuel": "Benzín"},
    "Overland Apache SFP 2020": {"cena": 150000, "role": None, "top_speed": 147, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Stuttgart Landschaft 2022": {"cena": 200000, "role": None, "top_speed": 124, "class": "Regular", "type": "SUV", "fuel": "Benzín"},
    "Vellfire Pioneer 2019": {"cena": 125000, "role": None, "top_speed": 128, "class": "Regular", "type": "Coupe", "fuel": "Benzín"},
    "Falcon Stallion 350 2015": {"cena": 100000, "role": None, "top_speed": 125, "class": "Regular", "type": "Coupe", "fuel": "Benzín"},
    "Chevlon Amigo Sport 2016": {"cena": 96000, "role": None, "top_speed": 129, "class": "Regular", "type": "Coupe", "fuel": "Benzín"},
    "Chevlon Amigo LZR 2011": {"cena": 90000, "role": None, "top_speed": 133, "class": "Regular", "type": "Coupe", "fuel": "Benzín"},

    # Prestige
    "Averon S5 2010": {"cena": 140000, "role": None, "top_speed": 117, "class": "Prestige", "type": "Coupe", "fuel": "Benzín"},
    "Leland Vault 2020": {"cena": 130000, "role": None, "top_speed": 125, "class": "Prestige", "type": "SUV", "fuel": "Benzín"},
    "Averon RS3 2020": {"cena": 180000, "role": None, "top_speed": 120, "class": "Prestige", "type": "Sedan", "fuel": "Benzín"},
    "Stuttgart Executive 2021": {"cena": 240000, "role": None, "top_speed": 128, "class": "Prestige", "type": "Sedan", "fuel": "Benzín"},
    "Terrain Traveller 2022": {"cena": 180000, "role": None, "top_speed": 129, "class": "Prestige", "type": "SUV", "fuel": "Benzín"},
    "Averon Q8 2022": {"cena": 220000, "role": None, "top_speed": 125, "class": "Prestige", "type": "SUV", "fuel": "Benzín"},
    "BKM Munich 2020": {"cena": 185000, "role": None, "top_speed": 125, "class": "Prestige", "type": "SUV", "fuel": "Benzín"},
    "Stuttgart Vierturig 2021": {"cena": 0, "role": None, "top_speed": 129, "class": "Prestige", "type": "Sedan", "fuel": "Benzín"},  # ⚠️ chybí cena v ceníku
    "Takeo Experience 2021": {"cena": 550000, "role": None, "top_speed": 140, "class": "Prestige", "type": "Coupe", "fuel": "Benzín"},
    "Averon R8 2017": {"cena": 800000, "role": None, "top_speed": 146, "class": "Prestige", "type": "Coupe", "fuel": "Benzín"},
    "Strugatti Ettore 2020": {"cena": 1200000, "role": None, "top_speed": 170, "class": "Prestige", "type": "Coupe", "fuel": "Benzín"},
    "Surrey 650S 2016": {"cena": 900000, "role": None, "top_speed": 150, "class": "Prestige", "type": "Coupe", "fuel": "Benzín"},
    "Leland LTS5-V Blackwing 2023": {"cena": 280000, "role": None, "top_speed": 122, "class": "Prestige", "type": "Sedan", "fuel": "Benzín"},
    "Falcon Heritage 2021": {"cena": 720000, "role": None, "top_speed": 167, "class": "Prestige", "type": "Coupe", "fuel": "Benzín"},
    "Ferdinand Jalapeno Turbo 2022": {"cena": 200000, "role": None, "top_speed": 155, "class": "Prestige", "type": "SUV", "fuel": "Benzín"},
    "Chevlon Corbeta X08 2014": {"cena": 450000, "role": None, "top_speed": 153, "class": "Prestige", "type": "Coupe", "fuel": "Benzín"},
    "Chevlon Corbeta 8 2023": {"cena": 600000, "role": None, "top_speed": 157, "class": "Prestige", "type": "Coupe", "fuel": "Benzín"},

    # Electric
    "Falcon Advance Bolt 2024": {"cena": 350000, "role": None, "top_speed": 250, "class": "Electric", "type": "Electric SUV", "fuel": "Elektrika"},
    "Averon Anodic 2024": {"cena": 500000, "role": None, "top_speed": 119, "class": "Electric", "type": "SUV", "fuel": "Elektrika"},
    "Celestial Truckatron 2024": {"cena": 800000, "role": None, "top_speed": 118, "class": "Electric", "type": "Truck", "fuel": "Elektrika"},
    "Celestial Type 9 2024": {"cena": 650000, "role": None, "top_speed": 170, "class": "Electric", "type": "Coupe", "fuel": "Elektrika"}
    
    # LEO Vehicles
    "Falcon Prime Eques 2003": {"cena": 16000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": None, "fuel": "Benzín"},
    "Chevlon Captain PPV 2006": {"cena": 28000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 113, "class": "Emergency", "type": "Sedan", "fuel": "Benzín"},
    "Bullhorn Pueblo Pursuit 2018": {"cena": 130000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 129, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "Falcon Interceptor Sedan 2017": {"cena": 65000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": None, "fuel": "Benzín"},
    "Bullhorn Prancer Pursuit 2011": {"cena": 100000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 122, "class": "Emergency", "type": "Coupe", "fuel": "Benzín"},
    "Falcon Stallion 350 2015": {"cena": 150000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 124, "class": "Emergency", "type": "Coupe", "fuel": "Benzín"},
    "Bullhorn Prancer Pursuit 2015": {"cena": 188000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 121, "class": "Emergency", "type": "Sedan", "fuel": "Benzín"},
    "Bullhorn Prancer Pursuit Widebody 2020": {"cena": 220000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 136, "class": "Emergency", "type": "Sedan", "fuel": "Benzín"},
    "Bullhorn Determinator SFP Fury 2022": {"cena": 240000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 158, "class": "Emergency", "type": "Coupe", "fuel": "Benzín"},
    "Chevlon Camion PPV 2008": {"cena": 70000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 132, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "Chevlon Camion PPV 2018": {"cena": 98000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 133, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "Chevlon Camion PPV 2021": {"cena": 110000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 127, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "BKM Munich 2020": {"cena": 220000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 124, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "Falcon Rampage PPV 2021": {"cena": 96000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 133, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "Falcon Traveller SSV 2022": {"cena": 130000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": None, "fuel": "Benzín"},
    "Falcon Interceptor Utility 2013": {"cena": 83000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": None, "fuel": "Benzín"},
    "Falcon Interceptor Utility 2019": {"cena": 102000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 124, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "Falcon Interceptor Utility 2020": {"cena": 110000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": None, "fuel": "Benzín"},
    "Averon Q8 2022": {"cena": 200000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 124, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "Falcon Advance SSV 2018": {"cena": 69000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": None, "fuel": "Benzín"},
    "Bullhorn BH15 SSV 2009": {"cena": 70000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 126, "class": "Emergency", "type": "Truck", "fuel": "Benzín"},
    "Falcon Advance Bolt 2024": {"cena": 210000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": None, "fuel": "Benzín"},
    "Chevlon Platoro PPV 2019": {"cena": 140000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 130, "class": "Emergency", "type": "Truck", "fuel": "Benzín"},
    "4-Wheeler": {"cena": 40000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 63, "class": "Emergency", "type": "ATV", "fuel": "Benzín"},
    "Canyon Descender LEO": {"cena": 50000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 67, "class": "Emergency", "type": "UTV", "fuel": "Benzín"},
    "Chevlon Commuter Van 2006": {"cena": 65000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 84, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    "Mobile Command 2005": {"cena": 350000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 101, "class": "Emergency", "type": "Mobile Command Vehicle", "fuel": "Benzín"},
    "Prisoner Transport": {"cena": 255000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 98, "class": "Emergency", "type": "Prisoner Transport Vehicle", "fuel": "Benzín"},
    "Emergency Services Falcon Advance+ 2020": {"cena": 200000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 118, "class": "Emergency", "type": "Truck", "fuel": "Benzín"},
    "SWAT Truck 2011": {"cena": 320000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 126, "class": "Emergency", "type": "Truck", "fuel": "Benzín"},
    "Stuttgart Runner": {"cena": 120000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": 122, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    
    # LEO Trailers
    "Radar": {"cena": 50000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": "Trailer", "fuel": None},
    "Flood Light": {"cena": 25000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": "Trailer", "fuel": None},
    "Kamerový": {"cena": 50000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": "Trailer", "fuel": None},
    "Equipment trailer": {"cena": 25000, "role": "1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864", "top_speed": None, "class": "Emergency", "type": "Trailer", "fuel": None},
    
    # Fire/EMS Vehicles
    "Fire Engine": {"cena": 120000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 100, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    "Heavy Tanker": {"cena": 140000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 102, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    "Ladder Truck": {"cena": 250000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 95, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    "Heavy Rescue": {"cena": 165000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 100, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    "Special Operations Unit": {"cena": 110000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 92, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    "Bullhorn Ambulance": {"cena": 135000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 100, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    "International Ambulance": {"cena": 108000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 100, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    "Medical Bus": {"cena": 480000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 140, "class": "Emergency", "type": "Industrial", "fuel": "Benzín"},
    "Canyon Descender": {"cena": 68000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 67, "class": "Emergency", "type": "UTV", "fuel": "Benzín"},
    "4 Wheeler": {"cena": 53000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 63, "class": "Emergency", "type": "ATV", "fuel": "Benzín"},
    "Paramedic SUV": {"cena": 68000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 123, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "FD Chevlon Camion 2018": {"cena": 107000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 133, "class": "Emergency", "type": "SUV", "fuel": "Benzín"},
    "Utility Falcon Advance+": {"cena": 89000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": None, "class": "Emergency", "type": None, "fuel": "Benzín"},
    "Squad Falcon Advance+ 2020": {"cena": 109000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 118, "class": "Emergency", "type": "Truck", "fuel": "Benzín"},
    "Brush Falcon Advance+ 2020": {"cena": 134000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 125, "class": "Emergency", "type": "Truck", "fuel": "Benzín"},
    "Falcon Advance": {"cena": 93500, "role": "1293617189005557867 || 1293617189005557866", "top_speed": None, "class": "Emergency", "type": None, "fuel": "Benzín"},
    "FD Bullhorn Prancer": {"cena": 188000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 125, "class": "Emergency", "type": "Sedan", "fuel": "Benzín"},
    "Mobile Command Center": {"cena": 335000, "role": "1293617189005557867 || 1293617189005557866", "top_speed": 158, "class": "Emergency", "type": "Command vehicle", "fuel": "Benzín"},
    
    # DOT Vehicles
    "Vellfire Evertt Crew Cab 1995": {"cena": 35000, "role": "1293617189005557865", "top_speed": 126, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Flatbed Tow Truck": {"cena": 130000, "role": "1293617189005557865", "top_speed": 113, "class": "Regular", "type": "Industrial", "fuel": "Benzín"},
    "Cone Truck": {"cena": 98000, "role": "1293617189005557865", "top_speed": 119, "class": "Regular", "type": "Industrial", "fuel": "Benzín"},
    "Falcon Advance+ Tow Truck 2020": {"cena": 155000, "role": "1293617189005557865", "top_speed": 119, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Falcon Advance+ Roadside Assist 2020": {"cena": 120000, "role": "1293617189005557865", "top_speed": 119, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Chevlon Platoro Utility": {"cena": 108000, "role": "1293617189005557865", "top_speed": 130, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Bucket Truck": {"cena": 110000, "role": "1293617189005557865", "top_speed": None, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Falcon Advance+ Utility": {"cena": 128000, "role": "1293617189005557865", "top_speed": None, "class": "Regular", "type": "Truck", "fuel": "Benzín"},
    "Street Sweeper": {"cena": 112000, "role": "1293617189005557865", "top_speed": 84, "class": "Regular", "type": "Industrial", "fuel": "Benzín"},
    "Salt Truck": {"cena": 168000, "role": "1293617189005557865", "top_speed": 107, "class": "Regular", "type": "Industrial", "fuel": "Benzín"},
    
    # DOT Trailers
    "Traffic Light Trailer": {"cena": 40000, "role": "1293617189005557865", "top_speed": None, "class": None, "type": "Trailer", "fuel": None},
    "Traffic Arrow Trailer": {"cena": 55000, "role": "1293617189005557865", "top_speed": None, "class": None, "type": "Trailer", "fuel": None},
    "LED Message Board Trailer": {"cena": 78000, "role": "1293617189005557865", "top_speed": None, "class": None, "type": "Trailer", "fuel": None},
    "Asphalt Trailer": {"cena": 89000, "role": "1293617189005557865", "top_speed": None, "class": None, "type": "Trailer", "fuel": None},
    "Flood Light Trailer": {"cena": 32000, "role": "1293617189005557865", "top_speed": None, "class": None, "type": "Trailer", "fuel": None},
}

}

# === ZBRANĚ ===
DOSTUPNE_ZBRANE = [
    "Beretta M9", "M249", "Remington MSR", "M14", "AK47", "PPSH 41",
    "Desert Eagle", "Colt M1911", "Kriss Vector", "LMT L129A1", "Skorpion",
    "Colt Python", "TEC-9", "Remington 870", "Lemat Revolver"
]

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

    # Zbraně typu C:
    "M14": 2000,
    "AK47": 2500,
    "PPSH 41": 2300,
    "LMT L129A1": 2600,
    "Remington 870": 2000,

    # Zbraně typu D:
    "Remington MSR": 15000,
    "M249":  12000
}

# === VĚCI A DROGY ===
DOSTUPNE_VECI = [
    "Chemikálie", "Edrin", "Mdma prášek", "Barvivo", "Plnidlo", 
    "Pseudoefedrin", "Čistič", "Cukr", "Máková pasta", "Semena marihuany", 
    "Voda", "Hnojivo", "Ocet", "Listy koky", "Sušička", "Formička", 
    "UV lampa", "Květináč", "Destilační sada", "Extraktor", 
    "Ochranná maska", "Ochranné rukavice", "Tabletovací lis", 
    "Pěstební světlo", "Varná sada"
]

CENY_VECI = {
    # 🔬 Suroviny
    "Chemikálie": 200,
    "Edrin": 300,
    "Mdma prášek": 200,
    "Barvivo": 50,
    "Plnidlo": 40,
    "Pseudoefedrin": 180,
    "Čistič": 90,
    "Cukr": 50,
    "Máková pasta": 150,
    "Semena marihuany": 250,
    "Voda": 10,
    "Hnojivo": 30,
    "Ocet": 15,
    "Listy koky": 350,

    # 🛠️ Nástroje
    "Sušička": 1500,
    "Formička": 1000,
    "UV lampa": 1000,
    "Květináč": 150,
    "Destilační sada": 2500,
    "Extraktor": 2000,
    "Ochranná maska": 800,
    "Ochranné rukavice": 100,
    "Tabletovací lis": 3000,
    "Pěstební světlo": 1000,
    "Varná sada": 1800
}

DROGY = ["Marihuana", "Kokain", "Metamfetamin", "Pervitin", "Extáze", "Heroin"]

VYROBA_COOLDOWN = 2  # minutes

RECEPTY = {
    "Marihuana": {
        "suroviny": {
            "Semena marihuany": 1,
            "Voda": 2,
            "Hnojivo": 1
        },
        "nastroje": {
            "Květináč": 1,
            "UV Lampa": 1,
            "Sušička": 1
        },
        "cas": 5,
        "selhani": 0
    },
    "Kokain": {
        "suroviny": {
            "Listy koky": 3,
            "Chemikálie": 2
        },
        "nastroje": {
            "Extraktor": 1,
            "Ochranné rukavice": 1
        },
        "cas": 6,
        "selhani": 0.10
    },
    "Metamfetamin": {
        "suroviny": {
            "Chemikálie": 3,
            "Pseudoefedrin": 2
        },
        "nastroje": {
            "Destilační sada": 1,
            "Ochranné rukavice": 1
        },
        "cas": 7,
        "selhani": 0.12
    },
    "Pervitin": {
        "suroviny": {
            "Pseudoefedrin": 3,
            "Čistič": 1
        },
        "nastroje": {
            "Destilační sada": 1,
            "Ochranné rukavice": 1
        },
        "cas": 5,
        "selhani": 0.09
    },
    "Extáze": {
        "suroviny": {
            "MDMA prášek": 2,
            "Barvivo": 1,
            "Plnidlo": 1
        },
        "nastroje": {
            "Formička": 1,
            "Ochranné rukavice": 1
        },
        "cas": 5,
        "selhani": 0.07
    },
    "Heroin": {
        "suroviny": {
            "Mák": 2,
            "Ocet": 1,
            "Chemikálie": 1
        },
        "nastroje": {
            "Destilační sada": 1,
            "Ochranná maska": 1
        },
        "cas": 6,
        "selhani": 0.11
    }
}
