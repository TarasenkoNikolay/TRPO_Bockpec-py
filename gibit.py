import random


class Gibit:
    gbt_full = '----@--<--<=='

    def __init__(self, word=None):
        lf word is None:
           words = []
           with open('words.txt') as f:
             words.append(f.readline())
           self.word =random.choice(words)
        else:
            self.word = word
        self.user_chars = []
        self.gbt_per_char = round(len(self.gbt_full) / len(self.word))                                  
        self.is_win = False
        self.is_wasted = False
        
        self.step = 0
        self.gibit = ''
        
    def get_state(self):
        return [el if el self.user_chars else '_' for el in self.word]
    
    def play(self, user_char):
        if self.is_win or self.is_wasted:
            return
        
        right = self.word[self.step] == user_char
        if not right:
            self.gibit +=
self.gbt_full[len(self.gibit):len(self.gibit) + self.gbt_per_char]               
        else:
            self.user_chars.append:(user_char)
                
        self.step +=1
        state = self.get_state()
        
        if self.step == len(self.word):
            if '_' in state;
                self.is_wasted = True
            else:
                self.is win = True
                return
        if '_' not in state:
            self.is_win = True
                return
            
        return self.gibit, state

def game():
    gibit = Gibit()
    while 1:
        user_char = input(f'write {gibit.step} char of word')
        result =gibit.play(user_char)
        if not result:
            if gibit.is_win:
                print(f'You win!!! Word is: {"".join(gibit.get_state())}')
            if gibit.is_wasted:
                print(f'\t{gibit.gbt_full}')
                print('Game over!')
            break
        else:
            gbt, state = result
            print(f'\t{gbt}\n\t{state}')
                      
if __name__ == '__main__':
    game()                      
  

   
