#this program solves the New York Times' Wordle game

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time




driver_service = Service(executable_path=r"C:\Users\Harish Kanagal\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
actions = ActionChains(driver)
#manifest = ["stare", "stabe", "zzzzz"]
#manifest = "hi"
#cont_state = True
driver.get("https://www.nytimes.com/games/wordle/main.bfba912f.js")

dd = driver.find_element(by=By.XPATH, value="/html/body/pre")
dta = dd.text
    #******

manifest = (dta[dta.find('Ma=[')+4 : dta.rfind('],Oa=')]).split(',')
    #exec(dta[dta.find('Ma=[')+1 : dta.rfind('],Ra=')+1])

for ndx, word in enumerate(manifest):
    manifest[ndx] = word.replace('"', '')
present_letters=[]    
#print(manifest)
    #print(word)
#time.sleep(20)
def updateList(wd, pos, letter, letter_state):
    #removes refrenced 
    global manifest
    #print("hihi")
    if(letter_state == 'absent'):
        #print(letter)
        #for word in manifest:
            #print("a")
            #if letter in word:
                #print(word)
                #manifest.remove(word)
                #print(manifest)
            
            #if else needed because like in the word 'sissy' the first 's' will show
            #as present and the second 's' will show as absent
            #we still want to keep the words with s in them, not delete them because the second
            #'s was absent
        #if letter in present_letters:
        manifest = [ word for word in manifest if not word[pos] == letter ]
                
        if wd.count(letter) == 1:
            manifest = [word for word in manifest if not letter in word]

    elif(letter_state == 'present'):
        present_letters.append(letter)
        #for word in manifest:
            #if word[pos] == letter:
                #manifest.remove(word)
        manifest = [ word for word in manifest if not letter == word[pos] ]
        manifest = [ word for word in manifest if letter in word ]
    elif(letter_state == 'correct'):
        #for word in manifest:
            #if word[pos] != letter:
                #manifest.remove(word)
        manifest = [ word for word in manifest if letter == word[pos] ]
        present_letters.append(letter)
    #cont_state = True
    #print(cont_state)
#loads data into manifest


#opens wordle, closes instructional overlay
def openWordle():
    driver.get("https://www.nytimes.com/games/wordle/index.html")

    #row1_xpath=r"//*[@id="board"]/game-row[1]//div/game-tile[1]//div"
    #time.sleep(5)
    #query = "Hello World!"
    #driver.find_element_by_id(id)
    #search = driver.find_element_by_name('q')
    #search = driver.find_element(by=By.NAME, value='q')
    #search.send_keys(query)
    #search.send_keys(Keys.RETURN)

    time.sleep(1)
    

    #search = driver.find_element_by_name('game')
    #driver.find_element_by_xpath('//*[@id="game"]')
    #actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0,0)

    ###this clears the instructions overlay at the beginning
    actions.move_to_element_with_offset(driver.find_element(by=By.TAG_NAME, value="body"), 0,0)
    actions.move_by_offset(50, 50).click().perform()
    #elem = driver.find_element_by_css_selector(".some > selector")
    #ac = ActionChains(driver)
    #ac.move_to_element(elem).move_by_offset(x_offset, y_offset).click().perform()


    #a = actions(driver)
    #a.moveToElement(search).click()

def playGame():
    #begins playing game
    try_word = "stare"
    #until all tiles are correct
    for letter in try_word:
        actions.send_keys(letter)
        actions.perform()
        time.sleep(1/4)
    entertime = driver.find_element(by=By.TAG_NAME, value="body")
    entertime.send_keys(Keys.RETURN)
    #update_dict()
    for row in range(4):
        for let in range(5):
            #gets letter name
            letter = driver.execute_script('return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(%s)").shadowRoot.querySelector("div > game-tile:nth-child(%s)").getAttribute("letter")'% (str(row+1), str(let+1)))
            #returns state (present, correct, or absent)
            letter_state = driver.execute_script('return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(%s)").shadowRoot.querySelector("div > game-tile:nth-child(%s)").getAttribute("evaluation")'% (str(row+1), str(let+1)))
            #print(letter_state)
            #print(let,letter, letter_state)
            #cont_state = False
            #if letter_state == "present":
                #print(letter)
                #for word in manifest:
                    #if letter not in word:
                        #manifest.remove(word)
                        
            
            updateList(try_word, let, letter, letter_state)
            time.sleep(1/2)
        #time.sleep(2)
        ####below is the progression manifest \/
        #########print(manifest)
        try_word = manifest[0]
        for letter in try_word:
            actions.send_keys(letter)
            actions.perform()
            time.sleep(1/4)
        entertime = driver.find_element(by=By.TAG_NAME, value="body")
        entertime.send_keys(Keys.RETURN)
        #time.sleep(3)
    #txtgrd = grd.text
    #print(grd)
    #print(manifest)
    
#loadWords()
#print(manifest)
openWordle()
playGame()
