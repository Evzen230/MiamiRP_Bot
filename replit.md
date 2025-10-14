# Miami RP Discord Bot

## Overview
A comprehensive Discord bot for managing a roleplay server economy, inventory, and player interactions. Built with Python, Discord.py, and MongoDB.

**Bot Status:** ✅ Online and Running  
**Database:** MongoDB Atlas  
**Language:** Python 3.11  

## Recent Changes (October 2025)
- **Security:** Removed hardcoded MongoDB credentials, moved to environment variables
- **Database:** Fixed MongoDB connection with automatic URL encoding for special characters
- **Code Quality:** Removed obsolete JSON file system, migrated fully to MongoDB
- **Bug Fixes:** Fixed leaderboard command to use MongoDB instead of data.json
- **Port Configuration:** Updated keep_alive server to use port 5000 for Replit compatibility

## Project Architecture

### Core Components
1. **main.py** - Main bot file with all commands and logic
2. **keep_alive.py** - Flask server for bot uptime monitoring
3. **MongoDB Database** - Cloud-hosted player data storage
4. **Discord Integration** - Slash commands and interactions

### Database Structure
```
Collection: hraci (players)
Document Schema:
{
  "_id": "user_id_string",
  "hotovost": 0,           // Cash in wallet
  "bank": 0,               // Money in bank
  "penize": 0,             // Total money (auto-calculated)
  "auta": {},              // Cars inventory {car_name: quantity}
  "zbrane": {},            // Weapons inventory {weapon_name: quantity}
  "veci": {},              // Items inventory {item_name: quantity}
  "drogy": {},             // Drugs inventory {drug_name: quantity}
  "collect_timestamps": {},// Weekly payment cooldowns per role
  "last_vyroba": null      // Last drug production timestamp
}
```

## Features

### 💰 Economy System
- **Balance Management:** `/balance` - View wallet and bank balance
- **Transfers:** `/pay` - Send money to other players
- **Banking:** `/vlozit`, `/vybrat` - Deposit/withdraw from bank
- **Weekly Payments:** `/collect` - Collect role-based weekly salaries (7-day cooldown per role)
- **Leaderboard:** `/leaderboard` - See richest players

### 🔫 Weapons System
- **Purchase:** `/koupit-zbran` - Buy weapons
- **Sell:** `/prodej-zbran` - Sell weapons to other players (with confirmation)
- **Admin Tools:** `/pridej-zbran`, `/odeber-zbran`

### 🚗 Vehicle System  
- **Purchase:** `/koupit-auto` - Buy vehicles
- **Sell:** `/prodej-auto` - Sell vehicles to other players (with confirmation)
- **Special Vehicles:** Role-locked vehicles for PD/EMS/FDOT (free for authorized roles)
- **Admin Tools:** `/pridej-auto`, `/odeber-auto`

### 📦 Items & Crafting
- **Buy Items:** `/kup-veci` - Purchase crafting materials and tools
- **Sell Items:** `/prodej-veci` - Sell items/drugs to other players
- **Drug Production:** `/vyrob` - Craft drugs from materials (2-minute cooldown)

### 🛡️ Admin Commands
- Money: `/pridej-penize`, `/odeber-penize`, `/reset-penize`
- Inventory: `/reset-inventory`
- Items: Various admin tools for managing player inventories

## Environment Variables

### Required Secrets
1. **DISCORD_BOT_TOKEN** - Discord bot authentication token
   - Get from: https://discord.com/developers/applications
   
2. **MONGO_URI** - MongoDB connection string
   - Format: `mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority`
   - Special characters in password are automatically URL-encoded

### Configuration
- **LOG_CHANNEL_ID:** 1293617189055758433 - Channel for bot action logs
- **VYROBA_COOLDOWN:** 2 minutes - Drug production cooldown
- **Weekly Payment Cooldown:** 7 days per role

## Role-Based Salaries
| Role ID | Amount | Position |
|---------|--------|----------|
| 1293617189005557873 | $3,000 | Občan (Citizen) |
| 1293617189005557870 | $25,000 | Ředitel: FHP |
| 1293617189005557868 | $25,000 | Ředitel: MPD |
| 1293617189005557867 | $10,000 | Ředitel: MFD |
| 1293617189005557865 | $10,000 | Ředitel: FDOT |
| 1293617189005557864 | $25,000 | Ředitel: FBI |
| 1293617189005557866 | $10,000 | Ředitel: EMS |
| 1293617189005557869 | $9,500 | Ředitel: MGMC |
| 1346163519070146681 | $9,500 | Ředitel: IRS |
| 1330524261030301707 | $9,500 | Ředitel: DMV |

## Technical Details

### Dependencies
- discord.py 2.5.2+ - Discord API wrapper
- pymongo 4.13.0+ - MongoDB driver
- Flask 3.1.1+ - Keep-alive web server
- motor 3.7.1 - Async MongoDB driver
- dnspython - MongoDB SRV connection support

### Workflow Configuration
- **Name:** Discord Bot
- **Command:** `python main.py`
- **Port:** 5000 (Flask keep-alive server)
- **Output:** Webview (for uptime monitoring)

### Security Features
- Environment-based secret management
- Automatic MongoDB URI credential encoding
- No hardcoded credentials in source code
- Transaction confirmations for player-to-player trades

## Development Notes

### MongoDB Connection
The bot automatically handles MongoDB URI encoding:
- Usernames and passwords with special characters are URL-encoded
- Connection is tested on startup with a ping command
- 5-second timeout for connection attempts

### Trade System
Player-to-player trades use Discord UI components:
- Buyer must confirm purchase with ✅ button
- Either party can cancel with ❌ button
- 60-second timeout for confirmation
- Automatic transaction rollback on cancellation

### Data Migration
- Old JSON file system removed
- All data now stored in MongoDB
- Player documents auto-created on first interaction
- Missing fields automatically added on user access

## Troubleshooting

### Bot Not Connecting to MongoDB?
1. Check MONGO_URI format in Secrets
2. Ensure password special characters are in the original URI (auto-encoded)
3. Verify MongoDB Atlas IP whitelist includes 0.0.0.0/0

### Commands Not Working?
1. Ensure bot has proper Discord permissions
2. Check bot is online in workflow logs
3. Verify slash commands are synced (automatic on startup)

### Keep-Alive Server?
- Runs on port 5000
- Responds with "Bot is running!" at root
- Used for uptime monitoring services

## Project Structure
```
.
├── main.py              # Main bot code
├── keep_alive.py        # Flask uptime server
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore patterns
└── replit.md           # This documentation
```

## Future Improvements
- Add database backups
- Implement transaction history
- Add more admin logging
- Create web dashboard for statistics
- Add anti-cheat mechanisms
