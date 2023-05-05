class Carte:
    def __init__(self,id_carte,titlu_carte,autor_carte,an_aparitie):
        self.__id_carte=id_carte
        self.__titlu_carte=titlu_carte
        self.__autor_carte=autor_carte
        self.__an_aparitie=an_aparitie
        self.__sters=False
    def get_sters(self):
        return self.__sters
    def set_sters(self,val):
        self.__sters=val
    def get_id_carte(self):
        return self.__id_carte
    def get_titlu_carte(self):
        return self.__titlu_carte
    def get_autor_carte(self):
        return self.__autor_carte
    def get_an_aparitie(self):
        return self.__an_aparitie
    def __str__(self):
        return f"{self.__id_carte},{self.__titlu_carte},{self.__autor_carte},{self.__an_aparitie}"
    def __eq__(self, other):
        return self.__id_carte==other.get_id_carte()
