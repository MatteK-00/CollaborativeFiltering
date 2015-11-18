import csv
import heapq
from sets import Set
import math

__author__ = 'matteo'

def __getK_Simil__(SimilMatrix, ID, k):
    listres = []
    for i in range (0,len(SimilMatrix)):
        if (SimilMatrix[ID][i] != 0):
            temp = SimilMatrix[ID][i]
        else:
            temp = SimilMatrix[i][ID]
        listres.append((temp, i))

    listres = heapq.nlargest(k,listres)
    return listres


def __recSystemObjUxU__(UserList,UserTest,SimilMatrix,PATH,K_1=1,K_2=5,K_3=3):
    with open (PATH+'UsagePredictionUxU','w') as URP:
        wr1 = csv.writer(URP, dialect='excel')
        resTP = 0
        TEST_SET_NON_OK = 0
        REC_LIST_EMPTY = 0

        for UT in range(0,len(UserTest)):
            #UT = 18
            temp = []
            temp2 = []
            res = []
            res2 = []
            #Simil_id = __getK_Simil__(SimilMatrix,UserTest[UT].usr_id,K)
            Simil_id = []

            #for i in heapq.nlargest(K_1,SimilMatrix[UT]):
                #Simil_id.append(i[1])

            Simil_id = heapq.nlargest(K_1,SimilMatrix[UT])

            Simil_id_Lista = []

            #CONFRONTO CON IL TEST SET
            confronto = UserTest[UT].extractItem()
            for i in range(0,len(Simil_id)):
                temp1 = []
                id = Simil_id[i][1]
                list = []
                for item in UserList[Simil_id[i][1]].usr_rw:
                    if item[1] in confronto:
                        temp1.append(item)
                        list.append(item)

                Simil_id_Lista.append((id,list))
                temp += heapq.nlargest(K_2,temp1)
            #------------------------#

            for j in temp:
                temp2.append(j[1])
            for l in temp2:
                res.append((temp2.count(l),l))
            res = Set(res)

            #CONFRONTO CON IL TRAINING SET
            #confronto = UserList[UT].extractItem()
            #for boh in res:
            #    if boh[1] not in confronto:
            #        res2.append(boh)
            #----------------------------#

            res = heapq.nlargest(K_3,res)

            racommendedList = []
            for i in res:
                racommendedList.append(i[1])

            #prova1 = UserTest[UT].usr_rw
            userTestList = __estraiItemTEST__(K_3,UserTest[UT].usr_rw)

            TP = 0
            for rl in userTestList:
                if rl[0] in racommendedList:
                    TP +=1

            recListPrint = []
            for rl in racommendedList:
                for i in UserTest[UT].usr_rw:
                    if rl == i[1]:
                        recListPrint.append((rl,i[0]))


            if userTestList[0] == 'voti troppo pochi o bassi':
                TEST_SET_NON_OK+=1
            elif racommendedList == []:
                REC_LIST_EMPTY += 1
                #prova = UserTest[UT].usr_rw
                #wr1.writerow([UserTest[UT].usr_id,prova,prova1,userTestList, racommendedList])

            resTP += TP
            #wr1.writerow([UserTest[UT].usr_id,'Vicinato = ',Simil_id,'TP = '+str(TP),userTestList, racommendedList])
            URP.write(str(UserTest[UT].usr_id) + ' Vicinato = ' + str(Simil_id) + ' TP = ' +str(TP) + str(userTestList) + str(recListPrint) + '\n')
            URP.write('Vicinato esteso ' + str(Simil_id_Lista) + '\n')

        print 'TP = ' +str(resTP)
        print 'Righe dataset scartate = '+ str(TEST_SET_NON_OK)
        print 'Righe con rec list vuota = ' + str(REC_LIST_EMPTY)

        wr1.writerow(['TP = ' +str(resTP) + ' Righe dataset scartate = '+ str(TEST_SET_NON_OK)+' K_1 = '+str(K_1),'K_2 = '+str(K_2),'K_3 = '+str(K_3)])

        URP.close()


    return 'TP = ' +str(resTP) + ' Righe dataset scartate = '+ str(TEST_SET_NON_OK)+' K_1 = '+str(K_1),'K_2 = '+str(K_2),'K_3 = '+str(K_3), ' REC_EMPTY =' + str(REC_LIST_EMPTY)
    #return str(TEST_SET_NON_OK),str(resTP),str(K_1),str(K_2),str(K_3)


def __recSystemObjIxI__(K,User,UserTest,ItemList,SimilMatrix,Y,PATH):
    with open (PATH+'UsagePredictionIxI','w') as URP:
        wr1 = csv.writer(URP, dialect='excel')
        RES = []


        for UT in range(0,len(UserTest)):
            Simil_id = []
            racommendedListTemp = []
            racommendedList = []
            racommendedPart = []
            racommendedListId = []
            bestUserItem = heapq.nlargest(K,User[UT].usr_rw)

            for item in bestUserItem:
                 Simil_id.append(item[1])

            for it in Simil_id:
                racommendedListTemp += SimilMatrix[it]

            for it_id in racommendedListTemp:
                racommendedPart.append(it_id[1])

            for l in racommendedPart:
                racommendedList.append((racommendedPart.count(l),l))

            racommendedList = Set(racommendedList)

            racommendedList = heapq.nlargest(K,racommendedList)

            for boh in racommendedList:
                racommendedListId.append(boh[1])



            UserTestList = UserTest[UT].extractItem()
            TP = FN  = FP = 0

            for rl in racommendedListId:
                if rl in UserTestList:
                    TP +=1
                else:
                    FP +=1
            for ur in UserTestList:
                if ur not in racommendedListId:
                    FN += 1
            resP = [TP,FN,FP]
            RES.append(resP)
            wr1.writerow([UT,' TP = '+str(TP) +' FP = '+str(FP),UserTestList, racommendedListId])

        tp = fn = fp  = 0
        for i in RES:
            tp += i[0]
            fn += i[1]
            fp += i[2]


        print 'TP =' +str(tp)
        print 'FP ='+ str(fp)

        Precision = (float(tp))/(tp+fp)
        Recall = (float(tp))/(tp+fn)

        wr1.writerow(['Precision = ' +str(Precision) +' Recall = ' + str(Recall)])

        URP.close()


    return 'Precision = ' +str(Precision) +' Recall = ' + str(Recall)  + ' TP = ' +str(tp) + ' FP = '+ str(fp)


def __estraiItemTEST__(K_3,Lista_RW):
    counter = 0
    res = []
    Lista_RW.sort(None,None,True)
    for i in Lista_RW:
        if i[0] == 5:
            res.append((i[1],(i[0])))
            counter += 1
        elif i[0] == 4 and counter < K_3:
            res.append((i[1],(i[0])))
            counter += 1
        elif i[0] < 4 and counter < K_3:
            return ['voti troppo pochi o bassi']


    return res
