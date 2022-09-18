import logging.config
from setting_5 import logger_config


logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def new_function():
    name = 'black'

    logger.debug('Enter in to the new_function()', extra={'black_name': name})


def main():
    logger.debug('Enter in to the main()')

if __name__ == '__main__':
    new_function()
    main()
