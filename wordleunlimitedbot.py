#solvs unlimited wordle

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver_service = Service(executable_path=r"C:\Users\Harish Kanagal\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
actions = ActionChains(driver)

driver.get("http://www.cs.ucf.edu/~dmarino/ucf/dictionary.txt")


dd = driver.find_element(by=By.XPATH, value="/html/body/pre")
dta = dd.text
                            #******

manifest = (dta.split('\n'))
                            #exec(dta[dta.find('Ma=[')+1 : dta.rfind('],Ra=')+1])

#for ndx, word in enumerate(manifest):
 #  manifest[ndx] = word.replace('"', '')
manifest = [ word for word in manifest if len(word) == 5 ]
#print(manifest)
originalManifest = manifest.copy()
present_letters=[]    

#print(manifest)
def origcpy():
    global manifest
    manifest = originalManifest.copy()
    present_letters.clear()
    #playGame()
def updateList(wd, pos, letter, letter_state):
    global manifest
    #print(letter, letter_state)
    if(letter_state == 'RowL-letter letter-absent'):
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
        

    elif(letter_state == 'RowL-letter letter-elsewhere'):
        present_letters.append(letter)
        #print(letter)
        #for word in manifest:
            #if word[pos] == letter:
                #manifest.remove(word)
        manifest = [ word for word in manifest if not letter == word[pos] ]
        manifest = [ word for word in manifest if letter in word ]
    elif(letter_state == 'RowL-letter letter-correct'):
        #for word in manifest:
            #if word[pos] != letter:
                #manifest.remove(word)
        manifest = [ word for word in manifest if letter == word[pos] ]
        present_letters.append(letter)
        



driver.get("https://www.wordleunlimited.com/")
time.sleep(1)

def playGame():
    global manifest
    try_word = "stare"

    for letter in try_word:
        actions.send_keys(letter)
        actions.perform()
        time.sleep(1/4)
    entertime = driver.find_element(by=By.TAG_NAME, value="body")
    entertime.send_keys(Keys.RETURN)

    #print(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]").get_attribute("className"))
        
    
    for row in range(2,7):
        #find_element(by=By.XPATH, value=xpath)
        ended_or_not = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[1]/div[9]').text
        #print(len(ended_or_not))
        if(len(ended_or_not) > 0):
            origcpy()
            break
        for let in range(1,6):
            letter = (driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div[%s]/div[%s]" %(str(row), str(let))).text).lower()
            #print(letter=='S')
            letter_state = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div[%s]/div[%s]"%(str(row), str(let))).get_attribute("className")
            updateList(try_word, let-1, letter, letter_state)
            ############print((manifest))
            #print(try_word, let-1, letter, letter_state)
            #time.sleep(1/4)

        
        try_word = manifest[0]
        for letter in try_word:
            actions.send_keys(letter)
            actions.perform()
            time.sleep(1/4)
        entertime = driver.find_element(by=By.TAG_NAME, value="body")
        entertime.send_keys(Keys.RETURN)
    try_word = "stare"
    manifest = originalManifest.copy()
    time.sleep(1)
    playGame()

#c()
#openWordle()
playGame()
