from colorama import init, Fore, Style
from datetime import datetime, date

init(autoreset=True)

from controllers.task_controller import (
    create_task, get_all_tasks,
    get_task_by_id, update_task, delete_task
)

def mostrar_tareas_como_tabla(tasks):
    print("-" * 135)
    print(Fore.CYAN + Style.BRIGHT + f"{'ID':<5} {'Título':<40} {'Descripción':<60} {'Fecha de tarea':<10}")
    print("-" * 135)
    
    for t in tasks:
        id_str = str(t.id)
        titulo = t.title[:40] if t.title else ''
        descripcion = t.description[:60] if t.description else ''
        fecha_str = t.fecha.strftime("%d/%m/%Y") if t.fecha else ''
        print(f"{id_str:<5} {titulo:<40} {descripcion:<60} {fecha_str:<15}")
    
    print("-" * 120)

def show_task_menu():
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "+-+- Menú To-Do -+-+ ")
    # print(f"\033[38;5;208m{Style.BRIGHT}\033[0m" + " 1. Crear tarea")

    print("\033[38;5;208m\033[1m 1. Crear tarea\033[0m")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + " 2. Ver tareas")
    print(Fore.GREEN + Style.BRIGHT + " 3. Buscar tarea por ID")
    print(Fore.CYAN + Style.BRIGHT + " 4. Actualizar tarea")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " 5. Eliminar tarea")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + " 6. Salir")

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
                fecha_input = input("📅 FECHA DE TAREA(DD/MM/AAAA): ").strip()

                try:
                    fecha = datetime.strptime(fecha_input, "%d/%m/%Y").date()
                    if fecha < date.today():
                        print(Fore.RED + "❌ La fecha no puede ser anterior a hoy.")
                        return
                except ValueError:
                    print(Fore.RED + "❌ Formato de fecha inválido. Usa el formato DD/MM/AAAA (ej: 23/05/2025).")
                    return

                task = create_task(title, fecha, desc)
                print(Fore.GREEN + f"\n✅ TAREA CREADA: {task}")
            elif choice == "2":
                tasks = get_all_tasks()
                if not tasks:
                    print(Fore.YELLOW + "⚠️  No hay tareas registradas.")
                else:
                    print(Fore.YELLOW
                     + Style.BRIGHT + "\n📋 Lista de tareas:")
                    mostrar_tareas_como_tabla(tasks)    

            # elif choice == "2":
            #     tasks = get_all_tasks()
            #     if not tasks:
            #         print(Fore.YELLOW + "⚠️  No hay tareas registradas.")
            #     else:
            #         print(Fore.BLUE + Style.BRIGHT + "\n📋 Lista de tareas:")
            #         for t in tasks:
            #             print_task(t)

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

if __name__     == "__main__":
    main()  