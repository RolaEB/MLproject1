## this file is responsible for creating my ML application as a package
## that can be inistalled and used in other projects 
## and even deployed to pypi

from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    HYPHEN_E_DOT = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # to remove the new line character from each requirement in the list
        requirements = [req.replace("\n", "") for req in requirements]
        
        # to remove the -e . from the requirements list if it exists
        # this is because -e . is used to connect setup.py to the requirements.txt file and is not needed in the requirements list 
        # everytime -e . is encountered setup will run

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements
setup(
    name='ml_project_01',
    version='0.0.1',
    author='Rola', 
    author_email="rola.elbakly@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)

## find_packages () works by considering all directories with an __init__.py file as packages and sub-packages. 
## then setup will create a package for each of these directories and sub-directories that can be imported like any other package in python ex. pandas.