class Person:
    name = ''  # имя у любого человека

    def __init__(self):  # конструктор базового класса
        print('The man is created')


class Employee(Person):
    jobTitle = ''  # наименование должности работника

    def __init__(self):  # конструктор дочернего класса
        print('The employee is created')
        # если нет конструктора, то вызовется базовый


class Customer(Person):
    email = ''  # почта клиента

    def __init__(self):
        Person.__init__(self)  # вызываем конструктор базового класса
        print('The customer is created')


og = Person()
og.name = 'Orkhan Gasanov'

janeEmployee = Employee()
janeEmployee.name = 'Jane Employee'  # поле наследуется от класса Person
janeEmployee.jobTitle = 'Web Developer'  #

bobCustomer = Customer()
bobCustomer.name = 'Bob Customer'  # поле наследуется от класса Person
bobCustomer.email = 'sendme@spam.com'













#
