from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='jspp',
      version=version,
      description="Json pretty printer",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='json pretty printer',
      author='Mike Lewis',
      author_email='mikelikespie@gmail.com',
      url='http://lolrus.org',
      license='MIT',
      include_package_data=True,
      zip_safe=True,
      entry_points="""
      [console_scripts]
      jspp = jspp:main
      """,
      )
