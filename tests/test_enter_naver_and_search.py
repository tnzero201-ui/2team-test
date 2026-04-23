from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def test_search_qa_on_naver():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)

    driver.get("https://www.naver.com")

    # 검색창 찾기
    search_box = wait.until(
        lambda d: d.find_element(By.NAME, "query")
    )

    # "QA" 입력 후 엔터
    search_box.send_keys("QA")
    search_box.send_keys(Keys.ENTER)

    # 검색 결과 페이지 확인
    wait.until(
        lambda d: "query=QA" in d.current_url
    )

    assert "query=QA" in driver.current_url

    driver.quit()