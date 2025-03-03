from unittest import TestCase
from EnigmaMachine import EnigmaMachine
from Reflector import Reflector
from Rotor import Rotor
from Plugboard import Plugboard

class TestEnigmaMachine(TestCase):
    
    def test_rotor_initialization(self):
        # Test initializing rotor and the length of wiring and reverse wiring
        rotor = Rotor(1, 0)
        self.assertEqual(len(rotor._wiring), 26)
        self.assertEqual(len(rotor._reverse_wiring), 26)
        
    def test_rotor_rotation(self):
        # Test rotating the rotor as well as the position of the rotor after rotating on the last position(25)
        rotor = Rotor(1, 0)
        self.assertEqual(rotor._position, 0)
        
        rotor.rotate()
        self.assertEqual(rotor._position, 1)
        
        rotor = Rotor(1, 25)
        rotor.rotate()
        self.assertEqual(rotor._position, 0)
    
    def test_reflector(self):
        # Test the reflector by checking if the reflection of a reflected character is the same as the original character
        reflector = Reflector()
        chars = ['A', 'B', 'Z']
        for char in chars:
            reflected = reflector.reflect(char)
            self.assertEqual(reflector.reflect(reflected), char)
    
    def test_plugboard(self):
        # Test the plugboard by checking if the pairs are correctly initialized
        plugboard = Plugboard("ABCDEFGHIJKLMNOPQRST")
        
        self.assertEqual(plugboard.swap('A'), 'B')
        self.assertEqual(plugboard.swap('B'), 'A')
        self.assertEqual(plugboard.swap('Z'), 'Z')
    
    def test_enigma_encryption_decryption(self):
        # Test the enigma machine itself which tests encrypting and decrypting text including the forward and backward mapping in the Rotor class
        
        test_messages = ["HELLO", "HELLOWORLD", "GOODBYE"]
        
        for message in test_messages:
            enigma = EnigmaMachine([1, 2, 3], [0, 0, 0], "ABCDEFGHIJKLMNOPQRST")

            encrypted = enigma.encrypt_decrypt_text(message)
            
            enigma = EnigmaMachine([1, 2, 3], [0, 0, 0], "ABCDEFGHIJKLMNOPQRST")
            
            decrypted = enigma.encrypt_decrypt_text(encrypted)
            
            self.assertEqual(decrypted, message)
    
    
  