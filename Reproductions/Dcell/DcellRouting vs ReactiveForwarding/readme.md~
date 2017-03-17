DcellRouting vs ReactiveForwarding(Rule install time):
I start the test by comparing the rule install time between 2 different routing algorithms: reactive forwarding and Dcell routing.
The topology stays the same, both using Dcell topology in SDN testbed.

note that in reactive forwarding rule will not expire if we keep ping within default timeout. We get the rule install time by starting one ping at a time, then wait for the rule expires and start another ping.

I have 5 sets of pings from different hosts.For each set that host ping another host we repeat it 10 times.
1hop: h11 ping h21	s11,s21
3hop: h12 ping h32	s12,s31,s32
4hop: h13 ping h23 	s13,s41,s42,s23
5hop: h14 ping h22	
5hop: h43 ping h53

There is a difference in algorithms, reactive forwarding trys to find the shortest path whereas Dcell find the path by calculation which means in some cases Dcell may not find the shortest path.

eg. h13 ping h23
in shortest path:	s13<->s41<->s40<->s42<->s23		4hop
in Dcell routing:	s13<->s10<->s11<->s21<->s20<->s23	5hop
