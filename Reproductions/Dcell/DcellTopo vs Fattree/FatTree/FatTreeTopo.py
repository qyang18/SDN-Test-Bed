from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
import random

"""
Instructions to run the topo:
    1. Go to directory where this fil is.
    2. run: sudo -E python Simple_Pkt_Topo.py.py

The topo has 4 switches and 4 hosts. They are connected in a star shape.
"""


class ParkingLotTopo(Topo):
    "Parking Lot Topology"
    def __init__(self, **opts):
    #def __init__(self, n=1, cpu=.1, bw=10,
     #            max_queue_size=None, **params):
        """Parking lot topology with one receiver
           and n clients.
           n: number of clients
           cpu: system fraction for each host
           bw: link bandwidth in Mb/s
           delay: link delay (e.g. 10ms)"""

        # Initialize topo
        Topo.__init__(self, **opts)
        #Topo.__init__(self, **params)

        # Host and link configuration
        #hconfig = {'cpu': cpu}
        #lconfig = {'bw': bw, 'max_queue_size': max_queue_size }

        # Create the actual topology
        #receiver = self.add_host('receiver')

        # Switch ports 1:uplink 2:hostlink 3:downlink
        #uplink, hostlink, downlink = 1, 2, 3

        # The following template code creates a parking lot topology
        # for N = 1
        # TODO: Replace the template code to create a parking lot topology for any arbitrary N (>= 1)
        # Begin: Template code

        root_switch = self.addSwitch('s0')

        #add five child switches and to each of them connect four hosts

        #for s in range(1,6):
        for s in range(1,5):
            switch = self.addSwitch('s%s' % s)
            self.addLink(root_switch, switch, bw=100)
            for h in range(1,4):
                host = self.addHost('h%s' % (((s-1)*3) + h) )
                self.addLink(host, switch, bw=100)

def randomPerfTest(net):
    #net.pingAll()
    print("start random perf test")
    #select 5 links of client-server pair and run iperf
    #50G
    totalFileSize=50000000000
    hostList=[]
    for i in range(1,6):
	clientID=str(random.randint(1,12))
	while (clientID in hostList):
		clientID=str(random.randint(1,12))
	hostList.append(clientID)

	serverID=str(random.randint(1,12))
	while (serverID in hostList):
		serverID=str(random.randint(1,12))
	hostList.append(serverID)

	print('generating iperf from h'+clientID+' to h'+serverID)
	client=net.getNodeByName('h'+clientID);
    	server=net.getNodeByName('h'+serverID);
	
       #file_size=10000000 around 9.2M finished in 0.1s
	file_size=500000000
	serverIperfArgs = 'iperf3 -s > serverLog%sv%d &' % (serverID, 4)
	clientIperfArgs = 'iperf3 -c %s -n %d -i 0.5 > clientLog%sv%d &' % (str(server.IP()),file_size, clientID, 4)
	#print(serverIperfArgs)
	#print(clientIperfArgs)
	server.cmd(serverIperfArgs)
	client.cmd(clientIperfArgs)

def run():
    c = RemoteController('c', '192.168.56.101', 6633)
    net = Mininet(topo=ParkingLotTopo(), host=CPULimitedHost,link=TCLink, controller=None)
    net.addController(c)
    net.start()

    randomPerfTest(net)
    CLI(net)
    net.stop()

# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()