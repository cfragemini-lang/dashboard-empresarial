# Guía de Despliegue: Dashboard Corporativo

Este repositorio está configurado para actualizar automáticamente el dashboard en SharePoint cada vez que realices cambios.

## � Link Público (SharePoint)
**URL Actual:** [https://cfragemini-lang.github.io/dashboard-empresarial/dashboard/index.html](https://cfragemini-lang.github.io/dashboard-empresarial/dashboard/index.html)

---

## 🚀 Flujo de Actualización (Lo que debes hacer)

Si realizas cambios en los datos o en el diseño localmente, sigue estos **3 pasos**:

1.  **Actualizar Datos**: Ejecuta el script de procesamiento:
    ```bash
    python scripts/process_coverage_storytelling.py
    ```
2.  **Preparar Cambios**: Registra los cambios en Git:
    ```bash
    git add .
    git commit -m "Actualización de datos (Fecha Actual)"
    ```
3.  **Subir a la Web**: Envía los cambios a GitHub (esto actualiza el link de SharePoint):
    ```bash
    git push origin main
    ```

---

## ⚠️ Notas Importantes
- **Caché**: Si subes cambios y no los ves de inmediato en SharePoint, presiona **CTRL + F5** en tu navegador.
- **Rama Principal**: Todo se maneja ahora en la rama `main`. La rama `master` ha sido eliminada para evitar confusiones.
- **Datos Pesados**: El archivo de datos (`datos_ficha_v2.js`) es grande (89MB). Al hacer el push, es normal que tome unos segundos adicionales.
