import matplotlib.pyplot as plt
from numpy import arange, random

def plot(filename):
    """TODO: Docstring for plot.
    :returns: TODO

    """

    f = open(filename, 'r')

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

    for each in result:
        print each, len(each)
    return result

data = []
for i in range(3,6):
    for j in range(2,5):
        data.extend(plot('clientLog-h'+str(j)+'v'+str(i)))

    data.extend(plot('serverLog-h1v'+str(i)))
    row = arange(10,50,0.5)
    for each in data:
        if len(each) > 0:
            plt.plot(row, each, 'r--', c=random.rand(3,1))
            #plt.plot(row, each, 'r--')
    pass

plt.axis([10,50,10,110])
plt.show()
