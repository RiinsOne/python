class Robot:

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('Hi there! I\'m ', self.name)


robot = Robot()

attr_name = 'model'
if hasattr(robot, attr_name):
    # hasattr(object, name) - проверка существования
    print(robot.model)
else:
    setattr(robot, attr_name, 'android')
    # robot.model = 'android'
    # setattr(object, name, value) - установка
print(robot.model)
print(getattr(robot, attr_name))
# delattr(object, name) - удаление
# delattr(robot, attr_name)
# print(robot.model)
