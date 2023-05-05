from erori.RepoError import RepoError


class RepoCarte:
    def __init__(self):
        self._carti={}
        self._undo=[]
    def get_all_undo(self):
        if len(self._undo)!=0:
            return self._undo
        else:
            raise RepoError("No more undo")
    def adauga_carte(self,carte):
        id_carte=carte.get_id_carte()
        if id_carte in self._carti:
            raise RepoError("Carte deja existenta in aplicatie!")
        self._carti[id_carte]=carte
        #self._undo.append(f"sterge_carte,{carte.get_id_carte()}")
    def sterge_carti(self,cifra):
        for carte in self._carti.values():
            if str(cifra) in str(carte.get_an_aparitie()):
                self._undo.append(f"adauga_carte,{carte}")
                carte.set_sters(True)

    def get_all(self):
        carti=[]
        for carte in self._carti.values():
            carti.append(carte)
        return carti
    def size(self):
        return len(self._carti)

