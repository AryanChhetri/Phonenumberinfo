import phonenumbers
//enter your number here
number=""

from phonenumbers import geocoder
country=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(country,"en"))

from phonenumbers import carrier 
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))
