from math import sqrt, exp, pi


def getNormalDistribution(distribution_parameters: tuple[float] | list[float]):
    """
    Returns a callable lambda function of normal distribution's PDF.
    # Parameters
    - `distribution_parameters` - list of distribution's parameters, mean and standard deviation(in that order)
    # Returns
    - a lambda function that takes an `x` argument and returns this argument's value from Gaussian PDF.
    """
    mean = distribution_parameters[0]
    std = distribution_parameters[1]
    return lambda x: round(
        1 / (std * sqrt(2 * pi)) * exp(-(1 / 2) * ((x - mean) / std) ** 2), 5
    )
