#here using phonenumber API
import phonenumbers

#here using one more API geocoder
from phonenumbers import geocoder

phone_number1=phonenumbers.parse("+917387057044","CH")

print(geocoder.description_for_number(phone_number1,"en"))

#importing carrier for verifying service provider
from phonenumbers import carrier

service_number=phonenumbers.parse("+917387057044","RO")
print(carrier,name_for_number(service_number,"en"))
