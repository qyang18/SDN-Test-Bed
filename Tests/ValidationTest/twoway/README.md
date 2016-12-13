# Two-Way Test 

## Goal

The goal of this test is to verify whether the links are “truly duplex” and whether the rate-limiters for tra c flowing in either direction are isolated. 

## Topo

The network consists of two host, between two hosts there are two switches, each host sending to the other. 

## Testbed

There are four testbed:

### One Mininet

All devices are virtualized by mininet.

### Two Mininet

There are two machines each running a mininet. Using GRE tunnel connect two mininets and each mininet virtualize half network devices.

### Mininet and Physical devices

Half devices in network are virtualized by mininet, others are real devices.

### Physical devices

All devices are real.


