from urllib.parse import urlparse
import os
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


CERO_OR_LESS_ERROR ='This field has to be blank or greater tha cero'
TELEPHON_FORMAT_ERROR = 'Telephone number has to be exactly 10 digits and contain only numbers, no spaces or hyphen minus'


class Place (models.Model):

	def validate_more_than_cero(value):
		'''
		It's ilogical to have a negative cuantities for some fields. You
		can't have a negative number of persons, cars or area  for a place.
		The validator also avoids having two values cero and null for a field.
		not allowing cero in the field
		'''
		if value < 1:
			raise ValidationError(_(CERO_OR_LESS_ERROR))

	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	indoors_capacity = models.IntegerField(
		null=True,
		blank=True,
		validators=[validate_more_than_cero]
	)
	outdoors_capacity = models.IntegerField(
		null=True,
		blank=True,
		validators=[validate_more_than_cero]
	)
	min_capacity = models.IntegerField(
		null=True,
		blank=True,
		validators=[validate_more_than_cero]
	)
	parking_capacity = models.IntegerField(
		null=True,
		blank=True,
		validators=[validate_more_than_cero]
	)
	kitchen_sqrt_m = models.IntegerField(
		null=True,
		blank=True,
		validators=[validate_more_than_cero]
	)
	food = models.BooleanField()
	ac = models.BooleanField()
	heating = models.BooleanField()
	games = models.BooleanField()
	active = models.BooleanField(default=True)
	last_modified = models.DateField(auto_now=True)
	latitude_longitude = gis_models.PointField()

	def __str__(self):
		return self.name+'-'+str(self.pk)


class Region(models.Model):

	region = models.CharField(max_length=100)

	def __str__(self):
		return str(self.region)


class Locality(models.Model):

	locality = models.CharField(max_length=100)
	region = models.ForeignKey(Region)

	def __str__(self):
		return str(self.locality)


class Address(models.Model):

	address_line_1 = models.CharField(max_length=100)
	address_line_2 = models.CharField(max_length=100, blank=True)
	address_line_3 = models.CharField(max_length=100, blank=True)
	postal_code = models.CharField(max_length=5, blank=True)
	locality = models.ForeignKey(Locality)
	place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)


class Telephone(models.Model):

	PHONE_TYPE_CHOICES = (
		('cell', 'Cellphone'),
		('local', 'Localphone'),
	)

	phone_regex = RegexValidator(regex=r'^\d{10}$', message=_(TELEPHON_FORMAT_ERROR))
	number = models.CharField(max_length=15, validators=[phone_regex])
	phone_type = models.CharField(max_length=15, choices=PHONE_TYPE_CHOICES)
	place = models.ForeignKey(Place, on_delete=models.CASCADE)


class Email(models.Model):

	email = models.EmailField()
	place = models.ForeignKey(Place, on_delete=models.CASCADE)


class Representative(models.Model):

	representative = models.CharField(max_length=50)
	place = models.ForeignKey(Place, on_delete=models.CASCADE)


class SocialMedia(models.Model):

	social_media = models.URLField()
	place = models.ForeignKey(Place, on_delete=models.CASCADE)


def create_path_for_picture(instance, filename):
	filename = os.path.basename(filename)
	#file will be uploaded to MEDIA_ROOT/place<_id>/filename
	return '{0}/{1}'.format(instance.place, filename)


class ProfilePicture(models.Model):

	picture = models.ImageField(upload_to=create_path_for_picture)
	place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)


class Picture(models.Model):

	picture = models.ImageField(upload_to=create_path_for_picture)
	place = models.ForeignKey(Place, on_delete=models.CASCADE)
