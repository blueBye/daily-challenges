import unittest

from manager import UserManager
from mock_db import MockDatabase


class TestMockDatabase(unittest.TestCase):

    def setUp(self):
        self.mock_db = MockDatabase()
        self.user_manager = UserManager(self.mock_db)

    def test_insert(self):
        self.user_manager.add_user("sara", "sara@quera.org")
        result = self.mock_db.execute("SELECT email FROM users WHERE username = ?", ("sara",)).fetchone()
        self.assertEqual(result, ("sara@quera.org",))

    def test_select(self):
        self.mock_db.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("sara", "sara@quera.org"))
        result = self.user_manager.get_user("sara")
        self.assertEqual(result, ("sara@quera.org",))
