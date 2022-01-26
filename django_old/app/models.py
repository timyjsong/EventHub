from django.db import models
from django.utils import timezone


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class State(models.Model):
    state_name = models.CharField(max_length=20)
    state_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=10)

    country_key = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class City(models.Model):
    city_name = models.CharField(max_length=50)
    state_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=10)

    state_key = models.ForeignKey(
        State,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Address(models.Model):
    address_name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    city_name = models.CharField(max_length=50)
    state_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=10)

    city_key = models.ForeignKey(
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
    address_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    state_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=10)

    address_key = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.url


class Datetime(models.Model):
    local_start_date = models.CharField(max_length=20)
    local_start_time = models.CharField(max_length=20)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return "{} {} in {}".format(
            self.local_start_date,
            self.local_start_time,
            self.timezone
        )


class Info(models.Model):
    please_note = models.CharField(max_length=200)
    legal_age_enforced = models.BooleanField()

    def __str__(self):
        return self.please_note


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_url = models.URLField()

    venue_key = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE
    )
    image_key = models.ForeignKey(
        Image,
        on_delete=models.CASCADE
    )
    datetime_key = models.ForeignKey(
        Image,
        on_delete=models.CASCADE
    )
    info_key = models.ForeignKey(
        Image,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
