# PYTHON Example for WebScraping on OneLiners
from selenium import webdriver
from time import sleep
import os

def print_gap(x):
    for i in range(x):
        print()
    return

def create_driver():
    #Change chrome driver path accordingly
    chrome_driver = "C:\Program Files\Google\Chrome\chromedriver.exe"
    created_driver = webdriver.Chrome(executable_path = chrome_driver)
    return created_driver

def search_google(driver, topic_name):
    topic_name_spliited = topic_name.split()

    topic_to_search = "https://google.com/search?q="

    for i in topic_name_spliited:
        topic_to_search = topic_to_search + ("+" + i)

    # topic-to-search  # https://google.com/search?q=+funniest+one+liners
    driver.get(topic_to_search)

    sleep(3)


def search_link(driver,link_number):
    # according to google search engine every link has been given class name 'g'
    list_searched = driver.find_elements_by_class_name("g")


    """
    for i in list_searched:
        print(i)

    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="369f6c59-875c-44d8-bf9e-f9134022114d")>
    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="f4a5164e-3dc3-451e-83e6-58523ef4ec8c")>
    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="472dfe60-7260-4ec3-b2eb-1ff48f8235b3")>
    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="c639bafa-f94e-4cc1-ab11-b581722b3fed")>
    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="05dcd8f4-6d7b-4573-957d-e95b1c7db317")>
    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="fbd2eb4d-6c0c-4549-b7e1-8d5c7b395a14")>
    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="1d3af5e3-1e60-415f-b298-e878f3bb3a3c")>
    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="01557e35-6976-4b93-89cf-b1339746b982")>
    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="ef4c2454-f594-4cb6-88f1-558a361452d8")>
    <selenium.webdriver.remote.webelement.WebElement (session="aa5f411d8fd399854c12cb0850674333", element="cf8d6ca7-5cbe-4bf2-be07-15ec30ecf997")>

    """

    # clicking the link according to matriculation index + 1 as described 
    list_searched[link_number].find_element_by_class_name("yuRUbf").click()
    return 

def get_content(driver,num):
    content = "#----------Some content from web page:--------#\n\n"
    start = 5      # index for xpath from which oneliners starts
    ss_list = []
    elems = driver.find_elements_by_tag_name("h2")
    # fetching data from web page to show on console
    for i in range(num):
        elem = elems[start + i]
        content += (f"{str(i+1)}: {elem.text[2:]}\n\n")      
        # moving window down to element and then taking its content and saving screenshots 
        a=webdriver.ActionChains(driver)
        a.move_to_element(elem).perform()
        ss_name =  os.getcwd() + f"\ScreenShots\OneLiner_{i+1}.png"
        driver.get_screenshot_as_file(ss_name)
        ss_list.append(ss_name)
        sleep(1)

    return content,ss_list




def main():
    return    

if __name__=="__main__":

    topic_to_search = "chandler's funniest one liners"
    matriculation_number = 4

    driver = create_driver()
    print_gap(2)
    print("#-------------driver created------------#")


    try : 
        search_google(driver, topic_to_search)
        print_gap(2)
        print("#---------google search is done--------#")



        search_link(driver, matriculation_number )
        print_gap(2)
        print("#------------link is clicked-----------#")

        # screenshots = []

        # for i in [1,2,3,4,5]:
        #     screenshots.append(os.getcwd() + f"\ScreenShots\OneLiner_{i}.png")

        content,screenshots  = get_content(driver, 5)
        
        # printing interesting oneliners taken from web page and then showing screenshots saved
        print_gap(2)
        print(content)

    except Exception as err: 
        print(f"\n\n\n !!!!! SOME ERROR !!!!!\n>       {err}")
    finally:
        driver.quit()
