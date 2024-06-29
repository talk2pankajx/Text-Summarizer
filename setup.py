import setuptools
from typing import List

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str)-> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.

    Parameters:
    file_path (str): The path to the requirements file.

    Returns:
    List[str]: A list of requirements read from the file.

    Note:
    - If the requirements file contains '-e .' (HYPEN_E_DOT), it will be removed from the list.
    """
    requirements = []
    with open(file_path, "r",) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
    
    


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_NAME = "talk2pankajx"
SRC_REPO = "Text_summarizer"
AUTHOR_EMAIL ="talk2pankajx@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    Long_description=long_description,
    description= "package for text summarization",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    instal_requires=get_requirements("requirements.txt"),
)