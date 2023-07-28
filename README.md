# naive-bayes
Naive Bayes classificator implementation.

# Theory

Naive Bayes is a conditional probability model: it assigns probabilities $P(y_k|X)$ for each of the K possible outcomes or classes with etiquettes $y_k$, given a problem instance to be classified, represented by a vector $X$ encoding some n features (independent variables).

Prawdopodobieństwo całkowite $P(y_k|X)$ jest proporcjonalne do:

$$P(X|y) \cdot P(y) = \Pi_{i=1}^n P(x_i|y)$$

where $n$ is a number of sample features.

# Implementation

Here we implement a Gaussian Naive Bayes that assumes a normal distribution of continous values associated with each class. 
