from datetime import datetime

from rest_framework.generics import ListAPIView, UpdateAPIView , DestroyAPIView ,RetrieveAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer ,DetailSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer


class BookingAPIView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'


class UpdateListView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class DeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
