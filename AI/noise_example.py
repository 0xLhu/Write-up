# Example code to add noise
for i, weight_matrix in enumerate(local_results["weights"]):
    noise = np.random.normal(loc=0.0, scale=1.0, size=weight_matrix.shape)
    local_results["weights"][i] += noise
