from odoo import models, fields

class Team(models.Model):
	_name = "gamezone.team"
	_description="Gaming Team Information"
	team_name = fields.Char(required=True)
	game_id = fields.Many2one("gamezone.game")
	player_ids = fields.One2many("gamezone.player", "team_id")
	captain_id = fields.Many2one("gamezone.player")
	wins = fields.Integer()
	losses = fields.Integer()
