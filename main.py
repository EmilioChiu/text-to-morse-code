from selenium import webdriver
import time

CHROME_PATH = "c:/development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.get("https://es.wikipedia.org/wiki/C%C3%B3digo_morse")

time.sleep(2)

table = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody')
all_letters = [letter.text for letter in table.find_elements_by_css_selector("tr td") if letter.text != " "]

normal_alphabet = []
morse_alphabet = []

for letter in range(len(all_letters)):
    if (letter + 1) % 2 == 0:
        morse_alphabet.append(all_letters[letter])
    else:
        normal_alphabet.append(all_letters[letter])

dictionary = {normal_alphabet[letter]: morse_alphabet[letter] for letter in range(len(normal_alphabet))}

to_convert = input("normal text to morse code: ")
morse_code = ""

for letter in to_convert:
    if letter.capitalize() in dictionary:
        morse_code += dictionary[letter.capitalize()]
        morse_code += ", "
    else:
        morse_code += letter

print(morse_code)
