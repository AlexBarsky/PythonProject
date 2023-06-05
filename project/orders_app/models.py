from django.db import models


class Organization(models.Model):
    org_address_street = models.TextField('Адресс')
    org_address_city = models.TextField('Город')
    org_postcode = models.TextField('Почтовый индекс')
    org_phone = models.TextField('Номер телефона')
    employees_count = models.TextField('Количество сотрудников')

    def __str__(self):
        return f"{self.org_address_street} {self.org_address_city} {self.org_postcode} {self.org_phone} " \
               f"{self.employees_count}"

    class Meta:
        db_table = 'organizations'
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Status(models.Model):
    statuses_name = models.CharField('Статус', max_length=50)

    def __str__(self):
        return f"{self.statuses_name}"

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Customer(models.Model):
    first_name = models.TextField('Имя')
    last_name = models.TextField('Фамилия')
    personal_phone = models.TextField('Номер телефона')
    visits = models.TextField('Количество посещений')
    status = models.ForeignKey(Status, on_delete=models.RESTRICT, verbose_name='Идентификатор статуса')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.personal_phone} {self.visits}"

    class Meta:
        db_table = 'customer'
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name='Покупатель')
    valuations = models.TextField('Оценка')
    orders_cost = models.TextField('Сумма заказа')
    orders_date = models.DateTimeField('Дата покупки', auto_now_add=True)

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заявки'


class Employee(models.Model):
    first_name = models.TextField('Имя')
    middle_name = models.TextField('Отчество')
    last_name = models.TextField('Фамилия')
    age = models.TextField('Возраст')
    personal_phone = models.TextField('Номер телефона')
    employees_email = models.TextField('E-mail адрес')
    employees_experience = models.TextField('Стаж работы')
    employees_salary = models.TextField('Зарплата сотрудника')
    employees_rating = models.TextField('Рейтинг сотрудника')
    login = models.TextField('Логин сотрудника')

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} {self.age} {self.personal_phone} {self.age}" \
               f"{self.employees_email} {self.employees_experience} {self.employees_salary} {self.employees_salary}" \
               f"{self.login}"

    class Meta:
        db_table = 'employee'
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Service(models.Model):
    services_name = models.TextField('Название услуги')
    services_price = models.TextField('Цена услуги')
    employee = models.ForeignKey(Employee, on_delete=models.RESTRICT, verbose_name='Мастер')

    def __str__(self):
        return f"{self.services_name} {self.services_price} {self.employee}"


class Purchase(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, verbose_name='Заказ')
    service = models.ForeignKey(Service, on_delete=models.RESTRICT, verbose_name='Услуга')

    class Meta:
        db_table = 'purchase'
        verbose_name = 'Услуги в заказе'
        verbose_name_plural = 'Услуги в заказе'

