from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
from models import contact_schema
import argparse
import pymongo
# import logging

# Create and Config logger
# logging.basicConfig(
#     format='%(levelname)s - (%(asctime)s) - %(message)s - (Line: %(lineno)d) - [%(filename)s]',
#     datefmt='%H:%M:%S',
#     encoding='utf-8',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)


class ContactManager:
    def __init__(self, connection_string, action, first_name, last_name, code, number, country=None, city=None,
                 address=None, new_first_name=None, new_last_name=None):
        self.actions = {
            'create': self.create,
            'list': self.list,
            'search': self.search,
            'update': self.update,
            'delete': self.delete
        }
        self.connection_string = connection_string
        self.collection = self.__get_collection()
        self.action = action
        self.first_name = first_name
        self.last_name = last_name
        self.code = code
        self.number = number
        self.country = country
        self.city = city
        self.address = address
        self.new_first_name = new_first_name
        self.new_last_name = new_last_name
        self.data = None
        self.criteria = {"name.first name": self.first_name, "name.last name": self.last_name}

    def __get_collection(self):
        client = pymongo.MongoClient(self.connection_string)
        db = client["Daneshkar"]
        contacts_collection = db["Contacts"]
        return contacts_collection

    def __fill_data(self):
        self.data = {
            "name": {
                "first name": self.first_name,
                "last name": self.last_name,
            }
        }

        if self.code:
            self.data["code"] = self.code

        if self.number:
            self.data["number"] = self.number

        address = dict()

        if self.country:
            address["country"] = self.country

        if self.city:
            address["city"] = self.city

        if self.address:
            address["address"] = self.address

        if address:
            self.data["address"] = address

        if self.new_first_name:
            self.data["first name"] = self.new_first_name

        if self.new_last_name:
            self.data["last name"] = self.new_last_name

    def __validate_data(self):
        if not (self.first_name and self.last_name):
            print("First name and Last name are required!")
            return
        try:
            validate(self.data, contact_schema)
            return True

        except ValidationError as e:
            print(f"Validation Error: {e}")
            return False

    def take_action(self):
        self.actions[self.action]()

    def create(self):
        self.__fill_data()

        if self.__validate_data():
            result = self.collection.insert_one(self.data)
            print(f"Inserted record with ID: {result.inserted_id}")

    def list(self):
        all_records = self.collection.find()
        if list(all_records):
            print("All records in Contacts collection:")
            for record in all_records:
                print(record)
        else:
            print("Collection is empty!")

    def search(self):
        matching_documents = self.collection.find(self.criteria)
        if list(matching_documents):
            print("Matching Documents:")
            print(*[document for document in matching_documents], sep="\n")
        else:
            print("No Matching Document!")

    def update(self):
        self.__fill_data()
        if self.__validate_data():
            result = self.collection.update_many(self.criteria, {"$set": self.data})
            print(f"Deleted {result.modified_count} documents!")

    def delete(self):
        result = self.collection.delete_many(self.criteria)
        print(f"Deleted {result.deleted_count} documents!")


if __name__ == '__main__':
    # logger.info('Configuring argument parser...')
    parser = argparse.ArgumentParser(
        prog='phone-list',
        description='A phone-list contains contacts with their personal information'
    )
    actions = ['create', 'list', 'search', 'update', 'delete']
    parser.add_argument('action', type=str, help='Action', choices=actions)
    parser.add_argument('-f', '--first_name', type=str, help='First name')
    parser.add_argument('-l', '--last_name', type=str, help='Last name')
    parser.add_argument('-d', '--code', type=str, help='Country code')
    parser.add_argument('-n', '--number', type=str, help='Phone number')
    parser.add_argument('-C', '--country', type=str, help='Country name')
    parser.add_argument('-c', '--city', type=str, help='City name')
    parser.add_argument('-a', '--address', type=str, help='Full Address')
    parser.add_argument('-F', '--new_first_name', type=str, help='New first name')
    parser.add_argument('-L', '--new_last_name', type=str, help='New last name')

    # logger.info('parsing arguments...')
    args = parser.parse_args()

    # Creating instance of Manager class
    connection = 'mongodb://localhost:27017/'
    contact_manager = ContactManager(connection, args.action, args.first_name, args.last_name, args.code, args.number,
                                     args.country, args.city, args.address, args.new_first_name, args.new_last_name)
    contact_manager.take_action()

    # logger.info('Done!')
