from odoo import models, fields


class Player(models.Model):
    _name = "gamezone.player"
    _description = "Gaming Player Information"

    real_name = fields.Char(required=True)
    gamer_name = fields.Char(required=True)
    email = fields.Char(required=True)
    contact = fields.Char(required=True)
    birthdate = fields.Date()
    game_ids = fields.Many2many("gamezone.game")
    team_id = fields.Many2one("gamezone.team")
    wins = fields.Integer()
    losses = fields.Integer()