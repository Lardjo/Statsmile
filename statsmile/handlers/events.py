#!/usr/bin/env python3

import math

from motor import Op
from tornado.gen import engine
from tornado.web import asynchronous
from .base import BaseHandler
from statsmile.common import libs


class EventsHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):

        pg = int(self.get_argument('page', 1))

        session = None
        if self.current_user:
            session = yield Op(self.db['users'].find_one, {'_id': self.current_user['userid']})


        cursor = self.application.db['matches'].find({'game_mode': {'$in': [7, 9, 15]}})
        pages = yield Op(cursor.count)

        max_pages = math.ceil(pages / 20)

        if pg > max_pages:
            return self.send_error(404)

        cursor = self.application.db['matches'].find({'game_mode': {'$in': [7, 9, 15]}},
                                                     sort=[('start_time', -1)],
                                                     limit=20).skip((pg-1)*20)
        event = yield Op(cursor.to_list)

        self.render('events.html', title="Events", session=session, event=event, heroes=libs.heroes,
                    mode=libs.mode, cluster=libs.cluster, page=pg, max_pages=max_pages)