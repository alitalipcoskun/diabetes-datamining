

class InvalidTresholdError(Exception):
    
    def __init__(
        self,
        treshold_value,
        msg
    ):
        self.__treshold_value = treshold_value
        self.__msg = msg
        
        super().__init__(msg)
        
        
    
    def __str__(self):
        return f"{self.__treshold_value} -> {self.__msg}"