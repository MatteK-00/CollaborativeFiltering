import csv
import math

__author__ = 'matteo'


def __simil_IxI_Obj__(Item_I,Item_J):
    l_i = Item_I.extractUser()
    l_j = Item_J.extractUser()
    common_user = list(set(l_i).intersection(l_j))
    if common_user == []:
        return 0.0
    else:
        numeratore = 0.0
        denominatore_i = 0
        denominatore_J = 0
        for user in common_user:
            t_i = filter( lambda x: x[1] == user, Item_I.item_rw)
            t_j = filter( lambda x: x[1] == user, Item_J.item_rw)
            membro_i = t_i[0][0] - Item_I.item_Average
            membro_j = t_j[0][0] - Item_J.item_Average
            numeratore += membro_i * membro_j
            denominatore_i += (membro_i**2)
            denominatore_J += (membro_j**2)

        denominatore = denominatore_i * denominatore_J

        if denominatore == 0:
            # print ('Warning denominatore 0 '+ str(len(common_item)))
            # if len(common_item) > 6:
            #     print User_I.usr_id
            #     print User_J.usr_id
            return 0.0
        else:
            return (numeratore/math.sqrt(denominatore))


def __simil_IxI_ObjFull__(ItemList,X,PATH,Written=True):
    #The Pearson correlation similarity User-User

    if Written:
        SimilMatrix = [[0 for x in range(X)] for y in range(X)]
        with open(PATH+'SimilMatrixIxI','r') as SM:
            counterLine = 0
            for line in csv.reader(SM, dialect="excel"):
                for i in range(0,len(SimilMatrix)):
                    SimilMatrix[counterLine][i] = line[i]
                counterLine +=1
            SM.close()

        return SimilMatrix
    else:
        with open(PATH+'SimilMatrixIxI','w') as SM:
            wr = csv.writer(SM, dialect='excel')
            for I_i in ItemList:
                row = []
                for I_j in ItemList:
                    if I_i.item_id == I_j.item_id:
                        row.append(0.0)
                    elif I_i.item_id < I_j.item_id:
                        row.append(__simil_IxI_Obj__(I_i,I_j))
                    else:
                        row.append(0.0)
                wr.writerow(row)
        return (__simil_IxI_ObjFull__(ItemList,X,PATH,True))
