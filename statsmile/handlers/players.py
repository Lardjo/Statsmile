#!/usr/bin/env python3

import tornado.web

from .base import BaseHandler
from bson import ObjectId


class PlayersHandler(BaseHandler):
    def get(self):
        session = self.application.db["users"].find_one({"_id": ObjectId(self.current_user)})
        players = self.application.db["users"].aggregate([
            {"$unwind": "$matches"},
            {"$project": {"avatar": 1, "steamid": 1, "matches": 1, "personaname": 1, "count": {"$add": [1]}}},
            {"$group": {"_id": "$personaname", "number": {"$sum": "$count"}, "steam": {"$first": "$steamid"}, "avatar": {"$first": "$avatar"}}},
            {"$sort": {"number": -1}},
            {"$limit": 50}
        ])
        self.render("players.html", session=session, players=players)