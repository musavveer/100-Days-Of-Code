# import phonenumbers library
import phonenumbers


# to get the location of the corresponding number 
from phonenumbers import geocoder
ch_number = phonenumbers.parse("enter_your_number", "CH")
print(geocoder.description_for_number(ch_number, "en"))


# to get the carrier of the corresponding number 
from phonenumbers import carrier
service_number = phonenumbers.parse("enter_your_number", "RO")
print(carrier.name_for_number(service_number, "en"))


# to get the time zone of the corresponding number 
from phonenumbers import timezone
gb_number = phonenumbers.parse("enter_your_number", "GB")
print(timezone.time_zones_for_number(gb_number))