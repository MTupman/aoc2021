f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day01\\input.txt","r")
# f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day01\\input_test.txt","r")
inputLines = f.readlines()
newLines = []

for line in inputLines:
    newLines.append(line.strip())

output = 0
prevDepth = int(newLines[0]) + int(newLines[1]) + int(newLines[2])

for index,depth in enumerate(newLines):
    currDepth = int(newLines[index]) + int(newLines[index + 1]) + int(newLines[index + 2])
    if currDepth > prevDepth:
        output += 1    
    prevDepth = currDepth
    if index >= len(newLines) - 3:
        break

print(output)