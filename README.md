# Webscraper and Weekly Text of My Favorite Football Team's Game

This is a program that webscrapes the [CBS Sports](https://www.cbssports.com/) schedule page of the University of Texas Longhorns and sends a weekly text with information on how to watch the upcoming game.

## Getting Started

This program was written in Python and utilizes Beautiful Soup and Celery. You will need to ensure these are downloaded on your machine. You will also need to set up an account with Twilio - the free trial account will suffice.

**Linux is required to run Celery!**

## Editing

### Phone Number

You _must_ edit the code to reflect your own Twilio account credentials and the phone number you wish to text every week. 

You can see in the following code from `webscraper.py`:
```
from TwilioCredentials import twilioLogin, twilioNumbers
```
that one way to do this is by creating a separate file called `TwilioCredentials.py` and adding your Twilio credentials and phone number to the `twilioLogin` and `twilioNumbers` dictionaries, respectively. 

You will want to add your `TwilioCredentials.py` to a `.gitignore` file so that your sensitive information is not posted to GitHub. 

### Team

You can edit the code to webscrape game information on a different team. Simply replace the URL in the URL variable in the `webscraper.py` file with the direct link to your desired team's schedule.

Note that this webscraper is specifically designed to scrape the CBS Sports website. Inserting a URL from any other website may result in an error.

### Weekly Text

You can edit the code to send the weekly text at a different time or day. In the `_celery.py` file, edit the `beat_schedule` dictionary by adjusting the `hour`, `minute`, and `day_of_week` parameters to your desired values. 

## Resources

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Celery](https://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
* [Twilio](https://www.twilio.com/)
