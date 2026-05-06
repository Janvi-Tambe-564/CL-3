import Pyro4
uri=input("server uri:")
concatenator=Pyro4.Proxy(uri)
s1=input("enter s1:")
s2=input("enter s2:")
result=concatenator.concatenator(s1,s2)
print(result)
