# COVID-19_InfoBot
This a primarily a web scraping project integrated with a priliminary response handling algorithm that I have built. The web scraping is done using selenium python and the pyttsx3 library is used for audio responses.

I personally use it for getting updated information from the websites I trust. However, you can choose any websites from where you will like to import data.

# Features

Information: Total cases, total recovered, total deaths - Headlines need advanced web scraping [Wil Include later] <br />
Audio responses <br />
Choice for male / female voice assisstant <br />
Advanced error handling conditions <br />
Mental health support <br />
Includes wide support for negative and positive responses <br />
Accepts voice commands for hands-free experience [Available in the upgraded version] <br />
Accessible to blind and deaf people [Available in the upgraded version] <br />
Includes preliminary slang support <br />
Includes exception handling for personal questions <br />

I would really love if someone could add more features to it.

# Algorithm

The algorithm breaks down the user inputs to seperate words and converts them to lower case [i.e. makes it case insensitive]. Then it matches these words with the keyword-tags database I created. Then based on the tags identified in the user response, the algorithm obtains latest information through web scraping and delivers customized outputs through the device audio.

# Set-up
Requires prior installation of selenium python, chromedriver, python 3.0+ and pyttsx3 library. Additionally, the source code uses ChromeDriver, but you can use the webdriver of your choice.
