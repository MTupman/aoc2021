def prt1(inputLines):
    
    #creates array of each character - .strip removed /n char - list() splits each character into list
    inputArray = []
    for line in inputLines:
        inputArray.append(list(line.strip()))       
    
    arrHeight = len(inputArray)
    arrWidth = len(inputArray[0])
    gamma = ""
    epsilon = ""

    for i in range(0,arrWidth):

        count0 = 0
        count1 = 0

        for j in range(0,arrHeight):

            if inputArray[j][i] == "0":
                count0 += 1
            else:
                count1 += 1
        
        if count0 > count1:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"

    print(gamma)
    print(epsilon)
    gammaDen = int(gamma,2)
    epsilonDen = int(epsilon,2)
    
    print("Answer --> " + str(gammaDen * epsilonDen))


def inputTest():
    f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day03\\input_test.txt","r")
    inputLines = f.readlines()
    prt1(inputLines)

def inputMain():
    f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day03\\input.txt","r")
    inputLines = f.readlines()
    prt1(inputLines)