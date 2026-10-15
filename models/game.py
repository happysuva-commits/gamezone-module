from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Game(models.Model):
    _name = "gamezone.game"
    _description = "Gaming Tournament Management"

    game_name = fields.Char(
        required=True
    )

    max_players = fields.Integer(
        required=True
    )

    is_team_game = fields.Boolean()

    team_a_score = fields.Integer(
        string="Team A Score",
        default=0,
    )

    team_b_score = fields.Integer(
        string="Team B Score",
        default=0,
    )

    winner = fields.Char(
        string="Winner",
        help="Winning team name, for example Team A",
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("running", "Running"),
            ("finished", "Finished"),
        ],
        string="Status",
        default="draft",
        required=True,
    )

    player_ids = fields.Many2many(
        "gamezone.player"
    )

    tournament_ids = fields.One2many(
        "gamezone.tournament",
        "game_id"
    )

    tournament_count = fields.Integer(
        compute="_compute_tournament_count"
    )

    
    # COMPUTED FIELD
    
    player_count = fields.Integer(
        compute="_compute_player_count"
    )

    def _compute_player_count(self):
        for record in self:
            record.player_count = len(record.player_ids)

    def _compute_tournament_count(self):
        for record in self:
            record.tournament_count = len(record.tournament_ids)

    
    # - OPEN TOURNAMENTS Click karya pachi linked Tournament records ni screen khole
    
    def action_open_players(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Players",
            "res_model": "gamezone.player",
            "view_mode": "list,form",
            "domain": [("id", "in", self.player_ids.ids)],
        }


    def action_open_game_results(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Game Results",
            "res_model": "gamezone.game",
            "view_mode": "list,form",
            "domain": [
                ("id", "=", self.id),
                ("state", "=", "finished"),
            ],
        }

    def action_open_tournaments(self):
        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "name": "Tournaments",
            "res_model": "gamezone.tournament",
            "view_mode": "list,form",
            "domain": [("game_id", "=", self.id)],
            "context": {
                "default_game_id": self.id,
            },
        }

    
    # ONCHANGE Field change karya pachi biji field ni value automatically badle
  
    @api.onchange("is_team_game")
    def _onchange_is_team_game(self):
        if self.is_team_game:
            self.max_players = 10

    
    # CONSTRAINT
    
    @api.constrains("max_players")
    def _check_max_players(self):
        for record in self:
            if record.max_players <= 0:
                raise ValidationError(
                    "Maximum Players must be greater than 0."
                )

   

    # Create Method 1: Fixed Game
    #button click par direct cricket create thase
    def action_create_game_1(self):
        game = self.env["gamezone.game"].create({
            "game_name": "Cricket Practice 1",
            "max_players": 11,
            "is_team_game": True,
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Created Game",
            "res_model": "gamezone.game",
            "view_mode": "form",
            "res_id": game.id,
            "target": "current",
        }

    # Method 2: Create Football Game
    def action_create_game_2(self):
        game = self.env["gamezone.game"].create({
            "game_name": "Football",
            "max_players": 11,
            "is_team_game": True,
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Football",
            "res_model": "gamezone.game",
            "view_mode": "form",
            "res_id": game.id,
            "target": "current",
        }

    # Method 3: Create Game with Uppercase Name
    def action_create_game_uppercase(self):
        game = self.env["gamezone.game"].create({
            "game_name": "CRICKET".upper(),
            "max_players": 11,
            "is_team_game": True,
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Uppercase Game",
            "res_model": "gamezone.game",
            "view_mode": "form",
            "res_id": game.id,
            "target": "current",
        }

    # Method 3: Create Game with Default Values
    def action_create_game_defaults(self):
        game = self.env["gamezone.game"].create({
            "game_name": "Default Game",
            "max_players": 4,
            "is_team_game": False,
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Default Game",
            "res_model": "gamezone.game",
            "view_mode": "form",
            "res_id": game.id,
            "target": "current",
        }

    # Method 4: Condition Based Create
    def action_create_game_condition(self):
        is_team_game = True

        if is_team_game:
            game_values = {
                "game_name": "Football",
                "max_players": 11,
                "is_team_game": True,
            }
        else:
            game_values = {
                "game_name": "Chess",
                "max_players": 2,
                "is_team_game": False,
            }

        game = self.env["gamezone.game"].create(game_values)

        return {
            "type": "ir.actions.act_window",
            "name": "Condition Based Game",
            "res_model": "gamezone.game",
            "view_mode": "form",
            "res_id": game.id,
            "target": "current",
        }

    # Method 5: Create New Game from Current Record
    def action_create_game_from_current(self):
        self.ensure_one()

        game = self.env["gamezone.game"].create({
            "game_name": self.game_name + " Copy",
            "max_players": self.max_players,
            "is_team_game": self.is_team_game,
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Copied Game",
            "res_model": "gamezone.game",
            "view_mode": "form",
            "res_id": game.id,
            "target": "current",
        }

    # Method 6: Create Tournament from Current Game
    def action_create_tournament_from_game(self):
        self.ensure_one()

        tournament = self.env["gamezone.tournament"].create({
            "tournament_name": self.game_name + " Tournament",
            "game_id": self.id,
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Created Tournament",
            "res_model": "gamezone.tournament",
            "view_mode": "form",
            "res_id": tournament.id,
            "target": "current",
        }

    # Method 7: Create Three Games in One Click
    def action_create_three_games(self):
        games = self.env["gamezone.game"].create([
            {
                "game_name": "VALORANT",
                "max_players": 5,
                "is_team_game": True,
            },
            {
                "game_name": "CS2",
                "max_players": 5,
                "is_team_game": True,
            },
            {
                "game_name": "PUBG",
                "max_players": 4,
                "is_team_game": True,
            },
        ])

        return {
            "type": "ir.actions.act_window",
            "name": "Created Games",
            "res_model": "gamezone.game",
            "view_mode": "list,form",
            "domain": [("id", "in", games.ids)],
            "target": "current",
        }

    # Method 8: Automatically Set Team Game to True
    def action_create_football_team_game(self):
        game = self.env["gamezone.game"].create({
            "game_name": "Football",
            "max_players": 11,
            "is_team_game": True,
        })

        return {
            "type": "ir.actions.act_window",
            "name": "Football Team Game",
            "res_model": "gamezone.game",
            "view_mode": "form",
            "res_id": game.id,
            "target": "current",
        }

    # Write Method 1: Start Game
    def action_start_game(self):
        self.write({
            "state": "running",
        })

        return True

    # Write Method 2: Finish Game
    def action_finish_game(self):
        self.write({
            "state": "finished",
        })
        return True

    # Write Method 3: Update Winner
    def action_update_winner(self):
        self.write({
            "winner": "Team A",
            "state": "finished",
        })
        return True

    # Write Method 4: Update Score
    def action_update_score(self):
        self.write({
            "team_a_score": 100,
            "team_b_score": 95,
        })
        return True

    # Write Method 5: Condition-Based Update
    def action_update_game_5(self):
        if self.is_team_game:
            self.write({
                "max_players": 20,
            })
        else:
            self.write({
                "max_players": 5,
            })

        return True

    # Write Method 6: Existing Value Based Update
    def action_update_game_6(self):
        self.write({
            "max_players": self.max_players + 5,
        })
        return True
