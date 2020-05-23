# For web scrapping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# For voice interactions
import time
import pyttsx3
import speech_recognition as sr

## Features to include: - Planning Phase
# Countries : Canada, India, US, Germany, Russia, Global - Added
# Information: Total cases, headlines, total recovered, total deaths, recoveries - Headlines need advanced web scraping
# Suggesstions to utilize time in lockdown, productive and found.
# Audio responses - Done
# Choice for male / female voice - Done
# Mental health support


# Setting up the audio
converter = pyttsx3.init()
converter.setProperty('rate', 185) # Speed of voice output
converter.setProperty('volume', 100) # Loudness of the voice
r = sr.Recognizer()

# Providing alternate choices for infobot
gender = input('Do you prefer male or female assisstant: ')
while(True):
    if 'male' in gender.lower().split():
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        botName = 'Hetav'
        break
    elif 'female' in gender.lower().split():
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        botName = 'Angelina'
        break
    else:
        converter.say("Sorry, I expected to recieve male or female as a response, try again")
        converter.runAndWait()
        gender = input('Do you prefer male or female assisstant: ')

converter.setProperty('voice', voice_id)

countrylist = ['canada','india', 'us', 'russia', 'germany', 'global']

# URL's needed for web scrapping
countries = {'canada': 'https://www.worldometers.info/coronavirus/country/canada/',
             'india': 'https://www.worldometers.info/coronavirus/country/india/',
            'us':'https://www.worldometers.info/coronavirus/country/us/',
             'russia': 'https://www.worldometers.info/coronavirus/country/russia/',
            'germany':'https://www.worldometers.info/coronavirus/country/germany/',
             'global': 'https://www.worldometers.info/coronavirus/'}

# Database of key words
corona = ['chinese virus', 'covid 19', 'covid-19', 'china virus', 'corona', 'virus', 'corona virus', 'covid', 'wuhan virus', 'pandemic']
total = ['amount','sum','overall', 'full', 'total', 'total', 'gross', 'entire']
headlines = ['headlines', 'latest news', 'news', 'updates', 'developments', 'highlights']
recovered = ['recovered', 'recoveries', 'recovery', 'healed', 'cured', 'survived', 'survivors']
deaths = ['deaths', 'died', 'death', 'succumbed', 'dying', 'killed', 'kill']
new = ['increase', 'increased', 'new', 'newly', 'recent', 'recently']
cases = ['cases', 'case', 'recently added cases', 'infected', 'detected', 'affected']
globalNews = ['global', 'world', 'worldwide', 'pitbull', 'international', 'earth', 'all around']
countriesSelect = [['canada'], ['india'], ['us', 'america', 'united', 'states'], ['germany'], ['russia', 'ussr'], globalNews]
prevent = ['prevent', 'prevention', 'preventative', 'precautions', 'precautious', 'care', 'saved', 'save', 'safe', 'secure', 'safety']
symptoms = ['symptoms', 'signs', 'sign', 'symptom', 'indication', 'warning', 'have', 'I']
negative = ['no', 'nothing', 'never', 'negative', 'none', 'nope', 'nah', 'off']
positive = ['yes','yep', 'yeah', 'yo', 'indeed', 'sure', 'yup', 'fosure', 'yea', 'ya']
personal = ['you', 'yours', 'your']
mentalHealth = ['sad', 'anxious', 'fear', 'scared', 'hopeless', 'useless', 'bad', 'worse', 'worst', 'worried', 'depression', 'breakdown', 'clueless']

# Bot starts interacting
print(botName + ': '+"Hello, I am " + botName + ", your personal covid 19 assistant. I provide corona specific information about Canada, India, US, Russia and Germany along with the global situation")
converter.say("Hello, I am " + botName + ", your personel covid 19 assistant")
converter.say("I provide corona specific information about Canada, India, US, Russia and Germany along with the global situation")
converter.runAndWait()

# Setting up the webdriver using selenium python
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.binary_location = "/usr/bin/chromium"


# Main Loop
while(True):

    # Initializing booleans for indentifying key words
    url = None
    total_needed = False
    headlines_needed = False
    recoveries_needed = False
    death_needed = False
    new_needed = False
    cases_needed = False
    corona_overall = False
    prevention = False
    symptoms_info = False
    counrty_identified = False
    negat = False
    repBool = False
    personalBool = False
    mentalBool = False

    print(botName + ': '+'So what can I do for you?')
    converter.say("So what can I do for you?")
    converter.runAndWait()

    # Processing user input
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

    responseOrg = format(text)
    response = responseOrg.lower().split()

    # Getting the country and URL
    for elem in countriesSelect:
        for keyword in elem:
            if keyword in response:
                countryInterest = elem[0]
                counrty_identified = True
                url = countries[elem[0]]
                break

    # Finding the info that should be delivered

    # Comparing response with key-words data base
    for elem in total:
        if elem in response:
            total_needed = True

    for elem in negative:
        if elem in response:
            negat = True

    for elem in headlines:
        if elem in response:
            headlines_needed = True

    for elem in recovered:
        if elem in response:
            recoveries_needed = True

    for elem in deaths:
        if elem in response:
            death_needed = True

    for elem in new:
        if elem in response:
            new_needed = True

    for elem in cases:
        if elem in response:
            cases_needed = True

    for elem in prevent:
        if elem in response:
            prevention = True

    for elem in symptoms:
        if elem in response:
            symptoms_info = True

    for elem in corona:
        if elem in response:
            corona_overall = True

    for elem in personal:
        if elem in response:
            personalBool = True

    for elem in mentalHealth:
        if elem in response:
            mentalBool = True

    # For testing purposes

    # If negative response
    if personalBool:
        print("I do not answer personal questions, sorry")
        converter.say("I do not answer personal questions, sorry")
        converter.runAndWait()

    else:
        if (negat):
            print(botName + ': '+"Goodbye see you soon, till then stay safe, stay indoors!")
            converter.say("Goodbye see you soon, till then stay safe, stay indoors!")
            converter.runAndWait()
            break

        elif mentalBool:
            # Web scraping mental health info
            driver = webdriver.Chrome("D:\Python files\Web Automation\chromedriver.exe")
            driver.get('https://www.nature.com/articles/d41586-020-00933-5')
            content = driver.find_element_by_xpath('//*[@id="content"]').text
            print(content[2587:3296])
            converter.say(content[2587:3296])
            converter.say(",,,Hey,, I am the creator of this bot speaking,, we all are facing difficulties and are struggling during this hard time, but remember, that tough times never lats, but tough people do!, so cheer up mate")
            converter.runAndWait()

        # Algorithm for deciding a relevant response
        elif (url != None):
            # Web scraping latest information
            driver = webdriver.Chrome("D:\Python files\Web Automation\chromedriver.exe")
            driver.get(url)
            info = driver.find_elements_by_xpath('//*[@id="maincounter-wrap"]/div/span')
            infected = info[0].text
            death = info[1].text
            recovered = info[2].text
            driver.close()

            # The bot chooses response based on user's input

            if (total_needed or recoveries_needed or death_needed or corona_overall):

                if total_needed or corona_overall:
                    print(botName + ': '+"Cases in", countryInterest.title(),":", infected)
                    converter.say(countryInterest + "currently has" + str(infected) + 'cases detected.')
                    converter.runAndWait()

                elif recoveries_needed or corona_overall:
                    print(botName + ': '+"Recoveries in", countryInterest.title(),":", recovered)
                    converter.say("Fortunately" + str(recovered)+"have recovered in " + countryInterest.title())
                    converter.runAndWait()

                elif death_needed or corona_overall:
                    print(botName + ': '+"Deaths in", countryInterest.title(),":", death)
                    converter.say("Unfortunately" + str(death)+"have died in " + countryInterest.title())
                    converter.runAndWait()

            elif counrty_identified:

                print(botName + ': '+"Cases in", countryInterest.title(),":", infected)
                converter.say(countryInterest.title() + "currently has" + str(infected) + 'cases detected.')
                converter.runAndWait()
                print(botName + ': '+"Recoveries in", countryInterest.title(),":", recovered)
                converter.say("Fortunately" + str(recovered)+"have recovered in" + countryInterest.title())
                converter.runAndWait()
                print(botName + ': '+"Deaths in", countryInterest.title(),":", death)
                converter.say("Unfortunately" + str(death)+"have died in" + countryInterest.title())
                converter.runAndWait()

        else:
            # If database cannot handle the user's question


            if corona_overall == False and not prevention:

                converter.say("I don't see that being related to corona, however I'll search on the internet for you")
                converter.runAndWait()
                # Questions that do not relate to corona
                driver = webdriver.Chrome("D:\Python files\Web Automation\chromedriver.exe")
                driver.get('https://www.google.com/')
                searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
                searchbox.send_keys(responseOrg)
                searchbox.send_keys(Keys.ENTER)
                converter.say("Your tab has been opened!")
                converter.runAndWait()

            else:
                # Webscraping general WHO guidlines

                # For General Corona Queries
                driver = webdriver.Chrome("D:\Python files\Web Automation\chromedriver.exe")
                driver.get('https://www.who.int/health-topics/coronavirus#tab=tab_1')
                infoGeneral = str(driver.find_elements_by_class_name('sf_colsIn')[51].text)[:245]

                # For preventative info
                if prevention:

                    infoGeneral += """To prevent infection and to slow transmission of COVID-19, do the following: Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub.
                                    Maintain at least 1 metre distance between you and people coughing or sneezing.
                                    Avoid touching your face. Cover your mouth and nose when coughing or sneezing.
                                    Stay home if you feel unwell."""

                # For symptoms related info
                if symptoms_info:
                    infoGeneral += "Common symptoms include fever, dry cough, tiredness and chest pain."

                driver.close()
                print(infoGeneral)
                converter.say(infoGeneral)
                converter.runAndWait()

    print(botName + ': '+"Do you wish to ask another question about corona?")
    converter.say("Do you wish to ask another question about corona?") # Iterating
    converter.runAndWait()

    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

    repeat = format(text)

    for elem in positive:
        if elem in repeat.lower().split():
            repBool = True

    if not repBool:
        print(botName + ': '+"Goodbye, see you soon, till then stay safe, stay indoors!")
        converter.say("Goodbye, see you soon, till then stay safe, stay indoors!")
        converter.runAndWait()
        break
