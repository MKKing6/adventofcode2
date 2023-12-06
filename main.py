input = open("input.txt").readlines()
sum = 0

red = 12
green = 13
blue = 14

#part 1
# for i, game in enumerate(input):
#   possible = True
#   sets = game.split(":")[1].split(";")
#   for set in sets:
#     colors = set.split(',')
#     for color in colors:
#       color = color.strip()
#       numColor = color.split(" ")
#       if numColor[1][0] == "r" and int(numColor[0]) > red:
#         possible = False
#       if numColor[1][0] == "g" and int(numColor[0]) > green:
#         possible = False
#       if numColor[1][0] == "b" and int(numColor[0]) > blue:
#         possible = False
#   if possible:
#     sum += i + 1
# print(sum)

#part 2
for game in input:
  redSet = []
  greenSet = []
  blueSet = []
  sets = game.split(":")[1].split(";")
  for set in sets:
    colors = set.split(',')
    for color in colors:
      color = color.strip()
      numColor = color.split(" ")
      if numColor[1][0] == "r":
        redSet.append(int(numColor[0]))
      if numColor[1][0] == "g":
        greenSet.append(int(numColor[0]))
      if numColor[1][0] == "b":
        blueSet.append(int(numColor[0]))
  redSet.sort()
  greenSet.sort()
  blueSet.sort()
  sum += redSet[-1] * greenSet[-1] * blueSet[-1]
print(sum)