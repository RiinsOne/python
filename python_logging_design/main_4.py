import logging.config
from setting_4 import logger_config


logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


words = ['new house', 'apple', 'ice cream', 3]



def main():
    for item in words:
        try:
            print(item.split(' '))
        except:
            # logger.debug(f'Exception here, item = {item}', exc_info=True)
            logger.exception(f'Exception here, item = {item}')
            pass

if __name__ == '__main__':
    main()
