Testbed topo:
 *****.jpg
 
ONOS Install guide:
https://wiki.onosproject.org/display/ONOS/ONOS+from+Scratch

UFW add rule to allow SDN connection:
$ sudo UFW allow <port>

Use screen for initialization of Pica8 via serial port(when Pica8 has no IP address)
$ screen /dev/ttyS0 115200

Install and configure Pica8:
$ sudo picos_boot
Select the mode of pica8 as Open vSwitch mode
$ sudo service picos start
$ sudo reboot

Add bridge on Pica8(a bridge means a virtual switch, * is the bridge name you set):
$ ovs-vsctl add-br br* 

Add port to the bridge(* is the port number on Pica8):
$ ovs-vsctl add-port br* ge-1/1/* -- set Interface ge-1/1/* type=pica8 

In switch mode you may not be able to connect with each other even if both devices connect to the same bridge,if you want to connect with each other without Pica8 connect to a controller, you can add a local flow rule and it will work.

Add flow rule(bidirectional):
$ ovs-ofctl add-flow br* in_port=1,actions=output:2
$ ovs-ofctl add-flow br* in_port=2,actions=output:1

dump port and check rx tx:
$ ovs-ofctl dump-ports br0

dump flow:
$ ovs-ofctl dump-flows br0

set controller(connect bridge to SDN controller):
$ ovs-vsctl set-controller br* tcp:*.*.*.*:6633

set OpenFlow protocol version:
$ ovs-vsctl set Bridge br* protocols=OpenFlow14


check connection:
$ netstat -an | grep 6633

Mininet and ONOS are installed on the same device, now connect mining to ONOS:

$ sudo mn --controller remote,ip=192.168.51.101
