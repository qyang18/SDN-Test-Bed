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

    #Intf('enp2s0', node=s1)
    Intf('eth0', node=s1)

    h1 = net.addHost('h1',ip='10.0.1.31')
    h2 = net.addHost('h2',ip='10.0.1.32')
    h3 = net.addHost('h3',ip='10.0.1.33')

    net.addLink(h1, s1, bw=100)
    net.addLink(h2, s1, bw=100)
    net.addLink(h3, s1, bw=100)

    net.start()
    #h1.cmd("./Server 6v6 &")
    #h2.cmd("./Server 5v6 &")
    #h3.cmd("./Server 4v6 ")

    #h1.cmd("./Client 6-1v1 10.0.1.11 &")
    #h2.cmd("./Client 5-2v1 10.0.1.12 &")
    #h3.cmd("./Client 4-3v1 10.0.1.13 ")
    CLI(net)
    net.stop()

setLogLevel( 'info' )
perfTest()
