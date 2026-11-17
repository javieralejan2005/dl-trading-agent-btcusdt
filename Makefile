# Atajos del proyecto.
# Requisitos: Python >= 3.11 y Node 22 LTS (o >= 24.12). Node 23 NO es compatible con jsdom/vitest.
.PHONY: help setup setup-backend setup-frontend test test-backend test-frontend lint lint-backend lint-frontend check-node dev-backend dev-frontend versions

PYTHON ?= python3.12
VENV   ?= .venv
PY     := $(VENV)/bin/python
NPM    ?= npm

help:
	@echo "make setup     -> crea .venv e instala dependencias backend + frontend"
	@echo "make test      -> pruebas backend (pytest) + frontend (vitest)"
	@echo "make lint      -> ruff + mypy en backend/, oxlint + eslint + vue-tsc en frontend/"
	@echo "make versions  -> actualiza la tabla de versiones del README"

setup: setup-backend setup-frontend
setup-backend:
	@test -x $(PY) || $(PYTHON) -m venv $(VENV)
	$(PY) -m pip install -q --upgrade pip
	$(PY) -m pip install -q -e "backend[dev]"
setup-frontend: check-node
	cd frontend && $(NPM) ci

check-node:
	@node -e 'const [M,m]=process.versions.node.split(".").map(Number); if(!((M===22&&m>=18)||(M===24&&m>=12)||M>24)){console.error("Node "+process.versions.node+" no es compatible. Usa Node 22 LTS (>=22.18) o >=24.12 (ver frontend/.nvmrc)."); process.exit(1)}'

test: test-backend test-frontend
test-backend:
	cd backend && ../$(PY) -m pytest
test-frontend: check-node
	cd frontend && $(NPM) test

lint: lint-backend lint-frontend
lint-backend:
	cd backend && ../$(PY) -m ruff check . && ../$(PY) -m ruff format --check . && ../$(PY) -m mypy
lint-frontend: check-node
	cd frontend && $(NPM) run lint:check && $(NPM) run type-check

dev-backend:
	cd backend && ../$(PY) -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
dev-frontend: check-node
	cd frontend && $(NPM) run dev

versions:
	$(PY) scripts/versions.py
