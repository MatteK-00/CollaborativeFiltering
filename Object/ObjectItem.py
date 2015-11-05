import csv
import ast

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

# def __getMatrixCF_ITEMTEST__(PATH,X):
#     Item = [Itm(i) for i in range(X)]
#
#     with open(PATH+'dataTest', 'r') as read1:
#         for line in csv.reader(read1, dialect="excel"):
#             User_id = int(line[0])
#             for i in ast.literal_eval(line[2]):
#                 Item[int(i[1])].addUsrRw(i[0],User_id,i[2])
#     read1.close()
#     return Item