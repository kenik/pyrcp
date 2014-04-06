import os
import pyrcp
import unittest
import tempfile

class PyrcpTestCase(unittest.TestCase):
    '''
    def setUp(self):
        self.db_fd, pyrcp.app.config['DATABASE'] = tempfile.mkstemp()
        self.db_fd, pyrcp.app.config.update(dict(
            DATABASE=tempfile.mkstemp(),
            DEBUG=True,
            SECRET_KEY='development key',
            USERNAME='admin',
            PASSWORD='default'
        ))

        pyrcp.app.config['TESTING'] = True
        self.app = pyrcp.app.test_client()
        init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(pyrcp.app.config['DATABASE'])
    '''
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
