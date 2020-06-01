from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from datetime import date

from grps.models import GroupDetail


class Hotel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    city = models.CharField(max_length=50, verbose_name='City')
    stars = models.PositiveSmallIntegerField(verbose_name='Stars')
    rooms = models.PositiveSmallIntegerField(verbose_name='Rooms',
                                             help_text='Total number of rooms')
    help_text = 'Number of floors that rooms are distributed'
    floors = models.PositiveSmallIntegerField(verbose_name='Floors',
                                              help_text=help_text)
    elevators = models.PositiveSmallIntegerField(verbose_name='Elevators')
    address = models.CharField(max_length=200, null=True, verbose_name='Address')
    phone_list = ArrayField(models.CharField(max_length=20, blank=True),
                            size=5, default=list, blank=True,
                            verbose_name='Phone List')
    email_list = ArrayField(models.EmailField(max_length=100, blank=True),
                            size=5, default=list, blank=True,
                            verbose_name='Email List')

    extra_notes = ArrayField(models.CharField(max_length=100, blank=True),
                             size=5, default=list, blank=True,
                             verbose_name='Extra Notes')

    # Hotel.hotel_reservation_set()

    @property
    def fullname(self):
        """ Returns the hotel's full name which includes
            the city that it is located """
        return f"{self.name.strip()} ({self.city.strip()})"

    class Meta:
        ordering = ['city', 'stars']
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.fullname


class HotelReservation(models.Model):
    group = models.ForeignKey(GroupDetail, on_delete=models.CASCADE, verbose_name='Group')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Hotel')
    help_text = 'The date that the hotel confirmed the reservation'
    confirmation_date = models.DateField(null=True,
                                         verbose_name='Confirmation Date',
                                         help_text=help_text)

    extra_notes = ArrayField(models.CharField(max_length=100, blank=True),
                             size=5, default=list, blank=True,
                             verbose_name='Extra Notes')

    # HotelReservation.hotel_deposit_set()
    # HotelReservation.hotel_room_reservation_set()

    @property
    def fullname(self):
        """ Returns the reservations full name which includes
            group's name and hotel's name. """
        return f"Reservation at {self.hotel} for {self.group}"

    class Meta:
        ordering = ['group', 'hotel']
        verbose_name = 'Hotel Reservation'
        verbose_name_plural = 'Hotel Reservations'

    def __str__(self):
        return self.fullname


class HotelDeposit(models.Model):
    deposit_date = models.DateField(default=date.today, verbose_name='Deposit Date')
    amount = models.DecimalField(max_digits=5,
                                 decimal_places=1,
                                 default=0.0,
                                 verbose_name='Amount')
    help_text = 'Choose hotel reservation from the list'
    hotel_reservation = models.ForeignKey(HotelReservation,
                                          on_delete=models.CASCADE,
                                          verbose_name='Reservation',
                                          help_text=help_text)

    extra_notes = ArrayField(models.CharField(max_length=100, blank=True),
                             size=5, default=list, blank=True,
                             verbose_name='Extra Notes')

    @property
    def fullname(self):
        """ Returns the deposit's full name which includes
            group's name, hotel's name and deposit amount. """
        return f"Deposit: {self.amount} € for {self.hotel_reservation}"

    class Meta:
        ordering = ['deposit_date']
        verbose_name = 'Hotel Deposit'
        verbose_name_plural = 'Hotel Deposits'

    def __str__(self):
        return self.fullname


class HotelRoomReservation(models.Model):
    class RoomType(models.TextChoices):
        SGL = 'SGL', 'Single Room'
        TWN = 'TWN', 'Twin Room'
        TRP = 'TRP', 'Triple Room'
        QTR = 'QTR', '4-Bed Room'
        SUI = 'SUI', 'Suite'
        SPE = 'SPE', 'Special Room'

    class MealPlan(models.TextChoices):
        NO = 'NO', 'No Meal'
        BB = 'BB', 'Bead & Breakfast'
        HB = 'HB', 'Half-Board'
        FB = 'FB', 'Full-Board'
        AI = 'AI', 'All-Inclusive'
    help_text = 'Choose hotel reservation from the list'
    hotel_reservation = models.ForeignKey(HotelReservation,
                                          on_delete=models.CASCADE,
                                          verbose_name='Hotel',
                                          help_text=help_text)
    room_type = models.CharField(max_length=3,
                                 choices=RoomType.choices,
                                 default=RoomType.TWN,
                                 verbose_name='Room Type')
    meal_plan = models.CharField(max_length=2,
                                 choices=MealPlan.choices,
                                 default=MealPlan.BB,
                                 verbose_name='Meal Plan')
    staying_date = models.DateField(default=date.today,
                                    verbose_name='Staying Date')
    rate_per_room = models.DecimalField(max_digits=5,
                                        decimal_places=1,
                                        default=0.0,
                                        verbose_name='Rate')
    help_text = 'Number of rooms required'
    quantity = models.PositiveSmallIntegerField(verbose_name='Quantity',
                                                help_text=help_text)

    extra_notes = ArrayField(models.CharField(max_length=100, blank=True),
                             size=5, default=list, blank=True,
                             verbose_name='Extra Notes')

    @property
    def total_cost(self):
        return self.rate_per_room*self.quantity

    class Meta:
        ordering = ['hotel_reservation']
        verbose_name = 'Hotel Room Reservation'
        verbose_name_plural = 'Hotel Room Reservations'

    def __str__(self):
        return f"Reservation: {self.quantity} {self.room_type}(s) {self.meal_plan}"
