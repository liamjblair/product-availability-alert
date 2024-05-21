from src.product_availability_alert import AvailabilityCheck
from src import constants

def run():
    # product of interest
    product = constants.PRODUCT
    url = f"https://www.varusteleka.com/en/{product}"
    availability = AvailabilityCheck(url)
    availability.parse_url()
    availability.check_availability()