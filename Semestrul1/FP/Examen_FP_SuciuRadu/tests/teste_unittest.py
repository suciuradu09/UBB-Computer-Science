import unittest
from service.spectacole_serv import spectacoleServ
from repository.spectacole_repo import spectacoleRepo_file
from domain.entities import Spectacol
from domain.validator import validator

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._serv = spectacoleServ
        self._repo = spectacoleRepo_file("unittest_file.txt")
        self._val = validator

    def test_validator(self):
        s1 = Spectacol('A', 'A', "Balet", 1000)
        s2 = Spectacol('', 'A', "Balet", 1000)
        s3 = Spectacol('C', 'C', "Balet", 12140)
        s4 = Spectacol('', 'C', "Balet", 21400)
        self.assertRaises(ValueError, self._val.validate, self, s2)

if __name__ == '__main__':
    unittest.main()
