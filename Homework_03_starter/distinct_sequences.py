import gen_text_3 as gen
from matplotlib import pyplot as plt

corpusList = gen.get_tidied_corpus("alice.txt").split()

distinctCount = {1:{}, 2:{}, 3:{}}
# E.G. distinctCount = {1: {(a): 1, (b): 1}, 2:{(a, b): 1}, 3: {}}

# Limits n to 20
nLimit = True
for c in range(len(corpusList)):
    if (corpusList[c]) not in distinctCount[1]:
        distinctCount[1][(corpusList[c])] = 1
    else:
        if (not nLimit) or distinctCount[1][(corpusList[c])] < 20:
            distinctCount[1][(corpusList[c])] += 1
    
    if c + 1 < len(corpusList):
        if (corpusList[c], corpusList[c + 1]) not in distinctCount[2]:
            distinctCount[2][(corpusList[c], corpusList[c + 1])] = 1
        else:
            if (not nLimit) or distinctCount[2][(corpusList[c], corpusList[c + 1])] < 20:
                distinctCount[2][(corpusList[c], corpusList[c + 1])] += 1

    if c + 2 < len(corpusList):
        if (corpusList[c], corpusList[c + 1], corpusList[c + 2]) not in distinctCount[3]:
                distinctCount[3][(corpusList[c], corpusList[c + 1], corpusList[c + 2])] = 1
        else:
            if (not nLimit) or distinctCount[3][(corpusList[c], corpusList[c + 1], corpusList[c + 2])] < 20:
                distinctCount[3][(corpusList[c], corpusList[c + 1], corpusList[c + 2])] += 1

maxNum = max(distinctCount[1].values())
xs = range(1, maxNum + 1)
ys1 = []
ys2 = []
ys3 = []

for x in xs:
    count = 0
    for d in distinctCount[1]:
        if distinctCount[1][d] == x:
            count += 1
    ys1.append(count)
    
    count = 0
    for d in distinctCount[2]:
        if distinctCount[2][d] == x:
            count += 1
    ys2.append(count)

    count = 0
    for d in distinctCount[3]:
        if distinctCount[3][d] == x:
            count += 1
    ys3.append(count)

# Reversed to stop overlap
plt.bar([x + 0.25 for x in xs], ys3, width = 0.25, label = "Third-Order")
plt.bar(xs, ys2, width = 0.25, label = "Second-Order")
plt.bar([x - 0.25 for x in xs], ys1, width = 0.25, label = "First-Order")

plt.xticks(xs)

print(len(distinctCount[1]))

print(sum(ys1))
print(sum(ys2))
print(sum(ys3))
plt.legend()
plt.ylabel('#n')  # always label axes!
plt.xlabel('n')
plt.savefig('my_plot.png')  # save before show
plt.show()
