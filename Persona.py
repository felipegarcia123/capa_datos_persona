from logger_base import log

class Persona:
    def __init__(self, id_persona = None, nombre = None, apellido = None, email = None, edad = None):
        self._id = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._edad = edad
    def __str__(self):
        return f'''
            ID {self._id} - Nombre : {self._nombre} - Apellido {self._apellido}
            Email: {self._email} - Edad: {self._edad}
            
        '''
    def getId(self):
        return  self._id
    def setId(self,id):
        self._id = id
    def getNombre(self):
        return  self._nombre
    def getApellido(self):
        return self._apellido
    def getEmail(self):
        return self._email
    def setEmail(self,email):
        self._email = email
    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
        self._edad = edad

# p = Persona(1,'JUAN','Garcia','juan@hot',21)
# log.info(p)
# p2 = Persona(nombre='Maria',apellido='Vega',email= 'mar@gm', edad=22)
# log.info(p2)
#
# p3 = Persona(3,'luis','peña','lpe@gm',20)
# log.info(p3)
