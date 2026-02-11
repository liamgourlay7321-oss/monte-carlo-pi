import numpy as np

def estimate_pi(n, seed = None):
    """
    Estimate Pi using Monte Carlo simulation.

    Parameters
    ----------
    n : Number of random samples
    seed : Random seed for reproducibility

    Returns
    -------
    Estimated value of Pi
    """
    if seed is not None:
        np.random.seed(seed)

    x = 2 * np.random.rand(n) - 1
    y = 2 * np.random.rand(n) - 1

    inside_circle = (x**2 + y**2) <= 1
    return 4 * np.mean(inside_circle)

if __name__ == "__main__":
    for runs in [100, 1_000, 10_000, 100_000]:
        pi_estimate = estimate_pi(runs, seed=42)
        print(f"n={runs}, Pi={pi_estimate:.6f}")
