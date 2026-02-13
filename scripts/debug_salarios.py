import json
import os

JS_FILE = r"C:\Users\crisrojagu\Documents\Proy_65\ficha_empresarial\datos\datos_ficha_completa.js"
SMLV_2025 = 1430000

def main():
    if not os.path.exists(JS_FILE):
        print(f"Error: No se encuentra el archivo {JS_FILE}")
        return

    print("Leyendo datos...")
    with open(JS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extraer el JSON (quitar 'const ... =' y ';')
    json_str = content.split('=', 1)[1].strip()
    if json_str.endswith(';'):
        json_str = json_str[:-1]
        
    data = json.loads(json_str)
    benchmarks = data.get("Benchmarks", {})
    
    print("\n" + "="*80)
    print(f"{'BENCHMARK':<40} | {'SMMLV':<10} | {'VALOR PESOS':<20}")
    print("-" * 80)
    
    # Grupos principales
    main_groups = ["BENCHMARK_FOCO", "BENCHMARK_GRANDES", "SISTEMA_TOTAL"]
    for group in main_groups:
        if group in benchmarks:
            val = benchmarks[group].get("SalarioPromedio", 0)
            pesos = val * SMLV_2025
            label = group.replace("BENCHMARK_", "").replace("_", " ")
            print(f"{label:<40} | {val:<10.2f} | ${pesos:,.0f}".replace(",", "."))
            
    print("-" * 80)
    print("RESUMEN SECTORES (CLUSTERS):")
    
    # Clusters
    clusters = sorted([k for k in benchmarks.keys() if k.startswith("BENCHMARK_CLUSTER_")])
    for c in clusters:
        val = benchmarks[c].get("SalarioPromedio", 0)
        pesos = val * SMLV_2025
        label = c.replace("BENCHMARK_CLUSTER_", "").replace("_", " ")
        print(f"{label:<40} | {val:<10.2f} | ${pesos:,.0f}".replace(",", "."))
        
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
