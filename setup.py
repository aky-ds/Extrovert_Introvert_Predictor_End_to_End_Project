from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list:
    """
    This function will return the list of requirements
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
project_name ='Entrovert_Introvert_Prediction'
project_author='ayazulhaqyousafzai'
author_gmail='syedthescientist@gmail.com'

setup(
    name=project_name,
    version='0.0.1',
    author=project_author,
    author_email=author_gmail,
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.6',
)