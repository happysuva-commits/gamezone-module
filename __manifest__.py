{
    "name": "GameZone",
    "version": "19.0.1.0.0",
    "summary": "Gaming Tournament Management",
    "category": "Services",
    "author": "Happy",
    "data": [
    "data/game_sequence.xml",

    "security/ir.model.access.csv",
    "views/game_views.xml",
    "views/player_views.xml",
    "views/team_views.xml",
    "views/menu_views.xml",
    "views/tournament_views.xml",
],
    "depends": ["base"],  # Kaya module ni dependency chhe
    "application": True,  # Apps ma proper application tarike treat thase
    "installable": True,  # Module install kari shakay
}