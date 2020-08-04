"""Example code for ENMT482 assignment."""

import numpy as np
import matplotlib.pyplot as plt


# Load data
filename = 'training1.csv'
data = np.loadtxt(filename, delimiter=',', skiprows=1)

# Split into columns
index, time, range_, velocity_command, raw_ir1, raw_ir2, raw_ir3, raw_ir4, sonar1, sonar2 = data.T


# Plot true range and sonar measurements over time
plt.figure(figsize=(12, 4))

plt.subplot(141)
plt.plot(time, range_)
plt.xlabel('Time (s)')
plt.ylabel('Range (m)')
plt.title('True range (Sensor Model)')

plt.subplot(142)
plt.plot(time, sonar1, '.', alpha=0.2)
plt.plot(time, range_)
plt.title('Sonar1')
plt.xlabel('Time (s)')

plt.subplot(143)
plt.plot(time, sonar2, '.', alpha=0.2)
plt.plot(time, range_)
plt.title('Sonar2')
plt.xlabel('Time (s)')


# My code goes here

# based on:
#  * https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm
#  * http://colingorrie.github.io/outlier-detection.html#modified-z-score-method
#  * http://contchart.com/outliers.aspx
#  * https://stats.stackexchange.com/questions/339932/iglewicz-and-hoaglin-outlier-test-with-modified-z-scores-what-should-i-do-if-t


sonarData = sonar1
trueDistance = range_

sonarBF = []
sonarBF.append(sonarData[0])
sonarCorrect = sonarData[0]

count = 0

for dataPoint in sonarData:
    if (count > 0):
        error = abs(dataPoint - sonarCorrect)
        if (error < 0.2):
            sonarBF.append(dataPoint)
            sonarCorrect = dataPoint
            count = count + 1
        else:
            sonarBF.append(sonarCorrect)
            count = count + 1

    else:
        count = count + 1
    


plt.subplot(144)
plt.plot(time, sonarBF, '.', alpha=0.2)
plt.title('Sonar1 removed outliers')
plt.xlabel('Time (s)')

plt.show()