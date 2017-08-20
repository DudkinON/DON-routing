import unittest

from settings import get_settings
from don.router.Router import Router


class Tests(unittest.TestCase):
    def test_get_controller(self):
        path = 'search'
        router = Router(path, get_settings())

        self.assertEqual(path, router.get_controller())
