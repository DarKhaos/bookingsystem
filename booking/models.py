from datetime import datetime
from enum import Enum

from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=210)
    dni = models.CharField(max_length=10, unique=True)
    guest = models.BooleanField(default=True)


class RoomType(Enum):
    SINGLE = "single", 1, 100
    DOUBLE = "double", 2, 180
    TRIPLE = "triple", 3, 220
    QUAD = "quad", 4, 260
    QUEEN = "queen", 1, 130
    KING = "king", 1, 150
    DOUBLE_DOUBLE = "double-double", 2, 200
    SUITE = "suite", 3, 450

    def __init__(self, _: str, number_of_beds: int, price: float):
        self.number_of_beds = number_of_beds
        self.price = price

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def get_by_value(cls, value: str) -> 'RoomType':
        for key in cls:
            if key.value == value:
                return key
        return None


class Room(models.Model):
    number = models.CharField(max_length=3, unique=True)
    room_type = models.CharField(max_length=len(RoomType.DOUBLE_DOUBLE.value), choices=RoomType.choices(),
                                 default=RoomType.SINGLE.value)


class IntervalDate(models.Model):
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()


class Booking(models.Model):

    class BookingStatus(Enum):
        PENDING = "pending"
        PAID = "paid"
        DELETED = "deleted"

        @classmethod
        def choices(cls):
            return [(key.value, key.name) for key in cls]

    booking_date = models.ForeignKey(IntervalDate, on_delete=models.RESTRICT)
    room = models.ForeignKey(Room, on_delete=models.RESTRICT)
    customers = models.ManyToManyField(Customer)
    created_date_time = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=len(BookingStatus.PENDING.value), choices=BookingStatus.choices(),
                              default=BookingStatus.PENDING.value)


class Payment(models.Model):

    class PaymentMethod(Enum):
        CASH = "cash"
        DEBIT_CARD = "debit card"
        CREDIT_CARD = "credit card"
        MOBILE_PAYMENT = "mobile payment"
        ELECTRONIC_BANK_TRANSFER = "electronic bank transfer"

        @classmethod
        def choices(cls):
            return [(key.value, key.name) for key in cls]

    payment_method = models.CharField(max_length=len(PaymentMethod.ELECTRONIC_BANK_TRANSFER.value),
                                      choices=PaymentMethod.choices(), default=PaymentMethod.CASH.value)
    booking = models.ForeignKey(Booking, on_delete=models.RESTRICT)
    amount = models.PositiveSmallIntegerField()
    date_time = models.DateTimeField(default=datetime.now())
