import datetime
import uuid

class Student:
    def __init__(self, student_id, name, program, campus, year_of_study):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.campus = campus
        self.year_of_study = year_of_study

class FeeStructure:
    def __init__(self, program, year, total_fee):
        self.program = program
        self.year = year
        self.total_fee = total_fee

class Payment:
    def __init__(self, student_id, amount, date=None, payment_id=None):
        self.payment_id = payment_id or str(uuid.uuid4())
        self.student_id = student_id
        self.amount = amount
        self.date = date or datetime.date.today().isoformat()