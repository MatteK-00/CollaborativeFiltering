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
            sum += i[1]
        self.usr_Average = sum/self.rw_count
        return self.usr_Average

    def addListRw(self):
        self.usr_rw=list

    def extractItem(self):
        temp = []
        for i in self.usr_rw:
            temp.append(i[1])
        return temp