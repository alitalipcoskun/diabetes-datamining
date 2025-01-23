import logging
from logging import handlers

class CustomLogger(object):
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR
    }
    
    
    def __init__(self,
                 filename: str="logs.log",
                 level: str="debug",
                 when: str="D",
                 back_count:int = 3,
                 format: str = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s') -> None:
        
        self.__logger = logging.getLogger(filename)
        str_format = logging.Formatter(format)
        self.logger.setLevel(self.level_relations.get(level))
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(str_format)
        
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=back_count, encoding='utf-8')
        th.setFormatter(str_format)
        self.logger.addHandler(console_handler)
        self.logger.addHandler(th)
        
        
    @property
    def logger(self):
        return self.__logger