from api.views import *
from . import BaseTestCase, app

class ViewTest(BaseTestCase):
    def test_dumb(self):
        self.app.get('/')
        assert True
