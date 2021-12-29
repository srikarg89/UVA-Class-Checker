# UVA-Class-Checker
Sends a text message when a class's quantity changes on Lou's List.

## Usage
1. Download the PhantomJS driver and make sure you can use it with Python's selenium.
2. Install Python's selenium and twilio libraries
3. Create a Twilio account and note down credentials.
4. Copy secret.sample.py into secret.py and replace blank credentials with your Twilio account credentials.
5. Go to the Lou's List semester page of the semester that you want to check
6. Copy the URL to the semester link into SEMESTER_URL in _bot.py_.
7. Using google developer tools, find the xpath of the link that you want to check. Change the ELEMENT_PATH value in _bot.py_ to match your xpath.

## Warning
Please don't abuse this by trying to attack the Lou's List website. The website only updates every 30 minutes, so a 900 second delay should be more than low enough.
