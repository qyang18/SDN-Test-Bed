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
s1 = net.addSwitch('s1',dpid='1000000000000011')
s2 = net.addSwitch('s2',dpid='1000000000000012')

info("*** Creating hosts\n")
h1 = net.addHost('h1',ip='12.0.1.1')
h2 = net.addHost('h2',ip='12.0.1.2')
h3 = net.addHost('h3',ip='12.0.1.3')
h4 = net.addHost('h4',ip='12.0.1.4')

info("*** Creating links\n")
link1 = net.addLink(s1,h1,cls=TCLink)
link1.intf1.config(bw=100)
link2 = net.addLink(s1,s2,cls=TCLink)
link2.intf1.config(bw=100)
link3 = net.addLink(s2,h2,cls=TCLink)
link3.intf1.config(bw=100)
link4 = net.addLink(s2,h3,cls=TCLink)
link4.intf1.config(bw=100)
link5 = net.addLink(s2,h4,cls=TCLink)
link5.intf1.config(bw=100)

info("*** Starting network\n")
net.build()
net.start()
CLI(net)
net.stop()
