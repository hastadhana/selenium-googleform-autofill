from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# first of all, get temperature from input
temp = input("Masukkan suhu hasil pemeriksaan : ")

# mandatory parameters
name = "John Doe"
age = 27
position = "Development"
contact_history = "Teman kantor"
form_url = ""


option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)

browser.get(form_url)

textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

# browser.implicitly_wait(1.5)
sleep(1.4)

# nama
textboxes[0].send_keys(name)
sleep(0.5)
# usia
textboxes[1].send_keys(age)
sleep(0.5)
# jenis kelamin
radiobuttons[0].click()
sleep(0.5)
# posisi
textboxes[2].send_keys(position)
sleep(1.3)


# initiate page transition, e.g.:
submitbutton.click()



# page 2 ========================================================================================

# browser.implicitly_wait(1.5)
sleep(1.4)

textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
textareas = browser.find_elements_by_class_name("quantumWizTextinputPapertextareaInput")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")


# Kondisi yang dialami saat ini
checkboxes[1].click()
sleep(0.55)
checkboxes[3].click()
sleep(0.55)
checkboxes[5].click()
sleep(0.55)
checkboxes[7].click()
sleep(0.55)
checkboxes[9].click()
sleep(0.55)
checkboxes[11].click()
sleep(0.55)

# Suhu badan saat ini
textboxes[0].send_keys(temp)
sleep(0.55)

# force to focus the element's view so it's clickable
ActionChains(browser).move_to_element(checkboxes[25]).click(checkboxes[25]).perform()

# Transportasi yang digunakan untuk ke kantor (24 jam terakhir) (unused, replaced with code above)
# checkboxes[13].click()
sleep(0.7)

# Tempat-tempat yang disinggahi (24 jam terakhir)
checkboxes[44].click()
sleep(0.6)

# Riwayat kontak
textareas[0].send_keys(contact_history)
sleep(1.3)




# initiate next page transition
submitbutton[1].click()



# page 3 ========================================================================================

# browser.implicitly_wait(1.5)
sleep(1.4)

submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")

checkboxes[0].click()
sleep(0.6)

# submit the final page
submitbutton[1].click()

sleep(2)

browser.close()