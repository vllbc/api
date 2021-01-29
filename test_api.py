import unittest
from app import db,app
from app.command import initdb,collection
from app.models import QidianModel


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:xwh5201314@localhost/test?charset=utf8'
        )
        db.create_all()
        self.client= app.test_client()
        self.runner = app.test_cli_runner()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_app_exist(self):
        self.assertIsNotNone(app)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_404(self):
        response = self.client.get("/aaa")
        data = response.get_data(as_text=True)
        self.assertIn("404",data)
        self.assertIn("Page Not Found!",data)

    def test_index(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn("主页未完成",data)

    def test_initdb_command(self):
        result = self.runner.invoke(initdb)
        self.assertIn("OK!",result.output)


if __name__ == '__main__':
    unittest.main()
