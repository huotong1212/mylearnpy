import logging


loggerRoot = logging.getLogger()
loggerRoot.setLevel(logging.WARNING)

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
# rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
#
# f_handler = logging.FileHandler('error.log')
# f_handler.setLevel(logging.ERROR)
# f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# logger.addHandler(rf_handler)
# logger.addHandler(f_handler)

sr = logging.StreamHandler()
fh = logging.FileHandler('test.log')

sr.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

fm = logging.Formatter("%(asctime)s  %(message)s")
fm2 = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")

# sr.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

sr.setFormatter(fmt=fm)
fh.setFormatter(fm2)

loggerRoot.addHandler(fh)
logger.addHandler(sr)

loggerRoot.debug('root debug message')
loggerRoot.info('root info message')
loggerRoot.warning('root warning message')
loggerRoot.error('root error message')
loggerRoot.critical('root critical message')

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')