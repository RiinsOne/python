import logging
import os


class MegaHandler(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        abs_script_folder_path = os.path.abspath(os.path.dirname(__file__))
        self.filename = os.path.join(abs_script_folder_path, filename)

    def emit(self, record):
        message = self.format(record)
        with open(self.filename, 'w') as file:
            file.write(message + '\n')


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
        },
        'file': {
            '()': MegaHandler,
            'level': 'DEBUG',
            'filename': 'debug_6.log',
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            # 'propagate': False
        }
    }
}
