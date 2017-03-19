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
from time import sleep


class TreeTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, **opts):
        Topo.__init__(self, **opts)
	centerSwitch=self.addSwitch(name = 's0',dpid='0000000000000001')
        for i in range(1, 6):   
            s = self.addSwitch(name = 's'+str(i),dpid='00000000000000'+str(i)+'0')
	    self.addLink(s,centerSwitch,bw=100)
            for j in range(1, 5):  
                h = self.addHost('h'+str(i)+str(j),ip='10.0.'+str(i)+'.'+str(j),mac='00:00:00:00:00:'+str(i)+str(j))
                s_h = self.addSwitch(name = 's'+str(i)+str(j),dpid='00000000000000'+str(i)+str(j)) 
		self.addLink(h, s_h , bw=100)
	    	self.addLink(s,s_h , bw=100)


def PerfTest(net):
    #net.pingAll()
    print("start random perf test")
    #select 5 links of client-server pair and run iperf
    #50G
    FileSize=50000000

    for i in range(0,20):
	#start 20 server, for each server we create 19 files to store logs of 19 connections with 19 other nodes. 
	print('generating server:h'+str(1+i/4)+str(1+i%4))
	server=net.getNodeByName('h'+str(1+i/4)+str(1+i%4))
	for j in range(1,21):
		serverIperfArgs = 'iperf -s -i 1 -p %d > log%sp%sv%d &' % (10000+j,i+1,j, 6)
		server.cmd(serverIperfArgs)

    for i in range(0,20):
	server=net.getNodeByName('h'+str(1+i/4)+str(1+i%4))
	for j in range(0,20):
		if i==j :
			continue
		#start 20 client sending data to all the rest 19 servers
		client=net.getNodeByName('h'+str(1+j/4)+str(1+j%4));
		clientIperfArgs = 'iperf -c %s -p %d -n %d -i 1 &' % (str(server.IP()),10001+j,FileSize)
		print('generating iperf client from'+str(client.IP())+' to '+str(server.IP())+'on port:'+str(10001+j))
		client.cmd(clientIperfArgs)

def start(  ):
    "Create network and run simple performance test"
    
    net = Mininet( controller=None, topo=TreeTopo(), link=TCLink, switch = OVSSwitch )
    c3 = RemoteController('c3', ip='192.168.56.101', port=6633)
    net.addController(c3)
    
    net.start()
    PerfTest(net)
    CLI(net)
    net.stop()

setLogLevel( 'info' )
start( )
