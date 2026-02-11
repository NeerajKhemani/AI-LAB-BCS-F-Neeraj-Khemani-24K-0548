class FirefightingRobot:
    def __init__(self, path):
        self.path = path

    def act(self, room, environment):
        if environment.rooms[room] == "fire":
            print(f"Fire detected in room {room} → Extinguishing fire")
            environment.extinguish_fire(room)
        else:
            print(f"Room {room} is safe → Moving on")


class Environment:
    def __init__(self):
        self.rooms = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }

        self.grid = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'j']
        ]

    def extinguish_fire(self, room):
        self.rooms[room] = "safe"

    def display(self):
        print("\nEnvironment Status:")
        for row in self.grid:
            for room in row:
                if self.rooms[room] == "fire":
                    print("F", end=" ")   
                else:
                    print(" ", end=" ")   
            print()
        print()


def run_robot(robot, environment):
    for step, room in enumerate(robot.path):
        print(f"Step {step + 1}: Robot enters room {room}")
        robot.act(room, environment)
        environment.display()

    print("Final Status: All rooms checked and fires extinguished.")


path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

environment = Environment()
robot = FirefightingRobot(path)

run_robot(robot, environment)
