# This file is used to install the package in the local system using the command: pip install -e .
# This command will install the package in the local system and we can use the package in any other python file by importing the package name.
# The package name is the name of the folder where the package is stored.


from setuptools import find_packages, setup  # 'find_packages' method will look for constructor file('__init__.py') in each and every folder and 
                                                # when 'find_packages' will get constructor file('__init__.py') then, that folder would be 
                                                # considered as our local package , so this is the idea to create our local package . 
                                                # that why we created '__init__.py' file because we want to make 'src' folder as our local package .
                                            # 'setup' method is used to install the package in the local system using the command: pip install -e .

setup(                                   # 'setup' method is used to install the package in the local system using the command: pip install -e .
    name = 'Medical Chatbot',           # 'name' is the name of the project we are working on.
    version= '0.0.0',                  # 'version' is the current version of the project we are working on.
    author= 'Rajkumar rawal',    # 'author' is the name of the author who is working on the project.
    author_email= 'rawalraj022@gmail.com',  # 'author_email' is the email of the author who is working on the project.
    packages= find_packages(),          # 'packages' is the list of packages we are working on.
    install_requires = []            # 'install_requires' is the list of packages that are required to run the project.

) 









