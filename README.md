# GameZone — Odoo 19 Module

## Overview
GameZone is a custom Odoo 19 Community module for managing gaming activities and tournaments.

## Features
- Manage games
- Manage players and teams
- Organize tournaments
- Track match results and scores

## Technologies
- Python
- XML
- Odoo 19 Community
- PostgreSQL

## Installation
1. Copy the `gamezone` folder into your custom Odoo addons directory.
2. Add the custom addons directory to the Odoo configuration.
3. Restart the Odoo server.
4. Update the Apps List.
5. Search for **GameZone** and install the module.

## Developer
Happy

## Status
Under development.


## How to Run

### Requirements
- Odoo 19 Community
- Python environment configured for Odoo
- PostgreSQL
- GameZone module source code

### Installation

1. Copy the `gamezone` folder into your Odoo custom addons directory.
2. Ensure the custom addons directory is included in the Odoo `addons_path`.
3. Restart Odoo.
4. Open Odoo in your browser and enable Developer Mode if needed.
5. Go to Apps and update the Apps List.
6. Search for **GameZone** and click Install.

### Run from Terminal

Activate your existing Python virtual environment and go to the Odoo source directory:

```bash
cd ~/workspace/community/19.0
source ~/workspace/env_19.0/bin/activate
python3 odoo-bin -d YOUR_DATABASE -u gamezone
```

Replace `YOUR_DATABASE` with your own Odoo database name.

Then open:

http://localhost:8069

Log in and open the GameZone application.

### Notes
- Configure your own database and addons path.
- This module is designed for Odoo 19 Community.
