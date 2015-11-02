import csv
import heapq
import math
from sets import Set

__author__ = 'matteo'





def __simil_UxU_ObjFull__(UserList,Y,PATH,Written=True):
    #The Pearson correlation similarity User-User

    if Written:
        SimilMatrix = [[0 for x in range(Y)] for y in range(Y)]
        with open(PATH+'SimilMatrixUxU','r') as SM:
            counterLine = 0
            for line in csv.reader(SM, dialect="excel"):
                for i in range(0,len(SimilMatrix)):
                    SimilMatrix[counterLine][i] = line[i]
                counterLine +=1
            SM.close()

        return SimilMatrix
    else:
        with open(PATH+'SimilMatrixUxU','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            for U_i in UserList:
                row = []
                for U_j in UserList:
                    if U_i.usr_id == U_j.usr_id:
                        row.append(0.0)
                    elif U_i.usr_id < U_j.usr_id:
                        row.append(__simil_UxU_Obj__(U_i,U_j))
                    else:
                        row.append(0.0)
                wr.writerow(row)
        return (__simil_UxU_ObjFull__(UserList,Y,PATH,True))


def __simil_UxU_Obj__(User_I,User_J):
    l_i = User_I.extractItem()
    l_j = User_J.extractItem()
    common_item = list(set(l_i).intersection(l_j))
    if common_item == []:
        return 0.0
    else:
        numeratore = 0.0
        denominatore = 0
        for item in common_item:
            t_i = filter( lambda x: x[1] == item, User_I.usr_rw)
            t_j = filter( lambda x: x[1] == item, User_J.usr_rw)
            membro_i = t_i[0][0] - User_I.average()
            membro_j = t_j[0][0] - User_J.average()
            numeratore += membro_i * membro_j
            denominatore += (membro_i**2) * (membro_j**2)


        if denominatore == 0:
            # print ('Warning denominatore 0 '+ str(len(common_item)))
            # if len(common_item) > 6:
            #     print User_I.usr_id
            #     print User_J.usr_id
            return 0.0
        else:
            return (numeratore/math.sqrt(denominatore))


