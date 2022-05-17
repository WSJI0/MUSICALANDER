from server import db

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.String(32), nullable=False)
    user_pw=db.Column(db.String(32), nullable=False)
    user_email=db.Column(db.String(32), nullable=False)
    user_name=db.Column(db.String(32), nullable=False)
    user_state=db.Column(db.Integer, nullable=False)
    
class Sessions(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.String(32), nullable=False)
    user_session=db.Column(db.String(32), nullable=False)