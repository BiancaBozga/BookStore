from domain.carte import Carte
from erori.RepoError import RepoError
from infrastructura.RepoCarteFile import FileRepoCarte


class Teste:
    def __init__(self):
        pass
    def ruleaza_toate_testele(self):
        self.__teste_repo()
    def __golire_fisier(self,cale_catre_fisier):
        with open(cale_catre_fisier,"w") as f:
            f.write("")
    def __teste_repo(self):
        cale_catre_fisier="testare/teste.txt"
        self.__golire_fisier(cale_catre_fisier)
        repo=FileRepoCarte(cale_catre_fisier)
        assert(repo.size()==0)
        id_carte=123
        titlu="anaaa"
        autor="anca"
        an=1098
        l=[]
        carte=Carte(id_carte,titlu,autor,an)
        repo.adauga_carte(carte)
        assert(repo.size()==1)
        try:
            repo.adauga_carte(carte)
            assert False
        except RepoError:
            assert True
        assert (repo.size() == 1)
        l.append(carte)
        assert(repo.get_all()==l)
        repo.sterge_carti(9)
        assert (repo.size() == 0)

