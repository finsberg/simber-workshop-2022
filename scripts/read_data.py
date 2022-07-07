# # Reading a recording using the `mps` package
#
# In this demo we will learn how to open a file an printing some basic info about the recording.
#
# First thing we need to do is to import the mps library

import mps

# Next thing we need to do is to specify the path to the file we want to open. Change the string below to the path to the file you want to open.
#
# Note that the path separator is different on Windows and Unix (Linux/Mac). If you are on Windows, the path will typically by something like `C:\Users\Henrik\Documents\file.tif` (i.e with `\` as separator), while on Unix the path will be similar to the example below.

path = "/Users/finsberg/Dropbox/Simber/data/20220105_omecamtiv_chipB/control_10850/20220105-80GCaMP20HCF-omecamtiv_Stream_B01_s1_TL-20-Stream.tif"

# The `mps` pacakge can read various file formats including `.tif`, `.stk`, `.nd2` and `.czi`.
#
# Now let us load the data by passing the path the `mps.MPS` object

data = mps.MPS(path)

# This will create an object the allow us to read the recording as well as metadata stored within the file. 
#
# You can list the available methods on this object using the `dir` method

# dir(data)

# And if you are working in a notebook you can also type `data.` and hit the `TAB` key.
#
# Lets print the data object

print(data)

# Now lets print the info attribute which will list some basic info about the data

print(data.info)

# If you want a little bit nicer looking output you can also use the pretty printer in python

import pprint
pprint.pprint(data.info)

# The actual frames are stored as the attribute `.frames`. This will be a numpy array of shape `(size_x, size_y, num_frames)`

data.frames.shape

# The frames contains pixel intensities that are typically stored as 16-bits unsigned integers (uint16)

data.frames

# The time stamps are stored in the attribute `time_stamps` as a numpy array of length `num_frames`

data.time_stamps.shape

data.time_stamps

# If the cells are paced then this information might be stored in the metadata of the recording. In this case this will be extracted in the attribute `pacing` which will also be a numpy array of length `num_frames`.

data.pacing.shape

data.pacing

# If the cell is not paced, or there is no information about the pacing stored within the recording, then this array will only contain zeros.


