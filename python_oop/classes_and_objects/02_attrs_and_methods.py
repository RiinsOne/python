class Robot:

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('Hi there! I\'m ', self.name)

    def go(self, x, y):
        print('Moving to point ', x, y)


robot = Robot()
robot.go(x=100, y=200)

robot.temperature = 1

while robot.temperature < 10:
    robot.temperature *= 2
print(robot.temperature)
print(robot.__dict__)  # {'name': 'R2D2', 'temperature': 16}
del robot.temperature
print(robot.__dict__)  # {'name': 'R2D2'}
# print(robot.temperature)  # AttributeError: 'Robot' object has no attribute 'temperature'

print('-----')

robot_2 = Robot()
robot_2.name = 'Wall-E'

print(robot.name, robot_2.name)
print(robot, robot_2)
print(robot == robot_2, robot is robot_2)

print('-----')

for attr_name in ('weight', 'height', ):
    setattr(robot, attr_name, 42)
print(hasattr(robot, 'weight'))
print(robot.weight)
print(getattr(robot, 'height'))
