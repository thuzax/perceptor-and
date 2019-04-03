class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, lr=1, epochs=100):
        self.W = [0] * (input_size + 1)
        # add one for bias
        self.epochs = epochs
        self.lr = lr

    def activation_fn(self, x):
        #print( " x=", x)
        #funcao binaria
        return 1 if x >= 0 else 0

        #funcao bipolar
        # return 1 if x >= 0 else -1



    def weighted_sum(self, x, w):
        if(len(x) != len(w)):
            raise Exception("List with differents sizes")
        r = 0
        for i in range(len(w)):
            r += x[i] * w[i]
        return r

    def predict(self, x):
        z = self.weighted_sum(self.W, x)
        a = self.activation_fn(z)
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(len(d)):
                x = [1] + X[i]
                y = self.predict(x)
                e = d[i] - y
                for j  in range(len(self.W)):
                    self.W[j] = self.W[j] + self.lr * e * x[j]


if __name__ == '__main__':
    print("----------------------AND----------------------")
    # AND training
    X = [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]
    d = [0, 0, 0, 1]

    input_size = 2
    perceptron_and = Perceptron(input_size)
    perceptron_and.fit(X, d)
    print("The W results = ",perceptron_and.W)

    # AND testing
    testes = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    print("Tests and results:")
    for t in testes:
        x = [1] + t
        print("\t", x[1], " AND ", x[2], " = ", perceptron_and.predict(x))

    print("----------------------OR----------------------")
    # OR training
    X = [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]
    d = [0, 1, 1, 1]

    input_size = 2
    perceptron_or = Perceptron(input_size)
    perceptron_or.fit(X, d)
    print("The W results = ",perceptron_or.W)

    # OR testing
    testes = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    print("Tests and results:")
    for t in testes:
        x = [1] + t
        print("\t", x[1], " OR ", x[2], " = ", perceptron_or.predict(x))


