import sys


def error_message_details(error, error_detail:sys):
    # Execution info
    _, _, exc_tb = error_detail.exc_info()
    
    # exc_tb variable includes which file the exception is occured on which line number etc.
    
    filename = exc_tb.tb_frame.f_code.co_filename
    
    error_message = f"An error occured! [{filename}]-[]-[]"
    
    