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


def __recSystemObjUxU__(UserList,UserTest,SimilMatrix,PATH,K_3=3):
    with open (PATH+'UsagePredictionUxU','w') as URP:
        wr1 = csv.writer(URP, dialect='excel')
        resTP = 0
        TEST_SET_NON_OK = 0
        REC_LIST_EMPTY = 0
        test = []

        for UT in range(0,len(UserTest)):
            temp = []
            temp2 = []
            res = []
            Simil_id = SimilMatrix[UT]
            Simil_id_Lista = []

            #CONFRONTO CON IL TEST SET
            confronto = UserTest[UT].extractItem()
            for i in range(0,len(Simil_id)):
                temp1 = []
                id = Simil_id[i][1]
                list = []
                for item in UserList[Simil_id[i][1]].usr_rw:
                    if item[1] in confronto and item[0] >= 4:
                        temp1.append(item)
                        list.append(item)

                Simil_id_Lista.append((id,list))
                temp += temp1
            #------------------------#


            #Calcolo della frequenza con cui si ripetono gli oggetti raccomandati dai vicini
            for j in temp:
                temp2.append(j[1])
            for l in temp2:
                res.append((temp2.count(l),l))
            res = Set(res)

            #Estrazione dei K_3 piu' frequenti
            res = heapq.nlargest(K_3,res)

            #Estrazione dei soli id degli oggetti raccomandati
            racommendedList = []
            for i in res:
                racommendedList.append(i[1])

            #Estrazione dei K_3 oggetti nel testset con votazione >= 4
            userTestList = __estraiItemTEST__(K_3,UserTest[UT].usr_rw)

            #confronto tra dati nel testset e raccomandazioni
            TP = 0
            for rl in userTestList:
                if rl[0] in racommendedList:
                    TP +=1

            #dati per l'output "verboso" circa le rw utilizzate per ogni utente nel vicinato
            recListPrint = []
            for rl in racommendedList:
                for i in UserTest[UT].usr_rw:
                    if rl == i[1]:
                        recListPrint.append((rl,i[0]))

            #dati necessari al calcolo della Precision, vengono calcolati gli oggetti esclusi perche' contenenti valutazioni troppo
            #basse nel testset e viene segnato il numero di raccomandazioni che (a causa di un vicinato troppo scarno) non sono potute
            #essere fatte
            if userTestList[0] == 'voti troppo pochi o bassi':
                TEST_SET_NON_OK+=1
            elif len(racommendedList) < K_3:
                REC_LIST_EMPTY += (K_3 - len(racommendedList))
                test.append(UT)

            resTP += TP

            URP.write(str(UserTest[UT].usr_id) + ' Vicinato = ' + str(Simil_id) + ' TP = ' +str(TP) + str(userTestList) + str(recListPrint) + '\n')
            URP.write('Vicinato esteso ' + str(Simil_id_Lista) + '\n')
            URP.write('\n')

        precision = (resTP*100)/float(((len(UserList)-TEST_SET_NON_OK)*K_3)-REC_LIST_EMPTY)

        print 'TP = ' +str(resTP)
        print 'Righe con test set non ok = '+ str(TEST_SET_NON_OK)
        print 'Raccomandazioni in meno  = ' + str(REC_LIST_EMPTY)
        print 'Raccomandazioni in meno  = ' + str(precision)

        wr1.writerow(['TP = ' +str(resTP) + ' precision = '+ str(precision)+ 'K_3 = '+str(K_3)])

        URP.close()


    return'TP = ' +str(resTP) + ' Precision = '+ str(precision) + ' Righe dataset scartate = '+ str(TEST_SET_NON_OK)+ ' K_3 = '+str(K_3), ' REC_EMPTY =' + str(REC_LIST_EMPTY)
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

                if len(Simil_id) == len(SimilMatrix[UT]):
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


        precision = resTP*100/float((len(UserList)-TEST_SET_NON_OK)*K_3-REC_LIST_EMPTY)
        print precision
        wr1.writerow(['TP = ' +str(resTP)  +' Righe dataset scartate = '+ str(TEST_SET_NON_OK)+' K_1 = '+str(K_1),'K_2 = '+str(K_2),'K_3 = '+str(K_3)])

        URP.close()


    return 'TP = ' +str(resTP) + ' Precision = '+ str(precision) + ' Righe dataset scartate = '+ str(TEST_SET_NON_OK)+' K_1 = '+str(K_1),'K_2 = '+str(K_2),'K_3 = '+str(K_3), ' REC_EMPTY =' + str(REC_LIST_EMPTY)
    #return str(TEST_SET_NON_OK),str(resTP),str(K_1),str(K_2),str(K_3)


def __estraiItemTEST__(K_3,Lista_RW):
    #Estrae almeno K_3 item dalla lista delle rw se esistono almeno K_3 oggetti con voto >= 4,
    #Se sono men0o restituisce una lista con un solo campo contenente un messaggio di warning
    #Se ci sono piu' di K_3 elementi con votazione uguale a 5 o 4 vengono selezionati tutte le recensioni con quella votazione
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
