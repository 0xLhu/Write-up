##Above some truncated code##

import numpy as np 

for i, weight_matrix in enumerate(local_results["weights"]):
    #Add some noises 
    noise = np.random.normal(loc=0.0, scale=1.0, size=weight_matrix.shape)
    local_results["weights"][i] += noise
    
#Send poisonned data to server

poisoned_weights_json = weights_to_json(local_results["weights"])
rq.post(URL + " /challenges/1", json=poisoned_weights_json).json()