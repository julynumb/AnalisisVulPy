import os
import sys
import pandas as pd

# Constantes
ORIGIN_DIR = "./FilesToProcess"
DESTINY_DIR = "./FilesByGroup"
COLUMN_FF = ["Group", "Status", "`Current Treatment`"]
#Se coloca el grupo que se desea filtrar
VALUES_FF = ["angier", "VULNERABLE", "Untreated"]

ORDER_COLUMN = ['Group', 'Related Finding', 'Root Nickname', 'Where', 'Report Moment', 'Status', 'Current Treatment']
SHEET="Data"


def find_excel_file():
    """Busca el primer archivo .xlsx o .xls en el directorio actual."""
    files = [f for f in os.listdir(
        ORIGIN_DIR) if f.lower().endswith(('.xlsx', '.xls'))]
    if not files:
        print("No se encontró ningún archivo Excel en este directorio.")
        sys.exit(1)
    if len(files) > 1:
        print("Se encontraron varios archivos Excel. Selecciona uno:")
        for i, f in enumerate(files, 1):
            print(f"  {i}. {f}")
        idx = int(input("Número de archivo: ")) - 1
        return files[idx]
    return files[0]


def complete_path(file_name, dir):
    return os.path.join(dir, str(file_name))


def first_filter(data):
    df_sub = data.query(f"{COLUMN_FF[0]} == '{VALUES_FF[0]}' and {COLUMN_FF[1]} == '{VALUES_FF[1]}' and {COLUMN_FF[2]} == '{VALUES_FF[2]}'")
    for idx, col in enumerate(ORDER_COLUMN):
        df_sub.insert(loc=idx, column=col, value=df_sub.pop(col))
    new_name = complete_path(f"{VALUES_FF[0]}.xlsx", DESTINY_DIR)
    df_sub.to_excel(new_name, index=False)


def main():
    # 1. Detectar y leer el Excel
    excel_file = complete_path(find_excel_file(), ORIGIN_DIR)
    print(f"Usando el archivo: {excel_file}")
    df = pd.read_excel(excel_file, sheet_name=SHEET)

    # 2. Filtrado de columnas
    first_filter(df)


if __name__ == "__main__":
    main()
