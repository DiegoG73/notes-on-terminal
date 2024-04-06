import datetime 
import hashlib
import users.connection as connection

connect = connection.connect()
database = connect[0]
cursor = connect[1]

class User:
    # * Creando el método contructor
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
    
    def register(self):
        dates = datetime.datetime.now()
        
        #^ Guardar las contraseñas tal cual no es muy seguro, por lo que, es importante hacer un hash que las cifre
        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf8'))
        
        #^ El "%S" sirve para sustituir esos porcentajes por algún valor que deseemos
        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.surname, self.email, encryption.hexdigest(), dates)
        
        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result
    
    def identified(self):
        
        #* Creando una consulta para comprobar que el usuario con email y contraseña exista
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        
        #* Cifrar contraseña
        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf8'))
        
        #* Datos para la consulta:
        user = (self.email, encryption.hexdigest())
        
        #* Ejecutar la consulta en si
        cursor.execute(sql, user)
        result = cursor.fetchone()
        
        return result