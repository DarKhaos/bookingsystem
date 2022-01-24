from abc import ABC, abstractmethod
from copy import copy
from typing import Any, List

from django.db.models import QuerySet

from booking.models import Payment, Customer, Room, Booking, IntervalDate


class CrudRepository(ABC):

    @abstractmethod
    def get_all(self, **kwargs) -> List[Any]:
        pass

    @abstractmethod
    def get_by_id(self, _id: int) -> Any:
        pass

    @abstractmethod
    def save(self, **kwargs) -> Any:
        pass

    @abstractmethod
    def update(self, _id: int, **kwargs) -> None:
        pass

    @abstractmethod
    def delete(self, _id: int) -> None:
        pass


class CustomerRepository(CrudRepository):

    def get_all(self, **kwargs) -> List[Customer]:
        return list(Customer.objects.filter(**kwargs))

    def get_by_id(self, _id: int) -> Customer:
        return Customer.objects.get(id=_id)

    def save(self, **kwargs) -> Customer:
        return Customer.objects.create(**kwargs)

    @staticmethod
    def get_filtered_customer(_id: int) -> QuerySet:
        return Customer.objects.filter(pk=_id)

    def update(self, _id: int, **kwargs) -> None:
        CustomerRepository.get_filtered_customer(_id).update(**kwargs)

    def delete(self, _id: int) -> None:
        CustomerRepository.get_filtered_customer(_id).delete()


class RoomRepository(CrudRepository):

    def get_all(self, **kwargs) -> List[Room]:
        return list(Room.objects.filter(**kwargs))

    def get_by_id(self, _id: int) -> Room:
        return Room.objects.get(id=_id)

    def save(self, **kwargs) -> Room:
        return Room.objects.create(**kwargs)

    @staticmethod
    def get_filtered_room(_id: int) -> QuerySet:
        return Room.objects.filter(pk=_id)

    def update(self, _id: int, **kwargs) -> None:
        RoomRepository.get_filtered_room(_id).update(**kwargs)

    def delete(self, _id: int) -> None:
        RoomRepository.get_filtered_room(_id).delete()


class BookingRepository(CrudRepository):

    def get_all(self, **kwargs) -> List[Booking]:
        return list(Booking.objects.filter(**kwargs))

    def get_by_id(self, _id: int) -> Booking:
        return Booking.objects.get(id=_id)

    @staticmethod
    def __copy_kwargs(kwargs) -> dict:
        return copy(kwargs)

    @staticmethod
    def __add_booking_date_id(kwargs) -> None:
        booking_date = IntervalDate.objects.get_or_create(start_date_time=kwargs['booking_date']['start_date_time'],
                                                          end_date_time=kwargs['booking_date']['end_date_time'])
        kwargs['booking_date_id'] = booking_date[0].id
        del kwargs['booking_date']

    @staticmethod
    def __get_customers(kwargs) -> List[Customer]:
        return list(Customer.objects.filter(id__in=kwargs['customers']))

    @staticmethod
    def __remove_customers(kwargs):
        del kwargs['customers']

    def save(self, **kwargs) -> Booking:
        added_kwargs = BookingRepository.__copy_kwargs(kwargs)
        BookingRepository.__add_booking_date_id(added_kwargs)
        customers = BookingRepository.__get_customers(added_kwargs)
        BookingRepository.__remove_customers(added_kwargs)
        booking = Booking.objects.create(**added_kwargs)
        booking.customers.add(*customers)
        return booking

    @staticmethod
    def get_filtered_booking(_id: int) -> QuerySet:
        return Booking.objects.filter(pk=_id)

    def update(self, _id: int, **kwargs) -> None:
        added_kwargs = BookingRepository.__copy_kwargs(kwargs)
        BookingRepository.__add_booking_date_id(added_kwargs)

        BookingRepository.__remove_customers(added_kwargs)
        BookingRepository.get_filtered_booking(_id).update(**added_kwargs)

    def delete(self, _id: int) -> None:
        BookingRepository.get_filtered_booking(_id).delete()


class PaymentRepository(CrudRepository):

    def get_all(self, **kwargs) -> List[Payment]:
        return list(Payment.objects.filter(**kwargs))

    def get_by_id(self, _id: int) -> Payment:
        return Payment.objects.get(id=_id)

    def save(self, **kwargs) -> Payment:
        return Payment.objects.create(**kwargs)

    @staticmethod
    def get_filtered_payment(_id: int) -> QuerySet:
        return Payment.objects.filter(pk=_id)

    def update(self, _id: int, **kwargs) -> None:
        PaymentRepository.get_filtered_payment(_id).update(**kwargs)

    def delete(self, _id: int) -> None:
        PaymentRepository.get_filtered_payment(_id).delete()
