from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Booking
from .serializer import CheckMyBookingSerializer


class GetMyBookings(APIView):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        serializer = CheckMyBookingSerializer(
            bookings,
            many=True,
        )
        return Response(serializer.data)


class CancelMyBooking(APIView):
    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise NotFound

    def put(self, request, pk):
        booking = self.get_object(pk)
        serializer = CheckMyBookingSerializer(
            booking,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            canceled_booking = serializer.save()
            serializer = CheckMyBookingSerializer(canceled_booking)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
