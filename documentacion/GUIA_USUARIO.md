# 📊 Guía de Usuario: Dashboard de Ficha Técnica Empresarial

## 🎯 ¿Qué es este Dashboard?

El Dashboard de Ficha Técnica Empresarial te permite analizar el perfil demográfico y los consumos de empresas afiliadas a Colsubsidio. Puedes ver:

- **Perfil de la empresa**: Total de afiliados, segmentación, categorías
- **Cobertura de consumos**: Cuántos afiliados usan cada servicio (Vivienda, Hoteles, etc.)
- **Comparación con benchmarks**: Cómo se compara tu empresa con otras similares
- **Indicadores clave**: Índice de Salud, Concentración de segmentos

---

## 🚀 Cómo Usar el Dashboard

### Paso 1: Abrir el Dashboard

1. Navega a la carpeta: `Proy_65/Dashboards/`
2. Haz doble clic en `dashboard_ficha_tecnica.html`
3. Se abrirá en tu navegador predeterminado
4. **Espera 10-30 segundos** mientras carga los datos (archivo de 99MB)

### Paso 2: Buscar una Empresa

1. En la parte superior verás un **buscador**
2. Escribe el nombre de la empresa (ej: "ECOPETROL")
3. Selecciona la empresa de la lista desplegable
4. El dashboard se actualizará automáticamente

### Paso 3: Interpretar las Métricas

#### 📈 Tarjetas de Métricas Clave

| Métrica | Qué Significa |
|---------|---------------|
| **Total Afiliados** | Número total de personas afiliadas a la empresa |
| **Segmento Predominante** | El segmento poblacional con más afiliados |
| **Categoría Predominante** | La categoría socioeconómica más común (A, B, C, D) |
| **Índice de Salud Sistémico** | Qué tan bien la empresa usa los servicios (0-100%) |
| **Coeficiente de Concentración** | Qué tan concentrada está la empresa en pocos segmentos |

#### 🏢 Resumen por Unidad de Negocio

Verás 4 tarjetas pequeñas (VIVIENDA, HOTELES, PISCILAGO, RYD) que muestran:
- **Consumos 2024 vs 2025**: Cuántos afiliados consumieron cada año
- **Variación %**: Si aumentó (▲) o disminuyó (▼)
- **Cobertura 2025**: Porcentaje de afiliados que consumieron

### Paso 4: Analizar por Unidad de Negocio

1. **Cambiar de UE**: Haz clic en los tabs (Vivienda, Hoteles, Piscilago, R&D)
2. **Filtrar segmentos**: 
   - Por defecto muestra todos los segmentos
   - Haz clic en el botón "Ver todos los segmentos" para cambiar a "Top 2"
   - Esto mostrará solo los 2 segmentos más importantes

#### 📊 Tarjetas de Segmentos

Cada segmento muestra:
- **Nombre del segmento** (ej: "Medio")
- **Total de afiliados** en ese segmento
- **Consumos 2024 y 2025**
- **Cobertura %**: Qué porcentaje del segmento consumió
- **Variación**: Si aumentó o disminuyó vs 2024
- **Comparación con benchmarks**: Cómo se compara con Grandes, Foco y Cluster

**Interpretación de colores:**
- 🟢 **Verde**: La empresa está por encima del benchmark
- 🔴 **Rojo**: La empresa está por debajo del benchmark
- ⚪ **Gris**: Igual o sin datos

### Paso 5: Gráfico Radar Competitivo

Al final de cada UE verás un **gráfico radar** (tipo telaraña):

- **Línea azul oscura gruesa**: Tu empresa
- **Línea gris**: Promedio de empresas Grandes
- **Línea amarilla**: Promedio de empresas Foco
- **Línea azul claro**: Promedio del Cluster de tu empresa

**Cómo leerlo:**
- Si tu línea azul está **más afuera** que las demás en un segmento → Estás ganando
- Si está **más adentro** → Tienes oportunidad de mejora
- Pasa el cursor sobre los puntos para ver el porcentaje exacto

### Paso 6: Ver Metodología

1. Haz clic en el botón **"❓ Metodología"** (arriba a la derecha)
2. Se abrirá un modal con las fórmulas de todos los indicadores
3. Cierra haciendo clic en la "X" o fuera del modal

---

## 💡 Consejos de Uso

### ✅ Buenas Prácticas

- **Compara siempre con benchmarks**: No solo veas tus números, compáralos con empresas similares
- **Analiza tendencias**: Fíjate si la variación 2024→2025 es positiva o negativa
- **Usa el filtro Top 2**: Para enfocarte en los segmentos más importantes
- **Revisa todas las UEs**: Cada unidad de negocio puede tener patrones diferentes

### ⚠️ Limitaciones

- **Datos históricos**: Solo muestra 2024 y 2025
- **Actualización**: Los datos no se actualizan en tiempo real (requiere reprocesar)
- **Navegador**: Funciona mejor en Chrome, Firefox o Edge (evitar Internet Explorer)

---

## 🔧 Solución de Problemas Comunes

### El dashboard no carga

**Problema:** Pantalla en blanco o mensaje de error

**Solución:**
1. Verifica que el archivo `datos_ficha_completa.js` existe en la carpeta `Datos/`
2. Prueba con otro navegador
3. Abre la consola del navegador (F12) y busca errores en rojo

### No aparecen empresas en el buscador

**Problema:** El buscador está vacío

**Solución:**
1. Espera 30 segundos más (el archivo es grande)
2. Refresca la página (F5)
3. Verifica que el archivo de datos no esté corrupto

### El gráfico radar se ve muy pequeño

**Problema:** Todos los valores están en el centro

**Solución:**
- Esto es normal si los porcentajes de cobertura son bajos (5-10%)
- El gráfico ajusta la escala automáticamente
- Usa el hover para ver los valores exactos

### Los números no coinciden con mis reportes

**Problema:** Diferencias en las cifras

**Solución:**
1. Verifica la fecha de actualización de los datos
2. Revisa que estés viendo la misma UE
3. Confirma que los filtros (Top 2 vs Todos) sean los mismos

---

## 📞 Soporte

Si tienes problemas técnicos o preguntas sobre los datos:

1. **Problemas técnicos del dashboard**: Contacta al equipo de desarrollo
2. **Preguntas sobre datos**: Contacta al área de Analítica
3. **Solicitud de actualización de datos**: Contacta al administrador del sistema

---

## 📝 Glosario

| Término | Definición |
|---------|------------|
| **Afiliado** | Persona vinculada a una empresa en Colsubsidio |
| **Benchmark** | Grupo de referencia para comparación |
| **Cluster** | Agrupación de empresas por sector (PÚBLICO, CONSTRUCCIÓN, etc.) |
| **Cobertura** | Porcentaje de afiliados que consumieron un servicio |
| **Foco** | Empresas estratégicas marcadas como prioritarias |
| **Grandes** | Empresas con más de X afiliados (pirámide "1 Grandes") |
| **Segmento** | Clasificación poblacional (Básico, Medio, Joven, Alto, etc.) |
| **UE** | Unidad de Negocio (Vivienda, Hoteles, Piscilago, R&D) |

---

**Versión:** 1.0  
**Última Actualización:** 2026-02-10
