from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController, OVSSwitch

from sys import argv

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

def start(  ):
    "Create network and run simple performance test"
    
    net = Mininet( controller=None, topo=DcellTopo(), link=TCLink, switch = OVSSwitch )
    c3 = RemoteController('c3', ip='192.168.56.101', port=6633)
    net.addController(c3)
  
    net.start()
    CLI(net)
    net.stop()

setLogLevel( 'info' )
start( )

