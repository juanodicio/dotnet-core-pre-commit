from setuptools import setup

setup(
   name='dotnetcore_precommit',
   version='1.0',
   description='Cross-platform .NET Core pre-commit hooks',
   author='Juan Odicio',
   author_email='juanodicio@gmail.com',
   packages=['dotnetcore_precommit'],  #same as name
   install_requires=[],
   entry_points={
    'console_scripts': [
        'dotnet_test=dotnetcore_precommit.dotnet_test:main',
    ],
   }
)