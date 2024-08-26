# Carga horária e percentual de faltas
# programação orientada a objeto

"""
Programação Orientada a Objeto
- Flask e Django

Programação Estruturada com OO
- Flet

Programação Funcional
- Lambda

"""
class Aluno():
    def __init__(self,cargahora,faltas):
        self.cargahora = cargahora
        self.faltas = faltas

    def calcular_faltas(self):
        percent_cargahora = self.cargahora * (25/100)
        msg = '' 
        if self.faltas > percent_cargahora:
            msg = 'retido'
        else:
            msg = 'não retido'    
        return f" falta-hora permitidas : {percent_cargahora} você faltou: {self.faltas} horas, resultado: {msg} por faltas"
    
# exercicio
# considere realizar uma avaliação para aprovar ou reprovar os alunos pelo percentual de faltas
