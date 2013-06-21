#!/usr/bin/env python3

import requests
import json
import xml.etree.ElementTree as ET

from functools import reduce


class GetUserStats:
    """
    Class Get User Stats
    Main class for get user statistics
    """
    def __init__(self, steamid, apikey):
        """
        Init function
        Default settings
        """
        self.steamid = steamid
        self.apikey = apikey
        self.match_id = None
        self.dict = {'steam': {}, 'games': {}, 'dota-game': {}}
        self.steam()
        self.dota()
        self.games()


    def steam(self):
        """
        Steam function
        Get all information about user
        """
        r = requests.get("http://steamcommunity.com/profiles/{0}?xml=1".format(self.steamid))
        f = r.text
        root = ET.fromstring(f.encode('utf-8'))
        for child in root:
            self.dict['steam'][child.tag] = child.text


    def dota(self):
        """
        Dota 2 function
        Get information about last match
        """
        options = {'matches_requested': '1', 'account_id': self.steamid, 'key': self.apikey} # Options
        r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/", params=options)
        f = json.loads(r.text)
        self.match_id = f['result']['matches'][0]['match_id'] or None # Get ID Match
        options = {'match_id': self.match_id, 'key': self.apikey} # Set new options for request
        r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/", params=options)
        f = json.loads(r.text)
        self.dict['dota-game'] = f['result']


    def games(self):
        """
        Steam Games function
        Get list games and parser top
        """
        games = {}
        total_games = 0
        r = requests.get("http://steamcommunity.com/profiles/{0}/games?xml=1".format(self.steamid))
        f = r.text
        root = ET.fromstring(f.encode('utf-8'))

        for a in root.findall('./games/game'):

            total_games += 1

            try:
                hours = a.find('hoursOnRecord').text
                name = a.find('name').text
                logo = a.find('logo').text
                appid = a.find('appID').text

                if ',' in hours:
                    hours = hours.replace(",", "")
                    games[appid] = {"name": name, "hours": float(hours), "logo": logo}
                else:
                    games[appid] = {"name": name, "hours": float(hours), "logo": logo}
            except:
                pass

        time = reduce(lambda a, b: a + b, map(lambda x: x[1]['hours'], games.items()))
        dict_as_list = games.values()
        best = sorted(dict_as_list, key=lambda k: k['hours'], reverse=True)[:6]
        best_time = reduce(lambda a, b: a + b, map(lambda x: x['hours'], best))
        other_time = time - best_time
        self.dict['games'] = {"total-time": time,
                              "total-games": total_games,
                              "other-time": other_time,
                              "best-time": best_time,
                              "best-1": {"name": best[0]['name'], "avatar": best[0]['logo'], "hours": best[0]['hours']},
                              "best-2": {"name": best[1]['name'], "avatar": best[1]['logo'], "hours": best[1]['hours']},
                              "best-3": {"name": best[2]['name'], "avatar": best[2]['logo'], "hours": best[2]['hours']},
                              "best-4": {"name": best[3]['name'], "avatar": best[3]['logo'], "hours": best[3]['hours']},
                              "best-5": {"name": best[4]['name'], "avatar": best[4]['logo'], "hours": best[4]['hours']},
                              "best-6": {"name": best[5]['name'], "avatar": best[5]['logo'], "hours": best[5]['hours']},
        }


if __name__ == "__main__":
    print("Ok! You just run this file. Don't import")
