from setuptools import setup, find_packages
import os

setup_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(setup_dir, 'requirements.txt'), 'r') as req_file:
    requirements = [line.strip() for line in req_file if line.strip()]

setup(
    name='dmia2021',
    version='0.1.0',
    description='dmia2021 package',
    author='Ilya Irkhin',
    packages=find_packages(exclude='tests'),
    install_requires=requirements,
)
