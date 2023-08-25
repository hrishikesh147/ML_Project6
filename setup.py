from setuptools import setup,find_packages

PROJECT_NAME="MLProject delivery time estimation"
PROJECT_VERSION="0.0.1"
DESCRIPTION="To predict the food delivery time in real-time"
AUTHOR="hrishikesh bhagawati"
AUTHOR_EMAIL="hrishikeshbhagawati@gmail.com"

REQUIREMENTS="requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements_list():
    with open(REQUIREMENTS) as req:
        req_list=req.readlines()
        req_list=[i.replace("\n","") for i in req_list]
        if HYPHEN_E_DOT in req_list:
            req_list.remove(HYPHEN_E_DOT)
        return req_list

setup(name=PROJECT_NAME,
      version=PROJECT_VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      #url='https://www.python.org/sigs/distutils-sig/',  url of the packages
      packages=find_packages(),
      install_requires=get_requirements_list()
     )