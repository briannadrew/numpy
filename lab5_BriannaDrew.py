# lab5_BriannaDrew.py

# Brianna Drew
# March 1, 2021
# ID: #0622446
# Lab #5

# OBSERVATIONS: First I tried keeping the original size of 1000, and each sorting method took
# so little time that I just got 0 seconds for each. Then, I tried a size of 5000 and got
# varying results each time I ran the program. The first time through, I got a time of 
# 0.0010294914245605469s for the Quicksort, 0s for Mergesort, and 0.0009646415710449219s for
# the Heapsort. When I ran it for a second and third time, I got 0s for all three sorts once
# again. The fourth time, I got 0.0009624958038330078s for the Quicksort, and 0s for the
# other two sorts. I kept running this repeatedly and sometimes I also got a time greater
# than 0s for Mergesort and 0s for the other two, and sometimes I also got a time greater
# than 0s for Heapsort and 0s for the other two. Therefore, there's no sufficient evidence
# that any of the sorting algorithms are slower or faster when compared to one another.
# Finally, I tried to increase the array size by quite an exponential amount to to 5000000
# to examine the results further. With this large of a size, the results were much more
# consistent. Out of 10 runthroughs of the program, for Quicksort, I got a minimum time of
# 0.15911245346069336s and a maximum time of 0.017453575134277344s. For the Mergesort, I
# got a minimum time of 0.2662851810455322s and a maximum time of 0.27536211738586426s.
# Finally, for the Heapsort, I got a minimum time of 0.42121995793151855s and a maximum time
# of 0.42897534370422363s. Therefore, from these results, it seems to support that Quicksort
# is the fastest of the three, Heapsort is the slowest, and Mergesort is in the middle.

# import required modules
import numpy as np
import time

arrSize = 5000000 # size of array

arr = np.random.randint(101, size = arrSize) # array creation

# display various summary statistics about the array we created
print("Number of Dimensions: ", arr.ndim, "\nShape: ", arr.shape,
    "\nData Type: ", arr.dtype, "\nMinimum Value: ", np.min(arr), 
    "\nMaximum Value: ", np.max(arr), "\nSum: ", np.sum(arr),
    "\nMean: ", np.mean(arr), "\nStandard Deviation: ", np.std(arr))

# SORTING (and getting start and finish times for each method)
# Quicksort
qStart = time.time()
np.sort(arr)
qEnd = time.time()

# Mergesort
mStart = time.time()
np.sort(arr, kind = "mergesort")
mEnd = time.time()

# Heapsort
hStart = time.time()
np.sort(arr, kind = "heapsort")
hEnd = time.time()

# calculate elapsed time for each sorting method
qElapsed = qEnd - qStart
mElapsed = mEnd - mStart
hElapsed = hEnd - hStart

# display elapsed time for each sorting method
print("\nQuicksort Elapsed Time (s): ", qElapsed, ", Mergesort Elapsed Time: ",
    mElapsed, ", Heapsort Elapsed Time: ", hElapsed)