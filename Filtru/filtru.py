class Filtru:
    def __init__(self,filtru_titlu="",filtru_an=-1):
        self.__filtru_titlu=filtru_titlu
        self.__filtru_an=filtru_an
    def set_filtru_an(self,filtru_nou_an):
        self.__filtru_an=filtru_nou_an
    def set_filtru_titlu(self,titlu_nou):
        self.__filtru_titlu=titlu_nou
    def get_filtru_an(self):
        return self.__filtru_an
    def get_filtru_titlu(self):
        return self.__filtru_titlu
    def __str__(self):
        return f"titlu={self.__filtru_titlu},an={self.__filtru_an}"
