class GenericProbe():
	def __init__(self):
		# audio setup
		self.CHUNK = None    # input buffer size in frames
		self.FORMAT = None   # data format
		self.CHANNELS = 2    # nchannels, up to two channels are supported
		self.RATE = None     # depends on input device, units 1/s
		self.p = None
		raise Exception('Generic, non-functional probe meant for development!')

	def open(self):
		pass

	def read(self, channel, npoints, verbose=False):
		pass

	def close(self):
		pass
