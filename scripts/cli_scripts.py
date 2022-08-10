# # Running command line scripts
#
# In this notebook we will go through some of the command line script that comes with the `cardiac-mps` package. These are useful if you want to analaze on or many files from the terminal.
#
# ## Running the scripts
#
# When you install the `cardiac-mps` package it will also install the the different scripts. There are three ways you can run these scripts:
#
# - By executing the `cardiac-mps` package as a modulde
#     ```
#     python -m mps <script command>
#     ```
#     e.g
#     ```
#     python -m mps analyze file.tif
#     ```
#
# - By dropping `python -m` in the command above
#
#     ```
#     mps <script command>
#     ```
#     e.g
#     ```
#     mps analyze file.tif
#     ```
# - Or by using the special names for the script
#     ```
#     <script command>
#     ```
#     e.g
#     ```
#     mps-analyze file.tif
#     ```
#
# Note that all scripts comes with a help flag which will display all available options, e.g
# ```
# > mps --help
# Usage: mps [OPTIONS] COMMAND [ARGS]...
#
# Options:
#   --version                       Show version
#   --license                       Show license
#   --install-completion [bash|zsh|fish|powershell|pwsh]
#                                   Install completion for the specified shell.
#   --show-completion [bash|zsh|fish|powershell|pwsh]
#                                   Show completion for the specified shell, to
#                                   copy it or customize the installation.
#   --help                          Show this message and exit.
#
# Commands:
#   analyze       Analyze flourecense data
#   motion        Estimate motion in stack of images
#   mps2mp4       Create movie of data file
#   phase-plot    Create movie of data file
#   split-pacing  Run script on a folder with files and this will copy the...
#   summary       Create a summary pdf of all files in the a directory.
#
# ```
# and
# ```
# > mps mps2mp4 --help
# Usage: mps mps2mp4 [OPTIONS] PATH
#
#   Create movie of data file
#
# Arguments:
#   PATH  Path to the mps file  [required]
#
# Options:
#   -o, --outfile TEXT    Output name for where you want to store the output
#                         movie. If not provided a the same name as the basename
#                         of the input file will be used
#   --synch / --no-synch  Start video at same time as start of pacing  [default:
#                         no-synch]
#   --help                Show this message and exit.
# ```

# ## Scripts
#
# Below we go through all the major scripts
#
# ### Convert recording into an mp4 file using `mps2mp4`
#
# This a simple script to convert an imaging file into an `.mp4` video file.
# Say you have a file `file.nd2`, then you can simply do
# ```
# mps2mp4 file.nd2
# ```
# or
# ```
# python -m mps mps2mp4 file.nd2
# ```
# and it will create a new `.mp4` with the same name as the imaging file.

# ### Run flourescense analysis using `mps-analyze`
#
# If you have an imaging file you might want to run a number of different analysis operations on it. The `mps-analyze` script takes as input an imaging file and output a folder with figures and spreadsheets.
#
# Say that we have a file `file.nd2`. Then we can analyze it using the command
# ```
# mps-analyze file.nd2
# ```
# or
# ```
# python -m mps analyze file.nd2
# ```
# You can also list all the possible option using the command
# ```
# mps-analyze --help
# ```
#
# The script will display some info in the terminal
#
# ```
# 2022-06-01 15:31:34,135 - mps.scripts.analyze - INFO - Run analysis script
# 2022-06-01 15:31:34,138 - mps.load - INFO - Load nd2 file /Users/henriknf/file.nd2
# 2022-06-01 15:31:34,309 - mps.load - INFO - Loaded 591 frames in 0.17 seconds
# 2022-06-01 15:31:37,174 - mps.scripts.analyze - INFO - Finished analyzing MPS data. Data stored folder 'file'.
# Total elapsed time: 3.04 seconds
# ```
# and a new folder called `file` contains the following files
#
# ```
# file
# ├── EAD_analysis.png
# ├── README.txt
# ├── apd_analysis.png
# ├── average.png
# ├── average_pacing.png
# ├── background.png
# ├── chopped_data.csv
# ├── chopped_data.png
# ├── chopped_data_aligned.png
# ├── data.npy
# ├── data.txt
# ├── metadata.json
# ├── original.png
# ├── original_pacing.png
# ├── settings.json
# ├── sliced_filtered.png
# ├── trace.png
# └── unchopped_data.csv
# ```
#
# The file called `README.txt` contains a description of all the files in the folder.
# For easy reference we also provide this description below
#
# - `apd_analysis.png`
#     Figure showing plots of action potential durations
#     and corrected actions potential durations (using
#     the friderica correction formula). Top panel shows
#     bars of the APD for the different beats where the *
#     indicated if the APD for that beat is significantly different.
#     The middle panel show the APD for each each plotted as a
#     line as well as a linear fit of the APD80 and cAPD80 line.
#     The intention behind this panel is to see it there is any
#     correlation between the APD and the beat number
#     The lower panel shows where the cut is made to compute
#     the different APDs
# - `average_pacing.png`
#     These are the average trace with pacing
# - `average.png`
#     These are the average of the traces in chopped_data
# - `background.png`
#     This plots the original trace and the background that we
#     subtract in the corrected trace.
# - `chopped_data_aligned.png`
#     All beats plotted on with the time starting at zero
# - `chopped_data.csv`
#     A csv file with the chopped data
# - `chopped_data.png`
#     Left panel: All the beats that we were able to extract from the corrected trace
#     Right panel: The intersection of all beats where APD80 and APD30 are within 1
#     standard deviation of the mean.
# - `data.npy`
#     A file containing all the results. You can load the results
#     in python as follows
#     ```python
#     >> import numpy as np
#     >> data = np.load('data.npy', allow_pickle=True).item()
#     ```
#     data is now a python dictionary.
# - `data.txt`
#     This contains a short summary of analysis.
# - `EAD_analysis.png`
#     A plot of the beats containing EADs
# - `frequency_analysis.png`
#     A plot of the frequencies of the different beats computed
#     as the time between peaks.
# - `metadata.json`
#     Metadata stored inside the raw data
# - `original_pacing.png`
#     This is the the raw trace obtained after averaging the frames
#     in the stack without any background correction or filtering
#     together with the pacing amplitude.
# - `original.png`
#     This is the the raw trace obtained after averaging the frames
#     in the stack without any background correction or filtering
# - `sliced_filtered.png`
#     Original trace where we have performed slicing and filtering
# - `trace.png`
#     The is the corrected version of the original trace where we
#     have performed a background correction and filtering
# - `unchopped_data.csv`
#     A csv file with all the unchopped data (original and corrected)
#
#

# ### Gettting a summary of all files in a folder using `mps-summary`
#
# If you have a folder containing several imaging files, then you can run `mps-summary` to get one figure with all the traces and one spreadsheet with some summary statistics.
#
# Say that we have a folder called `folder` containing several imaging files. Then you can run the command
# ```
# mps-summary folder
# ```
# or
# ```
# python -m mps summary folder
# ```
# and it will produce two new files called `mps_summary.csv` and `mps_summary.pdf` inside the folder.
#
# You can also list all the possible option using the command
# ```
# mps-summary --help
# ```
#

# ### Running motion analysis using `mps-motion`
#
# The motion script doesn't come with the `cardiac-mps` package and has to be installed separatelty. Plase check outalso have installed the [motion tracking script](https://github.com/ComputationalPhysiology/mps_motion_tracking) should should be able to also run
#
# ```
# python -m mps motion file.nd2
# ```
#
# or simply
#
# ```
# mps-motion file.nd2
# ```
# in order to run the motion analysis. As before you can do
# ```
# mps-motion --help
# ```
# to see all the available options. The script will produce a folder called `motion` containing the following files
# ```
# motion
# ├── features.csv
# ├── results.csv
# ├── settings.json
# ├── u_norm.png
# └── v_norm.png
# ```
# Here
# - `settings.json` are the settings used for the motion analysis
# - `u_norm.png` is a plot of the displacement norm averaged over the entire chip as a function of time.
# - `v_norm.png` is a plot of the velocity norm averaged over the entire chip as a function of time.
# - `results.csv` is a spreadsheet containing the traces
# - `features.csv` is a spreadsheet containing some features of each individual trace.
#
