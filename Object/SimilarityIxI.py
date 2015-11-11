import ast
import csv
import heapq
import math
import time

__author__ = 'matteo'

#TODO controllare similarita IxI

def __simil_IxI_Obj__(Item_I,Item_J):
    #l_i = Item_I.extractUser()
    #l_j = Item_J.extractUser()
    common_user = []#list(set(l_i).intersection(l_j))
    for i in Item_I.item_rw:
       for j in Item_J.item_rw:
            if i[1] == j[1]:
                common_user.append((i[0],j[0]))

    if common_user == []:
        return 0.0
    else:
        numeratore = 0.0
        denominatore = 0

        for user in common_user:
            #t_i = filter( lambda x: x[1] == user, Item_I.item_rw)
            #t_j = filter( lambda x: x[1] == user, Item_J.item_rw)
            membro_i = user[0] - Item_I.item_Average
            membro_j = user[1] - Item_J.item_Average
            numeratore += membro_i * membro_j
            denominatore += (membro_i**2) * (membro_j**2)

        if denominatore == 0:
            return 0.0
        else:
            return (numeratore/math.sqrt(denominatore))

        # for user in common_user:
        #     membro_i = user[0] - Item_I.item_Average
        #     membro_j = user[1] - Item_J.item_Average
        #     numeratore += membro_i * membro_j
        #     denominatore_i += (membro_i**2)
        #     denominatore_j += (membro_j**2)
        #
        # denominatore = math.sqrt(denominatore_i)*math.sqrt(denominatore_i)
        # if denominatore == 0:
        #     # print ('Warning denominatore 0 '+ str(len(common_item)))
        #     # if len(common_item) > 6:
        #     #     print User_I.usr_id
        #     #     print User_J.usr_id
        #     return 0.0
        # else:
        #     return (numeratore/denominatore)



def __simil_IxI_ObjFull__(ItemList,K,X,PATH,Written=True):
    #The Pearson correlation similarity User-User

    if Written:
        SimilMatrix = []
        with open(PATH+'SimilMatrixIxI','r') as SM:
            for line in csv.reader(SM, dialect="excel"):
                SimilMatrix.append(ast.literal_eval(line[0]))
            SM.close()

        return SimilMatrix
    else:
        with open(PATH+'SimilMatrixIxI','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            #a = time.time()
            #print a
            for I_i in ItemList:
                row = []
                for I_j in ItemList:
                    if I_i.item_id == I_j.item_id:
                        row.append((0.0, I_i.item_id))
                    else:
                        #row.append((__simil_IxI_Obj__(I_i,I_j),I_j.item_id))
                        row.append((__pearsonIxI__(I_i,I_j),I_j.item_id))

                    row = heapq.nlargest(K,row)
                #print time.time() - a
                wr.writerow([row])
                #break
        return (__simil_IxI_ObjFull__(ItemList,K,X,PATH,True))


def __simil_IxI_ObjFull2__(ItemList,K,X,PATH,Written=True):
    #The Pearson correlation similarity User-User

    if Written:
        SimilMatrix = []
        with open(PATH+'SimilMatrixIxI','r') as SM:
            for line in csv.reader(SM, dialect="excel"):
                SimilMatrix.append(ast.literal_eval(line[0]))
            SM.close()

        return SimilMatrix
    else:
        with open(PATH+'SimilMatrixIxI','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            #a = time.time()
            #print a
            for I_i in ItemList:
                row = []
                for I_j in ItemList:
                    if I_i.item_id == I_j.item_id:
                        row.append((0.0, I_i.item_id))
                    else:
                        #row.append((__simil_IxI_Obj__(I_i,I_j),I_j.item_id))
                        row.append((__pearsonIxI__(I_i,I_j),I_j.item_id))

                    row = heapq.nlargest(K,row)
                #print time.time() - a
                wr.writerow([row])
                #break
        return (__simil_IxI_ObjFull__(ItemList,K,X,PATH,True))



# calcolo la sample standard deviation
def sampleStandardDeviation(commonRw, mean_i,mean_j):
    sum_i = 0.0
    sum_j = 0.0
    if len(commonRw)-1 == 0:
        return (0.0,0.0)
    else:
        for x in commonRw:
            sum_i += (x[0] - mean_i)**2
            sum_j += (x[1] - mean_j)**2
        # return math.sqrt(sumv/(len(x)-1))

        return (math.sqrt(sum_i/(len(commonRw)-1)),math.sqrt(sum_j/(len(commonRw)-1)))


# calcolo il PCC
def __pearsonIxI__(Item_I, Item_J):
    score_i = []
    score_j = []

    common_user = []#list(set(l_i).intersection(l_j))
    for i in Item_I.item_rw:
       for j in Item_J.item_rw:
            if i[1] == j[1]:
                common_user.append((i[0],j[0]))

    if common_user == []:
        return 0.0
    else:
        stdDev = sampleStandardDeviation(common_user,Item_I.item_Average,Item_J.item_Average)

        if stdDev[0] == 0 or stdDev[1] == 0 :
            return 0.0
        else:
            for x in common_user:
                score_i.append((x[0] - Item_I.item_Average)/stdDev[0])
                score_j.append((x[1] - Item_J.item_Average)/stdDev[1])

        # multiplies both lists together into 1 list (hence zip) and sums the whole list
        # using zip to iterate over two lists in parallel
        valoreDaRitornare = 0.0
        try:
            valoreDaRitornare = (sum([i*j for i, j in zip(score_i, score_j)]))/(len(common_user)-1)
        except Exception:
            pass
        return valoreDaRitornare



