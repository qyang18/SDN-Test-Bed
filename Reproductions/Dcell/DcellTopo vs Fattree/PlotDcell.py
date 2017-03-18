#read all log files as file1,file2,....,filen
#for each file get the column at given time
#plot a CDF diagram with total data and time
import numpy as np
import matplotlib.pyplot as plt

def getLogFile(filename):
    # filename='log1'
    f=open(filename, 'r')
    data=[]
    counter=1

    for line in f:
        counter+=1
        if counter >= 8:
            if line[0] != '[':
                break
            # print([line.split('  ')[2],line.split('  ')[4]])
            data.append([line.split('  ')[2],line.split('  ')[4]])
    return data

def getLogFileInCDF(filename):
    # filename='log1'
    f=open(filename, 'r')
    data=[]
    counter=1

    for line in f:
        counter+=1

        segments=line.split('  ')

        if counter == 8:
            data.append([segments[2]] + dealWithUnit(segments[4]))

        if counter >= 9:
            if line[0] != '[':
                break

            data.append([segments[2]] + [(data[counter - 9][1] + dealWithUnit(segments[4])[0])] + [(dealWithUnit(segments[4])[1])])

    print(data)
    return data

def dealWithUnit(line):
    temp=line.split(' ')
    value=float(temp[-2])

    unit=temp[-1]
    if 'MBytes' in unit:
        pass
    elif 'KBytes' in unit:
        value=value/1024
    elif 'Bytes' in unit:
        value=value/1048576

    return [value,unit]

if __name__ == "__main__":
    # file=getLogFile('log1')
    # print(file)
    file=[]
    data=[]
    time=np.linspace(0,10,50)
    file.append(getLogFileInCDF('log1'))
    file.append(getLogFileInCDF('log2'))

    for i in range(0,50):
        tempData=0
        for eachfile in file:
            #get line i and add up together
            tempData+=eachfile[i][1]
        data.append(tempData)

    plt.title('CDF Plot of data transmitted and time')
    plt.xlabel('time')
    plt.ylabel('data')

    print(time)
    print(data)
    plt.plot(time, data)
    plt.show()
