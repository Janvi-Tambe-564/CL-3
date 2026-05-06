import Pyro4
@Pyro4.expose
class StringConcatenator:
	def concatenator(self,s1,s2):
		return s1+s2
daemon=Pyro4.Daemon()
uri=daemon.register(StringConcatenator)
print("server uri:", uri)
daemon.requestLoop()
