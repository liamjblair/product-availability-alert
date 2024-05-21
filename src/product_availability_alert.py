from selenium import webdriver
import requests
import constants
import time
from bs4 import BeautifulSoup
import smtplib
import logger


class AvailabilityAlert:

    def __init__(self, url) -> None:
        self.url = url

    def parse_url(self) -> str:
        try:
            web_driver = webdriver.Chrome()
            web_driver.get(url)
            time.sleep(5) 
            source = web_driver.page_source
            self.results = BeautifulSoup(source, "html.parser")

        except Exception as e:
            logger.error(f"An error occurred while parsing the URL: {e}")
        finally:
            if web_driver:
                web_driver.quit()

    def check_availability(self) -> bool:
        # search_string = "Unfortunately we are unable to deliver to the UK at this time."
        search_string="The Skrama is a versatile heavy-duty bush knife"
        found_string = self.results.find_all(string=lambda text: search_string in text)
        if found_string:
            self.send_email_alert()

    def send_email_alert(self):
        # SMTP server configuration
        smtp_server = constants.SMTLIB_SERVER
        smtp_port = constants.SMTLIB_PORT

        sender_email = constants.EMAIL_ADDRESS
        receiver_email = constants.EMAIL_ADDRESS
        sender_password = constants.EMAIL_PASS
        subject = "Varusteleka.com product avilability alert"
        email_body = f"""

            Varusteleka.com product avilability alert.

            Availabiliy to the UK may have changed. Check the website: {self.url}


        """
  
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            
            email_content = f"Subject: {subject}\n\n{email_body}"

            server.sendmail(sender_email, receiver_email, email_content)
            server.quit()

        except smtplib.SMTPAuthenticationError as e:
            logger.error(f"Authentication error: {e}")
        except smtplib.SMTPException as e:
            logger.error(f"An error occurred while sending the email: {e}.")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}.")


# product of interest
product = constants.PRODUCT
url = f"https://www.varusteleka.com/en/{product}"
availability = AvailabilityAlert(url)
availability.parse_url()
availability.check_availability()