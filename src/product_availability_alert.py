from selenium import webdriver
from src import constants
import time
from bs4 import BeautifulSoup
import smtplib
from src import logger


class AvailabilityCheck:

    def __init__(self, url) -> None:
        self.url = url

    def parse_url(self) -> str:

        """
        Parses the HTML content of the URL using Selenium WebDriver and BeautifulSoup.

        This method uses Selenium WebDriver to retrieve the HTML content of the URL 
        and then parses it using BeautifulSoup to extract structured data. The parsed 
        content is stored in the 'results' attribute of the class instance.
        
        """

        try:
            web_driver = webdriver.Chrome()
            web_driver.get(self.url)
            time.sleep(5) 
            source = web_driver.page_source
            self.results = BeautifulSoup(source, "html.parser")

        except Exception as e:
            logger.error(f"An error occurred while parsing the URL: {e}")
        finally:
            if web_driver:
                web_driver.quit()

    def check_availability(self) -> bool:

        """ 
        Checks if the specified string is found in the HTML document.

        This method searches for the specified string within the parsed HTML document
        obtained from the URL. If the string is not found, it returns False, indicating that
        the product is available. If the string is found, it returns True, indicating that
        shipping to the UK may still be unavailable.
                    
        """

        search_string = "Unfortunately we are unable to ship to the UK at this time."
        found_string = self.results.find_all(string=lambda text: search_string in text)
        if not found_string:
            self.send_email_alert()

    def send_email_alert(self):

        """
        Creates the SMTLIB connection witht the users email address and password. 
        If the return value of check_availability is False, we send an email alert 
        to the user including the link asking them to comfirm if delivery to the UK
        is now available.
        
        """
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
