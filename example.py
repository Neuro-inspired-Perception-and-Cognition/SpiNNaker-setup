import spynnaker.pyNN as p

p.setup(timestep=1.0)
pop = p.Population(3, p.IF_curr_exp(), label="MyPopulation")
p.run(100)
p.end()


# netsh interface ipv4 set address name="Ethernet" static 130.88.198.99 255.255.255.0 0.0.0.0