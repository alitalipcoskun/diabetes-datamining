import logging
from logging import handlers
import os
import sys

class CustomLogger(object):
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR
    }
    
    
    def __init__(self,
                 log_dir: str = "..",
                 filename: str="logs.log",
                 level: str="debug",
                 when: str="D",
                 back_count:int = 3,
                 format: str = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s') -> None:
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), log_dir))

        log_dir = os.path.join(root_dir, "logs")

        os.makedirs(log_dir, exist_ok=True) 
        
    
        log_path = os.path.join(log_dir, filename)
        print(log_path)
        
        self.__logger = logging.getLogger(log_path)
        self.logger.setLevel(self.level_relations.get(level))
        
        str_format = logging.Formatter(format)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(str_format)
        
        th = handlers.TimedRotatingFileHandler(filename=log_path, when=when, backupCount=back_count, encoding='utf-8')
        th.setFormatter(str_format)
        
        self.logger.addHandler(console_handler)
        self.logger.addHandler(th)
        
        
    @property
    def logger(self):
        return self.__logger