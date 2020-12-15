class Toyota:

    def __init__(self):
        self.color = 'red metallic'
        self.price = '1 000 000 rub'
        self.max_velocity = '200 km/h'
        self.current_velocity = '0 km/h'
        self.engine_rpm = 0

    def start(self):
        print('Engine is started')
        self.engine_rpm = 900

    def go(self):
        print('Go!')
        self.engine_rpm = 2000
        self.current_velocity = '20 km/h'


my_car = Toyota()
print('color', my_car.color)
print('price', my_car.price)
print('max_velocity', my_car.max_velocity)
print('rpm', my_car.engine_rpm)
print('current velocity', my_car.current_velocity)

my_car.start()
print('rpm', my_car.engine_rpm)
my_car.go()
print('rpm', my_car.engine_rpm)
print('current_velocity', my_car.current_velocity)

produced, plan = 0, 100
stock = []
while produced < plan:
    new_car = Toyota()
    stock.append(new_car)
    produced += 1


class Robot:

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('Hi there! I\'m ', self.name)


robot = Robot()
robot.hello()

robot_2 = robot
robot_2.hello()

robot_3 = robot_2
robot_3.hello()

robot_3.name = 'C-3PO'
robot_3.hello()

robot.hello()
