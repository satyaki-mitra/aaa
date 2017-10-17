direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']

class Lexicon:
    def scan(self, sentence):
        self.sentence = sentence
        self.words = sentence.split()
        stuff = []
        for word in self.words:
            if word in direction:
                stuff.append(('direction', word))
        return stuff

lexicon = Lexicon()
