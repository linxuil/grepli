from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='grepli',
     version='0.1',
     scripts=['grepli.py'],
     author="linxuil",
     author_email="linxuil.g@gmail.com",
     description="Implementation grep function for python",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/linxuil/grepli",
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Intended Audience :: Developers",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    entry_points={
        'console_scripts': [
            'grepli=console_scripts.main:main',
        ],
    },
 )