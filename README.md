# Product Availability Alert App

## Overview

This is a simple Python project designed to monitor the availability of a specific product on a camping website. The product is currently unavailable for shipping to the UK, and this script aims to alert the user when it becomes available for purchase from the UK.

## Skills/Technolgies

Python / Apache Airflow / Docker-Compose / Selenium / BeautifulSoup / SMTLIB / Logging
## Features

Uses Selenium and BeautifulSoup for web scraping to check the product availability.
Integrates with Airflow, running as a service in Docker, to schedule daily checks.
Sends email alerts when the product becomes available for purchase from the UK.

## Setup

Clone this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Set up your environment variables for email configuration (SMTP server, sender email, sender password, etc.).
Run Airflow in Docker with the provided Dockerfile and Airflow configuration.
Customize the URL of the camping website and the specific product to monitor in the AvailabilityCheck class.
Run docker-compose up --build to start the service.

