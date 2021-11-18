from django.db import models
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    address = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.address


class Venue(models.Model):
    name = models.CharField(max_length=80)
    url = models.URLField()
    parking_detail = models.CharField(max_length=50)
    accessible_seating = models.CharField(max_length=200)
    general_rule = models.CharField(max_length=50)

    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()

    # One to One : Event
    event = models.OneToOneField(
        Event,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.url


class Date(models.Model):
    local_start_date = models.DateField()
    local_start_time = models.TimeField()
    timezone = models.CharField(max_length=50)

    event = models.OneToOneField(
        Event,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return "{} {} in {}".format(
            self.local_start_date,
            self.local_start_time,
            self.timezone
        )


class Info(models.Model):
    please_note = models.CharField(max_length=200)
    legal_age_enforced = models.BooleanField()

    event = models.OneToOneField(
        Event,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.please_note


