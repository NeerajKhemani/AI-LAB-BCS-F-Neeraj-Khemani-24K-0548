#Task 1 – Traffic Light Reflex Agent
#Design a simple reflex agent for traffic control.
#Environment states:
#- Heavy Traffic
#- Light Traffic
#Rules:
#If Heavy → Green for longer
#If Light → Normal Green
#Sample Output:
#Percept: Heavy Traffic → Action: Extend Green Time
#Percept: Light Traffic → Action: Normal Green

class Environment:
    def __init__(self, traffic = 'Heavy'):
        self.traffic = traffic

    def get_percept(self):
        return self.traffic

    def change_traffic(self):
     if self.traffic == "Heavy":
        self.traffic = "Light"
     elif self.traffic == "Light":
        self.traffic = "Heavy"


class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        if percept == 'Heavy':
            return 'Extend Green Time'
        else:
            return 'Normal Green'


def run_agent(agent, environment):
        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"Percept - {percept}, Action - {action}")

agent = SimpleReflexAgent()
environment = Environment()
run_agent(agent, environment)

environment.change_traffic()
run_agent(agent, environment)
