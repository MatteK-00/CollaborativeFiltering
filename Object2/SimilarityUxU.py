import ast
import csv
import heapq
import math
from sets import Set
from SimilarityIxI import sampleStandardDeviation

__author__ = 'matteo'





def __simil_UxU_ObjFull__(UserList,K,Y,PATH,Written=True):
    #The Pearson correlation similarity User-User

    if Written:
        SimilMatrix = []
        with open(PATH+'SimilMatrixUxU','r') as SM:
            for line in csv.reader(SM, dialect="excel"):
                SimilMatrix.append(ast.literal_eval(line[0]))
            SM.close()

        return SimilMatrix
    else:
        with open(PATH+'SimilMatrixUxU','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            for U_i in UserList:
                row = []
                for U_j in UserList:
                    if U_i.usr_id == U_j.usr_id:
                        row.append((0.0, U_i.usr_id))
                    else:
                        #row.append((__simil_UxU_ObjProva__(U_i,U_j),U_j.usr_id))
                        row.append((pearson(U_i,U_j),U_j.usr_id))

                    #row=heapq.nlargest(K,row)

                row.sort(None,None,True)
                counter = 0
                for i in range(0,len(row)):
                    if row[i][0] <= K:
                        counter = i
                        break

                wr.writerow([row[0:counter]])
                #wr.writerow([row])
        return (__simil_UxU_ObjFull__(UserList,K,Y,PATH,True))


def __simil_UxU_ObjFull2__(UserList,K,Y,PATH,Written=True):
    #The Pearson correlation similarity User-User

    if Written:
        SimilMatrix = []
        with open(PATH+'SimilMatrixUxU2','r') as SM:
            for line in csv.reader(SM, dialect="excel"):
                SimilMatrix.append(ast.literal_eval(line[0]))
            SM.close()

        return SimilMatrix
    else:
        with open(PATH+'SimilMatrixUxU2','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            for U_i in UserList:
                row = []
                for U_j in UserList:
                    if U_i.usr_id == U_j.usr_id:
                        row.append((0.0, U_i.usr_id))
                    else:
                        row.append((__simil_UxU_Obj__(U_i,U_j),U_j.usr_id))
                        #row.append((pearson(U_i,U_j),U_j.usr_id))

                row.sort(None,None,True)
                counter = 0
                for i in range(0,len(row)):
                    if row[i][0] <= K:
                        counter = i
                        break

                wr.writerow([row[0:counter]])
                #wr.writerow([row])

        return (__simil_UxU_ObjFull2__(UserList,K,Y,PATH,True))


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
            membro_i = t_i[0][0] - User_I.usr_Average
            membro_j = t_j[0][0] - User_J.usr_Average
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





def pearson(User_I, User_J):
    score_i = []
    score_j = []

    common_user = []#list(set(l_i).intersection(l_j))
    for i in User_I.usr_rw:
       for j in User_J.usr_rw:
            if i[1] == j[1]:
                common_user.append((i[0],j[0]))

    if common_user == []:
        return 0.0
    else:
        stdDev = sampleStandardDeviation(common_user, User_I.usr_Average,User_J.usr_Average)

        if stdDev[0] == 0 or stdDev[1] == 0:
            return 0.0
        else:
            for x in common_user:
                score_i.append((x[0] - User_I.usr_Average)/stdDev[0])
                score_j.append((x[1] - User_J.usr_Average)/stdDev[1])

        # multiplies both lists together into 1 list (hence zip) and sums the whole list
        # using zip to iterate over two lists in parallel
        valoreDaRitornare = 0.0
        try:
            valoreDaRitornare = (sum([i*j for i, j in zip(score_i, score_j)]))/(len(common_user)-1)
        except Exception:
            pass
        return valoreDaRitornare






def __simil_UxU_ObjProva__(User_I,User_J):
    #l_i = Item_I.extractUser()
    #l_j = Item_J.extractUser()
    common_user = []#list(set(l_i).intersection(l_j))
    for i in User_I.usr_rw:
       for j in User_J.usr_rw:
            if i[1] == j[1]:
                common_user.append((i[0],j[0]))

    if common_user == []:
        return 0.0
    else:
        numeratore = 0.0
        denominatore_i = 0.0
        denominatore_j = 0.0

        for user in common_user:
            #t_i = filter( lambda x: x[1] == user, Item_I.item_rw)
            #t_j = filter( lambda x: x[1] == user, Item_J.item_rw)
            membro_i = user[0] - User_I.usr_Average
            membro_j = user[1] - User_J.usr_Average
            numeratore += membro_i * membro_j
            denominatore_i += (membro_i**2)
            denominatore_j += (membro_j**2)

        if denominatore_i == 0.0 or denominatore_j == 0.0:
            return 0.0
        else:
            return (numeratore/math.sqrt(denominatore_i*denominatore_j))
