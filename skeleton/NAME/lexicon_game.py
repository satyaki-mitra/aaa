class Lexicon(object):


    def scan(self, sentence):
        wordlist = sentence.split()
        result=[]
        verb=['go','kill','eat']
        direction=['north','south','east','west']
        noun=['bear','princess']
        stop=['the','in','of']
        vocab={'verb':verb,'direction':direction,'noun':noun,'stop':stop}
        for word in wordlist:
            found=False
            for key,value in vocab.items():
                if word.lower() in value:  
                    result.append((key,word))
                    found=True
                    break
            if not found:
                try:
                    word=int(word)
                    result.append(('number',word))
                except ValueError:
                    result.append(('error',word))
        return result  
