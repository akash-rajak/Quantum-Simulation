import numpy as np
import dimod
from dwave.system import DWaveSampler, EmbeddingComposite

# Define the Ising problem
h = {0: -1, 1: -1, 2: 2}
J = {(0, 1): 1, (1, 2): -1}

# Define the sampler
sampler = EmbeddingComposite(DWaveSampler())

# Solve the problem
response = sampler.sample_ising(h, J, num_reads=1000)

# Print the result
print(response)
