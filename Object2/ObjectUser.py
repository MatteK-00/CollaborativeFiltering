import csv
import copy
import ast
from random import randint, shuffle

__author__ = 'matteo'

class Usr:

    def __init__(self,usr_id,rw_count=0):
        self.usr_id = usr_id
        self.rw_count = rw_count
        self.usr_rw = []
        self.usr_Average = 0.0
        self.usr_N = []



    def addItemRw(self,item_rw,item_id,item_timesstamp):
        self.usr_rw.append((int(item_rw),int(item_id),int(item_timesstamp)))
        self.rw_count += 1


    def average(self):
        sum = 0.0;
        for i in self.usr_rw:
            sum += i[0]
        self.usr_Average = sum/self.rw_count
        return self.usr_Average

    def addListRw(self):
        self.usr_rw=list

    def extractItem(self):
        temp = []
        for i in self.usr_rw:
            temp.append(i[1])
        return temp



def __getMatrixCF__(PATH):
    #Restituisce la lista di oggetti di tipo Usr contenuti nel data training
    User = []
    with open(PATH+'dataTraining', 'r') as read1:
        for line in csv.reader(read1, dialect="excel"):
            temp = Usr(int(line[0]),int(line[1]))
            temp.usr_rw = ast.literal_eval(line[2])
            User.append(temp)
    read1.close()

    for j in User:
        j.average()

    return User

def __getMatrixCF_TESTSET__(PATH):
    #Restituisce la lista di oggetti di tipo Usr contenuti nel dataset
    User = []
    with open(PATH+'dataTest', 'r') as read1:
        for line in csv.reader(read1, dialect="excel"):
            temp = Usr(int(line[0]),int(line[1]))
            temp.usr_rw = ast.literal_eval(line[2])
            User.append(temp)
    read1.close()
    return User


def __WriteMatrixCF__(Prw,path,PATH,X,Y,listaEsclusi=[]):
    #Scrive i due file contenenti dataset e datatraing sulla base della percentuale Prw di dataset desiderata
    User = [Usr(i) for i in range(Y)]
    UserT = []
    lineCount = 0

    with open(path+'u.data', 'r') as read1:
        for line in csv.reader(read1, dialect="excel-tab"):
            if (int(line[1])-1) not in listaEsclusi:
                User[(int(line[0])-1)].addItemRw(line[2],int(line[1])-1,line[3])
                lineCount += 1
    read1.close()

    for U in User:
        Nrw = int(Prw*U.rw_count/100)

        l = []
        shuffle(U.usr_rw)
        for i in range(0,Nrw):
            l.append(U.usr_rw.pop())

        U.rw_count -= Nrw
        temp = Usr(U.usr_id,Nrw)
        temp.usr_rw = l
        UserT.append(temp)

    with open(PATH+'dataTraining','w') as file1:
        wr1 = csv.writer(file1, dialect='excel')
        for U in User:
            wr1.writerow([U.usr_id,U.rw_count,U.usr_rw])

        file1.close()


    with open(PATH+'dataTest','w') as file2:
        wr2 = csv.writer(file2, dialect='excel')
        for T in UserT:
            wr2.writerow([T.usr_id,T.rw_count,T.usr_rw])

        file2.close()









    # target = lineCount/test
    # counter = 0
    #
    # while counter < target:
    #     u = randint(0,(Y-1))
    #     if User[u].usr_rw_count > Nrw:
    #         c = 0
    #         l = []
    #         shuffle(User[u].item_rw)
    #         while c > Nrw:
    #             l.append(User[u].item_rw.pop())
    #             c +=1
    #         User[u].usr_rw_count -= Nrw
    #         UserT.append(Usr(u,l))
    #         counter += Nrw

    #return (User,UserT)
