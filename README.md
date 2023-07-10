# naive-bayes
Implementacja naiwnego klasyfikatora Bayesa.

# Teoria

Naiwny klasyfikator Bayesa zajmuje się liczeniem prawdopodobieństw warunkowych $P(y_k|X)$, gdzie $y_k$ to klasa etykiety, a $X$ to wektor cech klasyfikowanej próbki.

Człon *naiwny* pochodzi od założenia klasyfikatora, że założenia są niezależne.

Prawdopodobieństwo całkowite $P(y_k|X)$ jest proporcjonalne do:

$$P(y|X) 	\propto P(X|y) \cdot P(y) = \Pi_{i=1}^n P(x_i|y)$$

gdzie $n$ to liczba cech próbki.
