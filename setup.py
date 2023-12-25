from setuptools import setup, find_namespace_packages

setup(
    name = "ab_console",
    version = "0.1.0",
    description = "Mijn cursusproject GoIT Python Core",
    authors = "Oleksandr Pripa <ol.pripa@gmail.com>",
    url= 'https://github.com/olpripa/AdressBookConsole',
    license='MIT',
    packages= find_namespace_packages(),
    install_requires=['prompt-toolkit'],
    entry_points = {'console_scripts': ['ab-console=ab_console.ab_console:main']}
    )