from flask import Blueprint, request, jsonify
from app import db
from app.models import CurrencyExchange
from app.config import Config
import requests

api = Blueprint('api', __name__)

@api.route('/currency/rate_by_country', methods=['GET'])
def get_currency_rate_by_country():
    country = request.args.get('country')
    currency_exchange = CurrencyExchange.query.filter_by(country=country).first()
    if currency_exchange:
        return jsonify({currency_exchange.currency: currency_exchange.rate})
    else:
        return "Country not found", 404

@api.route('/fetch_and_store_exchange_data', methods=['GET'])
def fetch_and_store_exchange_data():
    url = f"https://api.exchangerate-api.com/v4/latest/USD"
    headers = {"X-RapidAPI-Key": Config.API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        rates = data['rates']
        for currency, rate in rates.items():
            currency_exchange = CurrencyExchange(currency=currency, country="", rate=rate)
            db.session.add(currency_exchange)
        db.session.commit()
        return "Data stored successfully"
    else:
        return "Failed to fetch data from API", 500

# Endpoint to fetch currency rate by currency code
@app.route('/currency/rate_by_currency', methods=['GET'])
def get_currency_rate_by_currency():
    currency = request.args.get('currency')
    cur.execute("SELECT rate FROM currency_exchange WHERE currency = %s", (currency,))
    rate = cur.fetchone()
    if rate:
        return jsonify({currency: rate[0]})
    else:
        return "Currency not found", 404

# Endpoint to fetch highest currency of the day
@app.route('/currency/highest_of_day', methods=['GET'])
def get_highest_currency_of_day():
    cur.execute("SELECT currency, rate FROM currency_exchange WHERE created_at::date = CURRENT_DATE ORDER BY rate DESC LIMIT 1")
    highest_currency = cur.fetchone()
    if highest_currency:
        return jsonify({highest_currency[0]: highest_currency[1]})
    else:
        return "No data available", 404

# Endpoint to fetch lowest currency of the day
@app.route('/currency/lowest_of_day', methods=['GET'])
def get_lowest_currency_of_day():
    cur.execute("SELECT currency, rate FROM currency_exchange WHERE created_at::date = CURRENT_DATE ORDER BY rate ASC LIMIT 1")
    lowest_currency = cur.fetchone()
    if lowest_currency:
        return jsonify({lowest_currency[0]: lowest_currency[1]})
    else:
        return "No data available", 404

# Endpoint to fetch history of a particular currency
@app.route('/currency/history', methods=['GET'])
def get_currency_history():
    currency = request.args.get('currency')
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=365)
    cur.execute("SELECT created_at, rate FROM currency_exchange WHERE currency = %s AND created_at BETWEEN %s AND %s",
                (currency, start_date, end_date))
    history = cur.fetchall()
    if history:
        return jsonify({entry[0].strftime('%Y-%m-%d'): entry[1] for entry in history})
    else:
        return "Currency not found or no history available", 404
