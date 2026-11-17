# Atajos del proyecto. Claude Code completará los objetivos conforme avance el plan.
.PHONY: help test lint versions
help:
	@echo "make test      -> pruebas backend + frontend"
	@echo "make lint      -> linters backend + frontend"
	@echo "make versions  -> actualiza la tabla de versiones del README"

test:
	@echo "TODO (Fase 1): pytest en backend/ y vitest en frontend/"
lint:
	@echo "TODO (Fase 1): ruff + mypy en backend/, eslint + vue-tsc en frontend/"
versions:
	python scripts/versions.py
