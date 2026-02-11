class GoalBasedAgent:
    def __init__(self, goal_subjects):
        self.goal_subjects = goal_subjects
        self.completed = []

    def update_model(self, subject):
        self.completed.append(subject)

    def predict_action(self, subject):
        return f"Studying {subject}"

    def act(self, subject):
        self.update_model(subject)
        return self.predict_action(subject)

    def goal_achieved(self):
        return set(self.completed) == set(self.goal_subjects)


class Environment:
    def __init__(self):
        self.subjects = ["AI", "Math", "Physics"]

    def get_next_subject(self):
        if self.subjects:
            return self.subjects.pop(0)
        return None


def run_agent(agent, environment):
    step = 0
    while not agent.goal_achieved():
        subject = environment.get_next_subject()
        if subject is None:
            break
        action = agent.act(subject)
        step += 1
        print(f"Step {step}: {action}")

    print("Goal Achieved: All subjects completed")


environment = Environment()
agent = GoalBasedAgent(["AI", "Math", "Physics"])

run_agent(agent, environment)
