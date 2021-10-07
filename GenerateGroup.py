import random
import timeit


class number:
    listArray = []

    def __init__(self, listArray):
        self.listArray = listArray

    def getListArray(self):
        return self.listArray


def concat(a, b, c):
    s1 = str(a)
    s2 = str(b)
    s3 = str(c)
    s = s1 + s2 + s3
    c = int(s)

    return c


def innitialize():
    a = []
    b = []
    c = []
    newArray = []
    for i in range(0, 6):
        a.append(random.randint(1, 9))
        b.append(random.randint(1, 9))
        c.append(random.randint(1, 9))

    for i in range(0, 6):
        newArray.append(concat(a[i], b[i], c[i]))

    return newArray


def bubbleSort(array=[]):
    for i in reversed(range(len(array))):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                temp = array[j + 1]
                array[j+1] = array[j]
                array[j] = temp

    return array


def divideTo2Groups(sortedArray=[]):
    array1 = []
    array2 = []
    count = 0

    # Mencari rata rata selisih
    for i in range(1, len(sortedArray)):
        count += sortedArray[i] - sortedArray[i-1]
    # rata-rata
    mean = count/(len(sortedArray)-1)

    # element array pertama pasti berada pada grup array1(karena sudah sorted)
    array1.append(sortedArray[0])

    # membagi menjadi 2 grup berdasarkan rata2 selisih
    for i in range(1, len(sortedArray)):
        # jika grup kedua masih kosong, fokus isi grup pertama
        if array2 == []:
            if(sortedArray[i] - sortedArray[i-1] <= mean):
                array1.append(sortedArray[i])
            # jika ditemukan selisih lebih dari mean, maka masuk grup kedua
            else:
                array2.append(sortedArray[i])
        # seterusnya masuk grup kedua
        else:
            array2.append(sortedArray[i])

    global number1
    global number2
    number1 = number(array1)
    number2 = number(array2)


def divideTo3Groups(sortedArray=[]):
    array1 = []
    array2 = []
    array3 = []
    count = 0
    indeksTerakhir = 0
    indeksTerakhir2 = 0

    # Mencari rata-rata
    for i in range(1, len(sortedArray)):
        count += sortedArray[i] - sortedArray[i-1]
    #rata -rata
    mean = count/(len(sortedArray)-1)
    array1.append(sortedArray[0])
    for i in range(1, len(sortedArray)):
        if(sortedArray[i] - sortedArray[i-1] <= mean):
            array1.append(sortedArray[i])
        else:
            indeksTerakhir = i
            break

    # Mencari rata-rata

    for i in range(indeksTerakhir + 1, len(sortedArray)):
        count += sortedArray[i] - sortedArray[i-1]
    #rata -rata
    mean = count/(len(sortedArray)-indeksTerakhir)
    array2.append(sortedArray[indeksTerakhir])
    for i in range(indeksTerakhir + 1, len(sortedArray)):
        if(sortedArray[i] - sortedArray[i-1] <= mean):
            array2.append(sortedArray[i])
        elif sortedArray[i] - sortedArray[i-1] > mean:
            indeksTerakhir2 = i
            break

    if(indeksTerakhir2 != 0):
        # Mencari rata-rata

        for i in range(indeksTerakhir2 + 1, len(sortedArray)):
            count += sortedArray[i] - sortedArray[i-1]
        #rata -rata
        mean = count/(len(sortedArray)-indeksTerakhir2)
        array3.append(sortedArray[indeksTerakhir2])
        for i in range(indeksTerakhir2 + 1, len(sortedArray)):
            if(sortedArray[i] - sortedArray[i-1] <= mean):
                array3.append(sortedArray[i])
    else:
        array3 = []

    global number3
    global number4
    global number5
    number3 = number(array1)
    number4 = number(array2)
    number5 = number(array3)


newArray = innitialize()
pilihan = 0


while pilihan != 2:
    start = timeit.default_timer()
    newArray = bubbleSort(newArray)
    divideTo2Groups(newArray)
    print("Hasil Array : ", newArray)
    print("\nKelompok 1 : ", number1.getListArray())
    print("Kelompok 2 : ", number2.getListArray())

    divideTo3Groups(newArray)
    print("\nKelompok 1 : ", number3.getListArray())
    print("Kelompok 2 : ", number4.getListArray())
    print("Kelompok 3 : ", number5.getListArray())

    end = timeit.default_timer()
    diff = end - start
    print("The time of execution of above program is :", "%.9f" %
          ((end - start)*1000))

    pilihan = int(input("Menu : \n1. Input \n2. Exit\nInput:"))

    if(pilihan == 1):
        inputAngka = int(input("Masukkan Angka : "))
        newArray.append(inputAngka)
