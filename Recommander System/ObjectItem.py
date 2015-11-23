import csv
import ast
import numpy as np
from sets import Set

__author__ = 'matteo'

class Itm:

    def __init__(self,item_id,usr_count=0):
        self.item_id = item_id
        self.rw_count = usr_count
        self.item_rw = []
        self.item_Average = 0.0
        self.item_N = []



    def addUsrRw(self,usr_rw,usr_id,item_timesstamp):
        self.item_rw.append((int(usr_rw),int(usr_id),int(item_timesstamp)))
        self.rw_count += 1


    def average(self):
        sum = 0.0
        if self.rw_count != 0:
            for i in self.item_rw:
                sum += i[0]

            self.item_Average = sum/self.rw_count

        return self.item_Average


    def addListRw(self):
        self.usr_rw=list

    def extractUser(self):
        temp = []
        for i in self.item_rw:
            temp.append(i[1])
        return temp


def __getMatrixCF_ITEM__(PATH,X):
    #Restituisce la lista di oggetti di tipo Itm contenuti nel data training

    Item = [Itm(i) for i in range(X)]

    with open(PATH+'dataTraining', 'r') as read1:
        for line in csv.reader(read1, dialect="excel"):
            User_id = int(line[0])
            for i in ast.literal_eval(line[2]):
                Item[int(i[1])].addUsrRw(i[0],User_id,i[2])
    read1.close()

    for j in Item:
        j.average()
    return Item

def __listaItemEliminati__(ItemList,N):
    list = []
    for i in ItemList:
        if (i.rw_count < N):
            list.append(i.item_id)

    return list


def __getMatrixCF_ITEM2__(PATH,X):
    Item = [Itm(i) for i in range(X)]

    with open(PATH+'dataTraining2', 'r') as read1:
        for line in csv.reader(read1, dialect="excel"):
            User_id = int(line[0])
            for i in ast.literal_eval(line[2]):
                Item[int(i[1])].addUsrRw(i[0],User_id,i[2])
    read1.close()

    for j in Item:
        j.average()
    return Item



def __listaItemEliminati__(ItemList,N):
    #restituisce la lista degli id degli oggetti con  numero di recensioni totali minore di N
    list = []
    for i in ItemList:
        if (i.rw_count < N):
            list.append(i.item_id)

    return list



def stampaItemCount(ItemList):
    res = []
    for i in ItemList:
        res.append(i.rw_count)
    res2 = []

    for i in range(0,1682):
        counter = 0
        for j in res:
            if i == j:
                counter += 1
        if counter != 0:
            res2.append((counter, i))

    stringa = ' '
    for i in res2:
        stringa += str(i)+ ' '

    print res
    a = np.array(res)
    print "Min:", np.min(a), "Max:", np.max(a)
    print "Percentile 10%", np.percentile(a, 10)
    print "Percentile 20%", np.percentile(a, 20)
    print "Percentile 30%", np.percentile(a, 30)
    print "Percentile 40%", np.percentile(a, 40)
    print "Percentile 50%", np.percentile(a, 50)
    print "Percentile 60%", np.percentile(a, 60)
    print "Percentile 70%", np.percentile(a, 70)
    print "Percentile 80%", np.percentile(a, 80)
    print "Percentile 90%", np.percentile(a, 90)
    print 'Mediana', np.median(a)
    print stringa

