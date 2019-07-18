#!/usr/bin/env python
''' This is a docstring for the markov module
'''
import random
import sys, argparse
import urllib.request as req

class Markov:
    def __init__(self, text, size = 1):
        #self.table = get_table(text)
        self.tables = []
        for i in  range(size):
            self.tables.append(
                get_table(text, size = i+1))

    def predict(self, data):
        #options = self.table.get(data, {})
        table = self.tables[len(data) - 1]
        options = table.get(data, {})
        if not options:
            raise KeyError(f'{data} not in training')
        possibles = []
        for letter, count in options.items():
            for i in range(count):
                possibles.append(letter)
        return random.choice(possibles)            
def get_table(text, size =1):
    '''This is the function docstring
    >>> get_table('ab')
    {'a':{'b':1}}
    '''
    results = {} # dictionary literal
    for i in range(len(text)):
        chars = text[i:i + size]
        try:
            out = text[i + size]
        except IndexError:
                break
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results

def fetch_url(url, fname):
    import urllib.request as req
    fin = req.urlopen(url)
    data = fin.read()
    with open(fname, mode = 'w', encoding = 'utf8') as fout:
        fout.write(data.decode('utf8'))

def from_file(fname, size = 1):
    fin = open(fname, encoding = 'utf8')
    m = Markov(fin.read(), size = size)
    return m

def repl(m):
    print("welcome to the repl")
    while True:
        try:
            txt = input('>')
        except KeyboardInterrupt:
            print("Goodbye")
            break
        try:
            res = m.predict(txt)
        except KeyError:
            print("Not found try again")
        except IndexError:
            print("Too long try again")
        else:
            print(res)

def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', help = 'File to load')
    ap.add_argument('-s', '--size', help = 'Size (default 1)',
                     default = 1, type = int)
    opt = ap.parse_args(args)
    if opt.file:
        m = from_file(opt.file, size= opt.size)
        repl(m)
            
if __name__ == '__main__':
    print(f"executing markov as {__name__}")
    #m = from_file('pp.txt', size=4)
    #repl(m)
    main(sys.argv[1:])
else:
    print(f"loading markov as {__name__}")
