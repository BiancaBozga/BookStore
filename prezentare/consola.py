from erori.RepoError import RepoError
from erori.ValidationError import ValidationError


class UI:
    def __init__(self,Service_carti,filtru):
        self.__service=Service_carti
        self.__filtru=filtru
        self.__comenzi={
            "adauga_carte":self.__ui_adauga_carte,
            "print_carti":self.__ui_print_carti,
            "sterge_carti":self.__ui_sterge_carti,
            "modifica_filtru":self.__ui_modifica_filtru,
            "undo":self.__ui_undo,
            "help":self.__ui_help
        }
    def __ui_help(self):
        if len(self.__params)!=0:
            print("nr parametrii invalid!")
            return
        for comanda in self.__comenzi:
            print(comanda)
           
    def __ui_undo(self):
        if len(self.__params)!=0:
            print("nr parametrii invalid!")
            return
        self.__service.undo_service()
    def __print_filtru(self):
        print(f"Filtrul actual este:{self.__filtru}")
        l=self.__service.filtrare(self.__filtru.get_filtru_titlu(), self.__filtru.get_filtru_an())
        for carte in l:
            print(carte)
    def __ui_modifica_filtru(self):
        if len(self.__params)!=2:
            print("numar_parametrii invalid!")
            return
        titlu_nou=self.__params[0]
        an_nou=int(self.__params[1])
        self.__filtru.set_filtru_an(an_nou)
        self.__filtru.set_filtru_titlu(titlu_nou)

    def __ui_sterge_carti(self):
        if len(self.__params)!=1:
            print("numar_parametrii invalid!")
            return
        cifra=int(self.__params[0])
        self.__service.sterge_carti_service(cifra)
        print("carti sterse cu succes!")
    def __ui_print_carti(self):
        if len(self.__params)>0:
            print("numar_parametrii invalid!")
            return
        lista=self.__service.get_all_service()
        if len(lista)<=0:
            print("nu exista carti in aplicatie!")
            return
        for carte in lista:
            print(carte)
    def __ui_adauga_carte(self):
        if len(self.__params)!=4:
            print("numar parametrii invalid!")
            return
        id_carte=int(self.__params[0])
        titlu_carte=self.__params[1]
        autor_carte=self.__params[2]
        an_aparitie=int(self.__params[3])
        self.__service.adauga_carte(id_carte,titlu_carte,autor_carte,an_aparitie)
        print("carte adaugata cu succes!")
    def run(self):
        while True:
            self.__print_filtru()
            parts=input(">>>")
            parts=parts.strip()
            if parts=="":
                continue
            if parts=="exit":
                return
            parts1=parts.split()
            comanda = parts1[0]
            self.__params = parts1[1:]
            if comanda in self.__comenzi:
                try:
                    self.__comenzi[comanda]()

                except ValueError:
                    print("UI:tip numeric invalid!")
                except ValidationError as ve:
                    print(f"ValidatinError: {ve}")
                except RepoError as re:
                    print(f"RepoError:{re}")
            else:
                print("comanda invalida!")




