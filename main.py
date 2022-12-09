#Adevent of Coding Day 1

# file1 = open('calorie_data.txt', 'r')
# lines = file1.readlines()
# arrayOfCalories = []
# sum = 0
# for line in lines:
#     if line == "\n":
#         arrayOfCalories.append(sum)
#         sum = 0
#     if not line == "\n":
#         sum = sum + int(line)
# topThree = 0
# for x in range(3):
#     maxCalorie = int(max(arrayOfCalories))
#     print(maxCalorie)
#     topThree = topThree + maxCalorie
#     arrayOfCalories.remove(maxCalorie)
#
# print(topThree)
# file1.close()

#Adevent of Coding Day 2

# file2 = open('rock_paper_scissors.txt', 'r')
# lines = file2.readlines()
# total_score = 0
# for line in lines:
#     game = line.split(' ')
#     oppHand = game[0]
#     myHand = game[1].split("\n")[0]
#     if myHand == "X":
#         total_score += 1
#     if myHand == "Y":
#         total_score += 2
#     if myHand == "Z":
#         total_score += 3
#     if (oppHand == "A" and myHand == "X") or (oppHand == "B" and myHand == "Y") or (oppHand == "C" and myHand == "Z"):
#         total_score += 3
#     if (oppHand == "A" and myHand == "Y") or (oppHand == "B" and myHand == "Z") or (oppHand == "C" and myHand == "X"):
#         total_score += 6
# print(total_score)
#
# total_score_2 = 0
# for line in lines:
#     game = line.split(' ')
#     oppHand = game[0]
#     result = game[1].split("\n")[0]
#     if result == "X":
#         if oppHand == "A":
#             total_score_2 += 3
#         if oppHand == "B":
#             total_score_2 += 1
#         if oppHand == "C":
#             total_score_2 += 2
#     if result == "Y":
#         total_score_2 += 3
#         if oppHand == "A":
#             total_score_2 += 1
#         if oppHand == "B":
#             total_score_2 += 2
#         if oppHand == "C":
#             total_score_2 += 3
#     if result == "Z":
#         total_score_2 += 6
#         if oppHand == "A":
#             total_score_2 += 2
#         if oppHand == "B":
#             total_score_2 += 3
#         if oppHand == "C":
#             total_score_2 += 1
# print(total_score_2)
#
# file2.close()

letterScore = {
    "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,
    "q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,
    "G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,
    "W":49,"X":50,"Y":51,"Z":52
}

def containsLetter(letter,string):
    if letter in string:
        return


file3 = open('rucksack.txt', 'r')
lines = file3.readlines()
score = 0
for line in lines:
    type(len(line)//2)
    firstHalf = line[:(len(line)//2)]
    secondHalf = line[(len(line)//2):]
    for letter in firstHalf:
        if letter in secondHalf:
            score += letterScore[letter]
            break

print(score)



file3.close()


