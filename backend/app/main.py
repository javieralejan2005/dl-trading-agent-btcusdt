"""Punto de entrada de la API FastAPI.

Modo único: PAPER. Este backend no contiene ninguna ruta ni cliente de órdenes reales.
"""

from fastapi import FastAPI

from app import __version__

MODO = "PAPER"


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI."""
    app = FastAPI(title="Agente BTC/USDT (Paper)", version=__version__)

    @app.get("/api/salud")
    def salud() -> dict[str, str]:
        """Comprobación de vida pública (no expone datos sensibles)."""
        return {"estado": "ok", "modo": MODO, "version": __version__}

    return app


app = create_app()
