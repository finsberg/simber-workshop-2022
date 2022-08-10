# Extracting a trace from the frames and analyze it

In this session we will learn how go from the raw images to a trace that we later will analyze. First lets load some data

```python
import mps

path = "/Users/finsberg/Dropbox/Simber/data/20220105_omecamtiv_chipB/control_10850/20220105-80GCaMP20HCF-omecamtiv_Stream_B01_s1_FITC-PS-Stream.tif"
data = mps.MPS(path)
```

Now lets take a look at the info and the shape of the frames

```python
print(f"{data.frames.shape = }")
print(f"{data.info = }")
```

## Plotting the first frame

We note that the first and second dimension are spatial and the third dimension is temporal. This means that if we want to get the first frame, then we can access this by selecting all of the two first indices (using the `:` notation for slicing numpy arrays) and selecting the `0` index in the temporal dimension

```python
first_frame = data.frames[:, :, 0]
```

Lets plot the first frame using `matplotlib`

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 10))
ax.imshow(first_frame)
ax.set_title("First frame")
```

We can also rotate the image 90 degrees by transposing the frame using the `.T` method on the array

```python
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(first_frame.T)
ax.set_title("First frame (transposed)")
```

## Computing an average trace

In order to get to a trace, we need to reduce each frame into a number so that we end up with an array of values for each time stamp. One way to do this is to average over the entire chip. For the first frame we can do this as follows

```python
first_frame_mean_value = first_frame.mean()
print(f"{first_frame_mean_value = }")
```

Now we would like to do this for each frame in `data.frames`. We could do this using a *for loop*, however, this will be quite inefficient. Since `data.frames` is a numpy array we can take the mean over the first two dimensions using the following code

```python
y = data.frames.mean(axis=(0, 1))
```

Here we pass in `axis=(0, 1)` to indicate that we should take the average over the first and second dimension.

Lets plot the trace against the time stamps.

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(data.time_stamps, y)
ax.grid()
ax.set_xlabel("Time [ms]")
ax.set_ylabel("Mean pixel intensity")
```

Note the following:

* The $y$-axis here is *mean pixel intensity*.
    - These values are not in general related to the physical unit of the trace (i.e calcium concentration or voltage)
    - This means that we cannot use features related to the magnitude of the trace, such as max and min values, but temporal values are valid
* The baseline is drifting (decaying as a function of time).
    - This due to photobleaching and we need to correct for this

<!-- #region -->
### Exercise: Selecting a subset of the pixels for extracting an average trace

In the above code we used all the pixels to compute the average however you could image that you only wanted to use the pixels where the tissue is, or even a smaller region. You can do this be finding the indices in the $x$ and $y$-direction. For example

```python
data.frames[400:600, 50:150, :]
```
will take out a region in (approximately) the center of the chip.

* Try to perform the averaging over a smaller region, and plot the trace. Does the shape and amplitude change?
<!-- #endregion -->

## Removing the baseline

The first thing we need to do is to remove the baseline so that the effect of photobleaching is removed. To do this we will use the `ap_features` package, by converting the trace into a `ap_features` object.

```python
import ap_features as apf

trace = apf.Beats(y=y, t=data.time_stamps)
```

```python
trace.plot()
```

Well, this looks very similar to what we had before. When constructing this object we can also pass in another argument called `background_correction_method`.

```python
trace = apf.Beats(y=y, t=data.time_stamps, background_correction_method="full")
trace.plot()
```

We now now see that the background is removed, and that the $y$-axis got different values. The correct label for the label would be $\Delta F / F_0$. Lets explain what this mean. First we will plot the original trace with the baseline

```python
fig, ax = plt.subplots()
ax.plot(trace.t, trace.original_y, label="original trace")
ax.plot(trace.t, trace.background, label="background")
ax.legend()
```

Now, $F_0$ would be the first value in the estimated baseline

```python
F_0 = trace.background[0]
```

and $\Delta F$ would be the original trace minus the baseline

```python
delta_F = trace.original_y - trace.background
```

```python
fig, ax = plt.subplots()
ax.plot(trace.t, delta_F / F_0)
```

### Exercise: Other types of background corrections
TBW


## Chopping a trace into individual beats

We have now a trace that we can work with, but in order to compute features such as action potential durations, we need to chop the trace into individual beats. With the `ap_features` package, this is pretty easy

```python
beats = trace.beats

print(f"{beats = }")
```

Lets loop over all the beats and plot then with different colors

```python
fig, ax = plt.subplots()
for beat in beats:
    ax.plot(beat.t, beat.y)
```

<!-- #region -->
As we can see, there are some gaps in the trace. This is due to the way the trace is chopped. There are two different algorithms for chopping the trace into individual beats. The first algorithm is used when we have pacing information available, in which case the algorithm will use the time of the pacing stimulus as a marker to chop. In this case we do not have this information and in this case the algorithm is a bit more complicated. You can read more about the algorithm in the `ap_features` documentation: https://computationalphysiology.github.io/ap_features/ap_features.html#ap_features.chopping.chop_data_without_pacing


### Exercise: Changing the settings for chopping

You might not be completely satisfied with the way the trace was chopped, and there are several options to chop the data into beats. When you create the trace you can also specify a set of options for chopping using the `chopping_options` argument, e.g
<!-- #endregion -->

```python
fig, ax = plt.subplots()
trace = apf.Beats(
    y=y,
    t=data.time_stamps,
    background_correction_method="full",
    chopping_options={"threshold_factor": 0.3, "extend_end": 300, "extend_front": 100},
)
for beat in trace.beats:
    ax.plot(beat.t, beat.y)
```

* Try to change the options for chopping, and see how it affects the results

```python
# Use these beats instead
beats = trace.beats
```

## Analyzing a single beat

Lets take a look at the second beat (since the first beats seems to still have some problems with the baseline)

```python
second_beat = beats[1]
print(f"{second_beat = }")
```

We can plot it

```python
second_beat.plot()
```

Lets also take a look at the available methods by print the attributes that does not start with and underscore (or by typing `second_beat.` and hitting TAB)

```python
import pprint
```

```python
pprint.pprint([attr for attr in dir(second_beat) if not attr.startswith("_")])
```

### APD80


You will see that there are quite a lot of options here. For example to compute the APD80 you can do

```python
APD80 = second_beat.apd(80)
print(f"{APD80 = :.2f} ms")  # Also specify that we only want two decimals
```

If you want to know how the APD80 was computed, you can use the `apd_point` method which will return the first and second time point that intersects the APD80 line

```python
APD80_point = second_beat.apd_point(80)
print(f"{APD80_point = }")
```

And to get the APD80 value, you just subtract these numbers

```python
print(f"{APD80_point[1] - APD80_point[0] = :.2f}")
```

#### Exercise: APD80 for each beat

- Try to compute the APD80 for each beat. Do you need any big differences?


### Corrected APD80 (cAPD80)

Another important feature is the corrected APD80, which is the APD80 value corrected for the beat rate. You can read more about the corrected apd here: https://computationalphysiology.github.io/ap_features/ap_features.html#ap_features.features.corrected_apd

When computing the corrected APD you also need to know the beat rate, but this information can not be computed from a single beat - we need the entire trace. However, when chopping the trace into beats, all the beats also get a pointer to the parent trace that is stored in the attribute `parent`

```python
second_beat.parent is trace
```

And the trace has an attribute called `beat_rate`

```python
trace.beat_rate
```

This will use the peak of each beat, and find the duration between each peak. The value stored in `trace.beat_rate` is the mean value of all of these beat rates. So see all the beat rates you can use the `.beat_rates` attribute

```python
trace.beat_rates
```

A related concept is the beating frequency which each

$$ \text{beating frequency} = \frac{\text{beat rate}}{60}$$

```python
trace.beating_frequency
```

And similarly we also have the individual beating frequencies

```python
trace.beating_frequencies
```

Coming back to the corrected APD, we can compute this as a method each beat

```python
cAPD80 = second_beat.capd(80, formula="friderica")
print(f"{cAPD80 = }")
```

There are two formulas implemented for computing the corrected APD, the `friderica` formula and `bazett` check out the documentation for more info


### Exercise: Compute other features

There are plenty of other features that you can compute. Check of the following methods

* `tau`
* `triangulation`
* `ttp`
* `upstroke`
* `integrate_apd`
* `maximum_relative_upstroke_velocity`
* `maximum_upstroke_velocity`
* `apd_up_xy`
* `detect_ead`

Look up the documentation and try to understand what these features are and try to see it the values you get make sense.



## Extracting traces from subregions of the chip

Now we will briefly discuss how to automatically extract traces from different regions of the chip. In the next session you will get a more thorough explanation on how to do this.

For reference, let us plot the first frame from the data

```python
fig, ax = plt.subplots(figsize=(15, 4))
plt.imshow(data.frames[:, :, 0].T)
print(data.frames.shape)
```

Now we will use a methods from the mps package to extract averages from different subregions.

```python
loc = mps.analysis.local_averages(
    data.frames, times=data.time_stamps, N=15, background_correction=True
)
```

We specify some number `N` (here we chose 15) which will be the number of regions along the major axis of the chip. The algorithm will then subdivide the chip into squares (i.e width equal height and width) and choose the number of regions along the minor axis such that the regions cover the chip.

We can take a look at the shape of this array

```python
print(loc.shape)
```

The last dimension will be the number of time steps.

We can plot all the traces at their spatial location in a large subplot as follow

```python
fig, ax = plt.subplots(
    loc.shape[1], loc.shape[0], sharex=True, sharey=True, figsize=(15, 6)
)
for i in range(loc.shape[0]):
    for j in range(loc.shape[1]):
        ax[j, i].plot(data.time_stamps, loc[i, j, :])
plt.show()
```

Or we can plot them all in the same plot (here we just plot the mid regions

```python
fig, ax = plt.subplots(figsize=(15, 8))
for i in range(loc.shape[0]):
    ax.plot(data.time_stamps, loc[i, 1], label=f"region {i}")
ax.legend(bbox_to_anchor=(1, 0.5), loc="center left")
plt.show()
```
