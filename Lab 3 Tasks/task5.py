import random
class LearningBasedAgent:
    def __init__(self, actions):
        self.Q = {}
        self.actions = actions
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1

    def get_Q_value(self, state, action):
        return self.Q.get((state, action), 0.0)

    def select_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        else:
            return max(self.actions, key=lambda a: self.get_Q_value(state, a))

    def learn(self, state, action, reward, next_state):
        old_Q = self.get_Q_value(state, action)
        best_future_Q = max([self.get_Q_value(next_state, a) for a in self.actions])
        self.Q[(state, action)] = old_Q + self.alpha * (reward + self.gamma * best_future_Q - old_Q)

    def act(self, state):
        return self.select_action(state)


class Environment:
    def __init__(self, state="Game Time"):
        self.state = state

    def get_percept(self):
        return self.state

    def get_reward(self, action):
        if action == "Play":
            return 5
        elif action == "Rest":
            return 1


def run_agent(agent, environment, steps):
    for step in range(steps):
        state = environment.get_percept()
        action = agent.act(state)
        reward = environment.get_reward(action)

        print(f"Step {step + 1}: Action {action} Reward {reward}")

        next_state = environment.get_percept()
        agent.learn(state, action, reward, next_state)

    print("\nQ-table Updated")
    print(agent.Q)


agent = LearningBasedAgent(["Play", "Rest"])
environment = Environment()

run_agent(agent, environment, 10)
