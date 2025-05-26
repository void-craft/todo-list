import os
from dotenv import load_dotenv

# Carga variables entorno desde .env 
load_dotenv()

from views.task_view import main

if __name__ == "__main__":
    main()
