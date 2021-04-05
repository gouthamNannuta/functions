def swapFileData():
    file1=input("enter the file1 name : ")
    file2=input("enter the file2 name : ")
    data_a=open(file1,"r")
    data_b=open(file2,"r")
    print(data_a)
    with open(file1,'r') as a:
        data_a =a.read()
    with open(file2,'r') as b:
        data_b =b.read()
    with open(file2,'w') as a:
        a.write(data_b)


swapFileData()
    