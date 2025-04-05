import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# constants for log configuration
LOG_DIR='logs'
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE=5*1024*1024 #5 mb
BACKUP_COUNT=3 # number of backup log file to keep

#construct log file path
log_dir_path=os.path.join(from_root(),LOG_DIR) # from root create logs
os.makedirs(log_dir_path,exist_ok=True) # if already exists , skip
log_file_path=os.path.join(log_dir_path,LOG_FILE) # in logs add datetime file

def configure_logger():
    '''
    configure logging with a rotating file handler and a console handler
    '''
    # create a custom logger
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # define formatter
    formatter = logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s - %(message)s')

    # file handler
    file_handler = RotatingFileHandler(log_file_path,maxBytes=MAX_LOG_SIZE,backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # console handler
    console_handler=logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    # add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# configure the logger
configure_logger()




