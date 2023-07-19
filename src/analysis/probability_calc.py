from math import sqrt, exp, pi


def getNormalDistribution(distribution_parameters: tuple[float] | list[float]):
    mean = distribution_parameters[0]
    std = distribution_parameters[1]
    return lambda x: round(
        1 / (mean * sqrt(2 * pi)) * exp(-(1 / 2) * ((x - mean) / std) ** 2), 5
    )
