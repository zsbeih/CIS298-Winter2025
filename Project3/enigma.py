from EnigmaMachine import EnigmaMachine

print("Please enter the Enigma machine settings:")
print("Format: '3 2 5 24 12 11 ABCDEFGHIJKLMNOPQRST'")
print("\nNote: First 3 numbers = rotor number(1-5)")
print("        Next 3 numbers = rotor positions (0-25)")
print("        Last 20 letters = 10 plugboard pairs")
settings = input("Input here: ")

settings_parsed = settings.split()
rotor_numbers = settings_parsed[0:3]
rotor_positions = settings_parsed[3:6]
plug_settings = settings_parsed[6]

continue_input = 'Y'
while(continue_input.lower() != 'n'):
    enigma = EnigmaMachine(rotor_numbers, rotor_positions, plug_settings)
    text = input("\nPlease input your text to be encryted or decrypted(anything besides a letter will be stripped): ")
    encrypted_decrypted_text = enigma.encrypt_decrypt_text(text)
    print(f"Output text: {encrypted_decrypted_text}")
    continue_input = input("\nWould you like to continue using the Enigma machine? (Y/n)")

