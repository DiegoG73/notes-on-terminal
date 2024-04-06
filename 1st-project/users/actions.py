import users.user as model
import notes.actions 

class Actions:
    
    def register(self):
        print("\nOk, te registro en el sistema")
        name = input("¿Cuál es tu nombre? ")
        surname = input("¿Cuáles son tus apellidos? ")
        email = input("¿Cuál es tu email? ")
        password = str(input("Por último, introduce una contraseña(Puede incluir letras, números y caracteres especiales) "))
        
        user = model.User(name, surname, email, password)
        register = user.register()
        
        if register[0] >= 1:
            print(f"\nPerfecto, el usuario {register[1].name} se ha registrado con el email {register[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("Vale, por favor, identifícate en el sistema:")
        
        try: 
            email = input("¿Cuál es tu email? ")
            password = str(input("Introduce tu contraseña: "))
            
            user = model.User('', '', email, password)
            login = user.identified()
            
            if email == login[3]:
                print(f"\nHola de nuevo {login[1]}, te has registrado en el sistema el {login[5]}")
                print("Has iniciado sesión con éxito")
                self.nextActions(login)
                
                
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"Fallo al iniciar sesión, por favor, verifica que tu email y contraseña sean correctos")

    def nextActions(self, user):
    
        print("""
            Acciones disponibles:
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar notas (eliminar)
            - Salir (salir)
        """)
        
        action = input("¿Qué deseas hacer? ")
        lower_action = action.lower()
        doThe = notes.actions.Actions()
        
        if lower_action == "crear" or lower_action == "crear nota":
            print("Vamos a crear la nueva nota")
            doThe.create(user)
            #* Así hacemos que nuestro programa se ejecute de nuevo
            self.nextActions(user)
            
            
        elif lower_action == "mostrar" or lower_action == "mostrar notas":
            print("Te muestro tus notas: ")
            #* Así hacemos que nuestro programa se ejecute de nuevo
            doThe.show(user)
            self.nextActions(user)
            
            
        elif lower_action == "eliminar" or lower_action == "eliminar nota":
            print("Vamos a eliminar tu/s nota/s")
            #* Así hacemos que nuestro programa se ejecute de nuevo
            doThe.deleted(user)
            self.nextActions(user)
            
            
        elif lower_action == "salir":
            print(f"Ok, {user[1]}, nos vemos pronto, no tardes :)")
            exit()
            
            
        else:
            print("Por favor, introduce una opción válida")
            #* Así hacemos que nuestro programa se ejecute de nuevo
            self.nextActions(user)