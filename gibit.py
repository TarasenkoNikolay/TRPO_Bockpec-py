import random
import os


class Gibit:
    man = '-@--<--<'

    def __init__(self):
        self.load_words()
        self.user_chars = []

    def load_words(self):
        self.words = []
        with open('words.txt') as f:
            self.words.append(f.readline())
        self.word = random.choice(self.words)

    def show_state(self):
        show_chars = [el if el in self.user_chars else '_' for el in self.word]
        print(show_chars)

    def play(self):
        start = ''
        loose_count = 0
        i = 0

        while 1:
            self.show_state()
            print(start)
            c = input('your char: ')
            c_i = self.word[i]
            self.user_chars.append(c)
            if c == c_i:
                print('ok!')
                i += 1
                continue

            if loose_count < len(self.man):
                start += self.man[loose_count]
                loose_count += 1
            else:
                print('you loose')
                return




if __name__ == '__main__':
    #Gibit().play()
    print('tests OK')
