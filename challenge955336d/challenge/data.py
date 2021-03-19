"""Routines associated with the application data.
"""
import json
courses = {}

def load_data():
    """Load the data from the json file.
    """
    f=open("E:\pythonproject\challenge955336d\challenge\json\course.json",)
    courses={}
    for line in f:
        print(line)
    courses = json.loads(f)
    print(courses)
    f.close()
    pass


