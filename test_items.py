from selenium.webdriver.common.by import By
from time import sleep
url = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_search_button_add_to_basket(browser):
    browser.get(url)
    sleep(10)

    buttons = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    # print('Button_name:', buttons[0].get_attribute('value'))

    assert len(buttons) == 1, 'No search btn-add-to-basket in page'







