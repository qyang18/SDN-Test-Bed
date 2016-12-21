import matplotlib.pyplot as plt
from numpy import arange, random

def plot(filename):
    """TODO: Docstring for plot.
    :returns: TODO

    """

    f = open(filename, 'r')
    print filename

    data = []
    for line in f:
        if line[0] == '[':
            if not '0.0-5' in line.split(' ')[4]:
                data.append( [line.split(' ')[2], line.split(' ')[-2]] )

    connections = []
    result = []

    for each in data:
        try:
            if each[0] in connections:
                result[connections.index(each[0])].append(float(each[1]))
            else:
                connections.append(each[0])
                result.append([])
                result[connections.index(each[0])].append(float(each[1]))
        except ValueError:
            pass

    for i in range(len(result)):
        result[i] = result[i][20:]

    return result

for i in range(1,6):
    data = []
    for j in range(4,7):
        data.extend(plot('serverLog-h'+str(j)+'v'+str(i)))

    row = arange(10,55,0.5)
    tmp = row
    for each in data:
        if len(each)  != len(row):
            tmp = row[:len(each)]
        plt.plot(tmp, each, 'k', c=random.rand(3,1))
        #plt.plot(tmp, each, 'r--')

    pass
    plt.axis([10,50,5,110])
    plt.show()

