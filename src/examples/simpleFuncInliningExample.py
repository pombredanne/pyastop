

def inlineFunc1(a, b):
	return a + b

a = inlineFunc1(1, 2) + inlineFunc1(3, 4)


class A(object):
	def __init__(self):
		self.val = 1

	def inlineMethod1(self, a):
		self.val += a
		return self.val

	def inlineMethod2(self, a):
		self.val += a
		return

	def testInline1(self):
		self.inlineMethod1(1)

	def testInline2(self):
		self.inlineMethod2(1)