# 📁 Documentación del Proyecto - Dashboard Ficha Técnica Empresarial

## 🎯 Propósito de esta Carpeta

Esta carpeta contiene toda la documentación del proyecto organizada por tipo de usuario. Comparte solo lo necesario según a quién se lo envíes.

---

## 📂 Estructura de Carpetas

```
Documentacion/
├── README.md                    ← Estás aquí
├── Usuario/                     ← Para usuarios finales
│   └── GUIA_USUARIO.md         ← Cómo usar el dashboard
└── Tecnica/                     ← Para desarrolladores/técnicos
    └── README_TECNICO.md       ← Arquitectura y scripts Python
```

---

## 👥 ¿Qué Compartir Según el Perfil?

### 🟢 Usuario Final (Analista de Negocio)

**Necesita saber:** Cómo usar el dashboard, interpretar métricas, solucionar problemas básicos

**Comparte:**
- ✅ `Usuario/GUIA_USUARIO.md`
- ✅ El archivo `dashboard_ficha_tecnica.html`
- ✅ Acceso a la carpeta `Datos/` (con `datos_ficha_completa.js`)

**NO compartas:**
- ❌ `Tecnica/` (demasiado técnico)
- ❌ Scripts de Python
- ❌ Archivos CSV fuente

---

### 🟡 Administrador del Sistema

**Necesita saber:** Cómo actualizar los datos, ejecutar scripts, mantener el sistema

**Comparte:**
- ✅ `Usuario/GUIA_USUARIO.md` (para entender el dashboard)
- ✅ `Tecnica/README_TECNICO.md` (secciones: "Scripts de Python", "Guía de Ejecución")
- ✅ Carpeta `Scripts/Procesamiento/`
- ✅ Acceso a archivos CSV fuente

**Opcional:**
- ⚠️ Sección completa de "Flujo de Datos (ETL)" si necesita entender el proceso

---

### 🔴 Desarrollador / Técnico

**Necesita saber:** Arquitectura completa, estructura de datos, cómo modificar/extender el sistema

**Comparte:**
- ✅ **TODO** en `Tecnica/README_TECNICO.md`
- ✅ Carpeta `Scripts/` completa
- ✅ Carpeta `Dashboards/` completa
- ✅ Estructura de datos (`Datos/`)
- ✅ Acceso a archivos CSV fuente (si va a reprocesar)

---

## 📋 Resumen de Archivos

| Archivo | Audiencia | Contenido |
|---------|-----------|-----------|
| **Usuario/GUIA_USUARIO.md** | 👤 Usuario Final | Cómo usar el dashboard, interpretar métricas, troubleshooting básico |
| **Tecnica/README_TECNICO.md** | 💻 Desarrollador | Arquitectura, ETL, scripts Python, estructura de datos, cruces |

---

## 🚀 Inicio Rápido por Perfil

### Para Usuario Final

1. Lee `Usuario/GUIA_USUARIO.md`
2. Abre `Dashboards/dashboard_ficha_tecnica.html`
3. ¡Listo para analizar empresas!

### Para Administrador

1. Lee `Usuario/GUIA_USUARIO.md` (entender el dashboard)
2. Lee `Tecnica/README_TECNICO.md` → Sección "Guía de Ejecución"
3. Ejecuta `Scripts/Procesamiento/process_coverage_storytelling.py` cuando necesites actualizar datos

### Para Desarrollador

1. Lee **TODO** `Tecnica/README_TECNICO.md`
2. Revisa los scripts en `Scripts/Procesamiento/`
3. Analiza el código del dashboard en `Dashboards/dashboard_ficha_tecnica.html`
4. Consulta la sección "Estructura de Datos" para entender el JSON

---

## 📊 Archivos del Proyecto (Referencia)

### Carpetas Principales

```
Proy_65/
├── Dashboards/
│   └── dashboard_ficha_tecnica.html    ← Frontend (52KB)
├── Datos/
│   └── datos_ficha_completa.js         ← Datos procesados (99MB)
├── Scripts/
│   └── Procesamiento/
│       └── process_coverage_storytelling.py  ← Script principal ETL
└── Documentacion/                       ← Esta carpeta
```

### Archivos Externos (No en el proyecto)

```
C:\Users\crisrojagu\Documents\Cruces_col\Cruces_col\data\
├── COLSUBSIDIO_LT_CV_IDN_CONSOLIDACION_FINAL_SEGM.csv  (1.2GB)
└── COLSUBSIDIO_LT_CV_IDN_LIST_EMPRESAS_SEGM.csv        (30MB)

C:\Users\crisrojagu\Documents\Consumos\data\
├── VIVIENDA.csv
├── HOTELES.csv
├── PISCILAGO.csv
├── RYD.csv
└── MEDICAMENTOS.csv
```

---

## 🔐 Consideraciones de Seguridad

### Datos Sensibles

Los siguientes archivos contienen **información confidencial** de empresas y afiliados:

- ❗ `datos_ficha_completa.js` (99MB)
- ❗ Todos los archivos CSV fuente
- ❗ Archivos JSON intermedios en `Datos/`

**Recomendaciones:**
- No compartir por correo electrónico
- Usar carpetas compartidas seguras (OneDrive, SharePoint)
- Limitar acceso solo a personal autorizado
- No subir a repositorios públicos (GitHub, GitLab)

### Archivos Seguros para Compartir

Estos archivos NO contienen datos sensibles:

- ✅ `dashboard_ficha_tecnica.html` (solo código)
- ✅ Scripts Python (solo lógica de procesamiento)
- ✅ Toda la carpeta `Documentacion/`

---

## 📞 Contacto y Soporte

| Tipo de Consulta | Contacto |
|------------------|----------|
| **Uso del dashboard** | Equipo de Analítica |
| **Problemas técnicos** | Equipo de Desarrollo |
| **Actualización de datos** | Administrador del Sistema |
| **Modificaciones al código** | Desarrollador Principal |

---

## 📝 Historial de Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2026-02-10 | Versión inicial con documentación completa |

---

**Mantenido por:** Equipo de Desarrollo - Colsubsidio  
**Última Actualización:** 2026-02-10
