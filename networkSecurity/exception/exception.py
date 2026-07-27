# Import the sys module.
# It provides access to Python's runtime information.
# We use sys.exc_info() to get details about the current exception.
import sys


# Create a custom exception class by inheriting from Python's Exception class.
# This allows us to display more meaningful error messages.
class NetworkSecurityException(Exception):

    # Constructor
    # error_message -> Original exception object (e.g., ZeroDivisionError)
    # error_details -> sys module (used to get traceback information)
    def __init__(self, error_message, error_details: sys):

        # Store the original error message
        self.error_message = error_message

        # exc_info() returns a tuple:
        # (exception_type, exception_value, traceback)
        _, _, exc_tb = error_details.exc_info()

        # Store the line number where the exception occurred.
        self.lineno = exc_tb.tb_lineno

        # Store the filename where the exception occurred.
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    # This method is automatically called when the exception object is printed.
    # Example:
    # print(e)
    # or
    # raise NetworkSecurityException(...)
    def __str__(self):

        return (
            "Error occurred in python script "
            "name [{0}] line number [{1}] "
            "error message [{2}]".format(
                self.file_name,
                self.lineno,
                str(self.error_message)
            )
        )


# # This block runs only when this file is executed directly.
# # It will not execute if this file is imported into another Python file.
# if __name__ == "__main__":

#     try:
#         # Generate an exception intentionally.
#         # Division by zero raises ZeroDivisionError.
#         a = 1 / 0

#         # This line never executes because the exception occurs above.
#         print("This will not be printed", a)

#     except Exception as e:
#         # Catch the original exception.

#         # Raise our custom exception instead.
#         # It includes:
#         # - File name
#         # - Line number
#         # - Original error message
#         raise NetworkSecurityException(e, sys)