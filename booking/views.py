from abc import ABCMeta
from copy import copy
from typing import Any, List

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from booking.services import CustomerService, Service, RoomService, BookingService, PaymentService


class CrudAPIView(APIView, metaclass=ABCMeta):

    def __init__(self, service) -> Service:
        self.service = service

    @staticmethod
    def _get_response(data: Any) -> Response:
        return Response(data)

    def get(self, request: Request, pk: int = None) -> Response:
        if pk is not None:
            return CrudAPIView._get_response(self.service.get_by_id(_id=pk))
        return CrudAPIView._get_response(self.service.get_all(**request.query_params))

    def _post(self, request: Request, data: List[dict]) -> int:
        _id = self.service.save(**data)
        return Response(status=201, headers={'Location': f'{request.build_absolute_uri()}{_id}'})

    def post(self, request: Request):
        return self._post(request, request.data)

    @staticmethod
    def __get_empty_response():
        return Response()

    def _put(self, data: Request, pk: int):
        self.service.update(_id=pk, **data)
        return CrudAPIView.__get_empty_response()

    def put(self, request: Request, pk: int):
        return self._put(request.data, pk)

    def delete(self, _: Request, pk: int):
        self.service.delete(_id=pk)
        return CrudAPIView.__get_empty_response()


class CustomerAPIView(CrudAPIView):

    def __init__(self):
        super(CustomerAPIView, self).__init__(CustomerService())


class RoomAPIView(CrudAPIView):

    def __init__(self):
        super(RoomAPIView, self).__init__(RoomService())


class BookingAPIView(CrudAPIView):

    def __init__(self):
        super(BookingAPIView, self).__init__(BookingService())


class PaymentAPIView(CrudAPIView):

    def __init__(self):
        super(PaymentAPIView, self).__init__(PaymentService())

    def get(self, request: Request, pk: int, ppk: int = None):
        if ppk is not None:
            return CrudAPIView._get_response(self.service.get_by_id(_id=ppk))
        return CrudAPIView._get_response(self.service.get_all(booking__id=pk))

    @staticmethod
    def __add_booking_id(request, pk):
        data = copy(request.data)
        data["booking_id"] = pk
        return data

    def post(self, request: Request, pk: int):
        data = PaymentAPIView.__add_booking_id(request, pk)
        return self._post(request, data)

    def put(self, request: Request, pk: int):
        data = PaymentAPIView.__add_booking_id(request, pk)
        return self._put(request, data)

    def delete(self, _: Request, pk: int, ppk: int):
        return super().delete(_, ppk)
