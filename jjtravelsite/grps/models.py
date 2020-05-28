from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from datetime import date


class JobPosition(models.Model):
    title = models.CharField(max_length=50, default='Tour Guide', verbose_name='Title')
    description = models.CharField(max_length=200, null=True, verbose_name='Description')

    # JobPosition.person_set()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=20, verbose_name='First Name')
    lastname = models.CharField(max_length=20, verbose_name='Last Name')
    nickname = models.CharField(max_length=20, verbose_name='Nickname')
    jobPosition = models.ForeignKey(JobPosition,
                                    on_delete=models.CASCADE,
                                    verbose_name='Job Position')
    phoneList = ArrayField(models.CharField(max_length=20, blank=True),
                           size=5, default=list, blank=True, verbose_name='Phone List')
    emailList = ArrayField(models.EmailField(max_length=100, blank=True),
                           size=5, default=list, blank=True, verbose_name='Email List')

    extraNotes = ArrayField(models.CharField(max_length=100, blank=True),
                            size=5, default=list, blank=True, verbose_name='Extra Notes')

    # Person.group_detail_set()

    @property
    def fullname(self):
        """ Returns the person's full name. """
        return f"{self.firstname.strip()} \
                 {self.lastname.strip()} \
                 ({self.nickname.strip()})"

    class Meta:
        ordering = ['lastname']

    def __str__(self):
        return self.fullname


class Restaurant(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    city = models.CharField(max_length=50, verbose_name='City')
    address = models.CharField(max_length=200, null=True, verbose_name='Address')
    phone_list = ArrayField(models.CharField(max_length=20, blank=True),
                            size=5, default=list, blank=True, verbose_name='Phone List')
    email_list = ArrayField(models.EmailField(max_length=100, blank=True),
                            size=5, default=list, blank=True, verbose_name='Email List')

    extra_notes = ArrayField(models.CharField(max_length=100, blank=True),
                             size=5, default=list, blank=True, verbose_name='Extra Notes')

    # Restaurant.restaurant_menu_set()

    @property
    def fullname(self):
        """ Returns the restaurants full name which includes
            the city that it is located """
        return f"{self.name.strip()} ({self.city.strip()})"

    class Meta:
        ordering = ['city']

    def __str__(self):
        return self.fullname


class RestaurantMenu(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    restaurant = models.ForeignKey(Restaurant,
                                   on_delete=models.CASCADE,
                                   verbose_name='Restaurant',
                                   help_text='Choose Restaurant')
    is_bread_included = models.BooleanField(default=True, verbose_name='Bread Included')
    is_tip_included = models.BooleanField(default=False, verbose_name='Tip Included')
    appetizer_list = ArrayField(models.CharField(max_length=50, blank=True),
                                size=5, default=list, blank=True,
                                verbose_name='Appetizers')
    soup_list = ArrayField(models.CharField(max_length=50, blank=True),
                           size=5, default=list, blank=True, verbose_name='Soups')
    salad_list = ArrayField(models.CharField(max_length=50, blank=True),
                            size=5, default=list, blank=True, verbose_name='Salads')
    main_dish_list = ArrayField(models.CharField(max_length=50, blank=True),
                                size=5, default=list, blank=True,
                                verbose_name='Main Dishes')
    dessert_list = ArrayField(models.CharField(max_length=50, blank=True),
                              size=5, default=list, blank=True, verbose_name='Desserts')
    drink_list = ArrayField(models.CharField(max_length=50, blank=True),
                            size=5, default=list, blank=True, verbose_name='Drinks')
    cost_per_person = models.DecimalField(max_digits=5,
                                          decimal_places=1,
                                          default=10.0,
                                          verbose_name='Cost/Person')

    extra_notes = ArrayField(models.CharField(max_length=100, blank=True),
                             size=5, default=list, blank=True, verbose_name='Extra Notes')

    # RestaurantMenu.restaurant_reservation_set()

    @property
    def full_name(self):
        return f'{self.name} -> {self.restaurant}'

    class Meta:
        ordering = ['restaurant']

    def __str__(self):
        return self.full_name


class GroupName(models.Model):
    departure_date = models.DateField(default=date.today,
                                      verbose_name='Departure Date',
                                      help_text='Date mentioned in the request email')
    name = models.CharField(max_length=50,
                            verbose_name='Name',
                            help_text='Name mentioned in the request email')

    @property
    def full_name(self):
        # return self.departure_date.strftime("%Y%m%d") + self.name
        return self.departure_date.strftime("%Y%m%d") + self.name

    def __str__(self):
        return self.full_name


class GroupDetail(models.Model):
    group_name = models.OneToOneField(GroupName,
                                      on_delete=models.CASCADE,
                                      primary_key=True,
                                      verbose_name='Group Name')
    tour_guide = models.ForeignKey(Person,
                                   null=True,
                                   on_delete=models.CASCADE,
                                   verbose_name='Tour Guide')
    pax = models.PositiveSmallIntegerField(null=True)
    is_tour_leader = models.BooleanField(default=True)                                  

    # GroupDetail.restaurant_reservation_set()
    # GroupDetail.hotel_reservation_set()
    # GroupDetail.site_visit_set()

    # @property
    # def group_name_to_string(self):
    #     return self.group_name.full_name

    class Meta:
        ordering = ['group_name']

    def __str__(self):
        return self.group_name.full_name


class RestaurantReservation(models.Model):
    group = models.ForeignKey(GroupDetail,
                              on_delete=models.CASCADE,
                              verbose_name='Group',
                              help_text='Choose a group from the list')
    restaurant_menu = models.ForeignKey(RestaurantMenu,
                                        on_delete=models.CASCADE,
                                        verbose_name='Menu',
                                        help_text='Choose a menu from the list')
    reservation_date_time = models.DateTimeField(default=timezone.now,
                                                 verbose_name='Date | Time')
    total_pax = models.PositiveSmallIntegerField(verbose_name='Total PAX',
                                                 help_text='Total meals served')
    free_pax = models.PositiveSmallIntegerField(verbose_name='Free Meals')
    # is_confirmed = models.BooleanField(default=False)
    extra_payment = models.DecimalField(max_digits=5,
                                        decimal_places=1,
                                        null=True,
                                        verbose_name='Extra Payment',
                                        help_text='Payment for emergency reasons')

    extra_notes = ArrayField(models.CharField(max_length=100, blank=True),
                             size=5, default=list, blank=True,
                             verbose_name='Extra Notes')

    @property
    def total_cost(self):
        pax = self.total_pax - self.free_pax
        return self.restaurant_menu.cost_per_person*pax + self.extra_cost

    class Meta:
        ordering = ['group']

    def __str__(self):
        return f'Reservation at {self.restaurant_menu.restaurant} for {self.group}'


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

    def __str__(self):
        return f"Reservation: {self.quantity} {self.room_type}(s) {self.meal_plan}"


class Site(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Name',
                            help_text='Name of the site visited')
    city = models.CharField(max_length=50,
                            verbose_name='City',
                            help_text='Main city where the site is located')

    @property
    def full_name(self):
        return f'{self.name} ({self.city})'

    class Meta:
        ordering = ['city', 'name']

    def __str__(self):
        return self.full_name


class SiteVisit(models.Model):
    class TransportatioMean(models.TextChoices):
        BUS = 'BUS', 'Bus'
        FER = 'FER', 'Ferry'
        AIR = 'AIR', 'Airplane'
        TRA = 'TRA', 'Train'
        WAL = 'WAL', 'Walk'
        TEL = 'TEL', 'Teleferik'
        KAT = 'KAT', 'Katamaran'

    site = models.ForeignKey(Site,
                             on_delete=models.CASCADE,
                             verbose_name='Site',
                             help_text='Choose a site from the list')
    group = models.ForeignKey(GroupDetail,
                              on_delete=models.CASCADE,
                              verbose_name='Group',
                              help_text='Choose a group from the list')
    date = models.DateField(default=date.today,
                            verbose_name='Date')
    arrival_time = models.TimeField(null=True, verbose_name='Arrival Time')
    departure_time = models.TimeField(null=True, verbose_name='Departure Time')
    transportation_mean = models.CharField(max_length=3,
                                           choices=TransportatioMean.choices,
                                           default=TransportatioMean.BUS,
                                           verbose_name='Transportation Mean')
    entrance_fee = models.PositiveSmallIntegerField(verbose_name='Entrance Fee')
    participating_clients = models.PositiveSmallIntegerField(
                                     verbose_name='Participating Clients')

    extra_notes = ArrayField(models.CharField(max_length=100, blank=True),
                             size=5, default=list, blank=True,
                             verbose_name='Extra Notes')

    @property
    def total_cost(self):
        return self.entrance_fee*self.participating_clients

    @property
    def full_name(self):
        return f'{self.group} visit at {self.site} on {self.date}'

    class Meta:
        ordering = ['site', 'date']

    def __str__(self):
        return self.full_name
