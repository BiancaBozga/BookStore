from domain.carte import Carte
from infrastructura.RepoCarte import RepoCarte


class FileRepoCarte(RepoCarte):
    def __init__(self,cale_catre_fisier):
        RepoCarte.__init__(self)
        self.__cale_catre_fisier=cale_catre_fisier
    def __read_all_from_file(self):
        with open(self.__cale_catre_fisier,"r") as f:
            lines=f.readlines()
            self._carti.clear()
            for line in lines:
                line=line.strip()
                if line!="":
                    parts=line.split(",")
                    id_carte=int(parts[0])
                    titlu_carte=parts[1]
                    autor_carte=parts[2]
                    an_aparitie=int(parts[3])
                    carte=Carte(id_carte,titlu_carte,autor_carte,an_aparitie)
                    self._carti[id_carte]=carte
    def __write_all_to_file(self):
        with open(self.__cale_catre_fisier,"w") as f:
            for carte in self._carti.values():
                if carte.get_sters()!=True:
                    f.write(str(carte)+'\n')
    def __append_to_file(self,carte):
        with open(self.__cale_catre_fisier,"a") as f:
            f.write(str(carte)+"\n")
    def adauga_carte(self,carte):
        self.__read_all_from_file()
        RepoCarte.adauga_carte(self,carte)
        self.__write_all_to_file()
    def get_all(self):
        self.__read_all_from_file()
        return RepoCarte.get_all(self)
    def sterge_carti(self,cifra):
        self.__read_all_from_file()
        RepoCarte.sterge_carti(self,cifra)
        self.__write_all_to_file()
    def size(self):
        self.__read_all_from_file()
        return RepoCarte.size(self)
    def get_all_undo(self):
        self.__read_all_from_file()
        return RepoCarte.get_all_undo(self)