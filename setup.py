from setuptools import setup, find_packages


version = '0.1'

setup(name='nethack',
      version=version,
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='',
      author='ryansb, rossdylan, oddshocks, and qalthos',
      author_email='',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'twisted',
          'ultrajson',
      ],
)
