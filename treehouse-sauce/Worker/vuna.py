from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


EMAIL = 'bileonairefx@gmail.com'
PASSWORD = 'kusoma2020'

HARVEST_URL = "https://teamtreehouse.com/tracks/intermediate-python"


def main():
    try:
        url = "https://teamtreehouse.com/signin"
        browser_path = " C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # noqa E501

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('user-data-dir=' + browser_path)
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')

        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url)
        try:
            email_input = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, "user_session_email")))  # noqa E501
            email_input[0].send_keys(EMAIL)

            pass_input = driver.find_element_by_id('user_session_password')
            pass_input.send_keys(PASSWORD)
            driver.find_element_by_xpath("//button[@class='button primary']").click()  # noqa E501
        except:  # noqa
            pass

        WebDriverWait(driver, 5)

        cards = []

        driver.get(HARVEST_URL)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'card')))  # noqa E501
            units = driver.find_elements_by_css_selector("a.card-box")  # noqa E501
        except:  # noqa
            pass

        for unit in units:
            res = unit.get_attribute("href")
            if res:
                cards.append(res)
                with open("output.txt", "a+") as file:
                    file.write(f"{res}\n")

        WebDriverWait(driver, 10)

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
