from abc import ABC
from copy import copy
from typing import List, Any

from booking.models import RoomType
from booking.repositories import CustomerRepository, RoomRepository, BookingRepository, \
    PaymentRepository
from booking.serializers import CustomerSerializer, RoomSerializer, BookingSerializer, PaymentSerializer


class Service(ABC):

    def __init__(self, repository, _class):
        self.repository = repository
        self._class = _class

    def get_all(self, **kwargs) -> List[Any]:
        return self._class(self.repository.get_all(**kwargs), many=True).data

    def get_by_id(self, _id: int) -> Any:
        return self._class(self.repository.get_by_id(_id)).data

    def save(self, **kwargs) -> int:
        record = self.repository.save(**kwargs)
        return record.id

    def update(self, _id: int, **kwargs) -> None:
        return self.repository.update(_id, **kwargs)

    def delete(self, _id: int) -> None:
        return self.repository.delete(_id)


class CustomerService(Service):

    def __init__(self):
        super(CustomerService, self).__init__(CustomerRepository(), CustomerSerializer)


class RoomService(Service):

    def __init__(self):
        super(RoomService, self).__init__(RoomRepository(), RoomSerializer)

    @staticmethod
    def __complete_room_fields(record):
        modified_record = copy(record)
        room_type = RoomType.get_by_value(record['room_type'])
        if room_type is not None:
            modified_record['number_of_beds'] = room_type.number_of_beds
            modified_record['price'] = room_type.price
        return modified_record

    def get_all(self, **kwargs) -> List[Any]:
        result = []
        for record in super().get_all(**kwargs):
            result.append(RoomService.__complete_room_fields(record))
        return result

    def get_by_id(self, _id: int) -> Any:
        return RoomService.__complete_room_fields(super().get_by_id(_id))


class BookingService(Service):

    def __init__(self):
        super(BookingService, self).__init__(BookingRepository(), BookingSerializer)


class PaymentService(Service):

    def __init__(self):
        super(PaymentService, self).__init__(PaymentRepository(), PaymentSerializer)
