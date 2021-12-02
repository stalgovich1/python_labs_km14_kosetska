from collections import Counter
files = []
text=[]
for i in range(1880, 2020):
    files.append("yob" + str(i) + ".txt")

d1 = {
}
male = []
female = []

def countWords(lines):
        wordDict = {}
        for line in lines:
            wordList = lines.split()
            for M in wordList:
                if M in wordDict: 
                    male = line.split(',')[2]
                    male = line.split(',')[0]
                else: wordDict[M] = 1
                return wordDict
def countWords(lines):
        wordDict = {}
        for line in lines:
            wordList = lines.split()
            for F in wordList:
                if F in wordDict: 
                    female = line.split(',')[2]
                    female = line.split(',')[0]
                else: wordDict[F] = 1
                return wordDict