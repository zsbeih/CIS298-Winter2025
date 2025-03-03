import random

class Rotor:
    def __init__(self, rotor_number, starting_position):
        self._rotor_number = int(rotor_number)
        self._position = int(starting_position)

        random.seed(rotor_number)
        
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        alphabet_shuffled = alphabet.copy()
        random.shuffle(alphabet_shuffled)

        self._wiring = {}
        self._reverse_wiring = {}
        for i in range(26):
            self._wiring[alphabet[i]] = alphabet_shuffled[i]
            self._reverse_wiring[alphabet_shuffled[i]] = alphabet[i]
            
    # Heavily influenced by this code: https://github.com/jackburne/Enigma/blob/master/Enigma/Rotor.py#L57-L85
    def forward_mapping(self, char): 
        letter_position = ord(char) - 65
        letter_position = (letter_position + self._position) % 26
        char = chr(letter_position + 65)
        
        map_output = self._wiring[char]
        
        letter_position2 = ord(map_output) - 65

        letter_position2 = (letter_position2 - self._position) % 26

        final_letter = chr(letter_position2 + 65)
        
        return final_letter 

    def backward_mapping(self, char):
        letter_position = ord(char) - 65
        letter_position = (letter_position + self._position) % 26
        char = chr(letter_position + 65)
        
        map_output = self._reverse_wiring[char]
        
        letter_position2 = ord(map_output) - 65
        letter_position2 = (letter_position2 - self._position) % 26
        final_letter = chr(letter_position2 + 65)
        
        return final_letter

    def rotate(self):
        self._position = (self._position + 1) % 26 