from app import db

class CurrencyExchange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rate = db.Column(db.Numeric, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
