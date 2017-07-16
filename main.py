from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open("input.txt") as inputFile:
    log = inputFile.readlines()

for i in log:

    varRollNo = i.split(',')[0]
    varMotherName = i.split(',')[1].strip('\n')
    driver = webdriver.Chrome()
    driver.get("http://results.unipune.ac.in/SE2014.aspx?Course_Code=70412&Course_Name=BE2012")
    rollNo = driver.find_element_by_id("ContentPlaceHolder1_txtSeatno")
    rollNo.send_keys(varRollNo)
    motherName = driver.find_element_by_id("ContentPlaceHolder1_txtMother")
    motherName.send_keys(varMotherName)
    motherName.send_keys(Keys.ENTER)
    list = []
    for element in driver.find_elements_by_tag_name('tr'):
           list.append(element.text)
    result  = list[-4].strip(" ")[-9:].split('/')
    perc = int(result[0])/int(result[1])*100;
    print(list[1].split('Mother Name')[0]+" "+list[-4].strip(" ")+" Percentage: "+str(round(perc,2))+"%")
    driver.close()
