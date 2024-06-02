import unittest
from utils.csv_reader import read_csv
from utils.json_writer import write_json
import os
import json

class TestCSVToJson(unittest.TestCase):

    def setUp(self):
        self.csv_file = 'test.csv'
        self.json_file = 'test.json'
        with open(self.csv_file, 'w') as f:
            f.write("name,age\nSahil,20\nSagar,22")

    def tearDown(self):
        os.remove(self.csv_file)
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

    def test_read_csv(self):
        data = read_csv(self.csv_file)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'Sahil')
        self.assertEqual(data[1]['age'], '20')

    def test_write_json(self):
        data = [{'name': 'Sahil', 'age': '20'}, {'name': 'Sagar', 'age': '22'}]
        write_json(data, self.json_file)
        with open(self.json_file, 'r') as f:
            json_data = json.load(f)
            self.assertEqual(len(json_data), 2)
            self.assertEqual(json_data[0]['name'], 'Sahil')
            self.assertEqual(json_data[1]['age'], '20')

if __name__ == "__main__":
    unittest.main()
