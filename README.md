# Horarios

Web con tu horario de clases (SMX) y tu horario de trabajo.

```
horarios-app/
├─ index.html              La web (horario de clases editable en la sección DATOS)
├─ horarios/               Aquí pones trabajo.pdf (o .png/.jpg)
├─ sync.py                 Sube los cambios de horarios/ a GitHub (una vez)
├─ SUBIR (...)             Doble clic para ejecutar sync.py
└─ .github/workflows/      Publica la web en GitHub Pages en cada push
```

## Puesta en marcha (una sola vez)

1. Crea un repositorio vacío en GitHub (por ejemplo `horarios`).
2. En esta carpeta:
   ```
   git init -b main
   git add .
   git commit -m "Primera versión"
   git remote add origin https://github.com/TU_USUARIO/horarios.git
   git push -u origin main
   ```
3. En GitHub: Settings → Pages → Source: **GitHub Actions**.
4. Tu web quedará en `https://TU_USUARIO.github.io/horarios/`.

Para que `push` no pida contraseña, inicia sesión con GitHub CLI (`gh auth login`)
o usa un token / clave SSH.

## Uso diario

1. Copia tu horario en la carpeta `horarios/` con el nombre `trabajo.pdf` (o .png/.jpg).
2. Haz **doble clic** en el archivo de subida de tu sistema:
   - Windows: `SUBIR (Windows).bat`
   - Mac: `SUBIR (Mac).command`
   - Linux: `SUBIR (Linux).sh`

Solo se sube cuando tú lo haces. También puedes ejecutar `python sync.py` en la terminal.

## Notas

- Ya no hay contraseña ni panel de administrador: quien pueda subir a tu
  repositorio es quien administra el horario.
- Si el repositorio es público, el PDF también lo es. Para un repo privado,
  GitHub Pages requiere un plan de pago.
- Para ver la web en local usa `python -m http.server` y abre http://localhost:8000
