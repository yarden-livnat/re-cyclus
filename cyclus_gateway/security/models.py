import datetime as dt
import uuid

from .utils import bcrypt
from cyclus_gateway.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    roles = db.Column(db.String(120), nullable=False, default='User')
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.now)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email, password=None, **kwargs):
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def verify_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)


class Token(db.Model):
    __tablename__ = 'blacklist'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    token_type = db.Column(db.String(10), nullable=False)
    user_identity = db.Column(db.String(50), nullable=False)
    revoked = db.Column(db.Boolean, nullable=False)
    expires = db.Column(db.DateTime, nullable=False)
