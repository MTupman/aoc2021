def prt1(inputArray):     
    
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

def prt2(inputArray, sensorType):
    
    arrHeight = len(inputArray)
    arrWidth = len(inputArray[0])

    #for each col in array
    for i in range(0,arrWidth):

        count0 = 0
        count1 = 0
        arrHeight = len(inputArray)
        if arrHeight == 1:
            break

        #for each row of column count 1s & 0s
        for j in range(0,arrHeight):

            if inputArray[j][i] == "0":
                count0 += 1
            else:
                count1 += 1
        
        #set if 0 or 1 rows to be deleted depending on oxy/co2 & count1/count0
        if sensorType == "oxy":
            if count1 >= count0:
                deleteChr = "0"
            else:
                deleteChr = "1"
        else:
            if count0 <= count1:
                deleteChr = "1"
            else:
                deleteChr = "0"
        
        currArrHeight = 0
        while currArrHeight < arrHeight:                        
            #delete row of array & move current index up 1
            if inputArray[currArrHeight][i] == deleteChr:   
                del inputArray[currArrHeight]
                currArrHeight -= 1
                arrHeight = len(inputArray)
            currArrHeight += 1

    return inputArray[0]
    
def prt2Driver(inputArray):

    inputArray2 = inputArray.copy()
    
    answerBinary = prt2(inputArray, "oxy")
    oxygenBin = ''.join(answerBinary)
    oxygen = int(oxygenBin,2)

    answerBinary = prt2(inputArray2, "co2")
    co2Bin = ''.join(answerBinary)
    co2 = int(co2Bin,2)
    
    print(oxygenBin)
    print("Oxygen --> " + str(oxygen))
    print(co2Bin)
    print("CO2 Scrubber --> " + str(co2))
    print("Life Support Rating --> " + str(oxygen * co2))

def createArray(inputLines):
    #creates array of each character - .strip removed /n char - list() splits each character into list
    inputArray = []
    for line in inputLines:
        inputArray.append(list(line.strip())) 
    return inputArray

def inputTest(puzzlePart):
    f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day03\\input_test.txt","r")
    inputLines = f.readlines()
    inputArray = createArray(inputLines)
    if puzzlePart == 1 :
        prt1(inputArray)
    elif puzzlePart == 2:
        prt2Driver(inputArray)

def inputMain(puzzlePart):    
    f = open("C:\\Users\\mtupm\\Documents\\VSCode\\Python_Sandbox\\AoC_2021\\Day03\\input.txt","r")
    inputLines = f.readlines()
    inputArray = createArray(inputLines)
    if puzzlePart == 1 :
        prt1(inputArray)
    elif puzzlePart == 2:
        prt2Driver(inputArray)

inputMain(2)