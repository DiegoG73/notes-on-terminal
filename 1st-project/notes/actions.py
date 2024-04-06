import notes.notes as model

class Actions:
    
    def create(self, user):
        print(f"\nOk, {user[1]}, vamos a crear una nueva nota...")
        
        title = input("Por favor, introduce el título de tu nota: ")
        description = input("Ahora, por favor, introduce el contenido de tu nota: ")
        
        notes = model.Note(user[0], title, description)
        save = notes.save()
        
        if save[0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {notes.title}")
            
        else: 
            print(f"\nNo se ha guardado la nota, lo siento {user[1]}")
            
            
    def show(self, user):
        print(f"\nVale, {user[1]}, aquí tienes tus notas: ")
        
        note = model.Note(user[0], "", "")
        notes = note.list()
        
        for note in notes:
            print("\n****************************************")
            print(note[2])
            print(note[3])
            print("****************************************")
            
    def deleted(self, user):
        print(f"\nOk, {user[1]}, vamos a borrar notas:")
        
        title = input("Introduce el título de la nota a borrar: ")
        note = model.note(user[0], title, "")
        delete = note.delete()
        
        if delete[0] >= 1:
            print(f"He borrado la nota: {note.title}")
        else:
            print("No se ha borrado la nota, por favor, inténtalo de nuevo más tarde")