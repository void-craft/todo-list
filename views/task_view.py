import sys
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.task_controller import (
    create_task, get_all_tasks,
    get_task_by_id, update_task, delete_task
)
def fondo_naranja(texto):
    return f"\033[48;5;208m{Style.BRIGHT + Fore.LIGHTWHITE_EX}{texto}\033[0m"

def show_task_menu():
    print(Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + "\n +-+- Menú To-Do -+-+ ")
    print(fondo_naranja(" 1. Crear tarea"))
    print(Back.YELLOW + Fore.LIGHTWHITE_EX + Style.BRIGHT + " 2. Ver tareas")
    print(Back.GREEN + Fore.LIGHTWHITE_EX + Style.BRIGHT + " 3. Buscar tarea por ID")
    print(Back.CYAN + Fore.LIGHTWHITE_EX + Style.BRIGHT + " 4. Actualizar tarea")
    print(Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + " 5. Eliminar tarea")
    print(Back.LIGHTMAGENTA_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + " 6. Salir")

def print_task(task):
    print(Fore.GREEN + f"\n🆔 {task.id} | {Style.BRIGHT}{task.title}")
    if task.description:
        print(Fore.LIGHTWHITE_EX + f"   ↳ {task.description}")

def main():
    while True:
        show_task_menu()
        choice = input(Fore.GREEN + "\nElige una opción: ").strip()
        print()

        try:
            if choice == "1":
                title = input("📝 TÍTULO: ").strip()
                desc = input("🗒️  DESCRIPCIÓN (opcional): ").strip()
                task = create_task(title, desc)
                print(Fore.GREEN + f"\n✅ TAREA CREADA: {task}")

            elif choice == "2":
                tasks = get_all_tasks()
                if not tasks:
                    print(Fore.YELLOW + "⚠️  No hay tareas registradas.")
                else:
                    print(Fore.BLUE + Style.BRIGHT + "\n📋 Lista de tareas:")
                    for t in tasks:
                        print_task(t)

            elif choice == "3":
                tid = int(input("🔍 ID de la tarea: "))
                task = get_task_by_id(tid)
                if task:
                    print_task(task)
                else:
                    print(Fore.RED + "❌ Tarea no encontrada.")

            elif choice == "4":
                tid = int(input("✏️  ID de la tarea a actualizar: "))
                title = input("Nuevo título: ").strip()
                desc = input("Nueva descripción: ").strip()
                updated = update_task(tid, title, desc)
                if updated:
                    print(Fore.GREEN + "✅ Tarea actualizada.")
                else:
                    print(Fore.RED + "❌ No se pudo actualizar.")

            elif choice == "5":
                tid = int(input("🗑️  ID de la tarea a eliminar: "))
                deleted = delete_task(tid)
                print(Fore.GREEN + "🗑️  Tarea eliminada." if deleted else Fore.RED + "❌ Tarea no encontrada.")

            elif choice == "6":
                print(Fore.CYAN + "\n👋 ¡Hasta luego!")
                break

            else:
                print(Fore.RED + "❌ Opción no válida.")

        except ValueError:
            print(Fore.RED + "❗ Entrada inválida. Asegúrate de ingresar números donde corresponda.")
        except Exception as e:
            print(Fore.RED + f"⚠️  Error inesperado: {e}")


