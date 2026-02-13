# 📊 Dashboard de Ficha Técnica Empresarial

## 🎯 Descripción

Este paquete contiene todo lo necesario para usar el **Dashboard de Ficha Técnica Empresarial** de forma independiente. Puedes compartir esta carpeta completa sin necesidad de incluir otros proyectos o dashboards.

---

## 📂 Contenido de la Carpeta

```
ficha_empresarial/
├── README.md                              ← Este archivo
├── dashboard/
│   └── index.html                         ← Dashboard (abrir en navegador)
├── datos/
│   └── datos_ficha_completa.js           ← Datos procesados (99MB)
├── scripts/
│   └── process_coverage_storytelling.py  ← Script para actualizar datos
└── documentacion/
    ├── README.md                          ← Guía de qué compartir
    ├── GUIA_USUARIO.md                    ← Manual de usuario
    └── README_TECNICO.md                  ← Documentación técnica
```

---

## 🚀 Inicio Rápido

### Para Usuarios Finales

1. **Abrir el dashboard:**
   - Navega a la carpeta `dashboard/`
   - Haz doble clic en `index.html`
   - Se abrirá en tu navegador

2. **Usar el dashboard:**
   - Espera 10-30 segundos mientras carga los datos
   - Busca una empresa en el buscador
   - Explora las métricas y gráficos

3. **Ayuda:**
   - Lee `documentacion/GUIA_USUARIO.md` para instrucciones detalladas

### Para Administradores (Actualizar Datos)

1. **Leer documentación técnica:**
   - Abre `documentacion/README_TECNICO.md`
   - Ve a la sección "Guía de Ejecución"

2. **Ejecutar script:**
   ```bash
   cd scripts/
   python process_coverage_storytelling.py
   ```

3. **El script generará:**
   - `datos/datos_ficha_completa.js` actualizado

---

## 📋 Requisitos

### Para Usar el Dashboard
- ✅ **Navegador moderno** (Chrome, Firefox, Edge, Safari)
- ✅ **Conexión a internet** (solo para cargar fuentes de Google)
- ❌ **NO requiere instalación**
- ❌ **NO requiere servidor web**

### Para Actualizar Datos (Solo Administradores)
- ✅ **Python 3.7+**
- ✅ **Acceso a archivos CSV fuente** (1.5GB total)
- ✅ **2-3 GB de RAM libre**

---

## 📚 Documentación

| Documento | Para Quién | Contenido |
|-----------|------------|-----------|
| **documentacion/GUIA_USUARIO.md** | 👤 Usuarios finales | Cómo usar el dashboard, interpretar métricas |
| **documentacion/README_TECNICO.md** | 💻 Desarrolladores | Arquitectura, scripts, estructura de datos |
| **documentacion/README.md** | 👥 Todos | Guía de qué compartir según perfil |

---

## 🔐 Consideraciones de Seguridad

### ⚠️ Datos Confidenciales

El archivo `datos/datos_ficha_completa.js` contiene **información sensible** de empresas y afiliados:

- ❌ **NO compartir por correo electrónico**
- ❌ **NO subir a repositorios públicos** (GitHub, GitLab)
- ✅ **Usar carpetas compartidas seguras** (OneDrive, SharePoint)
- ✅ **Limitar acceso solo a personal autorizado**

### ✅ Archivos Seguros

Estos archivos NO contienen datos sensibles y se pueden compartir:

- `dashboard/index.html` (solo código)
- `scripts/process_coverage_storytelling.py` (solo lógica)
- Toda la carpeta `documentacion/`

---

## 🎯 Casos de Uso

### 1. Compartir con Analista de Negocio

**Comparte:**
- ✅ Toda la carpeta `ficha_empresarial/`

**Instrucciones:**
- "Abre `dashboard/index.html` en tu navegador"
- "Lee `documentacion/GUIA_USUARIO.md` si tienes dudas"

---

### 2. Compartir con Administrador del Sistema

**Comparte:**
- ✅ Toda la carpeta `ficha_empresarial/`
- ✅ Acceso a archivos CSV fuente (ubicación externa)

**Instrucciones:**
- "Lee `documentacion/README_TECNICO.md` → Sección 'Guía de Ejecución'"
- "Ejecuta `scripts/process_coverage_storytelling.py` para actualizar datos"

---

### 3. Compartir con Desarrollador

**Comparte:**
- ✅ Toda la carpeta `ficha_empresarial/`
- ✅ Acceso a archivos CSV fuente
- ✅ `documentacion/README_TECNICO.md` completo

**Instrucciones:**
- "Lee toda la documentación técnica"
- "El código fuente está en `dashboard/index.html`"

---

## 🔧 Solución de Problemas

### El dashboard no carga

**Problema:** Pantalla en blanco o error

**Solución:**
1. Verifica que `datos/datos_ficha_completa.js` existe
2. Prueba con otro navegador
3. Abre la consola del navegador (F12) y busca errores

### No aparecen empresas

**Problema:** Buscador vacío

**Solución:**
1. Espera 30 segundos más (archivo grande)
2. Refresca la página (F5)
3. Verifica que el archivo de datos no esté corrupto

### Más ayuda

Consulta `documentacion/GUIA_USUARIO.md` → Sección "Solución de Problemas Comunes"

---

## 📊 Información del Sistema

| Métrica | Valor |
|---------|-------|
| **Total Empresas** | ~3,500 |
| **Total Afiliados** | ~1.6 millones |
| **Unidades de Negocio** | 5 (Vivienda, Hoteles, Piscilago, R&D, Medicamentos) |
| **Años de Datos** | 2024-2025 |
| **Tamaño de Datos** | 99 MB |

---

## 📞 Soporte

| Tipo de Consulta | Acción |
|------------------|--------|
| **Cómo usar el dashboard** | Lee `documentacion/GUIA_USUARIO.md` |
| **Cómo actualizar datos** | Lee `documentacion/README_TECNICO.md` |
| **Problemas técnicos** | Contacta al equipo de desarrollo |
| **Preguntas sobre datos** | Contacta al área de Analítica |

---

## 📝 Notas Importantes

1. **Actualización de Datos:**
   - Los datos NO se actualizan automáticamente
   - Requiere ejecutar el script Python manualmente
   - Frecuencia recomendada: Mensual

2. **Compatibilidad:**
   - Funciona en Windows, Mac y Linux
   - Requiere navegador moderno (últimas 2 versiones)

3. **Rendimiento:**
   - Primera carga: 10-30 segundos
   - Cargas posteriores: Más rápido (caché del navegador)

---

**Versión:** 1.0  
**Última Actualización:** 2026-02-10  
**Mantenido por:** Equipo de Desarrollo - Colsubsidio

---

## 🎁 Ventajas de Este Paquete

✅ **Autocontenido:** Todo en una sola carpeta  
✅ **Portable:** Copia y comparte fácilmente  
✅ **Independiente:** No requiere otros proyectos  
✅ **Documentado:** Guías para todos los perfiles  
✅ **Seguro:** Instrucciones claras sobre qué compartir
