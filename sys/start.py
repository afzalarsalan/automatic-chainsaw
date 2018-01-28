from flask import Flask, request, redirect, url_for
from flask_cors import CORS
from collections import deque
app = Flask(__name__)

class User:
    # User has:
        # Name
        # Phone
        # Location
        # On Queue or not
    queued = False

    def __init__(self, name, phone, pw):
        self.name = name
        self.password = pw
        self.phone = phone

    def enterQueue():
        queued = True

    def exitQueue():
        queued = False

    def setLocation(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def printInfo(self):
        print ('Name: ' + self.name)
        print ('Password: ' + self.password)
        print ('Phone: ' + self.phone)
    # Increase Queue time ? (Tree set?)

class Team ( ):
    #Attributes:
        # Team name
        # List of users
        # Time
    def __init__(self, teamCode,User):
        self.teamName = teamName
        self.listOfUsers = []
        self.listOfUsers.append(User)

    def add(self,User):
        self.listOfUsers.append(User)

    #def invite

    def getName(self):
        return self.teamName

class UserQueue:
    q = deque()

    def push(user):
        q.append(user)

    def pop():
        return q.popleft()

    def getList():
        return list(q)

    # Remove a user from the queue if they left
    def remove(user):
        q.remove(user)

    # Returns the first 5 players that are present as a team
    # Player may decline but implement that later
    def getTeam():
        tmp = None
        if len(q) >= 5:
            person = q.pop()
            person.exitQueue()
            tmp = Team(q.phone, q.name)
            p = 1
            while p < 5: 
                person = q.pop()
                person.exitQueue()
                tmp.add(person)
                p += 1
        return tmp

class Court:
    teams = []
    empty = True

    def used():
        empty = False

class Gym:
    courts = []
    
    def __init__(self, name, phone, longitude, latitude, numCourts):
        self.name = name
        self.phone = phone
        self.num = numCourts
        self.longitude = longitude
        self.latitude = latitude
        for i in range(numCourts):
            courts.append(Court())

    def nextAvailable(self):
        for i in range(self.num):
            if courts[i].empty:
                return i
        return -1

#Security can't hash right now.
accounts = dict()
q = UserQueue()
TeamQueue = deque()
gyms = dict()

@app.route('/', methods=['POST'])
def addAccount():
    phone = request.form['number']
    name = request.form['name']
    password = request.form['password']
    accounts[phone] = User(name, phone, password)
    accounts[phone].printInfo()
    return 'has been added!'

def listAccounts():
    for v in accounts.values():
        print ('Phone number: ' + v.phone)
        print ('Name: ' + v.name)
        print ('Password: ' + v.password)
    return 'Listed'

@app.route('/register/', methods=['GET', 'POST'])
def verifyAccount():
    phone = request.form['phone']
    password = request.form['password']
    for x in accounts:
        if x.phone is phone:
            return redirect(url_for('success'))
        else:
            return redirect(url_for(''))

@app.route('/success/')
def success():
    return ('successfully logged in')

@app.route('/queueUser/', methods=['POST'])
def queueUser():
    p = accounts[request.form['phone']]
    if not p.queued:
        p.enterQueue()
        q.push(p)

@app.route('/registerCourt/', methods=['POST'])
def addCourt():
    phone = request.form['number']
    longitude = request.form['longitude']
    latitude = request.form['latitude']
    name = request.form['name']
    courts = request.form['courts']
    gym[phone] = Gym(name, phone, longtitude, latitude, courts)
    return None

@app.route('/matchend/<int:court_id>', methods=['POST'])
def matchEnd(court_id):
    won = request.form['won']
    lost = request.form['lost']
    team = q.getTeam()

