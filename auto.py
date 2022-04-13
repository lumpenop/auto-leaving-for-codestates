from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import schedule
import time



def auto():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = '/Users/lumpen/Documents/chromedriver'
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.implicitly_wait(3)


    driver.execute_script('window.open("https://urclass.codestates.com/mypage");')  #구글 창 새 탭으로 열기
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
    time.sleep(1)

    # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/lumpen/Applications/Google Chrome.app/ChromeTemp" 
    try:
        
        logout = driver.find_element_by_css_selector('#root > div > div > div.header.fixed.css-0 > div > div > div > div.w3-dropdown-hover.css-uqa5a4 > div.w3-dropdown-content.w3-bar-block.w3-border > button')
        driver.execute_script("arguments[0].click();", logout)
        print('logout 성공')

    except:
        print('코드스테이츠 로그인이 안되어 있음')

    time.sleep(2)
    driver.close()
    print('탭 닫힘')

auto()

schedule.every().day.at("18:09").do(auto)

while True:
    schedule.run_pending()
    time.sleep(1)