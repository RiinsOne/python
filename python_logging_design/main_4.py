import logging.config
# from setting_4 import logger_config
import traceback
import os

#
# logging.config.dictConfig(logger_config)
# logger = logging.getLogger('app_logger')

logger = logging.getLogger('app')
abs_script_path = os.path.abspath(os.path.dirname(__file__))
handler = logging.handlers.RotatingFileHandler(
    '{}'.format(os.path.join(abs_script_path, 'test.log')),
    maxBytes=1 * 1024 * 1024,
    backupCount=2
)
logger.addHandler(handler)

# std_format = logging.Formatter('%(asctime)-12s %(levelname)-12s %(module)s %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
std_format = logging.Formatter(
    '{asctime}.{msecs:0<3.0f}    {levelname:<12}{module}    {message}',
    style='{',
    datefmt='%d.%m.%Y %H:%M:%S'
)
handler.setFormatter(std_format)
logger.setLevel('DEBUG')

logger.debug('-----')

# print(abs_script_path)

words = ['new house', 'apple', 'ice cream', 3]


def get_tb():
    tb = traceback.format_exc().split('\n')
    tb_call = tb[0]
    tb = tb_call + ', '.join(tb[1:])
    return tb[:-2]


def main():
    for item in words:
        try:
            # print(item.split(' '))
            item.split(' ')
        except AttributeError:
            # logger.debug(get_tb())
            logger.info('some error')
            logger.critical('text test')
            logger.warning(get_tb())
            pass
        except Exception as err:
            pass


# def main():
#     for item in words:
#         try:
#             # print(item.split(' '))
#             item.split(' ')
#         except Exception as err:
#             print(err)
#             logger.debug(f'Exception here, item = {item}', exc_info=True)
#             logger.exception(f'Exception here, item = {item}')
#             # logger.info('-----')
#             # print(dir(traceback))
#             print('-----')
#             t1 = traceback.format_exc()
#             # print(t1)
#             t1 = t1.split('\n')
#             print(', '.join(t1))
#             print('-----')
#             # print(t1)
#             pass

if __name__ == '__main__':
    main()
