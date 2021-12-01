f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day01\\input.txt","r")
# f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day01\\input_test.txt","r")
inputLines = f.readlines()
newLines = []

for line in inputLines:
    newLines.append(line.strip())

output = 0
prevDepth = newLines[0]

# for index,depth in enumerate(newLines):
#     currDepth = newLines[index]
#     if currDepth > prevDepth:
#         output += 1    
#     prevDepth = currDepth

nextSteps = newLines[1:]        #from item 1 to end
originalSteps = newLines[:-1]   #from item 0 to -1 from end
isIncrease = [n > o for n,o in zip(nextSteps, originalSteps)]
output = sum(isIncrease)

print(output)