from odoo import models, fields


class Tournament(models.Model):
    _name = "gamezone.tournament"
    _description = "Gaming Tournament Information"

    tournament_name = fields.Char(
        required=True
    )

    game_id = fields.Many2one(
        "gamezone.game",
        required=True
    )

    start_date = fields.Date()

    end_date = fields.Date()

    max_teams = fields.Integer()

    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("upcoming", "Upcoming"),
            ("ongoing", "Ongoing"),
            ("completed", "Completed"),
        ],
        default="draft"
    )