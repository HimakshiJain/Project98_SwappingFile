def swapFileData():
    fileName1 = input("enter file name 1")
    fileName2 = input("enter file name 2")

    readfile1 = open(fileName1, 'r')
    data_a = readfile1.read()
    readfile2 = open(fileName2, 'r')
    data_b = readfile2.read()
    #print(data_a)
    #print(data_b)

    with open(fileName1, 'w') as a:
        a.write(data_b)
    with open(fileName2, 'w') as b:
        b.write(data_a)

swapFileData()
    
    

