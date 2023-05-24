import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def trackphone():
    mobile_no = input("Enter a phone number with countery code:")
    mobile_no = phonenumbers.parse(mobile_no)

    #timezone

    print(timezone.time_zones_for_number(mobile_no))

    #carrier

    print(carrier.name_for_number(mobile_no, "en"))

    #region

    print(geocoder.description_for_number(mobile_no, "en"))

    #validating

    print("Valid mobile number:", phonenumbers.is_valid_number(mobile_no))

    #posibility

    print("Check possibility of number:", phonenumbers.is_possible_number(mobile_no))

trackphone()