import numpy as np 
import os 
import matplotlib.pyplot as plt
from PIL import Image

phon = {
    'a':'a',
    'i':'i',
    'u':'u',
    'e':'e',
    'o':'o',
    'ka':'ka',
    'ki':'ki',
    'ku':'ku',
    'ke':'ke',
    'ko':'ko',
    'sa':'sa',
    'si':'shi',
    'su':'su',
    'se':'se',
    'so':'so',
    'ha':'ha',
    'hi':'hi',
    'hu':'fu',
    'he':'he',
    'ho':'ho',
    'ta':'ta',
    'ti':'tchi',
    'tu':'tsu',
    'te':'te',
    'to':'to',
    'na':'na',
    'ni':'ni',
    'nu':'nu',
    'ne':'ne',
    'no':'no',
    'ha':'ha',
    'hi':'hi',
    'hu':'fu',
    'he':'he',
    'ho':'ho',
    'ma':'ma',
    'mi':'mi',
    'mu':'mu',
    'me':'me',
    'mo':'mo',
    'wa':'wa',
    'wo':'o',
    'ya':'ya',
    'yu':'yu',
    'yo':'yo',
    'n':'n',
    
}
class Quiz:
    number = 3
    typeof = 'Hiragana'
    #typeof = 'Katakana'
    consonants = ['','k','s','t','n','h']
    vogals = ['a','i','u','e','o']
    formats = ['png','jpg','jfif']
    def __init__(self):
        pass

    def select_random(self,number=3):
        combinations = []
        consonants = []
        vogals = []

        for n in range(number):
            consonant = ''       
            vogal = ''
            while(consonant + vogal not in phon.keys()):
                consonant = Quiz.consonants[np.random.randint(0,high=len(Quiz.consonants))]
                if(consonant != 'n'):
                    vogal = Quiz.vogals[np.random.randint(0,high=len(Quiz.vogals))]
                else:
                    list_of_vogals = Quiz.vogals + ['']
                    vogal = list_of_vogals[np.random.randint(0,high=len(list_of_vogals))]
            combinations.append(consonant + vogal)
            consonants.append(consonant)
            vogals.append(vogal)

        __loc__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
        directory = os.path.join(__loc__,Quiz.typeof)
        imgs = []
        for n in range(number):
            for form in Quiz.formats:
                pic_path = os.path.join(directory,consonants[n] + vogals[n] + '.' + form)
                try:
                    img = Image.open(pic_path)
                    #img[img<255] = 0
                    #img[img==255] = 1
                    imgs.append(img)
                    break
                except:
                    pass
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
        plt.imshow(imgs_comb)
        plt.show()
        tmp = ''
        for comb in combinations:
            tmp += phon[comb] 
        print(tmp)

if __name__ == "__main__":
    quiz = Quiz()
    quiz.select_random()