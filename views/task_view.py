import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.task_controller import (
    create_task, get_all_tasks,
    get_task_by_id, update_task, delete_task
)

def show_task_menu():
    print("=== TO-DO MENU ===")
    print("1. Crear tarea")
    print("2. Ver tareas")
    print("3. Buscar tarea por ID")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")

def main():
    while True:
        show_task_menu()
        choice = input("Elige una opción: ").strip()
        if choice == "1":
            title = input("Título: ").lower()
            desc  = input("Descripción (opcional): ")
            task = create_task(title, desc)
            print(f"Creada: {task}")
        elif choice == "2":
            for t in get_all_tasks():
                print(t)
        elif choice == "3":
            tid = int(input("ID de la tarea: "))
            print(get_task_by_id(tid))
        elif choice == "4":
            tid = int(input("ID de la tarea a actualizar: "))
            title = input("Nuevo título: ")
            desc  = input("Nueva descripción: ")
            print(update_task(tid, title, desc))
        elif choice == "5":
            tid = int(input("ID de la tarea a eliminar: "))
            deleted = delete_task(tid)
            print("Eliminada." if deleted else "No encontrada.")
        elif choice == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()    
