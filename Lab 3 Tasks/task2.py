import random
class Environment:
    def __init__(self, students_present= "No", light_status="OFF"):
        self.students_present = students_present
        self.light_status = light_status

    def get_percept(self):
        return self.students_present, self.light_status

    def update_students(self):
        self.students_present = random.choice(["Yes", "No"])

    def set_light(self, status):
        self.light_status = status


class ModelBasedAgent:
    def __init__(self):
        self.prev_students = None
        self.prev_light = None

    def act(self, percept):
        students, light = percept

        if students == "Yes" and light == "OFF":
            action = "Turn lights ON"
            new_light = "ON"
        elif students == "No" and light == "ON":
            action = "Turn lights OFF"
            new_light = "OFF"
        else:
            action = "No action"
            new_light = light

        self.prev_students = students
        self.prev_light = new_light

        return action, new_light

    def show_model(self):
        print(f"Internal Model → Previous Students: {self.prev_students}, Previous Light: {self.prev_light}")


def run_agent(agent, environment, steps=8):
    for step in range(1, steps + 1):
        print(f"\nStep {step}")

        environment.update_students()
        percept = environment.get_percept()

        action, new_light = agent.act(percept)
        environment.set_light(new_light)

        print(f"Percept → Students Present: {percept[0]}, Light Status: {percept[1]}")
        print(f"Action → {action}")
        agent.show_model()

agent = ModelBasedAgent()
environment = Environment()

run_agent(agent, environment)
