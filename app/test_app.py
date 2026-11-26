from app import app

def test_health():
    res = app.test_client().get("/health")
    assert res.status_code == 200
