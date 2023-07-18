from math import sqrt, exp, pi

def getNormalDistribution(mu: float, sigma: float):
    return lambda x: round(1/(sigma * sqrt(2*pi))* exp(-(1/2)*((x-mu)/sigma)**2), 5)