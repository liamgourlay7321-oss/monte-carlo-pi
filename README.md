# Monte Carlo Estimation of π

This project estimates the value of π using a Monte Carlo simulation.

## Method
Random points are sampled uniformly from the square [-1,1] × [-1,1].
The proportion that fall inside the unit circle is used to estimate π:

π ≈ 4 × (points inside circle / total points)

## Results
The estimate converges to π as the number of samples increases
