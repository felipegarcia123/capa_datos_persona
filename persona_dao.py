from Persona import Persona
from conexion import Conexion
from logger_base import log


class PersonaDao:
    _SELECCIONAR = 'SELECT * FROM person ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO person(nombre, apellido,email,edad) VALUES(%s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE person SET nombre =%s, apellido =%s, email =%s,edad = %s  WHERE id_persona =%s '
    _ELIMINAR = 'DELETE FROM person WHERE id_persona = %s'

    """
         This is a class method that selects all records from a database table and returns a list of Person
         objects.

         :param cls: The cls parameter is a reference to the class itself. It is used to access class-level
         attributes and methods. In this case, it is used to access the _SELECCIONAR attribute, which is a
         SQL query string for selecting records from a database table
         :return: The method `seleccionar` returns a list of `Persona` objects.
    """
    @classmethod
    def seleccionar(cls):
        with  Conexion.obtenerCursor() as cur:
            cur.execute(cls._SELECCIONAR)
            registros = cur.fetchall()
            personas = []
            for reg in registros:
                pers = Persona(reg[0],reg[1],reg[2],reg[3])
                personas.append(pers)
        return personas

    """
         This is a Python class method that updates a user's information in a database using input from the
         user.

         :param cls: The class object that the method belongs to
    """
    @classmethod
    def actulizar(cls):
        with Conexion.obtenerConexion() as con:
            with con.cursor() as cur:
                lis = []
                print('ACTIALIZAR REGISTRO'.center(30,'-'))
                id = int(input('ID del user a Actualizar:  '))
                n = input('Nombre nuevo: ')
                a = input('Apellido nuevo: ')
                em = input('Email nuevo:')
                edad = int(input('Edad nuevo:'))
                lis.extend([n, a, em, edad, id])
                res = tuple(lis)
                cur.execute(cls._ACTUALIZAR, res)
                updated_record = cur.rowcount
                log.debug(f'Updated records: {updated_record} - {res}' )

    """
         This is a Python class method that inserts a new record into a database table using user input and
         logs the result.

         :param cls: The cls parameter is a reference to the class itself. It is used to access class-level
         attributes and methods. In this case, it is used to access the _INSERTAR attribute, which is a SQL
         query string for inserting a new record into a database table
    """

    @classmethod
    def insertar(cls):
        with Conexion.obtenerConexion() as con:
            with con.cursor() as cur:
                lis = []
                print('INSERTAR REGISTRO'.center(30, '-'))
                n = input('Nombre : ')
                a = input('Apellido : ')
                em = input('Email :')
                edad = int(input('Edad :'))
                lis.extend([n, a, em, edad])
                res = tuple(lis)
                cur.execute(cls._INSERTAR,res)
                insert_record = cur.rowcount
                log.debug(f'Insert records: {insert_record} - {res}')


    """
         This is a class method in Python that deletes a record of a person from a database and logs the
         action.

         :param cls: The class itself, which is used to access class-level variables and methods
         :param persona: The parameter "persona" is an instance of a class representing a person, which has
         an attribute "_id" and a method "getNombre()" that returns the person's name. The method "eliminar"
         is a class method that takes a "persona" object as input and deletes the corresponding record from
    """

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion() as con:
            with con.cursor()as cur:
                valor = (persona._id,)
                cur.execute(cls._ELIMINAR,valor)
                deleted_record = cur.rowcount
                log.debug(f'Deleted records: {deleted_record} - {persona.getNombre()}')

# Main to execute and prove the respect methods
if __name__ == '__main__':

    #PersonaDao.actulizar()
    #PersonaDao.insertar()
    p1 =Persona(id_persona = 4)
    e = PersonaDao.eliminar(p1)
    log.info(f'Personsa eliminadas {e}')
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)
