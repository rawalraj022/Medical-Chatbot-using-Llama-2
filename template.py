# Template file is used to create the folders and files in the specified paths.
# If we execute Template file then it will create the folders and files in the specified paths 
    # and also log the information of the folder creation and file creation.


import os       #os is operating system dependent module and provides a way of using operating system dependent functionality.      
from pathlib import Path   # The Pathlib module in Python simplifies the way in working with file system paths. It uses classes instead of module-level functions.
import logging      # The logging module in Python is a powerful built-in module used to record diagnostic information or status information and history. 

# create a logging string in python to log the information of the folder creation. 
    # Why we need to create logging string f?
        # Because when ever we will execute template.py file, so it will also 
            # show us the log on the terminal whether this folder has been created or not. 
                # So, if folder is created then it will show us why folder is created and if 
                    # folder is not created then it will show us why folder is not created.
                        # and also logging string will show us the location as well where folder is created.
                        # So, to log these are the information we need to create logging string.
    # logging is inbuilt module in python which is used to log the information.

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

    # logging.basicConfig() function is used to set up the default handler and formatter for the logging and it will log the information.
    # level=logging.INFO: This is the logging level which is used to set the threshold level of logging and it will log the information which is greater than or equal to the INFO level.
    # format='[%(asctime)s]: %(message)s:': This is the format of the logging string and it will log the time and message.
        # [%(asctime)s]: This is the time when the log is generated and this will be replaced by the time when the log is generated.
        # %(message)s: This is the message which we want to log and this will be replaced by the message which we want to log.

list_of_files = [     # list_of_files is a list which is used to store the file paths.
    "src/__init__.py",  # __init__.py is used to treat the directory as a package and it will initialize the package.
    "src/helper.py",   # helper.py is used to write the helper functions.
    "src/prompt.py",  # prompt.py is used to write the prompt functions.
    ".env",          # .env is used to store the environment variables.
    "setup.py",        # setup.py is used to write the setup functions.
    "research/trials.ipynb",  # trials.ipynb is used to write the trials.
    "app.py",          # app.py is used to write the main application.
    "store_index.py",    # store_index.py is used to write the store index.
    "static/.gitkeep",   # .gitkeep is used to keep the empty directory in the git.
    "templates/chat.html"  # chat.html is used to write the chat template.

]

# Logic to create folders and files in the specified paths.

for filepath in list_of_files:     # filepath is a variable which is used to store the value of list_of_files and for loop to loop through the list_of_files.  

    # File path 'filepath' first of all we need to convert them to path. 
    # So, for that we need to use 'Path()' function and inside that we need to give the file path.

    filepath = Path(filepath)    # Path() function is used to convert the string to path object.

    # First upall, It will detect the operating system we are using and will convert the string to path object accordingly.

    # Separate the folder and file from the given file path using os.path.split method.
    filedir, filename = os.path.split(filepath)   # os.path.split() method is used to split the path name into a pair head and tail.

    # Check if the directory exists, if not, create it using 'os.makedirs'
    if filedir !="":           # If the filedir is not empty then it will create the directory.
        os.makedirs(filedir, exist_ok=True)     # os.makedirs() method is used to create a directory recursively and it will create the directory if it does not exist and 
                                                    # filedir is the directory name and 'exist_ok=True' is used to avoid the error if the directory already exists and not create the directory again.
        # Now we need to log the information of the directory creation.
        logging.info(f"Creating directory; {filedir} for the file {filename}")    # logging.info() is used to log the information and f is used to format the string and filedir is the directory name and filename is the file name.
    
    # Now after creating the folder we need to create the file inside the folder.
        # for that we need to write another logic to create the file inside the folder. 

    # Check if the file exists, if not, create it.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
        # Check if the file exists, if not, create it using 'open' method. 
        # 'os.path.exists(filepath)' is used to check whether the file exists or not.
        # 'os.path.getsize(filepath)' is used to get the size of the file.
        # 'os.path.getsize(filepath) == 0' is used to check whether the file is empty or not.
        # 'open' method is used to open the file and it will create the file if it does not exist.
        # 'w' is used to write the file and 'with' is used to open the file and close the file after writing the file.
        # 'pass' is used to do nothing and it is used to avoid the error if the file is already created.
        # 'logging.info()' is used to log the information of the file creation.
        # f is used to format the string and 
        # filepath is the file path.
        
    
    
    # If the file already exists, log the information.
    else:
        logging.info(f"{filename} is already created")

















