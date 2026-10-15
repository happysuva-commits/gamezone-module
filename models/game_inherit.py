from odoo import models, fields


class GameInherit(models.Model):
    _inherit = "gamezone.game"

    game_code = fields.Char(
        string="Game Code",
        default=lambda self: self.env["ir.sequence"].next_by_code(
            "gamezone.game"
        ),
        readonly=True,
        copy=False,
    )
