[metadata]
name             = opioidtools
version          = attr:opioidtools.__version__
author           = Group 15: Jennifer, Yi, Irene, Zac
author_email     = jenniferr.brown@berkeley.edu
description      = A Python library for Comparing Opioid Crude Rates & GDP
long_description = file: README.md, LICENSE.md
long_description_content_type = text/markdown
keywords         = tools
license          = MIT License
classifiers      =
	Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
include_package_data = True
packages = find:
# These should be consistent with what is specified in the environment.yml
python_requires  = >= 3.6,
install_requires =
	tqdm

[options.packages.find]
exclude =
    examples*
    docs*
