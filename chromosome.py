
class Chromosome:

    binary = ""
    fitness = 0.0
    real_value = 0.0

    def __init__(self, _binary,  _real_value , _fitness = 0.0 ):


        self.binary = _binary
        self.fitness = _fitness
        self.real_value = _real_value
