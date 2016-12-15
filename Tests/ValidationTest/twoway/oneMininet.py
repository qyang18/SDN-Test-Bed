from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController, OVSSwitch

from sys import argv

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, **opts):
        Topo.__init__(self, **opts)

  s1 = self.addSwitch('s1',dpid='1000000000000001')
	s2 = self.addSwitch('s2',dpid='1000000000000002')
            
  h1 = self.addHost('h1',ip='12.0.0.1')
	h2 = self.addHost('h2',ip='12.0.0.2')
        
	self.addLink(h1, s1, bw=100)
	self.addLink(s1, s2, bw=100)
	self.addLink(s2, h2, bw=100)

def perfTest(  ):
    "Create network and run simple performance test"
    topo = SingleSwitchTopo()
    net = Mininet( controller=RemoteController, topo=topo, link=TCLink, switch = OVSSwitch )
    c1 = net.addController('c1', ip='192.168.33.101', port=6033)
    c2 = net.addController('c2', ip='192.168.33.101', port=6133)
    c3 = net.addController('c3', ip='192.168.33.101', port=6233)
    	
    net.start()
    h1, h2 = net.getNodeByName('h1', 'h2')
    h1.cmd("./Server 5 &")
    h2.cmd("./Client 5 11.1.0.1 ")
    #CLI(net)
    net.stop()

setLogLevel( 'info' )
perfTest( )
