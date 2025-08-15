import sys

def error_message_detail(error, error_detail: sys):
    """
    Formats a detailed error message with filename and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Create the formatted error message string
    error_message = "error occurred in python script [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    # Return the created string
    return error_message

class CustomException(Exception):
    """
    Custom exception class that provides a formatted error message.
    """
    def __init__(self, error_message, error_detail: sys):
        # Correctly call the parent class's __init__ method
        super().__init__(error_message)
        # Generate the detailed error message using the helper function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        # Return the formatted error message when the exception is printed
        return self.error_message

# --- Example Usage ---
