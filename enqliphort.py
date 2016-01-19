import sys
from random import randint as rand

#2つの文章をリバースして混ぜあわせる
#クリフォートアセンブラのように
if __name__ == '__main__':
    sources = [sys.argv[1], sys.argv[2]]

    #短い方の文章に空白を挿入して長さを合わせる
    if(len(sources[0]) < len(sources[1])):
        sources = [sources[1],sources[0]]
    while(len(sources[0]) > len(sources[1])):
        index = rand(1,len(sources[1])-1)
        temp = sources[1][:index] + " " + sources[1][index:]
        sources = [sources[0],temp]

    sources = [src[::-1] for src in sources]
    output = ""
    for (c1,c2) in zip(sources[0],sources[1]):
        output += c1+c2
    output = output.replace(' ','')
    print(output)
