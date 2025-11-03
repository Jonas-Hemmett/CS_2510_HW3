import gen_text_3 as gen

corpusList = gen.get_tidied_corpus("alice.txt").split()

distinctCount = {1:{}, 2:{}, 3:{}}
# E.G. distinctCount = {1: {(a): 1, (b): 1}, 2:{(a, b): 1}, 3: {}}

for c in range(len(corpusList)):
    if (corpusList[c]) not in distinctCount[1]:
        distinctCount[1][(corpusList[c])] = 1
    else:
        distinctCount[1][(corpusList[c])] += 1
    
    if c + 1 < len(corpusList):
        if (corpusList[c], corpusList[c + 1]) not in distinctCount[2]:
            distinctCount[2][(corpusList[c], corpusList[c + 1])] = 1
        else:
            distinctCount[2][(corpusList[c], corpusList[c + 1])] += 1

    if c + 2 < len(corpusList):
        if (corpusList[c], corpusList[c + 1], corpusList[c + 2]) not in distinctCount[3]:
                distinctCount[3][(corpusList[c], corpusList[c + 1], corpusList[c + 2])] = 1
        else:
            distinctCount[3][(corpusList[c], corpusList[c + 1], corpusList[c + 2])] += 1

print(distinctCount[3])