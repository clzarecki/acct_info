from database import Database
import unittest

class TestDatabase(unittest.TestCase):

    def test_basic_add(self):
        events = """[
                {"account_id" : 1121345, "event_date": "2017-08-24", "account_standing": "G", "account_information": {"first_name": "John", "last_name": "Doe", "date_of_birth": "1986-08-18", "address": {"street_number": "123", "street_name": "Main Street", "city": "Centerville", "state": "CA", "zip_code": "91111"}, "email_address": "john_doe@gmail.com"} }, 
                {"account_id" : 1454581, "event_date": "2018-01-09", "account_standing": "B", "account_information": {"first_name": "Jane", "last_name": "Smith", "date_of_birth": "1975-09-09", "address": {"street_number": "345", "street_name": "Oak Drive", "unit_number": "12A", "city": "Mount Pleasant", "state": "CA", "zip_code": "90010"}, "email_address": "jane_smith@yahoo.com"} }
                ]"""

        db = Database()
        db.add_event_str(events)
        self.assertIsNone(db.query_account(1234567))

if __name__ == '__main__':
    unittest.main()
