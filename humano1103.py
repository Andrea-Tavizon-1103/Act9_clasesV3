print("Act 9 clase humano")
print("Andrea Tavizon Mat:22308051281103")
#zona de class
class humano1103:
    #zona de atributos dentro de la clase
    edad=0
    genero=""
    estatura=0
    colordepelo=""

    #zona de funciones dentro de la clase
    def correr1103(self,n):
        print(f"{n} esta corriendo")

    def caminar1103(self,n):
        print(f"{n} esta caminando en el parque")

    def hablar1103(self,n):
        print(f"{n} esta hablando con su mamá")

    def escuchar1103(slelf,n):
        print(f"{n} esta escuchando musica")

    #zona de creacion de objetos
andrea=humano1103()
emo=humano1103()
#zona de usando objetos    
print("resultados para andrea")
andrea.edad=16
andrea.genero="femenino"
andrea.estatura=1.55
andrea.colordepelo="cafe"
print(f"Edad: {andrea.edad}")
print(f"Edad: {andrea.genero}")
print(f"Edad: {andrea.estatura}")
print(f"Edad: {andrea.colordepelo}")
andrea.correr1103("andrea")
andrea.caminar1103("andrea")
andrea.hablar1103("andrea")
andrea.escuchar1103("andrea")

#-------------------------------------------

print("resultados para emo")
emo.edad=18
emo.genero="masculino"
emo.estatura=1.69
emo.colordepelo="negro"
print(f"Edad: {emo.edad}")
print(f"Edad: {emo.genero}")
print(f"Edad: {emo.estatura}")
print(f"Edad: {emo.colordepelo}")
emo.correr1103("emo")
andrea.caminar1103("emo")
andrea.hablar1103("emo")
andrea.escuchar1103("emo")