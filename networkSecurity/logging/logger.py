# Import the built-in logging module to record application events
import logging

# Import os module to work with file and folder paths
import os

# Import datetime class to generate timestamps
from datetime import datetime


# Create a unique log file name using the current date and time
# Example: 07_28_2026_00_45_12.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Create the path for the logs folder
# os.getcwd() returns the current working directory
# Example: D:\NetworkSecurity\logs
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)   ## no need to write LOG_FILE ,its create a folder(and inside a file same name )


# Create the logs directory if it does not already exist
# exist_ok=True prevents an error if the folder already exists
os.makedirs(logs_path, exist_ok=True)


# Create the full path of the log file
# Example:
# D:\NetworkSecurity\logs\07_28_2026_00_45_12.log\07_28_2026_00_45_12.log
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# Configure the logging system
logging.basicConfig(

    # Save all logs to this file
    filename=LOG_FILE_PATH,

    # Define how each log message should look
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",

    # Record INFO level and higher messages
    # Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
    level=logging.INFO,
)