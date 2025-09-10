"""
Genera datos BRUTOS (sin segmentaciones ni políticas, ni parámetros de probabilidad)
para un dashboard comercial. Crea 3 archivos dentro de ./data:

- data/customers.xlsx  (idCliente, nombre, zip, ciudad, IdRepre)
- data/reps.xlsx       (IdRepre, rep_name)
- data/sales.xlsx      (sale_id, idCliente, fecha, IdRepre, importe)

Requisitos:
    pip install pandas numpy XlsxWriter
Ejecución:
    python generate_raw_data.py
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime
from pathlib import Path

# ---------------------------
# Parámetros básicos
# ---------------------------
SEED = 123
N_REPS = 10
N_CUSTOMERS = 3000
DATE_START = datetime(2024, 1, 1)
DATE_END   = datetime(2025, 9, 1)

# Prefijos ZIP sencillos
CITY_ZIP_PREFIX = {
    "Madrid": "28",
    "Barcelona": "08",
    "Valencia": "46",
    "Sevilla": "41",
    "Bilbao": "48",
}

# Carpeta de salida
OUT_DIR = Path("./data")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_CUSTOMERS = OUT_DIR / "customers.xlsx"
OUT_REPS      = OUT_DIR / "reps.xlsx"
OUT_SALES     = OUT_DIR / "sales.xlsx"


def set_seed(seed=SEED):
    random.seed(seed)
    np.random.seed(seed)


def month_iter(start: datetime, end: datetime):
    d = datetime(start.year, start.month, 1)
    while d <= end:
        yield d
        # avanzar 1 mes
        if d.month == 12:
            d = datetime(d.year + 1, 1, 1)
        else:
            d = datetime(d.year, d.month + 1, 1)


def make_reps(n_reps=N_REPS) -> pd.DataFrame:
    return pd.DataFrame([
        {"IdRepre": f"R{i:03d}", "rep_name": f"Comercial {i}"}
        for i in range(1, n_reps + 1)
    ])


def make_customers(n_customers=N_CUSTOMERS, reps_df=None) -> pd.DataFrame:
    cities = list(CITY_ZIP_PREFIX.keys())
    rows = []
    for i in range(1, n_customers + 1):
        city = random.choice(cities)
        zip_code = CITY_ZIP_PREFIX[city] + f"{random.randint(0, 999):03d}"
        IdRepre = reps_df.sample(1)["IdRepre"].item()
        rows.append({
            "idCliente": f"C{i:05d}",
            "nombre": f"Cliente {i}",
            "zip": zip_code,
            "ciudad": city,
            "IdRepre": IdRepre,  # asignación simple de comercial
        })
    return pd.DataFrame(rows)


def make_sales(customers_df: pd.DataFrame) -> pd.DataFrame:
    """
    Genera ventas mensuales por cliente.
    Regla simple (sin exponer probabilidades): cada mes para cada cliente
    se sortean 0, 1 o 2 compras con pesos razonables (60%, 35%, 5%).
    Importe ~ lognormal para dar variabilidad realista.
    """
    rows = []
    sale_id = 1
    for _, c in customers_df.iterrows():
        for m in month_iter(DATE_START, DATE_END):
            # nº de compras en este mes (0-2) con pesos in-line
            n_purchases = random.choices([0, 1, 2], weights=[0.60, 0.35, 0.05], k=1)[0]
            for _ in range(n_purchases):
                day = random.randint(1, 28)  # día seguro
                date = datetime(m.year, m.month, day).date()
                amount = float(np.round(np.random.lognormal(mean=7.0, sigma=0.5), 2))
                rows.append({
                    "sale_id": f"S{sale_id:07d}",
                    "idCliente": c["idCliente"],
                    "fecha": date,          # YYYY-MM-DD
                    "IdRepre": c["IdRepre"],  # comercial asignado al cliente
                    "importe": amount,
                })
                sale_id += 1
    return pd.DataFrame(rows).sort_values("fecha").reset_index(drop=True)


def main():
    set_seed()
    reps_df = make_reps()
    customers_df = make_customers(reps_df=reps_df)
    sales_df = make_sales(customers_df)

    reps_df.to_excel(OUT_REPS, index=False)
    customers_df.to_excel(OUT_CUSTOMERS, index=False)
    sales_df.to_excel(OUT_SALES, index=False)

    print("✔ Datos brutos generados en ./data:")
    print(f"- {OUT_REPS}")
    print(f"- {OUT_CUSTOMERS}")
    print(f"- {OUT_SALES}")


if __name__ == "__main__":
    main()
