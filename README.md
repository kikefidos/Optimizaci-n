Optimizaci-n

.gitignore
Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

Entornos virtuales
venv/
env/
.venv/

Editor/IDE
.vscode/
.idea/
*.swp
*.swo

Variables de entorno
.env
.env.local

Datasets (opcional)
*.csv
*.xlsx
*.json
data/raw/
data/processed/

### 1. Clonación y Configuración:
```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/preprocesamiento-ciencia-datos.git
cd preprocesamiento-ciencia-datos

# Configura usuario
git config user.name "Tu Nombre"
git config user.email tu-email@ejemplo.com

# Crea y cambia a la rama feature
git checkout -b feature-preprocesamiento

# Crea el archivo preprocesamiento.py
touch src/preprocesamiento.py

# Añade los cambios
git add src/preprocesamiento.py

# Realiza el commit
git commit -m "feat: añade módulo de preprocesamiento con pipeline completo"

# Sube los cambios a GitHub
git push origin feature-preprocesamiento

git checkout main
git pull origin main
git branch -d feature-preprocesamiento
git push origin --delete feature-preprocesamiento

# Ver ramas
git branch


# Logs
*.log
