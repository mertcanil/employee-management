from models.employee import Employee
from services.database import db

class EmployeeLogic(object):

    def save(self, employee: Employee):
        try:
            employee.insert()
        except Exception as exception:
            raise Exception

    def get_all(self) -> list[Employee]:
        try:
            return Employee.query.all()
        except Exception as exception:
            raise Exception

    def get(self, id: int) -> Employee:
        try:
            return Employee.query.get(id)
        except Exception as exception:
            raise Exception

    def delete(self, id: int):
        try:
            employee = Employee.query.get(id)
            db.session.delete(employee)
            db.session.commit()
        except Exception as exception:
            raise Exception

    def update(self, id: int, employee: Employee):
        try:
            Employee.query.filter_by(id=id).update(dict(
                firstname = employee.firstname,
                lastname = employee.lastname,
                birth_date = employee.birth_date,
                street = employee.street,
                house_number = employee.house_number,
                zip_code = employee.zip_code,
                city = employee.city,
                position = employee.position
            ))
            db.session.commit()
        except Exception as exception:
            raise Exception