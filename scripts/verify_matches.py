
import csv
import os

CONSUMPTION_DIR = r"C:\Users\crisrojagu\Documents\Consumos\data"
DEMO_FILE = r"C:\Users\crisrojagu\Documents\Cruces_col\Cruces_col\data\COLSUBSIDIO_LT_CV_IDN_CONSOLIDACION_FINAL_SEGM.csv"

def check_overlap():
    print("Cargando NITs de demografía...")
    demo_nits = set()
    with open(DEMO_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        # ID_EMPRESA está en col 25, NIT_NUM en col 26
        for row in reader:
            if len(row) > 26:
                nit = row[25].strip()
                if nit: demo_nits.add(nit)
                nit_num = row[26].strip().split('.')[0]
                if nit_num:
                    if not nit_num.startswith('NIT'):
                        demo_nits.add(f"NIT{nit_num}")
                    else:
                        demo_nits.add(nit_num)

    print(f"Total NITs en demografía: {len(demo_nits)}")

    for ue in ["VIVIENDA", "HOTELES", "PISCILAGO", "RYD", "MEDICAMENTOS"]:
        path = os.path.join(CONSUMPTION_DIR, f"{ue}.csv")
        if not os.path.exists(path): continue
        
        print(f"\nAnalizando {ue}...")
        nit_col = 15
        if ue == "VIVIENDA": nit_col = 16
        elif ue == "RYD": nit_col = 20
        
        matches = 0
        total = 0
        with open(path, 'r', encoding='latin-1') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) > nit_col:
                    total += 1
                    nit = row[nit_col].strip().split('.')[0]
                    if not nit.startswith('NIT') and nit:
                        nit = f"NIT{nit}"
                    if nit in demo_nits:
                        matches += 1
                if total >= 1000: break
        
        if total > 0:
            print(f"Muestra de 1000: {matches} coincidencias ({matches/total*100:.1f}%)")

if __name__ == "__main__":
    check_overlap()
