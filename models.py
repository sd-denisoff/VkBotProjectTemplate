from flask_login import UserMixin

from app import db, login_manager


class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    vk_id = db.Column(db.Integer, primary_key=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=str(user_id)).first()
