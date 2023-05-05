from erori.ValidationError import ValidationError


class Validator_carte:
    def __init__(self):
        pass
    def valideaza_carte(self,carte):
        erori=""
        if carte.get_id_carte()<=0:
            erori+="id carte invalid!"+"\n"
        if carte.get_autor_carte()=="":
            erori+="nume autor invalid!"+"\n"
        if carte.get_titlu_carte()=="":
            erori+="titlu carte invalid!"+"\n"
        if carte.get_an_aparitie()<=0:
            erori+="an apartie invalid!"+"\n"
        if len(erori)>0:
            raise ValidationError(erori)