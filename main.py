from Filtru.filtru import Filtru
from business.service_carti import ServiceCarti
from infrastructura.RepoCarteFile import FileRepoCarte
from prezentare.consola import UI
from testare.teste import Teste
from validator.Validator_carte import Validator_carte


def main():
    teste=Teste()
    filtru=Filtru()
    validator=Validator_carte()
    cale_catre_fisier="carti.txt"
    repo=FileRepoCarte(cale_catre_fisier)
    service=ServiceCarti(validator,repo)
    consola=UI(service,filtru)
    teste.ruleaza_toate_testele()
    consola.run()

main()