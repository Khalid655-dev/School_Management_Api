import json
import time
from celery import Celery

import database
import utils
from models import Admin
from admin import AdminSignup

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
result_backend = 'db+mysql+mysqlconnector://root:admin655@localhost/SchoolManagement'
celery = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL, database_url=result_backend)


@celery.task(name='Add two numbers')
def add(x, y):
    return x + y


@celery.task(name="Testing with Database")
def create_admin(admin_: AdminSignup):
    hashed_password = utils.hash_(admin_['password'])
    admin_['password'] = hashed_password

    print(f"{admin_}")
    db = next(database.get_db())
    new_admin = Admin(**admin_)
    time.sleep(5)
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return json.dumps({
        "email": new_admin.email,
        "password": new_admin.password})
