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
        test = []

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
            elif len(racommendedList) < K_3:
                REC_LIST_EMPTY += (K_3 - len(racommendedList))
                test.append(UT)

                #prova = UserTest[UT].usr_rw
                #wr1.writerow([UserTest[UT].usr_id,prova,prova1,userTestList, racommendedList])

            resTP += TP
            #wr1.writerow([UserTest[UT].usr_id,'Vicinato = ',Simil_id,'TP = '+str(TP),userTestList, racommendedList])
            URP.write(str(UserTest[UT].usr_id) + ' Vicinato = ' + str(Simil_id) + ' TP = ' +str(TP) + str(userTestList) + str(recListPrint) + '\n')
            URP.write('Vicinato esteso ' + str(Simil_id_Lista) + '\n')

        print 'TP = ' +str(resTP)
        print 'Righe con test set non ok = '+ str(TEST_SET_NON_OK)
        print 'Raccomandazioni in meno  = ' + str(REC_LIST_EMPTY)
        #print test

        wr1.writerow(['TP = ' +str(resTP) + ' Righe dataset scartate = '+ str(TEST_SET_NON_OK)+' K_1 = '+str(K_1),'K_2 = '+str(K_2),'K_3 = '+str(K_3)])

        URP.close()


    return 'TP = ' +str(resTP) + ' Righe dataset scartate = '+ str(TEST_SET_NON_OK)+' K_1 = '+str(K_1),'K_2 = '+str(K_2),'K_3 = '+str(K_3), ' REC_EMPTY =' + str(REC_LIST_EMPTY)
    #return str(TEST_SET_NON_OK),str(resTP),str(K_1),str(K_2),str(K_3)


def ____recSystemObjUxUNextNeighbour__(UserList,UserTest,SimilMatrix,PATH,K_1=1,K_2=5,K_3=3,K_4=20):
    with open (PATH+'UsagePredictionUxU2','w') as URP:
        wr1 = csv.writer(URP, dialect='excel')
        resTP = 0
        TEST_SET_NON_OK = 0
        REC_LIST_EMPTY = 0

        for UT in range(0,len(UserTest)):
            #UT = 401
            temp = []
            temp2 = []
            res = []
            res2 = []
            #Simil_id = __getK_Simil__(SimilMatrix,UserTest[UT].usr_id,K)
            Simil_id = []

            #for i in heapq.nlargest(K_1,SimilMatrix[UT]):
                #Simil_id.append(i[1])

            controllo = True
            counter = 1
            while controllo:
                res = []
                Simil_id = heapq.nlargest(K_1*counter,SimilMatrix[UT])

                if len(Simil_id) == K_4:
                    controllo = False


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

                if len(res) >= K_3:
                    controllo = False
                else:
                    counter += 1

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
            elif len(racommendedList) < K_3:
                REC_LIST_EMPTY += (K_3 - len(racommendedList))
                #prova = UserTest[UT].usr_rw
                #wr1.writerow([UserTest[UT].usr_id,prova,prova1,userTestList, racommendedList])

            resTP += TP
            #wr1.writerow([UserTest[UT].usr_id,'Vicinato = ',Simil_id,'TP = '+str(TP),userTestList, racommendedList])
            URP.write(str(UserTest[UT].usr_id) + ' Vicinato = ' + str(Simil_id) + ' TP = ' +str(TP) + ' Testset: ' + str(userTestList) + ' Raccomandati: ' +  str(recListPrint) + '\n')
            URP.write('Vicinato esteso ' + str(Simil_id_Lista) + '\n')
            URP.write('\n')

        print 'TP = ' +str(resTP)
        print 'Righe con test set non ok = '+ str(TEST_SET_NON_OK)
        print 'Raccomandazioni in meno  = ' + str(REC_LIST_EMPTY)

        wr1.writerow(['TP = ' +str(resTP) + ' Righe dataset scartate = '+ str(TEST_SET_NON_OK)+' K_1 = '+str(K_1),'K_2 = '+str(K_2),'K_3 = '+str(K_3)])

        URP.close()


    return 'TP = ' +str(resTP) + ' Righe dataset scartate = '+ str(TEST_SET_NON_OK)+' K_1 = '+str(K_1),'K_2 = '+str(K_2),'K_3 = '+str(K_3), ' REC_EMPTY =' + str(REC_LIST_EMPTY)
    #return str(TEST_SET_NON_OK),str(resTP),str(K_1),str(K_2),str(K_3)


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
