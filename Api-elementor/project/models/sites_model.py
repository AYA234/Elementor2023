from models.db_model import db

class Site(db.Model):
    __tablename__ = 'sites'
    site_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    site_name=db.Column(db.Text)
    site_description=db.Column(db.Text)


    def __init__(self, user_id):
        self.user_id = user_id
