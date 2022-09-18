import logging


logging.basicConfig()
# logger = logging.getLogger()
# print(logger)


app_logger = logging.getLogger('app_logger')

console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)

f = logging.Formatter(fmt='%(levelname)s - %(name)s - %(message)s')
console_handler.setFormatter(f)

utils_logger = logging.getLogger('app_logger.utils')
utils_logger.setLevel('DEBUG')
# utils_logger.propagate = False  # отключить использование родительских хендлеров




# root.app_logger.utils_logger



def main():
    utils_logger.debug('OG Black')


if __name__ == '__main__':
    main()
