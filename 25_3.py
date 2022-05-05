import pytest

from selenium import webdriver #подключение библиотеки
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   # получение объекта веб-драйвера для нужного браузера
   # pytest.driver = webdriver.Chrome('F:\SF\SeleniumDrivers/chromedriver.exe')
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument('--kiosk')
   pytest.driver = webdriver.Chrome('F:\SF\SeleniumDrivers/chromedriver.exe', chrome_options = chrome_options)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.implicitly_wait(10)
   pytest.driver.quit()


def test_show_my_pets():
   pytest.driver.implicitly_wait(3)
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('trubalexan@gmail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('Pet2021Friends')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # pytest.driver.implicitly_wait(5)
   # # Проверяем, что мы оказались на главной странице пользователя
   # assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   # btn_my_pets = pytest.driver.find_element_by_link_text('Мои питомцы')
   # btn_my_pets.click()

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".card-title")))
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".text-center")))
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print('PyCharm')