import User.py
import Teams.py
import Account.py
import time
from collections import deque, stack

class Queues:
    randomQueue = deque()
    randomTeamQueue = deque()
    
    
    rqlength = 0
    rtqlength = 0
    

    ##### Emergency Queue #####
    kick = []

    # Check who's currently on the Emergency Queue
    def currentList():
        return kick
        # Add to front end when starting the app and entering as solo player

    # Add a team to the Emergency Queue
    def addKick(team):
        kick.append(team)
        # Signal from Timer to front end as well

    #Need to add kick, and countdown signals

    ##### Team Queue #####
    teamQueue = deque()

    # Returns the next 10 teams on the teams queue
    # Call this to front end when:
        # 1 team has been popped as they go to a match
        # There is a leaver in 1 team
    def nextTen():
        ret = []
        i = 0
        while teamQueue and i < 10:
            ret.append(teamQueue.pop())
            i += 1
        for team in reversed(ret):
            teamQueue.appendleft(team)
        return ret

    # Adds a team to the Team Queue
    def addTeam(team):
        teamQueue.append(team)

    # Gets next team from the Team Queue which has 5 people
    def popTeam():
        s = stack()
        nextteam = None
        while teamQueue and nextteam is None:
            tmp = teamQueue.pop()
            if len(tmp.listOfUsers) is 5:
                nextteam = tmp
            else:
                s.append(tmp)
        while s:
            teamQueue.appendleft(s.pop())
        return nextteam
        # Make sure front end update after this

    # Kick a specific team, assuming it exists
    def kickTeam(team):
        teamQueue.remove(team)

    
    # Never more than 5?
    def pushUser(user):
        uq.append(user)
        ulength += 1
        if ulength == 5:
            tmp = Team('Random Team '+(tlength+1), popUser())
            while uq:
                tmp.add(uq.popleft())
            tq.append(tmp)
        ulength = 0

    def push(team):
        tq.append(team)
        tlength += 1

    def pop():
        return tq.popleft()

    def popUser():
        return uq.popleft()

    #def removeUser(
        
