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
        self.assertIsNotNone(db.query_account(1121345))
        self.assertIsNotNone(db.query_account(1454581))
        self.assertEquals(db.query_account(1454581)["last_name"], "Smith")
        self.assertEquals(db.query_account(1121345)["address"]["street_name"], "Main Street")
        self.assertEquals(db.query_account(1121345)["email_address"], "john_doe@gmail.com")
        
        new_event = """{"account_id" : 1394755, "event_date": "2017-05-17", "account_standing": "B", "account_information": {"first_name": "Charles", "last_name": "Johnson", "date_of_birth": "1987-10-06", "address": {"street_number": "1014", "street_name": "Nebraska Avenue", "city": "Waterville", "state": "NY", "zip_code": "10001"}, "email_address": "charles_johnson@outlook.com"} }"""
        self.assertIsNone(db.query_account(1394755))
        db.add_event_str(new_event)
        self.assertIsNotNone(db.query_account(1394755))
        self.assertEquals(db.query_account(1394755)["address"]["zip_code"], "10001")

    def test_add_update(self):
        events = """[
                {"account_id" : 1121345, "event_date": "2017-08-24", "account_standing": "G", "account_information": {"first_name": "Patrick", "last_name": "Sherman", "date_of_birth": "1986-08-18", "address": {"street_number": "123", "street_name": "Main Street", "city": "Centerville", "state": "CA", "zip_code": "91111"}, "email_address": "john_doe@gmail.com"} }, 
                {"account_id" : 1454581, "event_date": "2018-01-09", "account_standing": "B", "account_information": {"first_name": "Jane", "last_name": "Smith", "date_of_birth": "1975-09-09", "address": {"street_number": "345", "street_name": "Oak Drive", "unit_number": "12A", "city": "Mount Pleasant", "state": "CA", "zip_code": "90010"}, "email_address": "jane_smith@yahoo.com"} }
                ]"""

        db = Database()
        db.add_event_str(events)
        self.assertIsNotNone(db.query_account(1121345))
        self.assertEquals(db.query_account(1121345)["last_name"], "Sherman")
        self.assertEquals(db.query_account(1121345)["address"]["street_name"], "Main Street")
        
        new_event = """{"account_id" : 1121345, "event_date": "2017-11-06", "account_standing": "G", "account_information": {"first_name": "Patrick", "last_name": "Sherman", "date_of_birth": "1986-08-18", "address": {"street_number": "42", "street_name": "Wallaby Way", "city": "Syndey", "state": "WA", "zip_code": "98014"}, "email_address": "john_doe@gmail.com"} }"""
        db.add_event_str(new_event)
        self.assertEquals(db.query_account(1121345)["last_name"], "Sherman")
        self.assertEquals(db.query_account(1121345)["address"]["street_name"], "Wallaby Way")
        self.assertEquals(db.query_account(1121345)["address"]["street_number"], "42")

    def test_add_no_update(self):
        events = """[
                {"account_id" : 1121345, "event_date": "2017-08-24", "account_standing": "G", "account_information": {"first_name": "Patrick", "last_name": "Sherman", "date_of_birth": "1986-08-18", "address": {"street_number": "123", "street_name": "Main Street", "city": "Centerville", "state": "CA", "zip_code": "91111"}, "email_address": "john_doe@gmail.com"} }, 
                {"account_id" : 1454581, "event_date": "2018-01-09", "account_standing": "B", "account_information": {"first_name": "Jane", "last_name": "Smith", "date_of_birth": "1975-09-09", "address": {"street_number": "345", "street_name": "Oak Drive", "unit_number": "12A", "city": "Mount Pleasant", "state": "CA", "zip_code": "90010"}, "email_address": "jane_smith@yahoo.com"} }
                ]"""

        db = Database()
        db.add_event_str(events)
        self.assertIsNotNone(db.query_account(1121345))
        self.assertEquals(db.query_account(1121345)["email_address"], "john_doe@gmail.com")
        self.assertEquals(db.query_account(1454581)["address"]["unit_number"], "12A")
        
        new_event = """[
                {"account_id" : 1121345, "event_date": "2017-03-10", "account_standing": "G", "account_information": {"first_name": "Patrick", "last_name": "Sherman", "date_of_birth": "1986-08-18", "address": {"street_number": "123", "street_name": "Main Street", "city": "Centerville", "state": "CA", "zip_code": "91111"}, "email_address": "mystery_man12@gmail.com"} }, 
                {"account_id" : 1454581, "event_date": "2018-01-07", "account_standing": "B", "account_information": {"first_name": "Jane", "last_name": "Smith", "date_of_birth": "1975-09-09", "address": {"street_number": "345", "street_name": "Oak Drive", "unit_number": "34D", "city": "Mount Pleasant", "state": "CA", "zip_code": "90010"}, "email_address": "jane_smith@yahoo.com"} }
                ]"""
        db.add_event_str(new_event)
        self.assertEquals(db.query_account(1121345)["email_address"], "john_doe@gmail.com")
        self.assertEquals(db.query_account(1454581)["address"]["unit_number"], "12A")

if __name__ == '__main__':
    unittest.main()
