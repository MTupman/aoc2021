f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day02\\input.txt","r")
# f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day02\\input_test.txt","r")
inputLines = f.readlines()
newLines = []

for line in inputLines:
    newLines.append(line.strip())

depth = 0
horizontal = 0

for pozChange in newLines:

    direction, magnitude = pozChange.split()
    dirCheck = direction[0:1]
    
    if dirCheck == "f":
        horizontal += int(magnitude)
    elif dirCheck == "u":
        depth -= int(magnitude)
    elif dirCheck == "d":
        depth += int(magnitude)
    else:
        print("Err1")

print("Horizontal --> " + str(horizontal))
print("Depth --> " + str(depth))

answer = horizontal * depth
print("Total --> " + str(answer))