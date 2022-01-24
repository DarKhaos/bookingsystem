from rest_framework.serializers import ModelSerializer

from booking.models import Customer, Room, Booking, IntervalDate, Payment


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'dni', 'guest']


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'room_type']


class IntervalDateSerializer(ModelSerializer):
    class Meta:
        model = IntervalDate
        fields = ['start_date_time', 'end_date_time']


class BookingSerializer(ModelSerializer):
    booking_date = IntervalDateSerializer()
    room = RoomSerializer()
    customers = CustomerSerializer(many=True)

    class Meta:
        model = Booking
        fields = ['id', 'booking_date', 'room', 'customers', 'created_date_time', 'status']


class PaymentSerializer(ModelSerializer):
    booking = BookingSerializer()

    class Meta:
        model = Payment
        fields = ['id', 'payment_method', 'booking', 'amount', 'date_time']

