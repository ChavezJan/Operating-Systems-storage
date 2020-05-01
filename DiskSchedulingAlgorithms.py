'''
    Disk Scheduling Algorithms
    Is the Homework of operating systems class - Universidad Panamericana Campus Guadalajara

    @author ChavezJan
    @author AcesTerra
    @author LOG1CRS

'''


# Function that reads a file and return a list with its content casted to int.
def fileReader():
    path = "File(numbers).txt"
    file = open(path, 'r')
    rawLines = file.readlines()
    procLines = []
    for line in rawLines:
        procLines.append(int(line))

    return procLines


'''
Functions that simulate First Come First Served method to access memory cilinders.
Parameters:
    file: List of numbers
Return:
    movements: Number of movements
'''


def fcfs(files):
    file = files.copy()

    movements = 0

    start = file[0]
    end = file[1]

    for i in range(1, len(file) - 1):
        cont = abs(start - end)

        movements = movements + cont
        start = file[i]
        end = file[i + 1]

    print("FCFS did", movements, "Movements")


'''
Functions that simulate Shortest Seek Time First method to access memory cilinders.
Parameters:
    file: List of numbers
Return:
    movements: Number of movements
'''


def sstf(files):
    file = files.copy()
    variable = 0
    movements = 0
    cont = 10000000

    start = file[variable]

    for i in range(len(file) - 1):
        for x in range(1, len(file)):
            if start != file[x]:
                distance = abs(start - file[x])

                if distance < cont:
                    cont = distance
                    variable = x
        movements += cont
        cont = 1000000
        file.remove(start)
        if len(file) != 1:
            start = file[variable - 1]
    print("SSTF did", movements, "Movements")


'''
Functions that simulate SCAN method to access memory cilinders.
Parameters:
    file: List of numbers
Return:
    mov: Number of movements
'''


def scan(line):
    lines = line.copy()
    pos = lines[0]
    movements = 0
    end = 4999
    start = min(lines)
    movements += abs(pos - end)
    pos = end
    movements += abs(pos - start)

    print("SCAN did", movements, "movements")


'''
Functions that simulate SCAN method to access memory cilinders.
Parameters:
    file: List of numbers
Return:
    mov: Number of movements
'''


def c_scan(line):
    lines = line.copy()
    pos = lines[0]
    movements = 0
    end = 4999
    maxmin = 0
    list = sorted(lines)
    for i in range(len(list)):
        if list[i] <= pos & lines[i] >= maxmin:
            maxmin = list[i + 2]
    # The loop will reads all memory read requests greater than the initial position
    for i in range(pos, end):
        if i in lines:
            movements += abs(pos - i)
            pos = i

    movements += abs(end)

    end = maxmin

    movements += abs(end)

    total_movements = movements
    print("C-SCAN did", total_movements, "Movements")


'''
Look disk scheduling simulator made with Python 3
@author LOG1CRS
@param lines
'''


def look(lines):
    # print("Look running")
    # Cretes a copy of the array so as not to affect the original arrangement, because we will use .remove function
    requests = lines.copy()
    pos = lines[0]
    movements = 0
    end = max(requests)
    start = min(requests)

    # The loop will reads all memory read requests greater than the initial position
    for i in range(pos, end):
        if i in requests:
            movements += abs(pos - i)
            pos = i
            requests.remove(i)

    # return to the beginning
    movements += abs(end - start)

    total_movements = movements
    print("LOOK did", total_movements, "Movements")


'''
C-Look disk scheduling simulator made with Python 3
@author LOG1CRS
@param lines
'''


def c_look(lines):
    # Cretes a copy of the array so as not to affect the original arrangement, because we will use .remove function
    requests = lines.copy()
    pos = lines[0]
    movements = 0
    maxmin = 0
    variable = 0
    end = max(requests)
    start = min(requests)

    # Loop to organize the numbers
    list = sorted(lines)
    for i in range(len(list)):
        if list[i] <= pos & lines[i] >= maxmin:
            maxmin = list[i + 2]

    # The loop will reads all memory read requests greater than the initial position
    for i in range(pos, end):
        if i in requests:
            movements += abs(pos - i)
            pos = i

    movements += abs(end - start)

    end = maxmin

    movements += abs(end - start)

    total_movements = movements
    print("C-LOOK did", total_movements, "Movements")


if __name__ == "__main__":
    lines = fileReader()
    fcfs(lines)
    sstf(lines)
    scan(lines)
    c_scan(lines)
    look(lines)
    c_look(lines)
