import pytest
from selenium import webdriver
from loginPassord import valid_mail, valid_password, valid_mail_space, \
    valid_mail_space2, valid_password_space, valid_password_space2
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture(autouse=True)
def authorization_page():
    link = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c" \
           "&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=b9cae24e" \
           "-d8be-46a7-b605-482d46a84f7c&theme&auth_type "

    pytest.driver = webdriver.Chrome(executable_path="C:/Users/user/Desktop/chromedriver.exe")
    pytest.driver.implicitly_wait(10)
    pytest.driver.get(link)
    return pytest.driver

@pytest.fixture
def autorRostelecom():
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()

@pytest.fixture
def authorization_space_mail():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail_space)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()

@pytest.fixture
def authorization_space_mail_2():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail_space2)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()

@pytest.fixture
def authorization_space_password():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password_space)
    pytest.driver.find_element(By.ID, 'kc-login').click()

@pytest.fixture
def authorization_space_password_2():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password_space2)
    pytest.driver.find_element(By.ID, 'kc-login').click()


@pytest.fixture
def authorization_empty_mail():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys('')
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()


@pytest.fixture
def authorization_empty_password():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail)
    pytest.driver.find_element(By.ID, 'password').send_keys('')
    pytest.driver.find_element(By.ID, 'kc-login').click()


@pytest.fixture
def registration_not_valid_mail():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys('qwerety')
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()



@pytest.fixture
def registration_not_valid_password():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail)
    pytest.driver.find_element(By.ID, 'password').send_keys('1')
    pytest.driver.find_element(By.ID, 'kc-login').click()


@pytest.fixture
def registration_phone_not_valid():
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()




@pytest.fixture
def registration_phone_empty():
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.find_element(By.ID, 'username').send_keys('')
    pytest.driver.find_element(By.ID, 'password').send_keys('')
    pytest.driver.find_element(By.ID, 'kc-login').click()



@pytest.fixture
def registration_login_not_valid():
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()



@pytest.fixture
def registration_login_empty():
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.find_element(By.ID, 'username').send_keys('')
    pytest.driver.find_element(By.ID, 'password').send_keys('')
    pytest.driver.find_element(By.ID, 'kc-login').click()



@pytest.fixture
def registration_ls_not_valid():
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_mail)
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'kc-login').click()


@pytest.fixture
def registration_ls_empty():
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.find_element(By.ID, 'username').send_keys('')
    pytest.driver.find_element(By.ID, 'password').send_keys('')
    pytest.driver.find_element(By.ID, 'kc-login').click()