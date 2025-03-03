from Reflector import Reflector
from Rotor import Rotor
from Plugboard import Plugboard

# Heavily influenced by this code: https://github.com/jackburne/Enigma/blob/master/Enigma/enigma.py#L10-L129
class EnigmaMachine:
    def __init__(self, rotor_numbers, rotor_positions, plug_settings):
        
        self._rotor1 = Rotor(rotor_numbers[0], rotor_positions[0])
        self._rotor2 = Rotor(rotor_numbers[1], rotor_positions[1])
        self._rotor3 = Rotor(rotor_numbers[2], rotor_positions[2])
        
        self._reflector = Reflector()
        self._plugboard = Plugboard(plug_settings)
    

    def encrypt_decrypt_text(self, text):

        result = ""
        for char in text:
            if char.isalpha(): 

                self._rotor1.rotate()
                
                if self._rotor1._position == 0:
                    self._rotor2.rotate()
                    
                    if self._rotor2._position == 0:
                        self._rotor3.rotate()

                char = char.upper()
                
                char = self._plugboard.swap(char)

                char = self._rotor3.forward_mapping(char)
                char = self._rotor2.forward_mapping(char)
                char = self._rotor1.forward_mapping(char)
                
                char = self._reflector.reflect(char)
                
                char = self._rotor1.backward_mapping(char)
                char = self._rotor2.backward_mapping(char)
                char = self._rotor3.backward_mapping(char)
                
                char = self._plugboard.swap(char)
                result += char
            else:
                continue
        
        return result
        