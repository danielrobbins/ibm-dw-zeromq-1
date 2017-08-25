#!/usr/bin/python3

from zmq_msg_core import *

class HelloMessage(MultiPartMessage):
	
	header = b"HELLO"


