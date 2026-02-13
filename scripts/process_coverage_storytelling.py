"""
Script de Procesamiento Final: Cobertura y Benchmarking
Combina Demografía (1.2GB) + Consumos para calcular coberturas 2024-2025.
"""

import csv
import json
import os
import base64
from collections import defaultdict
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# ==================== CONFIGURACIÓN ====================
DEMOGRAPHIC_FILE = r"C:\Users\crisrojagu\Documents\Cruces_col\Cruces_col\data\COLSUBSIDIO_LT_CV_IDN_CONSOLIDACION_FINAL_SEGM.csv"
EMPRESAS_SEGM_FILE = r"C:\Users\crisrojagu\Documents\Cruces_col\Cruces_col\data\COLSUBSIDIO_LT_CV_IDN_LIST_EMPRESAS_SEGM.csv"
CONSUMPTION_DIR = r"C:\Users\crisrojagu\Documents\Consumos\data"
OUTPUT_FILE = r"C:\Users\crisrojagu\Documents\Proy_65\ficha_empresarial\datos\datos_ficha_completa.js"
PASSWORD_DASHBOARD = "Bi2026_*"

# UEs
UES = ["VIVIENDA", "HOTELES", "PISCILAGO", "RYD", "MEDICAMENTOS"]

def clean_encoding(text):
    """Limpia artefactos comunes de codificación UTF-8 mal interpretados como Latin-1"""
    if not text: return text
    mappings = {
        "Ãš": "Ú",
        "Ã“": "Ó",
        "Ã ": "Á",
        "Ã‰": "É",
        "Ã\x8d": "Í", # Í
        "Ã‘": "Ñ",
        "Ã±": "ñ",
        "Ãº": "ú",
        "Ã³": "ó",
        "Ã¡": "á",
        "Ã©": "é",
        "Ã\xad": "í",
        "PÃšBLICO": "PÚBLICO",
        "CONSTRUCCIÃ“N": "CONSTRUCCIÓN",
        "CONSULTORÃ\x8dA": "CONSULTORÍA",
        "EDUCACIÃ“N": "EDUCACIÓN",
        "FARMACÃ‰UTICO": "FARMACÉUTICO",
    }
    for bad, good in mappings.items():
        text = text.replace(bad, good)
    return text

def get_age_range(age_str):
    try:
        age = int(float(age_str))
        if age < 18: return "Menor 18"
        if age <= 25: return "18-25"
        if age <= 35: return "26-35"
        if age <= 45: return "36-45"
        if age <= 55: return "46-55"
        if age <= 65: return "56-65"
        return "65+"
    except: return "N/D"

def encrypt_data(plaintext, password):
    """Cifra los datos con AES-256 (CBC) usando PBKDF2"""
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # Retornar salt + iv + ciphertext en una sola cadena base64
    combined = salt + iv + ciphertext
    return base64.b64encode(combined).decode('utf-8')

def main():
    print("=" * 80)
    print("PROCESAMIENTO DE COBERTURA Y STORYTELLING")
    print("=" * 80)
    
    # 0. CARGAR MAPA DE CLUSTERS EMPRESARIALES
    print("\nCargando mapa de clusters empresariales...")
    cluster_map = {}  # {ID_EMPRESA: CLUSTER_EMPRESARIAL_GRUPO}
    
    try:
        # Intentar UTF-8 con BOM primero, luego Latin-1
        encodings = ['utf-8-sig', 'latin-1']
        header = None
        rows = []
        
        for enc in encodings:
            try:
                with open(EMPRESAS_SEGM_FILE, 'r', encoding=enc) as f:
                    reader = csv.reader(f, delimiter=';')
                    header = next(reader)
                    rows = list(reader)
                    print(f"  ✓ Leído con {enc}")
                    break
            except (UnicodeDecodeError, StopIteration):
                continue
        
        if header:
            # Encontrar índices
            id_emp_idx = header.index('ID_EMP_FILIAL') if 'ID_EMP_FILIAL' in header else 5
            cluster_idx = header.index('CLUSTER_EMPRESARIAL_GRUPO') if 'CLUSTER_EMPRESARIAL_GRUPO' in header else 43
            
            for row in rows:
                if len(row) > max(id_emp_idx, cluster_idx):
                    id_emp = row[id_emp_idx].strip()
                    cluster = clean_encoding(row[cluster_idx].strip()) or "General"
                    if id_emp:
                        cluster_map[id_emp] = cluster
        
        print(f"  ✓ Cargados {len(cluster_map):,} clusters empresariales")
    except Exception as e:
        print(f"  ⚠️  Error cargando clusters: {e}")
        print("  Continuando sin clusters...")
    
    # 1. MAPEAREMOS CONSUMIDORES ÚNICOS
    # key: ID_PERSONA -> { UE: set(Years) }
    consumidores = defaultdict(lambda: defaultdict(set))
    
    for ue in UES:
        path = os.path.join(CONSUMPTION_DIR, f"{ue}.csv")
        if not os.path.exists(path):
            print(f"⚠️  Archivo no encontrado: {ue}.csv")
            continue
            
        print(f"Leyendo consumos de {ue}...")
        try:
            with open(path, 'r', encoding='latin-1') as f:
                reader = csv.reader(f, delimiter=',')
                next(reader) # header
                for row in reader:
                    if len(row) < 3: continue
                    persona_id = row[1].strip() # Index 1: ID_PERSONA o NUMERO_IDENTIFICACION_AFILIADO
                    fecha = row[0].strip() # Index 0: FECHA
                    if persona_id and fecha:
                        # Normalizar ID: agregar CC si no lo tiene
                        if not persona_id.startswith('CC'):
                            persona_id = f"CC{persona_id}"
                        
                        year = fecha[:4]
                        if year in ["2024", "2025"]:
                            consumidores[persona_id][ue].add(year)
        except Exception as e:
            print(f"Error en {ue}: {e}")

    print(f"{len(consumidores):,} consumidores únicos mapeados.")

    # 2. PROCESAREMOS EL ARCHIVO GRANDE (1.2GB)
    # data: { Total, Segmentos, Consumos, NIT, etc. }
    empresas = defaultdict(lambda: {
        "Total": 0, "NIT": "", "Piramide": "", "Foco": "", "Cluster": "",
        "Segmentos": defaultdict(int),
        "Edades": defaultdict(int),
        "Salarios": defaultdict(int),
        "Categorias": defaultdict(int),
        "Consumos": defaultdict(lambda: defaultdict(int)) # [UE][Year_Segment]
    })

    # Benchmarks
    benchmarks = defaultdict(lambda: {
        "Total": 0,
        "Segmentos": defaultdict(int),
        "Edades": defaultdict(int),
        "Salarios": defaultdict(int),
        "Categorias": defaultdict(int),
        "Consumos": defaultdict(lambda: defaultdict(int))
    })

    print(f"Leyendo demografía: {DEMOGRAPHIC_FILE}")
    
    # Para el archivo de 1.2GB, leerlo línea a línea es vital
    # Intentamos detectar encoding rápidamente
    try:
        with open(DEMOGRAPHIC_FILE, 'r', encoding='utf-8-sig') as f:
            f.readline()
        final_enc = 'utf-8-sig'
    except UnicodeDecodeError:
        final_enc = 'latin-1'
    
    print(f"  Usando encoding: {final_enc}")
    
    try:
        with open(DEMOGRAPHIC_FILE, 'r', encoding=final_enc) as f:
            reader = csv.reader(f, delimiter=';')
            next(reader) # header
            
            line_count = 0
            for row in reader:
                line_count += 1
                if line_count % 500000 == 0:
                    print(f"  Procesados {line_count:,} registros...")

                if len(row) < 73: continue
                
                emp_name = clean_encoding(row[51].strip())
                if not emp_name: continue
                
                persona_id = row[0].strip() # Index 0: ID_PERSONA
                seg = clean_encoding(row[12].strip()) or "Otros" # Index 12: SEGMENTO_POBLACIONAL
                nit = row[26].strip() # Index 26: NIT
                id_empresa = row[25].strip() # Index 25: ID_EMPRESA
                rango_edad = clean_encoding(row[7].strip()) or "N/D"
                # Categoría y Salario
                categoria = clean_encoding(row[1].strip()) or "N/D"
                rango_salarial = clean_encoding(row[8].strip()) or "N/D"
                
                # Mapeo de valores de Salario (SMLV)
                # Basado en los rangos observados en los datos
                SALARY_MAP = {
                    "Entre 1 y 1.5 SMLV": 1.25,
                    "Entre 1.5 y 2 SMLV": 1.75,
                    "Entre 2 y 2.5 SMLV": 2.25,
                    "Entre 2.5 y 3 SMLV": 2.75,
                    "Entre 3 y 4 SMLV": 3.5,
                    "Entre 4 y 6 SMLV": 5.0,
                    "Entre 6 y 8 SMLV": 7.0,
                    "Entre 8 y 10 SMLV": 9.0,
                    "Entre 10 y 20 SMLV": 15.0,
                    "Entre 20 y 30 SMLV": 25.0,
                    "Menor al SMLV": 0.8,
                    "Mayor a 30 SMLV": 35.0
                }
                
                salary_value = SALARY_MAP.get(rango_salarial, 0)
                
                target = empresas[emp_name]
                if not target["NIT"]:
                    target["NIT"] = nit
                    target["Piramide"] = clean_encoding(row[69].strip())
                    target["Foco"] = row[72].strip()
                    # Obtener cluster del mapa
                    target["Cluster"] = cluster_map.get(id_empresa, "General")
                    # Inicializar acumuladores de salario
                    target["SalarySum"] = 0
                    target["SalaryCount"] = 0
                
                target["Total"] += 1
                target["Segmentos"][seg] += 1
                target["Edades"][rango_edad] += 1
                target["Salarios"][rango_salarial] += 1
                target["Categorias"][categoria] += 1
                
                if salary_value > 0:
                    target["SalarySum"] += salary_value
                    target["SalaryCount"] += 1
                
                # Benchmarking Groups
                groups = ["SISTEMA_TOTAL"]
                if target["Piramide"] == "1 Grandes": groups.append("BENCHMARK_GRANDES")
                if target["Foco"] == "X": groups.append("BENCHMARK_FOCO")
                
                # REFINADO: Solo incluir en benchmark de cluster si es pirámide Grandes o Medianas
                if target["Cluster"] and target["Piramide"] in ["1 Grandes", "2 Medianas"]:
                    groups.append(f"BENCHMARK_CLUSTER_{target['Cluster']}")

                for g in groups:
                    benchmarks[g]["Total"] += 1
                    benchmarks[g]["Segmentos"][seg] += 1
                    benchmarks[g]["Edades"][rango_edad] += 1
                    benchmarks[g]["Salarios"][rango_salarial] += 1
                    benchmarks[g]["Categorias"][categoria] += 1
                    
                    if "SalarySum" not in benchmarks[g]:
                        benchmarks[g]["SalarySum"] = 0
                        benchmarks[g]["SalaryCount"] = 0
                    
                    if salary_value > 0:
                        benchmarks[g]["SalarySum"] += salary_value
                        benchmarks[g]["SalaryCount"] += 1

                # Cruce de Consumos
                pers_cons = consumidores.get(persona_id)
                if pers_cons:
                    for ue, years in pers_cons.items():
                        for yr in years:
                            key = f"{yr}_{seg}"
                            target["Consumos"][ue][key] += 1
                            for g in groups:
                                benchmarks[g]["Consumos"][ue][key] += 1

    except Exception as e:
        print(f"Error en demografía: {e}")
        return

    # 3. GUARDAR RESULTADOS
    print("Guardando resultados...")
    
    # 3. LIMPIAR Y FORMATEAR
    empresas_clean = {}
    for emp, data in empresas.items():
        # Calcular segmento predominante
        top_seg = "N/A"
        if data["Segmentos"]:
            top_seg = max(data["Segmentos"].items(), key=lambda x: x[1])[0]

        # Calcular salario promedio
        avg_salary = 0
        if data.get("SalaryCount", 0) > 0:
            avg_salary = data["SalarySum"] / data["SalaryCount"]

        empresas_clean[emp] = {
            "NIT": data["NIT"],
            "Piramide": data["Piramide"],
            "Foco": data["Foco"],
            "Cluster": data["Cluster"],
            "Total": data["Total"],
            "SegmentoPredominante": top_seg,
            "SalarioPromedio": round(avg_salary, 2),
            "Segmentos": dict(data["Segmentos"]),
            "Edades": dict(data["Edades"]),
            "Salarios": dict(data["Salarios"]),
            "Categorias": dict(data["Categorias"]),
            "Consumos": {ue: dict(cons) for ue, cons in data["Consumos"].items()}
        }
    
    benchmarks_clean = {}
    for bench, data in benchmarks.items():
        avg_salary = 0
        if data.get("SalaryCount", 0) > 0:
            avg_salary = data["SalarySum"] / data["SalaryCount"]

        benchmarks_clean[bench] = {
            "Total": data["Total"],
            "SalarioPromedio": round(avg_salary, 2),
            "Segmentos": dict(data["Segmentos"]),
            "Edades": dict(data["Edades"]),
            "Salarios": dict(data["Salarios"]),
            "Categorias": dict(data["Categorias"]),
            "Consumos": {ue: dict(cons) for ue, cons in data["Consumos"].items()}
        }
    
    output_data = {
        "Empresas": empresas_clean,
        "Benchmarks": benchmarks_clean
    }
    
    # Asegurar que el directorio existe
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Cifrar los datos antes de guardar
    json_str = json.dumps(output_data, ensure_ascii=False)
    encrypted_payload = encrypt_data(json_str, PASSWORD_DASHBOARD)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("const datosFichaEncrypted = \"")
        f.write(encrypted_payload)
        f.write("\";")

    print(f"Proceso completado. Datos guardados en {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
