from selenium import webdriver
import time

# Path to your Chrome user data
user_data_dir = 'C:/Users/zaida/AppData/Local/Google/Chrome for Testing/User Data'
profile_directory = 'Default' 

# Path to your Chrome (for testing) executable
chrome_executable_path = 'F:/chrome-win64/chrome.exe' 

# Set Chrome options
options = webdriver.ChromeOptions()
options.binary_location = chrome_executable_path

options.add_argument(f'user-data-dir={user_data_dir}')
options.add_argument(f'profile-directory={profile_directory}')

# Initialize the WebDriver with these options
driver = webdriver.Chrome(options=options)

# Navigate to website
driver.get("https://chat.openai.com/")

# Wait for search results to load
driver.implicitly_wait(2)

time.sleep(2)

text_area = driver.find_element(by="xpath", value="//textarea[@id='prompt-textarea']")
text_area.click()

init_input = '''We are playing a trivia, so for every question I ask and you answer correctly, you get one point. Rules: for every question just give me answer, no extra words/ information'''

text_area.send_keys(init_input)
text_area.submit()
time.sleep(2)

conversation_number = 5 # All odd ones are AI, all even ones are human
while True:
    text_area = driver.find_element(by="xpath", value="//textarea[@id='prompt-textarea']")
    text_area.click()
    print("-"*20)
    userinput= input("Enter your input or #quit: ")
    if userinput == "#quit":
        break
    
    text_area.send_keys(userinput)
    text_area.submit()
    
    while True:
        try:
            send_button = driver.find_element(by="xpath", value="//button[@data-testid='send-button']")
            break
        except:
            pass
    # send_button = driver.find_element(by="xpath", value="//button[@data-testid='send-button']")
    
    # driver.implicitly_wait(10)
    time.sleep(1)
    answer = driver.find_element(by="xpath", value=f"//div[@data-testid='conversation-turn-{conversation_number}']")
    
    # print(answer.text[answer.text.find("\n"):])
    print(answer.text[8:])
    time.sleep(1)
    conversation_number += 2