import Account.py
import Teams.py
import User.py
from collections import deque

class TeamQueue:
    q = deque()

    def push(team):
        q.append(team)

    def pop():
        q.popleft()
