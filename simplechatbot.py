import datetime
import requests
from bs4 import BeautifulSoup
import webbrowser, googlesearch
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def weather():
    city_inp = input("Enter the Name of City ->  ")
    if city_inp == "" or city_inp == " ":
        city_inp = 'Dubai'
    city = city_inp+" weather"
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(weather+"°C")
    print(f"{int(weather)*(9/5)+32} °F")

class chatbot():
    def __init__(self):
        pass
    def greet(self):
        self.gc = "Great Fine good awesome super not no well nice perfect super healthy bad sick"
        print("Bot: Hi! How are you doing?")
        self.user = input("User: ")
        self.break_yrn = False
        def search_keywords():
            for i in self.gc.split():
                self.question = self.user.lower().replace("?", '').replace(".", '').replace(',', '').replace("!", '').split()
                if i.lower() in self.question and i != 'not' or i.lower() in self.question and i != 'no' or i.lower() in self.question and i != 'bad' or i.lower() in self.question and i != 'sick':
        
                    print('Bot: Great! \n How can I help you?')
                    self.break_yrn = False
                    break
                else:
                    if self.user.split()[0] == 'not' or self.user.split()[0] == 'no':
                        self.break_yrn = True
                        break
                    else:
                        print("Didn't get that")
                        break
            if self.break_yrn == True:
                print("Bot: Oh, Take Care...")
                print("Bot: Is there any way that I can help you?")
                self.help_bot()
            else:
                self.help_bot()
        if "not bad" in self.user.lower() or 'not sick' in self.user.lower() or 'not ill' in self.user.lower():
            print('Bot: Great! \n How can I help you?')
            self.help_bot()
        else:
            search_keywords()   
        
    def help_bot(self):
        def time_def():
            format_string_time = '%H:%M:%S | %A, %d %B %Y'
            a_datetime_datetime = datetime.datetime.now()
            self.current_time = a_datetime_datetime.strftime(format_string_time)      
            print(f"The Current time is: {self.current_time}")

        def math_function():
            print("Bot: Enter the math expression")
            user_math = input("User: ")
            try: 
                print(eval(user_math))
            except:
                print("Bot: Oops, Could'nt solve that.")

        def google():
            def open_web(link):
                webbrowser.open(link)

            self.search_to = input("User: Google Search: ")
            self.link_list = []
            self.num = 1
            for j in googlesearch.search(self.search_to, tld="com", num=20, stop=20, pause=2):
                print(f'{self.num}) {j}')
                self.num += 1
                self.link_list.append(j)

            print('Bot: Enter Link Number (enter NONE to cancel): ')
            self.open_link = input("User: ")
            if self.open_link.lower() == "none":
                pass
            else:
                try:
                    open_link = int(self.open_link)-1
                except:
                    print("Bot: Only Numbers expected")
                open_web(self.link_list[open_link])  

        self.user_help = input("User: ")
        self.user_help_edit = self.user_help.lower().replace("?", '').replace(".", '').split()
        if "time" in self.user_help_edit:
            time_def()
        
        elif "date" in self.user_help_edit:      
            time_def()
        
        elif "day" in self.user_help_edit:     
            time_def()

        elif "temperature" in self.user_help_edit:     
            weather()

        elif "weather" in self.user_help_edit:     
            weather()

        elif "condition" in self.user_help_edit:     
            weather()

        elif "google" in self.user_help_edit or "open google" in self.user_help_edit or "search google" in self.user_help_edit:
            google()

        elif 'math' in self.user_help_edit or 'maths' in self.user_help_edit or 'mathematics' in self.user_help_edit:
            math_function()

        else:
            print("Bot: Oops, I dont think I exactly understand it.")

bot = chatbot()
bot.greet()