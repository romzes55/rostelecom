from loginPassord import valid_mail, valid_password
from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест 1. Вход в ЛК по почте с правильными, валидными данными
def test_authorization(autorRostelecom):
    # Проверяем что зашли в ЛК. Сравниваем фамилию, которую указали при регистрации с той что указана в ЛК.
    assert pytest.driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == 'Романов'
    pytest.driver.quit()


# Тест 2. Вход в ЛК по почте с правильными, валидными данными с пробелом вначале почты
def test_authorization_space_mail(authorization_space_mail):
    # Проверяем что зашли в ЛК. Сравниваем фамилию, которую указали при регистрации с той что указана в ЛК.
    assert pytest.driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == 'Романов'
    pytest.driver.quit()


# Тест 3. Вход в ЛК по почте с правильными, валидными данными с пробелом в конце почты
def test_authorization_space_mail_2(authorization_space_mail_2):
    # Проверяем что зашли в ЛК. Сравниваем фамилию, которую указали при регистрации с той что указана в ЛК.
    assert pytest.driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == 'Романов'
    pytest.driver.quit()


# Тест 4. Вход в ЛК по почте с правильными, валидными данными с пробелом в начале пароля
def test_authorization_space_password(authorization_space_password):
    # Проверяем что зашли в ЛК. Сравниваем фамилию, которую указали при регистрации с той что указана в ЛК.
    assert pytest.driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == 'Романов'
    pytest.driver.quit()


# Тест 5. Вход в ЛК по почте с правильными, валидными данными с пробелом в конце пароля
def test_authorization_space_password_2(authorization_space_password_2):
    # Проверяем что зашли в ЛК. Сравниваем фамилию, которую указали при регистрации с той что указана в ЛК.
    assert pytest.driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == 'Романов'
    pytest.driver.quit()


# Тест 6. Вход в ЛК по почте с пустыми полями ввода почта и пароль
def test_authorization_empty(authorization_empty):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 7. Вход в ЛК по почте с пустым полем почта и правильным полем пароль
def test_authorization_empty_mail(authorization_empty_mail):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 8. Вход в ЛК по почте с пустым полем пароль и правильным полем почта
def test_authorization_empty_password(authorization_empty_password):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 9. Вход в ЛК по почте с невалидным полем почта и правильным паролем
def test_registration_not_valid_mail(registration_not_valid_mail):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 10. Вход в ЛК по почте с невалидным полем пароль и правильным полем почта
def test_registration_not_valid_password(registration_not_valid_password):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 11. Вход в ЛК по померу телефона с правильными и валидными данными, но для полей "Почта" и "Пароль"
def test_registration_phone_not_valid(registration_phone_not_valid):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 12. Вход в ЛК по померу телефона с пустыми полями
def test_registration_phone_empty(registration_phone_empty):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 13. Вход в ЛК по логину с правильными данными для полей "почта" и "пароль"
def test_registration_login_not_valid(registration_login_not_valid):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 14. Вход в ЛК по логину с пустыми полями
def test_registration_login_empty(registration_login_not_valid):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 15. Вход в ЛК по лицевому счету с правильными данными для полей "почта" и "пароль"
def test_registration_ls_not_valid(registration_ls_not_valid):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()


# Тест 16. Вход в ЛК по лицевому счету с пустыми полями
def test_registration_ls_empty(registration_ls_empty):
    # Проверяем что не зашли в ЛК и остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Авторизация'
    pytest.driver.quit()
