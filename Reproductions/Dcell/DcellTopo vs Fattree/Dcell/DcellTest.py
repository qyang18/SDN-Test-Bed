from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController, OVSSwitch
from sys import argv
import logging
import os
import random


#logging.basicConfig(filename='./Dcell.log', level=logging.INFO)
#logger = logging.getLogger(__name__)

class DcellTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, **opts):
        Topo.__init__(self, **opts)

        for i in range(1, 6):   #5 subnetwork(DCell 0),5 switch
            s = self.addSwitch(name = 's'+str(i),dpid='00000000000000'+str(i)+'0')
            for j in range(1, 5):   #every DCell0
                h = self.addHost('h'+str(i)+str(j),ip='10.0.'+str(i)+'.'+str(j),mac='00:00:00:00:00:'+str(i)+str(j))
                s_h = self.addSwitch(name = 's'+str(i)+str(j),dpid='00000000000000'+str(i)+str(j))  #allocate dpid?
		self.addLink(h, s_h , bw=100)
	    	self.addLink(s,s_h , bw=100)

        for i in range(1, 5):
            for j in range(i, 5):   #[i; j] and [j+1; i] are connected
                self.addLink('s'+str(i)+str(j), 's'+str(j+1)+str(i), bw=100)

def randomPerfTest(net):
    print("start random perf test")
    #select 5 links of client-server pair and run iperf

    hostList=[]
    for i in range(1,6):
	clientID=str(random.randint(1,5))+str(random.randint(1,4))
	while (clientID in hostList):
		clientID=str(random.randint(1,5))+str(random.randint(1,4))
	hostList.append(clientID)

	serverID=str(random.randint(1,5))+str(random.randint(1,4))
	while (serverID in hostList):
		serverID=str(random.randint(1,5))+str(random.randint(1,4))
	hostList.append(serverID)

	print('generating iperf from h'+clientID+' to h'+serverID)
	client=net.getNodeByName('h'+clientID);
    	server=net.getNodeByName('h'+serverID);
	#print("./Server "+serverID+"v2 &")
	server.cmd("./Server "+serverID+"v2 &")
	#print("./Client "+clientID+"v2 "+str(server.IP())+" &")
	client.cmd("./Client "+clientID+"v2 "+str(server.IP())+" &")

def start(  ):
    "Create network and run simple performance test"
    
    net = Mininet( controller=None, topo=DcellTopo(), link=TCLink, switch = OVSSwitch )
    c3 = RemoteController('c3', ip='192.168.56.101', port=6633)
    net.addController(c3)
  
    net.start()
    #h11, h21 = net.getNodeByName('h11','h21')
    #h21.cmd("./Server 11-21v1")
    #h11.cmd("./Client 11-21v5 10.0.2.1")
    randomPerfTest(net)
    CLI(net)
    net.stop()

setLogLevel( 'info' )
start( )

