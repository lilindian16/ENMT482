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

plt.subplot(144)
plt.plot(time, raw_ir2, '.', alpha=0.2)
plt.title('Sonar2')
plt.xlabel('Time (s)')


# My code goes here
sonar1Data = sonar1
sonar2Data = sonar2
ir1Data = raw_ir1
ir2Data = raw_ir2
ir3Data = raw_ir3
ir4Data = raw_ir4
trueDistance = range_

sonar1BF = []
sonar2BF = []
ir1BF = []
ir2BF = []
ir3BF = []
ir4BF = []

correctValueArray = []

dataArray = [sonar1Data, sonar2Data, ir1Data, ir2Data, ir3Data, ir4Data]
lbfArray = [sonar1BF, sonar2BF, ir1BF, ir2BF, ir3BF, ir4BF]


count = 0
for dataSet in dataArray:
    sums = 0
    meanRange = 2
    for i in range(meanRange):
        sums = sums + dataSet[i]
    mean = sums / meanRange
    print(mean)
    lbfArray[count].append(mean)
    correctValueArray.append(mean)
    count = count + 1

# Removing the outliers
dataSetArrayCount = 0
for dataSet in dataArray:
    dataIndex = 0
    for sensorData in dataSet:
        if (dataIndex > 0):
            error = abs(sensorData - correctValueArray[dataSetArrayCount])
            if (error < 0.1):
                lbfArray[dataSetArrayCount].append(sensorData)
                correctValueArray[dataSetArrayCount] = sensorData
                dataIndex = dataIndex + 1
            else:
                correction = correctValueArray[dataSetArrayCount]
                lbfArray[dataSetArrayCount].append(correction)
                dataIndex = dataIndex + 1

        else:
            dataIndex = dataIndex + 1

    dataSetArrayCount = dataSetArrayCount + 1
    
# Plotting figures
plt.figure(figsize=(12, 2))

plt.subplot(121)
plt.plot(time, lbfArray[0], '.', alpha=0.2)
plt.title('Sonar1 removed outliers')
plt.xlabel('Time (s)')

plt.subplot(122)
plt.plot(time, lbfArray[1], '.', alpha=0.2)
plt.title('Sonar2 removed outliers')
plt.xlabel('Time (s)')

plt.figure(figsize=(12, 4))

plt.subplot(141)
plt.plot(time, lbfArray[2], '.', alpha=0.2)
plt.title('IR 1 removed outliers')
plt.xlabel('Time (s)')

plt.subplot(142)
plt.plot(time, lbfArray[3], '.', alpha=0.2)
plt.title('IR 2 removed outliers')
plt.xlabel('Time (s)')

plt.subplot(143)
plt.plot(time, lbfArray[4], '.', alpha=0.2)
plt.title('IR 3 removed outliers')
plt.xlabel('Time (s)')

plt.subplot(144)
plt.plot(time, lbfArray[5], '.', alpha=0.2)
plt.title('IR 4 removed outliers')
plt.xlabel('Time (s)')

plt.show()