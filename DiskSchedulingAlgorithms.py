'''
    Disk Scheduling Algorithms
    Is the Homework of operating systems class - Universidad Panamericana Campus Guadalajara

    @author ChavezJan
    @author AcesTerra
    @author LOG1CRS

'''



#Function that reads a file and return a list with its content casted to int.
def FileReader():
    path = "File(numbers).txt"
    file = open(path, 'r')
    rawLines = file.readlines()
    procLines = []
    for line in rawLines:
        line = line
        procLines.append(int(line))

    return procLines

'''
Functions that simulate First Come First Served method to access memory cilinders.
Parameters:
    file: List of numbers
Return:
    movements: Number of movements
'''
def FCFS(file):
    print("FCFS ")
    print("First Come First Served")

    movements = 0

    start = file[0]
    end = file[1]

    for i in range(1,1000,1):

        cont = int(start) - int(end)

        if cont <= 0:
            cont = cont * (-1)

        movements = movements + cont
        start = file[i]
        end = file[i + 1]

    print("FCFS did", movements, "Movements!")

'''
Functions that simulate Shortest Seek Time First method to access memory cilinders.
Parameters:
    file: List of numbers
Return:
    movements: Number of movements
'''
def SSTF(file):
    print("SSTF")
    print("Shortest Seek Time First")

    variable = 0
    cont = 1000000
    movements = 0
    y = 0

    start = file[y]

    for i in range(1001):

        for x in range(1, 1000):

            distance = int(file[x]) - int(start)

            if distance <= 0:
                distance = distance * (-1)

            if distance < cont:
                variable = x
                cont = distance

        movements = movements + cont
        start = file[variable]
        file[y] = 10000000
        y = variable
        cont = 1000000

    print("SSTF did", movements, "Movements!")

def SCAN(lines):
    print("To be defined")

def C_SCAN(lines):
    print("To be defined")

if __name__ == "__main__":
    lines = FileReader()
    FCFS(lines)
    SSTF(lines)
    SCAN(lines)
    C_SCAN(lines)
