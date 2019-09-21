exitCount = 0
enterCount = 0
numEntranceEscalators = 2
numExitEscalators = 2
time = 0
dt = 1

class Escalator:
    def __init__(self):
        self.IsEntranceEscalator = True
        self.escBoundStart = 0.0
        self.escBoundEnd = 100.0

class PassengerSection:
    def __init__(self):
        maxoccupancy = 100
        canaddpassenger = True

class PassiveRideSection:
    def __init__(self):
        basemoverate = 10.0
        occupancy = 75

class ActiveRideSection:
    def __init__(self):
        basemoverate = 10.0
        occupancy = 75

class Passenger:
    def __init__(self,l):
        moverate = 4
        occupancy = 75
        location = l
        position = 0.0
        isEnteringPassenger = True
        tempPosition = 0.0

    def enter(self):
        return

    def move(self):
        return

    def exit(self):
        return

    def onBoard(self):
        return

    def offBoard():
        return

class ActivePassenger:
    def __init__(self):
        activemoverate = 3

class EntranceArea:
    def __init__(self):
        maxflow = 0.0
        currentflow = 0.0
        entrancestart = 0.0
        entranceend = 100
        currentoccupancy = 0
        maxoccupancy = 0

    def generateEntPassenger(self):
        return

class ExitArea:
    def __init__(self):
        maxflow = 0.0
        currentflow = 0.0
        exitstart = 0.0
        exiteend = 100
        currentoccupancy = 0
        maxoccupancy = 0

    def generateExitPassenger(self):
        return
