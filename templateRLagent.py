"""
Placeholder class for communication with code base
Allows the current decision maker to be overriden with your RL input

 - Decision encoding: [0,1,2,NaN] = [left change, right change, no change, let MPC decide]
"""

# Notes:
# - Feel free to edit this file as appropriate, changing template names requires changes troughout code base

class RLAgent:
    """
    RL agent class:
    Decides the appropriate choice of MPC pathplanner

    Methods:
    - setTrafficState: Fetches the current traffic state
    - setEgoVehicleState: Fetches the current ego vehicle state
    - getDecision: Returns the appropriate trajectory option to decision master

    Variables:
    - trafficState: Current state of traffic
    - egoState: Current state of the ego vehicle
    - decision: Current decision made by the RL agent
    """
    def __init__(self):
        self.trafficState = []
        self.egoState = []
        self.decision = float('nan')

    def setTrafficState(self):
        pass
    def setEgoVehicleState(self):
        pass

    def getDecision(self):
        # Returns final decision for RL agent
        return self.decision

