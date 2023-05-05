from domain.carte import Carte


class ServiceCarti:
    def __init__(self,validator_carte,Repo_carti):
        self.__repo=Repo_carti
        self.__validator=validator_carte
    def undo_service(self):
        operatii=self.__repo.get_all_undo()
        operatie=operatii.pop()
        operatie=operatie.split(',')
        if operatie[0]=="adauga_carte":
            self.adauga_carte(int(operatie[1]),operatie[2],operatie[3],int(operatie[4]))



    def adauga_carte(self,id_carte,titlu_carte,autor_carte,an_aparitie):
        carte=Carte(id_carte,titlu_carte,autor_carte,an_aparitie)
        self.__validator.valideaza_carte(carte)
        self.__repo.adauga_carte(carte)
    def get_all_service(self):
        return self.__repo.get_all()
    def sterge_carti_service(self,cifra):
       self.__repo.sterge_carti(cifra)

    def filtrare(self,filtru_nume="",filtru_an=-1):
        toti=self.__repo.get_all()
        lista=[]
        if filtru_an==-1 and filtru_nume=="":
            return toti
        if filtru_an!=-1 and filtru_nume=="":
            lita=[x for x in toti if x.get_an_aparitie()<filtru_an]
        if filtru_nume!="" and filtru_an==-1:
            lista=[x for x in toti if x.get_titlu_carte() in filtru_nume]
        if filtru_an!=-1 and filtru_nume!="":
            lista = [x for x in toti if x.get_titlu_carte() in filtru_nume and x.get_an_aparitie()<filtru_an ]
        return lista


