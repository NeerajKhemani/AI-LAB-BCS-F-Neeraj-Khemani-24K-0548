class UtilityBasedAgent:
    def __init__(self):
        pass

    def calculate_utility(self, distance, rating):
        return rating - distance

    def select_action(self, restaurants):
        utilities = {}

        for name, info in restaurants.items():
            utility = self.calculate_utility(info['distance'], info['rating'])
            utilities[name] = utility
            print(f"Restaurant {name} Utility = {utility}")

        # select restaurant with maximum utility
        best = max(utilities, key=utilities.get)
        return best


class Environment:
    def __init__(self):
        self.restaurants = {
            'A': {'distance': 5, 'rating': 7},
            'B': {'distance': 5, 'rating': 9}
        }

    def get_percept(self):
        return self.restaurants


def run_agent(agent, environment):
    percept = environment.get_percept()
    selected = agent.select_action(percept)
    print("\nSelected Restaurant:", selected)


agent = UtilityBasedAgent()
environment = Environment()


run_agent(agent, environment)
