import sys
import logging



def error_message_detail(error:Exception, error_detail: sys):
    '''
    extract detailed error information including file name , line name and the error message
    :param error : the exception that occurred
    :param error_detail : the sys module to access traceback details.
    :return : A formatted error message string
    '''
    # Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()

    # get the file name where the exception happened
    filename = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"

    # get the line numbber where the exception happend
    line_number = exc_tb.tb_lineno if exc_tb else "Unknown"

    # create a formatted error messsage string with filename,linenumber and the actual error 
    error_message = f"Error occurred in python script: [{filename} at line: {line_number}] : {str(error)}"

    # log the error for the better tracking
    logging.error(error_message)

    return error_message



class MyException(Exception):
    '''
    custom exception class for handling errors 
    '''
    def __init__(self, error_message: str, error_detail: sys):
        '''initialize the exception with a detailed error message.
        :param error_message : A string describing the error
        :param error_detail : The sys module to access traceback details.
        '''

        # Call the basic class constructor with the error message
        super().__init__(error_message)

        # format the detailed error message using the error_message_detail function
        self.error_message =error_message_detail(error_message, error_detail)

    def __str__(self) :
        '''
        returns the string representation of the error message
        '''
        return self.error_message