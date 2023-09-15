

def readtxt():
    with open("D:\Mine\python\SeleniumProjects\DemoFiles\demotxt.txt", 'r') as fd:
        #data = fd.read()
        #print(data)

        lines = fd.readlines()
        for line in lines:
            print("*", line)




if __name__ == "__main__":
    readtxt()