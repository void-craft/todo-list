from colorama import init, Fore, Style
from datetime import datetime, date

init(autoreset=True)

from controllers.task_controller import (create_task, get_all_tasks,
                                         get_task_by_id, update_task,
                                         delete_task)


def display_tasks_in_table(tasks):
    """ Mostra tareas en forma tabla """
    tasks = sorted(tasks, key=lambda task: task.date or date.max)
    print("-" * 122)
    print(
        Fore.CYAN + Style.BRIGHT +
        f"{'ID':<5} {'Título':<40} {'Descripción':<60} {'Fecha de tarea':<10}")
    print("-" * 122)

    for task in tasks:
        id_str = str(task.id)
        titulo = task.title[:40] if task.title else ''
        descripcion = task.description[:60] if task.description else ''
        if task.date:
            if task.date < date.today():
                color = Fore.RED
            elif task.date == date.today():
                color = Fore.LIGHTYELLOW_EX
            else:
                color = Fore.GREEN
            date_str = color + task.date.strftime("%d/%m/%Y") + Style.RESET_ALL
        else:
            date_str = ''

        print(f"{id_str:<5} {titulo:<40} {descripcion:<60} {date_str:<15}")

    print("-" * 122)

    legend = (f"{Fore.GREEN}🟩 Pendiente{Style.RESET_ALL}  |    "
              f"{Fore.YELLOW}🟨 Hoy{Style.RESET_ALL}  |    "
              f"{Fore.RED}🟥 Finalizada{Style.RESET_ALL}")
    print("\n " + legend + "\n")


def show_task_menu():
    """ Mostra el Menú """
    print("\n")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "-+" * 61)
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "\n+-+- Menú To-Do -+-+ \n")
    print("\033[38;5;208m\033[1m 1. Crear tarea\033[0m")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + " 2. Ver tareas")
    print(Fore.GREEN + Style.BRIGHT + " 3. Buscar tarea por ID")
    print(Fore.CYAN + Style.BRIGHT + " 4. Actualizar tarea")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " 5. Eliminar tarea")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + " 6. Salir")


def print_task(task):
    """ Imprima la tarea añadida"""
    print(Fore.GREEN + f"\n{task.id} | {Style.BRIGHT}{task.title}")
    if task.description:
        print(Fore.LIGHTWHITE_EX + f"   ↳ {task.description}")

def main():
    while True:
        # Llama el menu
        show_task_menu()
        choice = input(Fore.CYAN + Style.BRIGHT +
                       "\nElige una opción: ").strip()
        print()

        try:
            # Añadir una tarea
            if choice == "1":
                title = input("Nuevo título: ").strip()
                if not title:
                    print(Fore.RED + "El título no puede estar vacío.\n")
                    continue
                desc = input("Descripción (opcional): ").strip()
                date_input = input("Nueva Fecha (DDMMYYYY, dejar vacío para hoy): ").strip()
    
                if date_input:  # Solo valida si usuario escribe algo
                    if not (date_input.isdigit() and len(date_input) == 8):
                        print(Fore.RED + "Formato inválido. Escribe la fecha como 8 dígitos: DDMMYYYY.")
                        continue
        
                    date_formateada = f"{date_input[:2]}/{date_input[2:4]}/{date_input[4:]}"
                    task, error = create_task(title, date_formateada, desc)
                else:
                    task, error = create_task(title, None, desc)  # "None"(nada) llamará fecha por defecto
    
                if error:
                    print(Fore.RED + f"\nError: {error}\n")
                else:
                    print(Fore.GREEN + Style.BRIGHT + "\nTarea Creada Con Éxito: \n")
                    print_task(task)

            # Ver todas las tareas
            elif choice == "2":
                tasks = get_all_tasks()
                if not tasks:
                    print(Fore.YELLOW + "No hay tareas registradas.")
                else:
                    print(Fore.YELLOW + Style.BRIGHT + "\nLista de tareas:")
                    display_tasks_in_table(tasks)

            # Busca una tarea
            elif choice == "3":
                tid = int(input("ID de la tarea: "))
                task = get_task_by_id(tid)
                if task:
                    display_tasks_in_table([task])
                else:
                    print(Fore.RED + "Tarea no encontrada.\n")

            # Actualiza una tarea
            elif choice == "4":
                try:
                    tid = int(input("ID de la tarea a actualizar: "))
                    task = get_task_by_id(tid)
                    if not task:
                        print(Fore.RED + "Tarea no encontrada.\n")
                        continue

                    print_task(task)

                    title = input("\nNuevo título: ").strip()
                    if not title:
                        print(Fore.RED + "El título no puede estar vacío.\n")
                        continue

                    desc = input("Nueva descripción: ").strip()
                    date_input = input("Nueva Fecha (DDMMYYYY, dejar vacío para no cambiar): ").strip()

                    if date_input:  # Solo valida si usuario escribe algo
                        if not (date_input.isdigit() and len(date_input) == 8):
                            print(Fore.RED + "Formato inválido. Escribe la fecha como 8 dígitos: DDMMYYYY.\n")
                            continue

                        date_formateada = f"{date_input[:2]}/{date_input[2:4]}/{date_input[4:]}"
                        updated, error = update_task(tid, title, desc, date_formateada)
                    else:
                        updated, error = update_task(tid, title, desc)

                    if error:
                        print(Fore.RED + f"\nError: {error}\n")
                    elif updated:
                        print(Fore.GREEN + Style.BRIGHT + "\nTAREA ACTUALIZADA CON ÉXITO:")
                        print_task(updated)
                    else:
                        print(Fore.RED + "No se pudo actualizar.")

                except ValueError:
                    print(Fore.RED + "Entrada inválida. Ingresa un número para el ID.\n")

            # Elimina una tarea     
            elif choice == "5":
                try:
                    tid = int(input("ID de la tarea a eliminar: "))
                    task = get_task_by_id(tid)
                    if not task:
                        print(Fore.RED + "Tarea no encontrada.\n")
                        continue

                    print_task(task)
                    confirm = input(
                        Fore.YELLOW +
                        "\n¿Estás seguro de que deseas eliminar esta tarea? (s/n):\n"
                    ).strip().lower()
                    if confirm != "s":
                        print(Fore.CYAN + "Eliminación cancelada.\n")
                        continue

                    deleted = delete_task(tid)
                    print(Fore.GREEN +
                          "Tarea eliminada." if deleted else Fore.RED +
                          "No se pudo eliminar.")

                except ValueError:
                    print(Fore.RED +
                          "ID inválido. Debe ser un número entero.\n")

            # Sal del menu
            elif choice == "6":
                print(Fore.CYAN + "\n¡Hasta luego!\n")
                break

            else:
                print(Fore.RED + "Opción no válida.\n"
                      "")

        except ValueError:
            print(
                Fore.RED +
                "Entrada inválida. Asegúrate de ingresar números donde corresponda.\n"
            )
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}")
