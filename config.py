
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
    "Falcon Stallion 350 1969": {"cena": 50666, "role": None, "top_speed": 114, "class": "Classic", "type": "Coupe", "fuel": "Gasoline"},
    "Bullhorn Prancer 1969": {"cena": 48500, "role": None, "top_speed": 112, "class": "Classic", "type": "Coupe", "fuel": "Gasoline"},
    "Falcon Advance 100 Holiday Edition 1956": {"cena": 25000, "role": None, "top_speed": 115, "class": "Classic", "type": "Truck", "fuel": "Gasoline"},
    "Chevlon Corbeta C2 1967": {"cena": 29000, "role": None, "top_speed": 140, "class": "Classic", "type": "Coupe", "fuel": "Gasoline"},
    "Sentinel Platinum 1968": {"cena": 32450, "role": None, "top_speed": 107, "class": "Classic", "type": "Sedan", "fuel": "Gasoline"},
    "Bullhorn Foreman 1988": {"cena": 0, "role": None, "top_speed": 119, "class": "Classic", "type": "Sedan", "fuel": "Gasoline"},
    "Arrow Phoenix Nationals 1977": {"cena": 47000, "role": None, "top_speed": 123, "class": "Classic", "type": "Coupe", "fuel": "Gasoline"},
    "Vellfire Runabout 1984": {"cena": 39000, "role": None, "top_speed": 107, "class": "Classic", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon L/35 Extended 1981": {"cena": 24900, "role": None, "top_speed": 121, "class": "Classic", "type": "Truck", "fuel": "Gasoline"},
    "Chevlon Inferno 1981": {"cena": 19975, "role": None, "top_speed": 135, "class": "Classic", "type": "Truck", "fuel": "Gasoline"},
    "Chevlon L/15 1981": {"cena": 16700, "role": None, "top_speed": 121, "class": "Classic", "type": "Truck", "fuel": "Gasoline"},
    "Falcon Coupe Hotrod 1934": {"cena": 28900, "role": None, "top_speed": 129, "class": "Classic", "type": "Coupe", "fuel": "Gasoline"},
    "Leland Birchwood Hearse 1995": {"cena": 0, "role": None, "top_speed": 126, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},

    # Regular
    "Falcon Traveller 2003": {"cena": 12500, "role": None, "top_speed": 128, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Chevlon Camion 2002": {"cena": 8900, "role": None, "top_speed": 98, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Falcon Prime Eques 2003": {"cena": 9000, "role": None, "top_speed": 155, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Vellfire Evertt 1995": {"cena": 14500, "role": None, "top_speed": 124, "class": "Regular", "type": "Truck", "fuel": "Gasoline"},
    "Overland Apache 1995": {"cena": 9950, "role": None, "top_speed": 110, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Vellfire Prima 2009": {"cena": 17850, "role": None, "top_speed": 66, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Overland Apache 2011": {"cena": 42000, "role": None, "top_speed": 128, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Overland Buckaroo 2018": {"cena": 42700, "role": None, "top_speed": 131, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Falcon Scavenger 2016": {"cena": 39700, "role": None, "top_speed": 127, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Falcon Fission 2015": {"cena": 35000, "role": None, "top_speed": 165, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Chevlon Captain 2009": {"cena": 11850, "role": None, "top_speed": 126, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Vellfire Riptide 2020": {"cena": 45200, "role": None, "top_speed": 136, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Bullhorn BH15 2009": {"cena": 30500, "role": None, "top_speed": 127, "class": "Regular", "type": "Truck", "fuel": "Gasoline"},
    "Elysion Slick 2014": {"cena": 19000, "role": None, "top_speed": 107, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Chevlon Commuter Van 2006": {"cena": 25000, "role": None, "top_speed": 84, "class": "Regular", "type": "Industrial", "fuel": "Gasoline"},
    "Chevlon Amigo LZR 2016": {"cena": 0, "role": None, "top_speed": 121, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon Landslide 2007": {"cena": 19500, "role": None, "top_speed": 128, "class": "Regular", "type": "Truck", "fuel": "Gasoline"},
    "Falcon Traveller 2022": {"cena": 90000, "role": None, "top_speed": 185, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Navara Boundary 2022": {"cena": 45990, "role": None, "top_speed": 140, "class": "Regular", "type": "Truck", "fuel": "Gasoline"},
    "Bullhorn Determinator 2008": {"cena": 49000, "role": None, "top_speed": 125, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon Camion 2021": {"cena": 49500, "role": None, "top_speed": 128, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Chevlon Camion 2018": {"cena": 34500, "role": None, "top_speed": 131, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Chevlon Camion 2008": {"cena": 28050, "role": None, "top_speed": 126, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Chevlon Revver 2005": {"cena": 40000, "role": None, "top_speed": 132, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Falcon Rampage Bigfoot 2-Door 2021": {"cena": 65000, "role": None, "top_speed": 99, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Bullhorn Prancer 2011": {"cena": 45990, "role": None, "top_speed": 126, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Bullhorn Prancer 2015": {"cena": 48500, "role": None, "top_speed": 133, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Navara Imperium 2020": {"cena": 22500, "role": None, "top_speed": 110, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Falcon Advance 2018": {"cena": 70000, "role": None, "top_speed": 175, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Falcon Advance Beast 2017": {"cena": 100000, "role": None, "top_speed": 185, "class": "Regular", "type": "Performance SUV", "fuel": "Gasoline"},
    "Falcon Rampage Beast 2021": {"cena": 129500, "role": None, "top_speed": 99, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Falcon Advance 2022": {"cena": 140000, "role": None, "top_speed": 195, "class": "Regular", "type": "Performance SUV", "fuel": "Gasoline"},
    "Bullhorn Prancer Widebody 2020": {"cena": 105000, "role": None, "top_speed": 136, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Bullhorn Determinator SFP Fury 2022": {"cena": 99500, "role": None, "top_speed": 162, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},
    "Bullhorn Determinator SFP Blackjack Widebody 2022": {"cena": 124999, "role": None, "top_speed": 162, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},
    "Vellfire Prairie 2022": {"cena": 60000, "role": None, "top_speed": 131, "class": "Regular", "type": "Truck", "fuel": "Gasoline"},
    "Bullhorn Pueblo 2018": {"cena": 79500, "role": None, "top_speed": 125, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Navara Horizon 2013": {"cena": 198500, "role": None, "top_speed": 157, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon Antilope 1994": {"cena": 0, "role": None, "top_speed": 74, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Leland LTS 2010": {"cena": 27500, "role": None, "top_speed": 122, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Overland Apache SFP 2020": {"cena": 92000, "role": None, "top_speed": 147, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Stuttgart Landschaft 2022": {"cena": 249000, "role": None, "top_speed": 124, "class": "Regular", "type": "SUV", "fuel": "Gasoline"},
    "Vellfire Pioneer 2019": {"cena": 199820, "role": None, "top_speed": 128, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},
    "Falcon Stallion 350 2015": {"cena": 139000, "role": None, "top_speed": 125, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon Amigo Sport 2016": {"cena": 55250, "role": None, "top_speed": 129, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon Amigo LZR 2011": {"cena": 58500, "role": None, "top_speed": 133, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon Platoro 2019": {"cena": 59000, "role": None, "top_speed": 131, "class": "Regular", "type": "Truck", "fuel": "Gasoline"},
    "Chryslus Champion 2005": {"cena": 43000, "role": None, "top_speed": 100, "class": "Regular", "type": "Sedan", "fuel": "Gasoline"},
    "Lawn Mower": {"cena": 2900, "role": None, "top_speed": 11, "class": "Regular", "type": "ATV", "fuel": "Gasoline"},
    "4-Wheeler": {"cena": 13500, "role": None, "top_speed": 60, "class": "Regular", "type": "ATV", "fuel": "Gasoline"},
    "Pea Car 2025": {"cena": 86900, "role": None, "top_speed": 67, "class": "Regular", "type": "Coupe", "fuel": "Gasoline"},

    # Prestige
    "Averon S5 2010": {"cena": 132795, "role": None, "top_speed": 117, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},
    "Leland Vault 2020": {"cena": 124900, "role": None, "top_speed": 125, "class": "Prestige", "type": "SUV", "fuel": "Gasoline"},
    "Averon RS3 2020": {"cena": 169000, "role": None, "top_speed": 120, "class": "Prestige", "type": "Sedan", "fuel": "Gasoline"},
    "Stuttgart Executive 2021": {"cena": 0, "role": None, "top_speed": 128, "class": "Prestige", "type": "Sedan", "fuel": "Gasoline"},
    "Terrain Traveller 2022": {"cena": 159000, "role": None, "top_speed": 129, "class": "Prestige", "type": "SUV", "fuel": "Gasoline"},
    "Averon Q8 2022": {"cena": 190000, "role": None, "top_speed": 125, "class": "Prestige", "type": "SUV", "fuel": "Gasoline"},
    "BKM Munich 2020": {"cena": 156000, "role": None, "top_speed": 125, "class": "Prestige", "type": "SUV", "fuel": "Gasoline"},
    "Stuttgart Vierturig 2021": {"cena": 162000, "role": None, "top_speed": 129, "class": "Prestige", "type": "Sedan", "fuel": "Gasoline"},
    "Takeo Experience 2021": {"cena": 475000, "role": None, "top_speed": 140, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},
    "Averon R8 2017": {"cena": 650000, "role": None, "top_speed": 146, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},
    "Strugatti Ettore 2020": {"cena": 1500000, "role": None, "top_speed": 170, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},
    "Surrey 650S 2016": {"cena": 890000, "role": None, "top_speed": 150, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},
    "Leland LTS5-V Blackwing 2023": {"cena": 255000, "role": None, "top_speed": 122, "class": "Prestige", "type": "Sedan", "fuel": "Gasoline"},
    "Falcon Heritage 2021": {"cena": 620900, "role": None, "top_speed": 167, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},
    "Ferdinand Jalapeno Turbo 2022": {"cena": 145000, "role": None, "top_speed": 155, "class": "Prestige", "type": "SUV", "fuel": "Gasoline"},
    "Chevlon Corbeta X08 2014": {"cena": 96000, "role": None, "top_speed": 153, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon Corbeta RZR 2014": {"cena": 350000, "role": None, "top_speed": 163, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon Corbeta 1M Edition 2014": {"cena": 0, "role": None, "top_speed": 153, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},
    "Chevlon Corbeta 8 2023": {"cena": 410000, "role": None, "top_speed": 157, "class": "Prestige", "type": "Coupe", "fuel": "Gasoline"},

    # Electric
    "Falcon Advance Bolt 2024": {"cena": 350000, "role": None, "top_speed": 250, "class": "Electric", "type": "Electric SUV", "fuel": "Electric"},
    "Falcon eStallion 2024": {"cena": 51000, "role": None, "top_speed": 124, "class": "Electric", "type": "SUV", "fuel": "Electric"},
    "Averon Anodic 2024": {"cena": 69990, "role": None, "top_speed": 119, "class": "Electric", "type": "SUV", "fuel": "Electric"},
    "Celestial Truckatron 2024": {"cena": 179950, "role": None, "top_speed": 122, "class": "Electric", "type": "Truck", "fuel": "Electric"},
    "Celestial Type-6 2023": {"cena": 46780, "role": None, "top_speed": 145, "class": "Electric", "type": "Sedan", "fuel": "Electric"},
    "BKM Risen Roadster 2020": {"cena": 164295, "role": None, "top_speed": 146, "class": "Electric", "type": "Coupe", "fuel": "Electric"},

    # PD/EMS/FDOT Vehicles (FREE for authorized roles)
    "Falcon Prime Eques 2003": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Chevlon Captain PPV 2006": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Bullhorn Pueblo Pursuit 2018": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Falcon Interceptor Sedan 2017": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Bullhorn Prancer Pursuit 2011": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Falcon Stallion 350 2015": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Bullhorn Prancer Pursuit 2015": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Bullhorn Prancer Pursuit Widebody 2020": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Bullhorn Determinator SFP Fury 2022": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Chevlon Camion PPV 2008": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Chevlon Camion PPV 2018": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Chevlon Camion PPV 2021": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "BKM Munich 2020": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Falcon Rampage PPV 2021": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Falcon Traveller SSV 2022": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Falcon Interceptor Utility 2013": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Falcon Interceptor Utility 2019": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Falcon Interceptor Utility 2020": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Averon Q8 2022": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Falcon Advance SSV 2018": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Bullhorn BH15 SSV 2009": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Falcon Advance Bolt 2024": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Chevlon Platoro PPV 2019": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "4-Wheeler": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Canyon Descender LEO": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Chevlon Commuter Van 2006": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Mobile Command 2005": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Prisoner Transport": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Emergency Services Falcon Advance+ 2020": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "SWAT Truck 2011": {'cena': 0, 'role': '1338975549711978568 || 1293617189005557870 || 1293617189005557868 || 1293617189005557864'},
    "Fire Engine": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Heavy Tanker": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Ladder Truck": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Heavy Rescue": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Special Operations Unit": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Bullhorn Ambulance": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "International Ambulance": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Medical Bus": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Canyon Descender": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "4 Wheeler": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Paramedic SUV": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "FD Chevlon Camion 2018": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Utility Falcon Advance+": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Squad Falcon Advance+ 2020": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Brush Falcon Advance+ 2020": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Falcon Advance": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "FD Bullhorn Prancer": {'cena': 0, 'role': '1293617189005557867 || 1293617189005557866'},
    "Mobile Command Center": {'cena': 0, 'role': '1293617189005557867 || 12936171890055557866'},
    "Vellfire Evertt Crew Cab 1995": {'cena': 0, 'role': '1293617189005557865'},
    "Flatbed Tow Truck": {'cena': 0, 'role': '1293617189005557865'},
    "Cone Truck": {'cena': 0, 'role': '1293617189005557865'},
    "Falcon Advance+ Tow Truck 2020": {'cena': 0, 'role': '1293617189005557865'},
    "Falcon Advance+ Roadside Assist 2020": {'cena': 0, 'role': '1293617189005557865'},
    "Chevlon Platoro Utility": {'cena': 0, 'role': '1293617189005557865'},
    "Bucket Truck": {'cena': 0, 'role': '1293617189005557865'},
    "Falcon Advance+ Utility": {'cena': 0, 'role': '1293617189005557865'},
    "Street Sweeper": {'cena': 0, 'role': '1293617189005557865'},
    "Salt Truck": {'cena': 0, 'role': '1293617189005557865'},
    "Traffic Light Trailer": {'cena': 0, 'role': '1293617189005557865'},
    "Traffic Arrow Trailer": {'cena': 0, 'role': '1293617189005557865'},
    "LED Message Board Trailer": {'cena': 0, 'role': '1293617189005557865'},
    "Asphalt Trailer": {'cena': 0, 'role': '1293617189005557865'},
    "Flood Light Trailer": {'cena': 0, 'role': '1293617189005557865'},
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
