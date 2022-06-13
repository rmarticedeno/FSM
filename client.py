import rpyc

c = rpyc.connect('localhost', 6000)

print(c.root.info())