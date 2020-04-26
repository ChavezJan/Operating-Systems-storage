def ReadFile():
    ruta = "1.txt"

    file = open(ruta, 'r')

    file = file.readlines()

    FCFS(file)
    SSTF(file)


def FCFS(file):
    print("FCFS")
    print("First Come First Served")

    movements = 0

    start = file[0]
    end = file[1]

    for i in range(1, 1000, 1):

        cont = int(start) - int(end)

        if cont <= 0:
            cont = cont * (-1)

        movements = movements + cont
        start = file[i]
        end = file[i + 1]

    print("FCFS did", movements, "Movements!")


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

    print("SSTF did", movements, "Movements")


if __name__ == "__main__":
    ReadFile()
