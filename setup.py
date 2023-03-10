from distutils.core import setup
from pathlib import Path
setup(
  name = 'TOPSIS-AMRIT-102003690',         # How you named your package folder (MyLib)
  packages = ['TOPSIS-AMRIT-102003690'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TOPSIS Package for Multiple Criteria Decision Making',   # Give a short description about your library
  author = 'Amritpal Singh',                   # Type in your name
  url = 'https://github.com/iamritpalsingh1/TOPSIS',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/iamritpalsingh1/TOPSIS/archive/refs/tags/v_05.tar.gz',    # I explain this later on
  keywords = ['Topsis', 'MCDM', 'package'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  # read the contents of your README file

  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ]
)
