# # Reading a recording using the `mps` package
#
# In this demo we will learn how to open a file an printing some basic info about the recording.
#
# First thing we need to do is to import the mps library

import mps

# Next thing we need to do is to specify the path to the file we want to open.
# If you have already have some data you can use that (in this case change the string below to the path to the file you want to open), otherwise you can download some sample data

# +
from pathlib import Path

path = Path("data.tif")


# -


def download_data():
    print("Downloading data. Please wait...")
    link = "https://www.dropbox.com/s/gowdo5t8c78mtkh/data.tif?dl=1"
    import urllib.request
    import time

    urllib.request.urlretrieve(link, path)
    time.sleep(1.0)
    print("Done downloading data")


# Download the data if file does not exist
if not path.is_file():
    download_data()

# The `mps` pacakge can read various file formats including `.tif`, `.stk`, `.nd2` and `.czi`.
#
# Now let us load the data by passing the path the `mps.MPS` object

data = mps.MPS(path)

# This will create an object the allow us to read the recording as well as metadata stored within the file.
#
# Lets print the data object

print("data = ", data)

# We can aslo use a bit more convenient way to print this in python using f-strings

print(f"{data = }")

# You can list the available methods on this object using the `dir` method
# And if you are working in a notebook you can also type `data.` and hit the `TAB` key.

print(f"{dir(data) = }")

# Now lets print the info attribute which will list some basic info about the data

print(f"{data.info = }")

# If you want a little bit nicer looking output you can also use the pretty printer in python

import pprint

pprint.pprint(data.info)

# The actual frames are stored as the attribute `.frames`. This will be a numpy array of shape `(size_x, size_y, num_frames)`

print(f"{data.frames.shape = }")

# The frames contains pixel intensities that are typically stored as 16-bits unsigned integers (uint16)

print(f"{data.frames = }")

# The time stamps are stored in the attribute `time_stamps` as a numpy array of length `num_frames`

print(f"{data.time_stamps.shape = }")

print(f"{data.time_stamps = }")

# If the cells are paced then this information might be stored in the metadata of the recording. In this case this will be extracted in the attribute `pacing` which will also be a numpy array of length `num_frames`.

print(f"{data.pacing.shape = }")

print(f"{data.pacing = }")

# If the cell is not paced, or there is no information about the pacing stored within the recording, then this array will only contain zeros.
