word=str(input("Enter the word."))
score=0
point1=["a" , "e" , "i" , "l" , "n" , "o" , "r" , "s" , "t" , "u":]
point2=["g" ,"d"]
point3=["b" , "c" , "p" , "m"]
point4=["f" , "h" , "w" , "v" , "y"]
point5=["k"]
point8=["j", "k"]
point10=["q" , "z"]
def scorecalc(word,score):
    for i in range (len(word)):
        print(word[i])
    if (word[i]) == "a" or "e" or "i" or "l" or "n" or "o" or "r" or "s" or "t" or "u":
        score=(score+1)
    if (word[i]) == "g" or "d":
        score=(score+2)
    if (word[i]) == "b" or "c" or "p" or "m":
        score=(score+3)
    if (word[i]) == "f" or "h" or "w" or "v" or "y":
        score=(score+4)
    if (word[i]) == "k":
        score=(score+5)
    if (word[i]) == "j" or "k":
        score=(score+8)
    if (word[i]) == "q" or "z":
        score=(score+10)
    
    return score


scorecalc=scorecalc(word, score)
print(scorecalc)

letters=["a", "a", "a", "a", "a", "a", "a", "a", "a", "b", "b", "c",
"c", "c", "d", "d", "d", "d", "e", "e", "e", "e", "e", "e",
"e", "e", "e", "e", "e", "e", "f", "f", "g", "g", "g", "h",
"h", "i", "i", "i", "i", "i", "i", "i", "i", "i", "j", "k",
"l", "l", "l", "l", "m", "m", "n", "n", "n", "n", "n", "n",
"o", "o", "o", "o", "o", "o", "o", "o", "p", "p", "q", "r",
"r", "r", "r", "r", "r", "s", "s", "s", "s", "t", "t", "t",
"t", "t", "t", "u", "u", "u", "u", "v", "v", "w", "w", "x",
"y", "y", "z"]