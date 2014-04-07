import os
import pyrcp
import unittest
import tempfile

class PyrcpTestCase(unittest.TestCase):

    app = pyrcp.app.run()

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('kenik', '123123')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('wrong_user', '123123')
        assert 'Invalid username' in rv.data
        rv = self.login('kenik', '31e1wd1')
        assert 'Invalid password' in rv.data


if __name__ == '__main__':
    unittest.main()

