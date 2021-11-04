import json
import pytest
db = None


class StudentResults:

    def __init__(self):
        self.loaded_result = None

    def connect(self, result_file):
        with open(result_file) as json_file:
            self.loaded_result = json.load(json_file)

    def get_result_data(self, student_name):
        for student in self.loaded_result['students']:
            if student['name'] == student_name:
                return student

    def close(self):
        pass


# @pytest.fixture(scope='module')
# def db():
#     db = StudentResults()
#     db.connect('my_students.json')
#     yield db
#     db.close()


def setUp_module(module):
    global db
    db = StudentResults()
    db.connect('my_students.json')


def tearDown_module(module):
    db.close()


def test_odogwu_results():
    odogwu = db.get_result_data('Odogwu')
    assert odogwu['id'] == 1
    assert odogwu['name'] == 'Odogwu'
    assert odogwu['result'] == 'Passed'


def test_igwe_results():
    igwe = db.get_result_data('Igwe')
    assert igwe['id'] == 2
    assert igwe['name'] == 'Igwe'
    assert igwe['result'] == 'Failed'
