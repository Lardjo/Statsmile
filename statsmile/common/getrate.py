#!/usr/bin/env python3


def dota_rate(matches, user):
    mt = matches
    for (win, offset) in enumerate(mt):
        if len(offset['players']) < 10:
            del mt[win]
        for player in offset['players']:
            if not ('leaver_status' or 'hero_id') in player:
                del mt[win]
            elif player['hero_id'] == 0:
                del mt[win]
            elif player['leaver_status'] == 3:
                del mt[win]
            else:
                pass
        else:
            pass
    temp = rate(mt, user)
    return temp


def rate(matches, user):
    temp = {}
    wins = 0
    loses = 0
    temp['dota_count'] = len(matches)
    for match in matches:
        for player in match['players']:

            if 'account_id' in player:
                if player['account_id'] == user:
                    if match['radiant_win'] and player['player_slot'] in (0, 1, 2, 3, 4):
                        wins += 1
                    elif not match['radiant_win'] and player['player_slot'] in (128, 129, 130, 131, 132):
                        wins += 1
                    else:
                        loses += 1
                else:
                    pass
            else:
                pass
    temp['dota_wins'] = wins
    temp['dota_loses'] = loses
    return temp