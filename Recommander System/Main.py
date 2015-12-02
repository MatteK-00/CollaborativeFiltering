from GestioneInput import __initData, __addNote
from ObjectItem import __getMatrixCF_ITEM__, stampaItemCount,__listaItemEliminati__, __getMatrixCF_ITEM2__
from ObjectUser import __WriteMatrixCF__, __getMatrixCF__, __getMatrixCF_TESTSET__
from RecommenderSystem import __recSystemObjUxU__, ____recSystemObjUxUNextNeighbour__
from SimilarityUxU import __simil_UxU_ObjFull__, __simil_UxU_ObjFull2__, __simil_UxU_ObjProva__, pearson
from SimilarityIxI import __simil_IxI_ObjFull__, __simil_IxI_ObjFull2__

__author__ = 'matteo'


def main(nome,nTest=None,K_0=20,K_1=10,K_2=5,K_3=3,K_4=20,dataset='ml-100k',path='Dataset/ml-100k/',X=0,Y=0):

    if dataset == 'ml-100k':
        path='Dataset/ml-100k/'
        X=1682
        Y=943
    elif dataset == 'ml-1m':
        path='Dataset/ml-1m/'
        X=3952
        Y=6040
    elif dataset == 'yelp':
        print "dataset mancante"
        #path='Dataset/yelp_dataset_academic/'
        X=13490
        Y=130873

    PATH = __initData(path,nome,dataset,K_0,nTest)

    print PATH

    ############ Costruzione dataset SENZA ITEM con MINIMO RW 5 ############
    #Seleziono tutto il dataset come data training (dataset = 0)
    __WriteMatrixCF__(0,path,PATH,X,Y)
    #Estraggo la lista degli oggetti
    Item = __getMatrixCF_ITEM__(PATH,X)
    #Estraggo la lista degli id degli oggetti con meno di 5 rw
    Itemlist = __listaItemEliminati__(Item,5)
    #Ricalcolo data-set e training-set sulla base della percentuale K_0, tutti le rw contenenti
    # gli oggetti in Itemlist saranno eliminate
    __WriteMatrixCF__(K_0,path,PATH,X,Y)

    #Istanzio le liste di utenti per i dati di training e test set
    User2 = __getMatrixCF__(PATH,Itemlist)
    UserTest2 = __getMatrixCF_TESTSET__(PATH,Itemlist)


    #########################################################################


    ############ Costruzione dataset sulla base del parametro K_0 ############

    #__WriteMatrixCF__(K_0,path,PATH,X,Y)

    User = __getMatrixCF__(PATH)
    UserTest = __getMatrixCF_TESTSET__(PATH)

    ##########################################################################

    print "----------------"
    #Calcolo/Leggo la matrice di Similarita'
    SimMatrix = __simil_UxU_ObjFull__(User,K_4,Y,PATH,Written=False)

    #Lancio il Racommander System sul dataset
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,1))
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,2))
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,3))
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,4))
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,5))

        #Calcolo/Leggo la matrice di Similarita'
    SimMatrix = __simil_UxU_ObjFull2__(User,K_4,Y,PATH,Written=False)

    #Lancio il Racommander System sul dataset
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,1))
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,2))
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,3))
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,4))
    __addNote(path,__recSystemObjUxU__(User,UserTest,SimMatrix,PATH,5))

    print "----------------"
    #Calcolo/Leggo la matrice di Similarita'
    SimMatrix = __simil_UxU_ObjFull__(User2,K_4,Y,PATH,Written=False)

    #Lancio il Racommander System sul dataset
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,1))
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,2))
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,3))
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,4))
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,5))

        #Calcolo/Leggo la matrice di Similarita'
    SimMatrix = __simil_UxU_ObjFull2__(User,K_4,Y,PATH,Written=False)

    #Lancio il Racommander System sul dataset
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,1))
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,2))
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,3))
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,4))
    __addNote(path,__recSystemObjUxU__(User2,UserTest2,SimMatrix,PATH,5))

    print "----------------"

    #Vecchio racommander a vicinato di grandezza variabile
    #__addNote(path,__recSystemObjUxUNextNeighbour__(User,UserTest,SimMatrix,PATH,K_1,K_2,K_3,20))


if __name__ == "__main__":
    #K_0 = PERCENTUALE TEST SET
    #K_1 = VICINATO NEL RECCOMMANDER
    #K_2 = NUMERO DI OGGETTI DA ESTRARRE PER OGNI UTENTE NEL VICINATO
    #K_3 = NUMERO DI RACCOMANDAZIONI FINALE
    #K_4 = DIMENSIONE RIGA MATRICE DI SIMILARITA'
    main('FullData',8,K_0=30,K_1=4,K_2=4,K_3=2,K_4=0.9 ,dataset='ml-100k')




