import sys
import os
from collections import OrderedDict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import youtube_dl


EMAIL = ''
PASSWORD = ''
EXTERNAL_DL = 'aria2c'
HOME_DIR = os.getcwd()


def move_to_course_directory(title):
    """Check if current directory is home directory. If not, change to it.
    Make a course directory and move to it.
    If course directory already exists, just move to it.
    If everything fails break the program.
    """

    # Move to home directory if we are somewhere else (e.g. course subdir)
    if os.getcwd() != HOME_DIR:
        os.chdir(HOME_DIR)
    try:
        # Make a directory with course name
        os.mkdir(title)
        os.chdir(title)
    except FileExistsError:
        # Position yourself in course directory
        os.chdir(title)
    except:  # noqa
        print('Could not create subdirectory for the course: {}'.format(title))


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
            email_input = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, "user_session_email")))  # noqa E501
            email_input[0].send_keys(EMAIL)

            pass_input = driver.find_element_by_id('user_session_password')
            pass_input.send_keys(PASSWORD)
            driver.find_element_by_xpath("//button[@class='button primary']").click()  # noqa E501
        except:  # noqa
            pass

        WebDriverWait(driver, 5)

        for track in open('tracks.txt'):
            driver.get(track)

            cards = []

            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'card')))  # noqa E501
                units = driver.find_elements_by_css_selector("a.card-box")  # noqa E501
            except:  # noqa
                pass

            for unit in units:
                res = unit.get_attribute("href")
                if res:
                    cards.append(res)

            link_index = 1  # counter for item from link.txt

            for link in cards:
                driver.get(link)

                sections = []

                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'syllabus-stages')))  # noqa E501
                    elements = driver.find_elements_by_css_selector("div#syllabus-stages a")  # noqa E501
                except:  # noqa
                    pass

                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'workshop-steps')))  # noqa E501
                    elements = driver.find_elements_by_css_selector("div#workshop-steps a")  # noqa E501
                except:  # noqa
                    pass

                for element in elements:
                    res = element.get_attribute("href")
                    if res:
                        sections.append(res)

                # Generate folder name and move to it
                parts = link.split('/')
                title = "{:02d}-{}".format(link_index, parts[-1])
                link_index += 1

                if len(sys.argv) > 1:
                    move_to_course_directory(title)

                videos = OrderedDict({})
                videos_index = 1

                for section in sections:
                    driver.get(section)

                    try:
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'video-container')))  # noqa E501
                        video = driver.find_elements_by_xpath("//source[@type='video/mp4']")[0].get_attribute("src")  # noqa E501
                        if video:
                            video_title = "{:02d}-{}".format(videos_index, removeReservedChars(driver.find_elements_by_tag_name('h1')[0].text))  # noqa E501

                            videos[video_title] = video  # noqa E501
                            videos_index += 1

                            if len(sys.argv) > 1:
                                # Youtube-dl options
                                options = {
                                    'outtmpl': video_title,
                                    'external_downloader': EXTERNAL_DL,
                                    # ,'verbose': True,
                                }

                                with youtube_dl.YoutubeDL(options) as ydl:
                                    ydl.download([video])

                                WebDriverWait(driver, 10)

                    except:  # noqa
                        pass

            WebDriverWait(driver, 10)

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
