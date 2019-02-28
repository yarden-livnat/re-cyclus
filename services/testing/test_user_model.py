import unittest
import datetime

from recyclus_gateway import db
from recyclus_gateway.security.models import User
from testing.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            username="test",
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        # auth_token = user.encode_auth_token(user.id)
        # self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = User(
            username='test',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        # auth_token = user.encode_auth_token(user.id)
        # self.assertTrue(isinstance(auth_token, bytes))
        # self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8") ) == 1)
