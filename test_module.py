"""
test script for student database project 
"""
from SMG import StudentManagerController, StudentModel
import pytest

def test_generate_id():
    manager = StudentManagerController()
    generated_id = manager.generate_id()
    assert generated_id > 0

def test_remove_student():
    manager = StudentManagerController()
    student = StudentModel(name="John", age=20, score=85)
    manager.add_student(student)
    assert manager.remove_student(student.id)

#command line: pytest test_module.py