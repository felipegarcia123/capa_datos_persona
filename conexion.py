from logger_base import log
import psycopg2
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'ADMIN'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _con = None
    _cur = None

    @classmethod
    def obtenerConexion(cls):
        if cls._con is None:
            try:
                cls._con = psycopg2.connect(host = cls._HOST,
                                            user = cls._USERNAME,
                                            password = cls._PASSWORD,
                                            port = cls._DB_PORT,
                                            database = cls._DATABASE
                                            )
                log.info(f'Conexion exitosa {cls._con}')
                return cls._con
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener la conexion {e}')
                sys.exit()
        else:
            return cls._con


    @classmethod
    def obtenerCursor(cls):
        if cls._cur is None:
            try:
                cls._cur = cls.obtenerConexion().cursor()
                log.info(f'Se ejecuto correctamente el cursor {cls._cur}')
                return cls._cur
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor {e}')
                sys.exit()
        else:
            return cls._cur

if __name__ == '__main__':
  Conexion.obtenerConexion()
  Conexion.obtenerCursor()
                