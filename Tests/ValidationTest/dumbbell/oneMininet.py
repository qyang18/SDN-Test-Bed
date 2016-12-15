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
s1 = net.addSwitch('s1',dpid='1000000000000041')
s2 = net.addSwitch('s2',dpid='1000000000000042')

info("*** Creating hosts\n")
h1 = net.addHost('h1',ip='12.0.4.1')
h2 = net.addHost('h2',ip='12.0.4.2')
h3 = net.addHost('h3',ip='12.0.4.3')
h4 = net.addHost('h4',ip='12.0.4.4')
h5 = net.addHost('h5',ip='12.0.4.5')
h6 = net.addHost('h6',ip='12.0.4.6')
h7 = net.addHost('h7',ip='12.0.4.7')
h8 = net.addHost('h8',ip='12.0.4.8')

info("*** Creating links\n")
linkss = net.addLink(s1,s2,cls=TCLink)
linkss.intf1.config(bw=100)
link11 = net.addLink(s1,h1,cls=TCLink)
link11.intf1.config(bw=100)
link12 = net.addLink(s1,h2,cls=TCLink)
link12.intf1.config(bw=100)
link13 = net.addLink(s1,h3,cls=TCLink)
link13.intf1.config(bw=100)
link14 = net.addLink(s1,h4,cls=TCLink)
link14.intf1.config(bw=100)
link21 = net.addLink(s2,h5,cls=TCLink)
link21.intf1.config(bw=100)
link22 = net.addLink(s2,h6,cls=TCLink)
link22.intf1.config(bw=100)
link23 = net.addLink(s2,h7,cls=TCLink)
link23.intf1.config(bw=100)
link24 = net.addLink(s2,h8,cls=TCLink)
link24.intf1.config(bw=100)


info("*** Starting network\n")
net.build()
net.start()
CLI(net)
net.stop()
