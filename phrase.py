class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.comparison_phrase = []
        self.hidden_phrase = ['_' if char!=' ' else ' ' for char in list(self.phrase)]
    
    def __iter__(self):
        yield from self.phrase
    
    def __eq__(self, other):
        return self.comparison_phrase == other
    
    def display(self):
        return print('\n',*self.hidden_phrase, sep=" ")
    
    def check_complete(self):
        if self.comparison_phrase == self.phrase or '_' not in self.hidden_phrase:
            return True
        
    def check_letter(self, guess):
        for i, letter in enumerate(self.phrase):
            if letter == guess:
                self.hidden_phrase[i] = letter
                self.comparison_phrase.append(letter)
        if guess in self.comparison_phrase:
            return True
