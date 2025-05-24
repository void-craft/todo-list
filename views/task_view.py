from colorama import init, Fore, Style
from datetime import datetime, date

init(autoreset=True)

from controllers.task_controller import (
    create_task, get_all_tasks,
    get_task_by_id, update_task, delete_task
)

def mostrar_tareas_como_tabla(tasks):
    tasks = sorted(tasks, key=lambda t: t.fecha or date.max)
    print("-" * 122)
    print(Fore.CYAN + Style.BRIGHT + f"{'ID':<5} {'Título':<40} {'Descripción':<60} {'Fecha de tarea':<10}")
    print("-" * 122)
    
    for t in tasks:
        id_str = str(t.id)
        titulo = t.title[:40] if t.title else ''
        descripcion = t.description[:60] if t.description else ''
        if t.fecha:
            if t.fecha < date.today():
                color = Fore.RED
            elif t.fecha == date.today():
                color = Fore.LIGHTYELLOW_EX
            else:
                color = Fore.GREEN
            fecha_str = color + t.fecha.strftime("%d/%m/%Y") + Style.RESET_ALL
        else:
            fecha_str = ''
        
        print(f"{id_str:<5} {titulo:<40} {descripcion:<60} {fecha_str:<15}")
    
    print("-" * 122)
    
    leyenda = (
        f"{Fore.GREEN}🟩 Pendiente{Style.RESET_ALL}  |    "
        f"{Fore.YELLOW}🟨 Hoy{Style.RESET_ALL}  |    "
        f"{Fore.RED}🟥 Finalizada{Style.RESET_ALL}"
    )
    print("\n " + leyenda + "\n")

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
        choice = input(Fore.CYAN + "\nElige una opción: ").strip()
        print()

        try:
            if choice == "1":
                title = input("📝 TÍTULO: ").strip()
                title = input("Nuevo título: ").strip()
                if not title:
                    print(Fore.RED + "❌ El título no puede estar vacío.\n")
                    continue
                desc = input("🗒️  DESCRIPCIÓN (opcional): ").strip()
                fecha_input = input("Nueva Fecha (DDMMYYYY): ").strip()

                # Validación del formato esperado (8 dígitos numéricos)
                if not (fecha_input.isdigit() and len(fecha_input) == 8):
                    print(Fore.RED + "❌ Formato inválido. Escribe la fecha como 8 dígitos: DDMMYYYY.")
                    continue

                # Insertar barras automáticamente
                fecha_formateada = f"{fecha_input[:2]}/{fecha_input[2:4]}/{fecha_input[4:]}"

                # Intentar convertir a fecha válida
                try:
                    fecha = datetime.strptime(fecha_formateada, "%d/%m/%Y").date()
                    if fecha < date.today():
                        print(Fore.RED + "❌ La fecha no puede ser anterior a hoy.")
                        continue
                except ValueError:
                    print(Fore.RED + "❌ Fecha inválida. Asegúrate de que la fecha existe.")
                    continue


                task = create_task(title, fecha, desc)
                print(Fore.GREEN + "\n✅ TAREA CREADA CON ÉXITO:\n")
                
            elif choice == "2":
                tasks = get_all_tasks()
                if not tasks:
                    print(Fore.YELLOW + "⚠️  No hay tareas registradas.")
                else:
                    print(Fore.YELLOW
                     + Style.BRIGHT + "\n📋 Lista de tareas:")
                    mostrar_tareas_como_tabla(tasks)    

            elif choice == "3":
                tid = int(input("🔍 ID de la tarea: "))
                task = get_task_by_id(tid)
                if task:
                    mostrar_tareas_como_tabla([task]) 
                else:
                    print(Fore.RED + "❌ Tarea no encontrada.\n")

            elif choice == "4":
                try:
                    tid = int(input("✏️  ID de la tarea a actualizar: "))
                    task = get_task_by_id(tid)
                    if not task:
                        print(Fore.RED + "❌ Tarea no encontrada.\n")
                        continue

                    print_task(task)

                    title = input("\nNuevo título: ").strip()
                    if not title:
                        print(Fore.RED + "❌ El título no puede estar vacío.\n")
                        continue

                    desc = input("Nueva descripción: ").strip()
                    fecha_input = input("Nueva Fecha (DDMMYYYY): ").strip()

                    if not (fecha_input.isdigit() and len(fecha_input) == 8):
                        print(Fore.RED + "❌ Formato inválido. Escribe la fecha como 8 dígitos: DDMMYYYY.\n")
                        continue

                    fecha_formateada = f"{fecha_input[:2]}/{fecha_input[2:4]}/{fecha_input[4:]}"
                    try:
                        fecha = datetime.strptime(fecha_formateada, "%d/%m/%Y").date()
                        if fecha < date.today():
                            print(Fore.RED + "❌ La fecha no puede ser anterior a hoy.\n")
                            continue
                    except ValueError:
                        print(Fore.RED + "❌ Fecha inválida.")
                        continue

                    updated = update_task(tid, title, desc, fecha)
                    if updated:
                        print(Fore.GREEN + "\n🔄 TAREA ACTUALIZADA CON ÉXITO:")
                        print_task(updated)
                    else:
                        print(Fore.RED + "❌ No se pudo actualizar.")

                except ValueError:
                    print(Fore.RED + "❗ Entrada inválida. Ingresa un número para el ID.\n")


            elif choice == "5":
                try:
                    tid = int(input("🗑️  ID de la tarea a eliminar: "))
                    task = get_task_by_id(tid)
                    if not task:
                        print(Fore.RED + "❌ Tarea no encontrada.\n")
                        continue

                    print_task(task)
                    confirm = input(Fore.YELLOW + "\n⚠️  ¿Estás seguro de que deseas eliminar esta tarea? (s/n):\n").strip().lower()
                    if confirm != "s":
                        print(Fore.CYAN + "🔄 Eliminación cancelada.\n")
                        continue

                    deleted = delete_task(tid)
                    print(Fore.GREEN + "🗑️  Tarea eliminada." if deleted else Fore.RED + "❌ No se pudo eliminar.")

                except ValueError:
                    print(Fore.RED + "❗ ID inválido. Debe ser un número entero.\n")

            elif choice == "6":
                print(Fore.CYAN + "\n👋 ¡Hasta luego!\n")
                break

            else:
                print(Fore.RED + "❌ Opción no válida.\n"
                "")

        except ValueError:
            print(Fore.RED + "❗ Entrada inválida. Asegúrate de ingresar números donde corresponda.\n")
        except Exception as e:
            print(Fore.RED + f"⚠️  Error inesperado: {e}")

if __name__     == "__main__":
    main()  