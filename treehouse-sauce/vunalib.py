import os
from collections import OrderedDict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import youtube_dl


EMAIL = '2020tomrae@gmail.com'
PASSWORD = 'kusoma2020'
EXTERNAL_DL = 'aria2c'
HOME_DIR = os.getcwd()
WAIT_SECONDS = 6


def removeReservedChars(value):
    """ Remove reserved characters because of Windows OS compatibility
    """
    return "".join(i for i in value if i not in r'\/:*?"<>|')


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
            email_input = WebDriverWait(driver, WAIT_SECONDS).until(EC.visibility_of_all_elements_located((By.ID, "user_session_email")))  # noqa E501
            email_input[0].send_keys(EMAIL)

            pass_input = driver.find_element_by_id('user_session_password')
            pass_input.send_keys(PASSWORD)
            driver.find_element_by_xpath("//button[@class='button primary']").click()  # noqa E501
        except:  # noqa
            pass

        WebDriverWait(driver, WAIT_SECONDS)

        link_index = 1  # counter for item from link.txt

        for link in open('vunalib.txt'):
            driver.get(link)

            sections = []

            try:  # courses
                WebDriverWait(driver, WAIT_SECONDS).until(EC.presence_of_element_located((By.ID, 'syllabus-stages')))  # noqa E501
                elements = driver.find_elements_by_css_selector("div#syllabus-stages a")  # noqa E501
            except:  # noqa
                pass

            try:  # workshops and practise
                WebDriverWait(driver, WAIT_SECONDS).until(EC.presence_of_element_located((By.ID, 'workshop-steps')))  # noqa E501
                elements = driver.find_elements_by_css_selector("div#workshop-steps a")  # noqa E501
            except:  # noqa
                pass

            try:  # bonus
                WebDriverWait(driver, WAIT_SECONDS).until(EC.presence_of_element_located((By.CLASS_NAME, 'achievement-steps')))  # noqa E501
                elements = driver.find_elements_by_css_selector("div.achievement-steps li a")  # noqa E501
            except:  # noqa
                pass

            for element in elements:
                res = element.get_attribute("href")
                if res:
                    sections.append(res)

            # Generate folder name and move to it
            parts = link.split('/')
            title = "{:02d}-{}--".format(link_index, removeReservedChars(parts[-1]))  # noqa E501
            link_index += 1

            videos = OrderedDict({})
            videos_index = 1

            for section in sections:
                driver.get(section)

                try:
                    WebDriverWait(driver, WAIT_SECONDS).until(EC.presence_of_element_located((By.ID, 'video-container')))  # noqa E501
                    video = driver.find_elements_by_xpath("//source[@type='video/mp4']")[0].get_attribute("src")  # noqa E501
                    if video:
                        video_ttl = "{:02d}-{}".format(videos_index, removeReservedChars(driver.find_elements_by_tag_name('h1')[0].text))  # noqa E501
                        video_title = title + video_ttl
                        video_title = video_title.replace("\n", "")

                        videos[video_title] = video  # noqa E501
                        videos_index += 1

                        with open("video.txt", "a+") as file:
                            file.write(f"{video_title}@ {video}\n")

                        WebDriverWait(driver, WAIT_SECONDS)

                except:  # noqa
                    pass

        WebDriverWait(driver, WAIT_SECONDS)

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
