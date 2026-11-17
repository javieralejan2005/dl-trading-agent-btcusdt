#!/usr/bin/env python3
"""Genera la tabla de 'Tecnologías y versiones' del README con las versiones REALMENTE instaladas.

Uso:  python scripts/versions.py
Reemplaza lo que haya entre <!-- VERSIONES:START --> y <!-- VERSIONES:END --> en README.md.
Si una tecnología no está instalada, aparece como 'no instalado' (no se inventan versiones).
"""
import json, shutil, subprocess, sys
from importlib import metadata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PY = [  # (paquete pip, para qué se usa)
    ("fastapi", "API del backend"), ("uvicorn", "Servidor ASGI"), ("pydantic", "Validación de datos y JSON del LLM"),
    ("sqlalchemy", "Persistencia (SQLite)"), ("apscheduler", "Ciclo programado"), ("httpx", "Cliente HTTP (MEXC, Ollama)"),
    ("tensorflow", "Modelo predictivo (Keras)"), ("scikit-learn", "Escaladores / regresión lineal"), ("numpy", "Cálculo numérico"),
    ("pandas", "Datos"), ("pytest", "Pruebas backend"), ("ruff", "Linter Python"), ("mypy", "Tipado estático Python"),
]
NODE = [  # (paquete npm, para qué se usa)
    ("vue", "Interfaz (Vue 3)"), ("typescript", "Tipado del frontend"), ("vite", "Build y servidor de desarrollo"),
    ("pinia", "Estado de la UI"), ("vitest", "Pruebas frontend"), ("eslint", "Linter JS/TS"), ("vue-tsc", "Chequeo de tipos Vue"),
]

def cmd(args):
    exe = shutil.which(args[0])
    if not exe:
        return None
    try:
        r = subprocess.run([exe, *args[1:]], capture_output=True, text=True, timeout=20)
        return (r.stdout or r.stderr).strip().splitlines()[0] if (r.stdout or r.stderr) else None
    except (subprocess.SubprocessError, OSError):
        return None

def pip_ver(n):
    try: return metadata.version(n)
    except metadata.PackageNotFoundError: return None

def npm_ver(n):
    p = RAIZ / "frontend" / "node_modules" / n / "package.json"
    try: return json.loads(p.read_text(encoding="utf-8")).get("version")
    except (OSError, ValueError): return None

filas = [("Python", sys.version.split()[0], "Lenguaje del backend"),
         ("Node.js", (cmd(["node", "-v"]) or "").lstrip("v") or None, "Entorno del frontend"),
         ("Ollama", (cmd(["ollama", "--version"]) or "").split()[-1] if cmd(["ollama", "--version"]) else None, "LLM local")]
filas += [(n, pip_ver(n), d) for n, d in PY] + [(n, npm_ver(n), d) for n, d in NODE]

tabla = ["| Tecnología | Versión | Uso |", "|---|---|---|"]
tabla += [f"| {n} | {v or 'no instalado'} | {d} |" for n, v, d in filas]
bloque = "<!-- VERSIONES:START -->\n" + "\n".join(tabla) + "\n\n_Generado con `scripts/versions.py`._\n<!-- VERSIONES:END -->"

readme = RAIZ / "README.md"
txt = readme.read_text(encoding="utf-8")
a, b = txt.find("<!-- VERSIONES:START -->"), txt.find("<!-- VERSIONES:END -->")
if a == -1 or b == -1:
    sys.exit("No encontré los marcadores VERSIONES en README.md")
readme.write_text(txt[:a] + bloque + txt[b + len("<!-- VERSIONES:END -->"):], encoding="utf-8")
print("README.md actualizado con", len(filas), "tecnologías.")
