from app import db


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stockname = db.Column(db.String(50), index=True, unique=True)
    place = db.Column(db.String(50), index=True)
    hostname = db.Column(db.String(50), index=True)
    content = db.Column(db.String(200))
    contact = db.Column(db.String(50))
    capacity = db.Column(db.String(50))

    def __repr__(self):
        return '<Stock {}>'.format(self.stockname)