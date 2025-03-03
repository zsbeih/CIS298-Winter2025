class Plugboard:
    def __init__(self, plug_settings):

        self.wiring = {}
        for i in range(0, len(plug_settings), 2):
            a = plug_settings[i]
            b = plug_settings[i + 1]
            self.wiring[a] = b
            self.wiring[b] = a

    def swap(self, char):
        plugboard_char = self.wiring.get(char, char) 
        return plugboard_char