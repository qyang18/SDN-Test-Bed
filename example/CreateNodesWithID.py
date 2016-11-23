from mininet.net import Mininet
from mininet.topolib import TreeTopo
from mininet.node import RemoteController, OVSSwitch
import re
import sys

from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.link import Intf
from mininet.util import quietRun


net = Mininet(controller = RemoteController, switch = OVSSwitch)

info("*** Creating controllers\n")
c0 = RemoteController('c0', ip='127.0.0.1', port=6633) # set controller
net.addController(c0) # add controller to mininet

info("*** Creating switches\n")
s1 = net.addSwitch('s1',dpid='0000000000000005')

info("*** Creating hosts\n")
h1 = net.addHost('h1',ip='10.0.1.1')
h2 = net.addHost('h2',ip='10.0.1.2')

info("*** Creating links\n")
net.addLink(s1,h1)
net.addLink(s1,h2)

intfName = sys.argv[ 1 ] if len( sys.argv ) > 1 else 'eth1' # 'eth1' can be instead by physical ethernet you want to assign to mininet switch
_intf = Intf( intfName, node=s1) # assign physical port to switch in mininet

info("*** Starting network\n")
net.build()
net.start()
CLI(net)
net.stop()
