import random

class Reflector:
    def __init__(self):
        random.seed(0)
        
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        alphabet_shuffled = alphabet.copy()
        random.shuffle(alphabet_shuffled)
        
        self._wiring = {}
        
        for i in range(0, len(alphabet_shuffled), 2):
            a = alphabet_shuffled[i]
            b = alphabet_shuffled[i + 1]
            self._wiring[a] = b
            self._wiring[b] = a

    def reflect(self, char):
        reflected_char = self._wiring[char]
        return reflected_char