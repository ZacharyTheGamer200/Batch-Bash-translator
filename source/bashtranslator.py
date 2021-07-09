file=input("what batch file do you want to convert. Please put in same directory as where you're running this app from:")
file = open(file,"r")
content = file.readlines()
file.close()



def findcommandlinenumber(command):
    #make a list to store all instances of the command found
    lineswithcommand = []
    for num, line in enumerate(content, 1):
        if command in line:
            lineswithcommand.append(num)
            #return num
    return lineswithcommand
    #return(content[1])

def main():
    testhelloworld = findcommandlinenumber("echo")
    print(testhelloworld)
    #get list length
    max = len(testhelloworld)
    i = 0
    while (i < max - 1):
        print(content[testhelloworld[i]])
        i+=1

    #convert the echo strings to bash and write to a file

    #iterate through the strings from testhelloworld and use split method to get words after echo command
    finalresult = []
    i = 0
    while (i < max - 1):
        currentlineevaluated = (content[testhelloworld[i]])
        if "echo" in currentlineevaluated:
            x = currentlineevaluated.split("echo")
            finalresult.append(x[1])
        i+=1
    print(finalresult)
    #get length of finalresult and add echo before all the lines
    i = 0
    finallength = len(finalresult)
    while (i < finallength-1):
        for i in range(finallength):
            getstufftoadd = finalresult[i].strip()
            finalresult[i] = "echo '"  + getstufftoadd + "'"
            i+=1

    #write all the lines to a new file
    f = open("converted.bash","w")
    i=0
    while (i < finallength-1):
        for i in range(finallength):
            f.write(finalresult[i] + "\n")
            i+=1
    f.close()
    print(finalresult)






main()