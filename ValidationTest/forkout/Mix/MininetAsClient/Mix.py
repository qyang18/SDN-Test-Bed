from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController, OVSSwitch
from mininet.link import Intf
from sys import argv

def perfTest(  ):
    "Create network and run simple performance test"
    net = Mininet( controller=RemoteController, topo=None, link=TCLink )
    c1 = net.addController('c1', ip='192.168.33.101', port=6033)
    c2 = net.addController('c2', ip='192.168.33.101', port=6133)
    c3 = net.addController('c3', ip='192.168.33.101', port=6233)

    s1 = net.addSwitch('s1',dpid='1000000000000001')
    #s2 = self.addSwitch('s2',dpid='1000000000000002')
    #Intf('enp2s0', node=s1)
    Intf('eth0',node=s1)
    h1 = net.addHost('h1',ip='10.0.1.31')
    #h2 = self.addHost('h2',ip='12.0.0.2')

    net.addLink(h1, s1, bw=100)

    net.start()
    h1 = net.getNodeByName('h1')

    h1.cmd("./Client 1-2v10 10.0.1.11&")
    h1.cmd("./Client 1-3v10 10.0.1.12&")
    h1.cmd("./Client 1-4v10 10.0.1.13 ")
    #CLI(net)
    net.stop()

setLogLevel( 'info' )
perfTest()
