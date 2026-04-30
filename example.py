import spynnaker.pyNN as p

p.setup(timestep=1.0)
pop = p.Population(3, p.IF_curr_exp(), label="MyPopulation")
p.run(100)
p.end()
