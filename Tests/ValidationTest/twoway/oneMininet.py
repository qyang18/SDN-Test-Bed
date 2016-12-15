from mininet.net import Mininet
from mininet.topolib import TreeTopo
from mininet.node import RemoteController, OVSSwitch
from mininet.link import TCLink
import re
import sys

from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.link import Intf
from mininet.util import quietRun

info("*** Creating controllers\n")
net = Mininet( controller=RemoteController, switch = OVSSwitch )

c1 = net.addController('c1', ip='192.168.33.101', port=6033)
c2 = net.addController('c2', ip='192.168.33.101', port=6133)
c3 = net.addController('c3', ip='192.168.33.101', port=6233)

info("*** Creating switches\n")
s1 = net.addSwitch('s1',dpid='1000000000000001')
s2 = net.addSwitch('s2',dpid='1000000000000002')

info("*** Creating hosts\n")
h1 = net.addHost('h1',ip='12.1.0.1')
h2 = net.addHost('h2',ip='12.1.0.2')

info("*** Creating links\n")
link11 = net.addLink(s1,h1,cls=TCLink)
link11.intf1.config(bw=100)
link12 = net.addLink(s1,s2,cls=TCLink)
link12.intf1.config(bw=100)
link22 = net.addLink(s2,h2,cls=TCLink)
link22.intf1.config(bw=100)

#net.addLink(host, switch, bw=10, delay='5ms', loss=10, use_htb=True)

info("*** Starting network\n")
net.build()
net.start()
CLI(net)
net.stop()
