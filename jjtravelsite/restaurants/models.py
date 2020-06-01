from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from datetime import date

from grps.models import GroupDetail


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
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

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
        verbose_name = 'Restaurant Menu'
        verbose_name_plural = 'Restaurant Menus'

    def __str__(self):
        return self.full_name


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
        verbose_name = 'Restaurant Reservation'
        verbose_name_plural = 'Restaurant Reservations'

    def __str__(self):
        return f'Reservation at {self.restaurant_menu.restaurant} for {self.group}'
