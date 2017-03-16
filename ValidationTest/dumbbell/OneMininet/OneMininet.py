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

        s1 = self.addSwitch('s1',dpid='1000000000000041')
        s2 = self.addSwitch('s2',dpid='1000000000000042')

        h1 = self.addHost('h1',ip='12.0.4.1')
        h2 = self.addHost('h2',ip='12.0.4.2')
        h3 = self.addHost('h3',ip='12.0.4.3')
        h4 = self.addHost('h4',ip='12.0.4.4')
        h5 = self.addHost('h5',ip='12.0.4.5')
        h6 = self.addHost('h6',ip='12.0.4.6')

        self.addLink(s1, s2, bw=100)
        self.addLink(s1, h1, bw=100)
        self.addLink(s1, h2, bw=100)
        self.addLink(s1, h3, bw=100)
        self.addLink(s2, h4, bw=100)
        self.addLink(s2, h5, bw=100)
        self.addLink(s2, h6, bw=100)

def perfTest(  ):
    "Create network and run simple performance test"
    topo = SingleSwitchTopo()
    net = Mininet( controller=RemoteController, topo=topo, link=TCLink, switch= OVSSwitch )
    c1 = net.addController('c1', ip='192.168.33.101', port=6033)
    c2 = net.addController('c2', ip='192.168.33.101', port=6133)
    c3 = net.addController('c3', ip='192.168.33.101', port=6233)

    net.start()
    h1, h2, h3, h4, h5, h6= net.getNodeByName('h1', 'h2', 'h3', 'h4', 'h5', 'h6')
    h4.cmd("./Server 4v5 &")
    h5.cmd("./Server 5v5 &")
    h6.cmd("./Server 6v5 &")

    h1.cmd("./Client 1-6v5 12.0.4.6 &")
    h2.cmd("./Client 2-5v5 12.0.4.5 &")
    h3.cmd("./Client 3-4v5 12.0.4.4 ")
    #CLI(net)
    net.stop()

setLogLevel( 'info' )
perfTest( )
