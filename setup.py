from setuptools import setup

setup(name='s23project',
      version='0.0.1',
      description='s23project package',
      maintainer='<Carolina Colombo Tedesco>',
      maintainer_email='<ccolomb2@andrew.cmu.edu>',
      license='MIT',
      packages=['s23project'],
      entry_points={'console_scripts': ['oa = s23project.main:main']}, 
      long_description='''A long
      multiline description.''')
