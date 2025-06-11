from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time

# ChromeDriver 경로 설정
chrome_driver_path = 'C:/chromedriver-win64/chromedriver.exe'

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument('--headless')  # 브라우저 창을 열지 않음
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 웹 드라이버 초기화
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 브라우저 창 크기 설정
driver.set_window_size(1920, 1080)

# 캡처할 URL 목록
urls = [
    '',
    # ... 추가 URL ...
]

# 각 URL에 대해 스크린샷 캡처
for i, url in enumerate(urls):
    driver.get(url)
    time.sleep(2)  # 페이지 로드 대기 (필요에 따라 조정)

    # <h2 class="tit01"> 요소의 텍스트 가져오기
    try:
        title_element = driver.find_element(By.CSS_SELECTOR, 'h2.tit01')
        title_text = title_element.text
        # 파일 이름에 사용할 수 없는 문자를 대체
        title_text = title_text.replace(' ', '_').replace('/', '_')
    except Exception as e:
        print(f'Error finding title on {url}: {e}')
        title_text = f'screenshot_{i+1}'

    # 페이지의 실제 콘텐츠 높이 가져오기
    total_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    driver.set_window_size(1920, total_height)  # 콘텐츠 높이에 맞춰 창 크기 설정

    screenshot_path = f'{title_text}.jpg'
    driver.save_screenshot(screenshot_path)
    print(f'Screenshot saved: {screenshot_path}')

# 드라이버 종료
driver.quit()