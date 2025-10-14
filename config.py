
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
    "Falcon Stallion 350 1969": {"cena": 260000, "role": None, "top_speed": 185, "class": "Classic", "type": "Sports Car", "fuel": "Petrol"},
    "Bullhorn Prancer 1969": {"cena": 245000, "role": None, "top_speed": 175, "class": "Classic", "type": "Sedan", "fuel": "Petrol"},
    "Falcon Advance 100 Holiday Edition 1956": {"cena": 95000, "role": None, "top_speed": 140, "class": "Classic", "type": "Sedan", "fuel": "Petrol"},
    "Chevlon Corbeta C2 1967": {"cena": 185000, "role": None, "top_speed": 200, "class": "Classic", "type": "Sports Car", "fuel": "Petrol"},
    "Sentinel Platinum 1968": {"cena": 115000, "role": None, "top_speed": 160, "class": "Classic", "type": "Luxury Sedan", "fuel": "Petrol"},
    "Bullhorn Foreman 1988": {"cena": 105000, "role": None, "top_speed": 150, "class": "Classic", "type": "Pickup Truck", "fuel": "Diesel"},
    "Arrow Phoenix Nationals 1977": {"cena": 240000, "role": None, "top_speed": 195, "class": "Classic", "type": "Sports Car", "fuel": "Petrol"},
    "Vellfire Runabout 1984": {"cena": 95000, "role": None, "top_speed": 135, "class": "Classic", "type": "Hatchback", "fuel": "Petrol"},
    "Chevlon L/35 Extended 1981": {"cena": 105000, "role": None, "top_speed": 145, "class": "Classic", "type": "Van", "fuel": "Diesel"},
    "Chevlon Inferno 1981": {"cena": 97500, "role": None, "top_speed": 170, "class": "Classic", "type": "Sports Car", "fuel": "Petrol"},
    "Chevlon L/15 1981": {"cena": 92000, "role": None, "top_speed": 140, "class": "Classic", "type": "Pickup Truck", "fuel": "Petrol"},

    # Regular
    "Falcon Traveller 2003": {"cena": 15000, "role": None, "top_speed": 160, "class": "Regular", "type": "SUV", "fuel": "Petrol"},
    "Chevlon Camion 2002": {"cena": 10000, "role": None, "top_speed": 140, "class": "Regular", "type": "Pickup Truck", "fuel": "Diesel"},
    "Falcon Prime Eques 2003": {"cena": 9000, "role": None, "top_speed": 155, "class": "Regular", "type": "Sedan", "fuel": "Petrol"},
    "Vellfire Evertt 1995": {"cena": 20000, "role": None, "top_speed": 145, "class": "Regular", "type": "Pickup Truck", "fuel": "Petrol"},
    "Overland Apache 1995": {"cena": 12000, "role": None, "top_speed": 150, "class": "Regular", "type": "SUV", "fuel": "Diesel"},
    "Vellfire Prima 2009": {"cena": 10000, "role": None, "top_speed": 155, "class": "Regular", "type": "Sedan", "fuel": "Petrol"},
    "Overland Apache 2011": {"cena": 40000, "role": None, "top_speed": 165, "class": "Regular", "type": "SUV", "fuel": "Diesel"},
    "Overland Buckaroo 2018": {"cena": 45000, "role": None, "top_speed": 170, "class": "Regular", "type": "SUV", "fuel": "Diesel"},
    "Falcon Scavenger 2016": {"cena": 40000, "role": None, "top_speed": 175, "class": "Regular", "type": "SUV", "fuel": "Petrol"},
    "Falcon Fission 2015": {"cena": 35000, "role": None, "top_speed": 165, "class": "Regular", "type": "Sedan", "fuel": "Petrol"},
    "Chevlon Captain 2009": {"cena": 20000, "role": None, "top_speed": 150, "class": "Regular", "type": "SUV", "fuel": "Petrol"},
    "Vellfire Riptide 2020": {"cena": 55000, "role": None, "top_speed": 180, "class": "Regular", "type": "Pickup Truck", "fuel": "Diesel"},
    "Bullhorn BH15 2009": {"cena": 30000, "role": None, "top_speed": 160, "class": "Regular", "type": "SUV", "fuel": "Diesel"},
    "Elysion Slick 2014": {"cena": 20000, "role": None, "top_speed": 170, "class": "Regular", "type": "Sports Sedan", "fuel": "Petrol"},
    "Chevlon Commuter Van 2006": {"cena": 30000, "role": None, "top_speed": 135, "class": "Regular", "type": "Van", "fuel": "Diesel"},
    "Chevlon Amigo LZR 2016": {"cena": 100000, "role": None, "top_speed": 195, "class": "Regular", "type": "Sports Car", "fuel": "Petrol"},
    "Chevlon Landslide 2007": {"cena": 26000, "role": None, "top_speed": 155, "class": "Regular", "type": "SUV", "fuel": "Petrol"},
    "Falcon Traveller 2022": {"cena": 90000, "role": None, "top_speed": 185, "class": "Regular", "type": "SUV", "fuel": "Hybrid"},
    "Navara Boundary 2022": {"cena": 65000, "role": None, "top_speed": 175, "class": "Regular", "type": "Pickup Truck", "fuel": "Diesel"},
    "Bullhorn Determinator 2008": {"cena": 70000, "role": None, "top_speed": 180, "class": "Regular", "type": "SUV", "fuel": "Petrol"},
    "Chevlon Camion 2021": {"cena": 75000, "role": None, "top_speed": 170, "class": "Regular", "type": "Pickup Truck", "fuel": "Diesel"},
    "Chevlon Camion 2008": {"cena": 30000, "role": None, "top_speed": 150, "class": "Regular", "type": "Pickup Truck", "fuel": "Diesel"},
    "Chevlon Revver 2005": {"cena": 50000, "role": None, "top_speed": 175, "class": "Regular", "type": "Sports Sedan", "fuel": "Petrol"},
    "Falcon Rampage Bigfoot 2-Door 2021": {"cena": 70000, "role": None, "top_speed": 165, "class": "Regular", "type": "Off-Road Truck", "fuel": "Diesel"},
    "Bullhorn Prancer 2011": {"cena": 50000, "role": None, "top_speed": 170, "class": "Regular", "type": "Sedan", "fuel": "Petrol"},
    "Navara Imperium 2020": {"cena": 30000, "role": None, "top_speed": 160, "class": "Regular", "type": "Sedan", "fuel": "Petrol"},
    "Falcon Advance 2018": {"cena": 70000, "role": None, "top_speed": 175, "class": "Regular", "type": "SUV", "fuel": "Petrol"},
    "Falcon Advance Beast 2017": {"cena": 100000, "role": None, "top_speed": 185, "class": "Regular", "type": "Performance SUV", "fuel": "Petrol"},
    "Falcon Rampage Beast 2021": {"cena": 130000, "role": None, "top_speed": 190, "class": "Regular", "type": "Performance Truck", "fuel": "Diesel"},
    "Falcon Advance 2022": {"cena": 140000, "role": None, "top_speed": 195, "class": "Regular", "type": "Performance SUV", "fuel": "Hybrid"},
    "Bullhorn Prancer Widebody 2020": {"cena": 170000, "role": None, "top_speed": 205, "class": "Regular", "type": "Sports Sedan", "fuel": "Petrol"},
    "Bullhorn Determinator SFP Fury 2022": {"cena": 185000, "role": None, "top_speed": 210, "class": "Regular", "type": "Performance SUV", "fuel": "Petrol"},
    "Vellfire Prairie 2022": {"cena": 80000, "role": None, "top_speed": 180, "class": "Regular", "type": "SUV", "fuel": "Hybrid"},
    "Bullhorn Pueblo 2018": {"cena": 100000, "role": None, "top_speed": 185, "class": "Regular", "type": "SUV", "fuel": "Petrol"},
    "Navara Horizon 2013": {"cena": 250000, "role": None, "top_speed": 220, "class": "Regular", "type": "Luxury Sports Sedan", "fuel": "Petrol"},
    "Chevlon Antilope 1994": {"cena": 7000, "role": None, "top_speed": 130, "class": "Regular", "type": "Compact Car", "fuel": "Petrol"},
    "Leland LTS 2010": {"cena": 42000, "role": None, "top_speed": 175, "class": "Regular", "type": "Sports Sedan", "fuel": "Petrol"},
    "Overland Apache SFP 2020": {"cena": 150000, "role": None, "top_speed": 200, "class": "Regular", "type": "Performance SUV", "fuel": "Petrol"},
    "Stuttgart Landschaft 2022": {"cena": 200000, "role": None, "top_speed": 215, "class": "Regular", "type": "Luxury SUV", "fuel": "Hybrid"},
    "Vellfire Pioneer 2019": {"cena": 125000, "role": None, "top_speed": 190, "class": "Regular", "type": "Pickup Truck", "fuel": "Diesel"},
    "Falcon Stalion 350": {"cena": 100000, "role": None, "top_speed": 195, "class": "Regular", "type": "Sports Car", "fuel": "Petrol"},
    "Chevlon Amigo S 2011": {"cena": 85000, "role": None, "top_speed": 185, "class": "Regular", "type": "Sports Sedan", "fuel": "Petrol"},
    "Chevlon Amigo S 2016": {"cena": 96000, "role": None, "top_speed": 190, "class": "Regular", "type": "Sports Sedan", "fuel": "Petrol"},
    "Chevlon Amigo LZR 2011": {"cena": 90000, "role": None, "top_speed": 195, "class": "Regular", "type": "Sports Car", "fuel": "Petrol"},

    # Prestige
    "Averon S5 2010": {"cena": 140000, "role": None, "top_speed": 210, "class": "Prestige", "type": "Luxury Sedan", "fuel": "Petrol"},
    "Leland Vault 2020": {"cena": 130000, "role": None, "top_speed": 205, "class": "Prestige", "type": "Luxury SUV", "fuel": "Petrol"},
    "Averon RS3 2020": {"cena": 180000, "role": None, "top_speed": 225, "class": "Prestige", "type": "Sports Sedan", "fuel": "Petrol"},
    "Stuttgart Executive: 2021": {"cena": 240000, "role": None, "top_speed": 230, "class": "Prestige", "type": "Luxury Sedan", "fuel": "Hybrid"},
    "Terrain Traveller 2022": {"cena": 180000, "role": None, "top_speed": 215, "class": "Prestige", "type": "Luxury SUV", "fuel": "Hybrid"},
    "Averon Q8 2022": {"cena": 220000, "role": None, "top_speed": 220, "class": "Prestige", "type": "Luxury SUV", "fuel": "Hybrid"},
    "BKM Munich 2020": {"cena": 185000, "role": None, "top_speed": 225, "class": "Prestige", "type": "Luxury Sedan", "fuel": "Petrol"},
    "Stuttgart Vierturig: 2021": {"cena": 250000, "role": None, "top_speed": 235, "class": "Prestige", "type": "Luxury Sedan", "fuel": "Hybrid"},
    "Takeo Experience 2021": {"cena": 550000, "role": None, "top_speed": 270, "class": "Prestige", "type": "Luxury SUV", "fuel": "Hybrid"},
    "Averon R8 2017": {"cena": 800000, "role": None, "top_speed": 320, "class": "Prestige", "type": "Supercar", "fuel": "Petrol"},
    "Strugatti Ettore 2020": {"cena": 1200000, "role": None, "top_speed": 380, "class": "Prestige", "type": "Hypercar", "fuel": "Petrol"},
    "Surrey 650S 2016": {"cena": 900000, "role": None, "top_speed": 330, "class": "Prestige", "type": "Supercar", "fuel": "Petrol"},
    "Leland LTS5-V Blackwing 2023": {"cena": 280000, "role": None, "top_speed": 245, "class": "Prestige", "type": "Performance Sedan", "fuel": "Petrol"},
    "Falcon Heritage 2021": {"cena": 720000, "role": None, "top_speed": 310, "class": "Prestige", "type": "Supercar", "fuel": "Petrol"},
    "Ferdinand Jalapeno Turbo: 2022": {"cena": 200000, "role": None, "top_speed": 230, "class": "Prestige", "type": "Sports SUV", "fuel": "Petrol"},
    "Chevlon Corbeta TZ 2014": {"cena": 450000, "role": None, "top_speed": 290, "class": "Prestige", "type": "Sports Car", "fuel": "Petrol"},
    "Chevlon Corbeta 8 2023": {"cena": 600000, "role": None, "top_speed": 305, "class": "Prestige", "type": "Supercar", "fuel": "Petrol"},

    # Electric
    "Falcon Advance Bolt 2024": {"cena": 350000, "role": None, "top_speed": 250, "class": "Electric", "type": "Electric SUV", "fuel": "Electric"},
    "Averon Anodic 2024": {"cena": 500000, "role": None, "top_speed": 280, "class": "Electric", "type": "Electric Sedan", "fuel": "Electric"},
    "Celestial Truckatron 2024": {"cena": 800000, "role": None, "top_speed": 200, "class": "Electric", "type": "Electric Truck", "fuel": "Electric"},
    "BKM Risen Roadster 2020": {"cena": 650000, "role": None, "top_speed": 300, "class": "Electric", "type": "Electric Sports Car", "fuel": "Electric"},

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
