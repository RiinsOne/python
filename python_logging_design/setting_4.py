logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '%(asctime)s.%(msecs)03d %(levelname)-8s %(module)s %(message)s',
            # 'format': '{asctime}.{msecs:0<3.0f} - {levelname} - {pathname}:{lineno}\t{message}',
            # 'style': '{',
            'datefmt': '%d.%m.%Y %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console'],
            # 'propagate': False
        }
    },

    # 'filters': {},
    # 'root': {}  # '': {}
    # 'incremental': True,
}
