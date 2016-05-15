import requests
import sys
import pytz
from datetime import date, datetime, timedelta

from utils import *
from settings import KEY, TOKEN, BOARD_ID, MEMBER_ID, TIMEZONE
from core.actions_presenter import ActionsPresenter


class TrelloBot:

    API_BASE_URL = 'https://api.trello.com/1'
    KEY = None
    TOKEN = None
    BOARD_ID = None
    MEMBER_ID = None
    TIMEZONE = None

    presenter = None
    
    def __init__(self, key, token, board_id, member_id, timezone=pytz.utc):
        self.KEY = key
        self.TOKEN = token
        self.BOARD_ID = board_id
        self.MEMBER_ID = member_id
        self.TIMEZONE = timezone
        self.presenter = ActionsPresenter(timezone)

    def fetch_my_actions(self, start_period, end_period):
        params = {
            'limit': 1000,
            'memberCreator': 'false',
            'member_fields': 'fullName',
            'since': start_period,
            'before': end_period,
            'fields': 'type,date,data',
            'filter': 'addMemberToCard,removeMemberFromCard',
            'key': self.KEY,
            'token': self.TOKEN
        }
        actions = requests.get('{url}/boards/{board_id}/actions?{params}'.format(
            url=self.API_BASE_URL,
            params=fast_urlencode(params),
            board_id=self.BOARD_ID)).json()
        # loop thru actions and show only mine
        my_actions = []
        for action in reversed(actions):
            if action['member']['id'] == self.MEMBER_ID:
                my_actions.append(action)
        self.presenter.present(my_actions)
        

if __name__ == '__main__':
    if len(sys.argv) == 3:
        start_period = sys.argv[1]  # assuming %Y-%m-%d format
        end_period = sys.argv[2]
    else:
        # for the previous workday - if today is monday, show actions since friday
        weekday = date.today().weekday()
        if (weekday == 0):  # Monday
            start_period = (date.today() - timedelta(days=3)).strftime('%Y-%m-%d')
        elif (weekday == 6):  # Sunday
            start_period = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')
        else:  # Saturday and any other days
            start_period = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        end_period = date.today().strftime('%Y-%m-%d')

    bot = TrelloBot(KEY, TOKEN, BOARD_ID, MEMBER_ID, TIMEZONE)
    bot.fetch_my_actions(start_period, end_period)
