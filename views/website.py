from flask import Blueprint, redirect, render_template, request
from models.employee import Employee
from logic.employee_logic import EmployeeLogic

website = Blueprint("website", __name__, url_prefix="")
employee_logic = EmployeeLogic()

@website.route("/")
def index():
    return render_template("index.html", employee=employee_logic.get_all())

@website.route("create")
def create():
    return render_template("employee.html", do="create", employee=None)

@website.post("employee-create")
def create_employee():
    try:
        employee = Employee(
            request.form.get("firstname"),
            request.form.get("lastname"),
            request.form.get("birth_date"),
            request.form.get("street"),
            request.form.get("house_number"),
            request.form.get("zip_code"),
            request.form.get("city"),
            request.form.get("position")
        )
        employee_logic.save(employee)
        return redirect("/")
    except Exception as exception:
        return str(exception)

@website.get("/edit")
def update():
    try:
        employee_id = request.args.get("id")
        return render_template("employee.html", do="edit", employee=employee_logic.get(int(employee_id)))
    except Exception as exception:
        return str(exception)

@website.post("employee-edit")
def employee_update():
    try:
        employee_id = request.form.get("employee_id")
        employee = Employee(
            request.form.get("firstname"),
            request.form.get("lastname"),
            request.form.get("birth_date"),
            request.form.get("street"),
            request.form.get("house_number"),
            request.form.get("zip_code"),
            request.form.get("city"),
            request.form.get("position")
        )
        employee_logic.update(int(employee_id), employee)
        return redirect("/")
    except Exception as exception:
        return str(exception)

@website.get("delete")
def delete():
    try:
        employee_id = request.args.get("id")
        employee_logic.delete(int(employee_id))
        return redirect("/")
    except Exception as exception:
        return str(exception)