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
        verbose_name = 'Job Position'
        verbose_name_plural = 'Job Positions'

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
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return self.fullname


