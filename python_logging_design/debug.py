import logging


logging.basicConfig(level='DEBUG', filename='mylog.log')
logger = logging.getLogger()
print(logger)  # <RootLogger root (WARNING)>

print()
# logger.setLevel('DEBUG')  # logging.DEBUG

print(logger.level)  # 30
print()

print(logger.handlers)


def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')
    # print(dir(logger))

if __name__ == '__main__':
    main('og')
