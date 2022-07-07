import mps
import matplotlib.pyplot as plt

path = "/Users/finsberg/Dropbox/Simber/data/20220105_omecamtiv_chipB/control_10850/20220105-80GCaMP20HCF-omecamtiv_Stream_B01_s1_TL-20-Stream.tif"

data = mps.MPS(path)
first_frame = data.frames[:, :, 0]

fig, ax = plt.subplots()
ax.imshow(first_frame)
plt.show()

# Transpose
fig, ax = plt.subplots()
ax.imshow(first_frame.T)
plt.show()
