# Guía de Despliegue: Dashboard Corporativo

Este repositorio contiene el Dashboard de Ficha Técnica Empresarial con un sistema de **cifrado de grado militar (AES-256)** para proteger los datos sensibles en entornos públicos.

## 🛡️ Seguridad de Datos
Los archivos en la carpeta `datos/` están cifrados. Aunque el repositorio sea público, nadie podrá leer la información de las empresas sin la clave de acceso.

**Clave de Acceso:** `Bi2026_*`

---

## 🚀 Pasos para Subir a GitHub

1.  **Crear el Repositorio**: En GitHub, crea un nuevo repositorio (puede ser público).
2.  **Subir Archivos**: Sube todo el contenido de la carpeta `ficha_empresarial` (excepto los archivos ignorados por `.gitignore`).
3.  **Activar GitHub Pages**:
    *   Ve a **Settings** > **Pages**.
    *   En "Build and deployment", selecciona la rama `main` y la carpeta `/(root)`.
    *   GitHub te dará una URL (ej: `https://usuario.github.io/proyecto/dashboard/index.html`).

---

## 🏢 Cómo Embeber en SharePoint

Para que el dashboard aparezca dentro de una página de SharePoint:

1.  Copia la URL que te dio GitHub Pages.
2.  En SharePoint, edita la página donde quieras poner el dashboard.
3.  Agrega un web part de **"Inserción" (Embed)**.
4.  Pega el siguiente código, cambiando la URL por la tuya:

```html
<iframe src="TU_URL_DE_GITHUB_AQUI" width="100%" height="800px" style="border:none;"></iframe>
```

---

## 🛠️ Actualización de Datos
Cada vez que necesites actualizar los datos:
1.  Ejecuta el script `scripts/process_coverage_storytelling.py` en tu máquina local.
2.  El script generará automáticamente el archivo JS cifrado en `datos/`.
3.  Sube ese nuevo archivo JS a GitHub y el dashboard se actualizará automáticamente en SharePoint.
