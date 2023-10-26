import unittest
from source import Account, Site, welcome, change_password


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = Account("Ali_Babaei", "5Dj:xKBA", "0030376459", "09121212121", "SAliB_SAliB@gmail.com")
        self.account2 = Account("salib_alibabaeeiiii", "5Dj:ppQ4", "0030376459", "09129163011", "XXA_12B@gmail.com")

    def test_init(self):
        self.assertEqual(self.account1.username, "Ali_Babaei")
        self.assertIn('_', self.account1.username)
        self.assertEqual(self.account1.username.count('_'), 1)
        self.assertEqual(self.account1.password, 'aca87bf6767f2dbb19d1d5b5d01e3d07eab8ea0f16741bd70e7c0784f0b3916d')
        self.assertEqual(self.account1.user_id, '0030376459')
        self.assertEqual(self.account1.phone, '09121212121')
        self.assertEqual(self.account1.email, 'SAliB_SAliB@gmail.com')

    def test_welcome_short(self):
        self.assertEqual(welcome(self.account1), 'welcome to our site Ali Babaei')

    def test_welcome_long(self):
        self.assertEqual(self.account2.username, 'salib_alibabaeeiiii')
        self.assertEqual(welcome(self.account2), 'welcome to our site Salib Alibabaee...')

    def test_change_password_fail_wrong(self):
        self.assertEqual(change_password(self.account1, 'abcdABCD123', 'newPasswo0rd'), None)

    def test_change_password_fail_invalid(self):
        with self.assertRaises(Exception) as e:
            change_password(self.account1, '5Dj:xKBA', 'newPassword')
        self.assertTrue("invalid password" in str(e.exception))

    def test_change_password_success(self):
        self.assertEqual(change_password(
            self.account1, '5Dj:xKBA', 'newPassw0rd'), 
            'your password is changed successfully.')


class TestSite(unittest.TestCase):
    def setUp(self):
        self.site1 = Site("salib.net")
        self.account1 = Account("Ali_Babaei", "5Dj:xKBA", "0030376459", "09121212121", "SAliB_SAliB@gmail.com")
        self.account2 = Account("Babk_Dadaei", "123ASsdz", "0030376459", "09134112121", "Batol_12@godzilla.com")

    def test_init_site(self):
        self.assertEqual(self.site1.url, "salib.net")
        self.assertListEqual(self.site1.register_users, [])
        self.assertListEqual(self.site1.active_users, [])

    def test_register_success(self):
        self.assertEqual(self.site1.register(self.account1), "register successful")

    def test_register_fail(self):
        self.assertEqual(self.site1.register(self.account2), "register successful")
        with self.assertRaises(Exception) as e:
            self.site1.register(self.account2)
        self.assertTrue("user already registered" in str(e.exception))

    def test_login_success_email_password(self):
        self.site1.register(self.account1)
        self.assertEqual(self.site1.login(**{'email': self.account1.email, 'password': '5Dj:xKBA'}), "login successful")
        self.assertEqual(self.site1.login(**{'email': self.account1.email, 'password': '5Dj:xKBA'}), "user already logged in")
        self.assertEqual(self.site1.login(**{'username': self.account1.username, 'password': '5Dj:xKBA'}), "user already logged in")

    def test_login_success_username_password(self):
        self.site1.register(self.account2) 
        self.assertEqual(self.site1.login(**{'username': self.account2.username, 'password': '123ASsdz'}), "login successful")
        self.assertEqual(self.site1.login(**{'username': self.account2.username, 'password': '123ASsdz'}), "user already logged in")
        self.assertEqual(self.site1.login(**{'email': self.account2.email, 'password': '123ASsdz'}), "user already logged in")

    def test_logout(self):
        self.site1.register(self.account2) 
        self.assertEqual(self.site1.login(**{'username': self.account2.username, 'password': '123ASsdz'}), "login successful")
        self.assertEqual(self.site1.logout(self.account2), "logout successful")
        self.assertEqual(self.site1.logout(self.account2), "user is not logged in")


if __name__ == '__main__':
    unittest.main()
