from fastapi.testclient import TestClient

from app.main import create_app


def test_salud_responde_ok_y_modo_paper() -> None:
    cliente = TestClient(create_app())
    r = cliente.get("/api/salud")
    assert r.status_code == 200
    cuerpo = r.json()
    assert cuerpo["estado"] == "ok"
    assert cuerpo["modo"] == "PAPER"
