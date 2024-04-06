"""
Proyecto Python con MySQL:
-   Abrir asistente
-   Login o registro
-   Si elegimos registro, creará un usuario en la base de datos
-   Login: Identifica el usuario y comenzará el registro y demás acciones de notas
-   Crear notas
-   Mostrar notas
-   Borrar notas
"""
from users import actions


print("""
® SPANISH VERSION 🇪🇸
Acciones disponibles:
    - Registro
    - Login
""")

doThe = actions.Actions()
action = input("¿Qué deseas hacer? ")
lower_action = action.lower()

if lower_action == "registro":
    doThe.register()
elif lower_action == "login":
    doThe.login()
else:
    print("Por favor, introduce una opción correcta")