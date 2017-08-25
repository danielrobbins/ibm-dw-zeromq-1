#!/usr/bin/python3

from zmq_msg_core import *

class FileMessage(MultiPartMessage):

	header = b"FILE"

	def __init__(self, filename, contents):
		self.filename = filename
		self.contents = contents

	@property
	def msg(self):
		# returns list of all message frames as a byte-string:
		return [ self.header, self.filename.encode("utf-8"), self.contents ]

# vim: ts=4 sw=4 noet
