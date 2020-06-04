import numpy as np 
import os 
import matplotlib.pyplot as plt
from PIL import Image

class Quiz:
    phonetics = {
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
        'da':'da',
        'di':'di',
        'du':'du',
        'de':'de',
        'do':'do',
        'pa':'pa',
        'pi':'pi',
        'pu':'pu',
        'pe':'pe',
        'po':'po',
        'ba':'ba',
        'bi':'bi',
        'bu':'bu',
        'be':'be',
        'bo':'bo',
    }
    def __init__(self,**kwargs):
        # Standards of variables. Hiragana, all consonants, all vogals.
        self.typeof = kwargs.get('type_of_char','Hiragana')
        self.consonants = kwargs.get('consonants',['','k','s','t','n','h','m','r','w','y','d','p','b'])
        self.vogals = kwargs.get('vogals',['a','i','u','e','o'])

    def select_random(self,number=2):
        combinations = []
        consonants = []
        vogals = []
        fill_transparency = True
        for n in range(number):
            consonant = ''       
            vogal = ''
            while(consonant + vogal not in Quiz.phonetics.keys()):
                consonant = self.consonants[np.random.randint(0,high=len(self.consonants))]
                if(consonant == 'n' and len(consonants) != 0):
                    list_of_vogals = self.vogals + ['']
                    vogal = list_of_vogals[np.random.randint(0,high=len(list_of_vogals))]
                else:
                    vogal = self.vogals[np.random.randint(0,high=len(self.vogals))]
            combinations.append(consonant + vogal)
            consonants.append(consonant)
            vogals.append(vogal)

        __loc__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
        directory = os.path.join(__loc__,self.typeof)
        imgs = []
        for n in range(number):
            pic_path = os.path.join(directory,consonants[n] + vogals[n] + '.png')
            try:
                img = Image.open(pic_path).convert("L")
                imgs.append(img)
            except:
                pass
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
        
        if(fill_transparency):
            cut = 190
            imgs_comb[imgs_comb<=cut] = 0
            imgs_comb[imgs_comb>cut] = 1
        
        ax = plt.imshow(imgs_comb,cmap='gray',vmin=0,vmax=1)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        plt.show()
        tmp = ''
        for comb in combinations:
            tmp += Quiz.phonetics[comb].capitalize() + ' '
        print()
        print('Answer: ' + tmp)
        print()
if __name__ == "__main__":
    consonants = ['','b']  
    vogals = ['a','i','u','e','o']
    type_of_char = 'Hiragana'
    number_of_characters = 3
    #typeofchar = 'Katakana'
    quiz = Quiz(
        type_of_char=type_of_char,
        consonants=consonants,
        vogals=vogals)
    quiz.select_random(number_of_characters)