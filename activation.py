import math

class ActivationFunction:
    # __singleton = None
    # def __new__(cls):
    #     cls.__singleton = cls
    def __init__(self, type='Sigmoid'):
        # if self.__singleton is None:
        #     self.__singleton = self
        # cls = self.__singleton
        self.func = self.sigmoid
        self.dfunc = self.dsigmoid

        if type == 'Sigmoid':
            self.func = self.sigmoid
            self.dfunc = self.dsigmoid
        elif type == 'Sign':
            self.func, self.dfunc = self.sign, self.dsign

    # def run(self):
    #     return self.func(x)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    # derivative of our sigmoid function, in terms of the output (i.e. y)
    def dsigmoid(self, y):
        return y * (1 - y)

    def sign(self, x):
        if x >= 0:
            return 1
        else:
            return -1

    def dsign(self, y):
        return 1

if __name__ == '__main__':
    myfunc = ActivationFunction('Sigmoid')
    print(myfunc.sigmoid(2))
    print(myfunc.dsigmoid(0.1))
