%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import pandas as pd
import numpy as np

data = pd.read_csv('presient_heights.csv')
heights = np.array(data['heights[cm]')
print(heights)

print('Mean height:   ', heights.mean())
print('Standard Deviation:    ', heights.std())
print('Munimum height:    ', heights.min())
print('Maximum height:    ', heights.max())
print('25th percentile:     ', np.percentile(heights, 25))
print('Median:    ', np.median(heights))
print('75th percentile:   ', np.percentile(heights, 75))

#visualisation of the data

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height in cm')
plt.ylabel('number');
