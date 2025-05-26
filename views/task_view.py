from colorama import init, Fore, Style
from datetime import date
from controllers.task_controller import (
    create_task, get_all_tasks, get_task_by_id,
    update_task, delete_task
)

init(autoreset=True)

#COLORES
COLOR_TITLE = Fore.CYAN + Style.BRIGHT
COLOR_SUCCESS = Fore.GREEN + Style.BRIGHT
COLOR_WARNING = Fore.YELLOW + Style.BRIGHT
COLOR_ERROR = Fore.RED + Style.BRIGHT
COLOR_MENU = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
COLOR_INFO = Fore.LIGHTWHITE_EX
COLOR_PROMPT = Fore.LIGHTBLUE_EX + Style.BRIGHT


def display_tasks_in_table(tasks):
    """Muestra las tareas en forma de tabla"""
    tasks = sorted(tasks, key=lambda task: task.date or date.max)
    print("-" * 122)
    print(COLOR_TITLE + f"{'ID':<5} {'Título':<40} {'Descripción':<60} {'Fecha de tarea':<10}")
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

    legend = (
        f"{Fore.GREEN}🟩 Pendiente{Style.RESET_ALL}  |  "
        f"{Fore.YELLOW}🟨 Hoy{Style.RESET_ALL}  |  "
        f"{Fore.RED}🟥 Finalizada{Style.RESET_ALL}"
    )
    print("\n " + legend + "\n")


def show_task_menu():
    """Muestra el menú principal"""
    print("\n" + COLOR_MENU + "-+" * 40)
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "\n+-+- Menú To-Do -+-+\n")
    print("\033[38;5;208m\033[1m 1. Crear tarea\033[0m")
    print(COLOR_WARNING + " 2. Ver tareas")
    print(COLOR_SUCCESS + " 3. Buscar tarea por ID")
    print(COLOR_TITLE + " 4. Actualizar tarea")
    print(COLOR_PROMPT + " 5. Eliminar tarea")
    print(COLOR_MENU + " 6. Salir")


def print_task(task):
    print(COLOR_SUCCESS + f"\n{task.id} | {Style.BRIGHT}{task.title}")
    if task.description:
        print(COLOR_INFO + f"   ↳ {task.description}")


def handle_create_task():
    title = input("Nuevo título: ").strip()
    if not title:
        print(COLOR_ERROR + "El título no puede estar vacío.\n")
        return

    desc = input("Descripción (opcional): ").strip()
    date_input = input("Nueva Fecha (DDMMYYYY, dejar vacío para hoy): ").strip()

    task, error = create_task(title, date_input, desc)
    if error:
        print(COLOR_ERROR + f"\nError: {error}\n")
    else:
        print(COLOR_SUCCESS + "\nTarea Creada Con Éxito:\n")
        print_task(task)


def handle_view_tasks():
    tasks = get_all_tasks()
    if not tasks:
        print(COLOR_WARNING + "No hay tareas registradas.")
    else:
        print(COLOR_WARNING + "\nLista de tareas:")
        display_tasks_in_table(tasks)


def handle_search_task():
    try:
        tid = int(input("ID de la tarea: "))
        task = get_task_by_id(tid)
        if task:
            display_tasks_in_table([task])
        else:
            print(COLOR_ERROR + "Tarea no encontrada.\n")
    except ValueError:
        print(COLOR_ERROR + "ID inválido. Debe ser un número entero.\n")


def handle_update_task():
    try:
        tid = int(input("ID de la tarea a actualizar: "))
        task = get_task_by_id(tid)
        if not task:
            print(COLOR_ERROR + "Tarea no encontrada.\n")
            return

        print_task(task)

        title = input("\nNuevo título: ").strip()
        if not title:
            print(COLOR_ERROR + "El título no puede estar vacío.\n")
            return

        desc = input("Nueva descripción: ").strip()
        date_input = input("Nueva Fecha (DDMMYYYY, dejar vacío para no cambiar): ").strip()

        updated, error = update_task(tid, title, desc, date_input)
        if error:
            print(COLOR_ERROR + f"\nError: {error}\n")
        elif updated:
            print(COLOR_SUCCESS + "\nTAREA ACTUALIZADA CON ÉXITO:")
            print_task(updated)
           
        else:
            print(COLOR_ERROR + "No se pudo actualizar.")
    except ValueError:
        print(COLOR_ERROR + "Entrada inválida. Ingresa un número para el ID.\n")


def handle_delete_task():
    try:
        tid = int(input("ID de la tarea a eliminar: "))
        task = get_task_by_id(tid)
        if not task:
            print(COLOR_ERROR + "Tarea no encontrada.\n")
            return

        print_task(task)
        confirm = input(COLOR_WARNING + "\n¿Estás seguro de que deseas eliminar esta tarea? (s/n): ").strip().lower()
        if confirm != "s":
            print(COLOR_TITLE + "Eliminación cancelada.\n")
            return

        deleted = delete_task(tid)
        if deleted:
            print(COLOR_SUCCESS + "Tarea eliminada.")
        else:
            print(COLOR_ERROR + "No se pudo eliminar.")
    except ValueError:
        print(COLOR_ERROR + "ID inválido. Debe ser un número entero.\n")


#  Menú principal
def main():
    while True:
        show_task_menu()
        choice = input(COLOR_TITLE + "\nElige una opción: ").strip()
        print()

        try:
            if choice == "1":
                handle_create_task()
            elif choice == "2":
                handle_view_tasks()
            elif choice == "3":
                handle_search_task()
            elif choice == "4":
                handle_update_task()
            elif choice == "5":
                handle_delete_task()
            elif choice == "6":
                print(COLOR_TITLE + "\n¡Hasta luego!\n")
                break
            else:
                print(COLOR_ERROR + "Opción no válida.\n")
        except Exception as e:
            print(COLOR_ERROR + f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
