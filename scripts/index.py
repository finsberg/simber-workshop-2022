# # MPS coding session
#
# In this session we will learn how to use the `mps` and the `ap_features` package.
#
# The `mps` package is a python library for reading and analyzing mps recordings.
# You can find more info about the package here: https://github.com/computationalPhysiology/mps
#
#
# The `ap_features` package (stands for Action Potential features) is also a python library (partly written in C for performance) and is used internally in the `mps` package to compute different features of a traces. All of the logic for chopping the traces into individual beats and computing different features (such as APD) is implemented in this package. You can find more info about the package here: https://github.com/computationalPhysiology/ap_features
#
#
# ## Notebooks
#
# Here you will find a few notebooks that you can use to learn more about the functionality of the `mps` and `ap_feature` packages.
#
# - [Importing a file using the mps library and printing some info about it](read_data.ipynb)
# - [Extracting a trace from the frames and analyze it](analyze_trace.ipynb)
# - [Running command line scripts](cli_scripts.ipynb)
#
# ## Python scripts
# All notebooks as also available as pure python scripts in the [scripts](scripts) folder


