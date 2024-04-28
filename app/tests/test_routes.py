import pytest
from app import create_app, db
from app.models import CurrencyExchange

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_currency_rate_by_country(client):
    response = client.get('/currency/rate_by_country?country=USD')
    assert response.status_code == 200

    data = response.json()
    assert 'USD' in data
