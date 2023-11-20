from selenium import webdriver
import time
import pyperclip

# Path to your Chrome user data
user_data_dir = 'C:/Users/zaida/AppData/Local/Google/Chrome for Testing/User Data'
profile_directory = 'Default' 

# Path to your Chrome (for testing) executable
chrome_executable_path = 'F:/chrome-win64/chrome.exe' 

# Set Chrome options
options = webdriver.ChromeOptions()
options.binary_location = chrome_executable_path
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
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

conversation_number = 5

# Clear the clipboard when the program starts
pyperclip.copy("")
response_text = ""
while True:
    clipboard_content = pyperclip.paste()
    while response_text == clipboard_content:
        clipboard_content = pyperclip.paste()
        time.sleep(0.5)
    # Check for new clipboard content
    if clipboard_content.strip() and clipboard_content.strip() != "#quit":
        userinput = clipboard_content
        userinput = userinput.replace("\n", " ")
        text_area = driver.find_element(by="xpath", value="//textarea[@id='prompt-textarea']")
        text_area.click()
        text_area.send_keys(userinput)
        time.sleep(0.5)
        text_area.submit()

        while True:
            try:
                send_button = driver.find_element(by="xpath", value="//button[@data-testid='send-button']")
                break
            except:
                pass

        time.sleep(1)
        answer = driver.find_element(by="xpath", value=f"//div[@data-testid='conversation-turn-{conversation_number}']")
        
        response_text = answer.text[8:]
        print(response_text)
        pyperclip.copy(response_text)  # Copy response to clipboard
        time.sleep(1)
        conversation_number += 2

        # Clear the clipboard after processing the command

    elif clipboard_content.strip() == "#quit":
        break

    time.sleep(0.5)  # Small delay to avoid high CPU usage

# Close the browser
driver.quit()
