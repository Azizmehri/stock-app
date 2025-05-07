from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

EMAIL = "mohamed.aziz.mehri.pro@gmail.com"
PASSWORD = "mehriferrari0727"

def get_stock():
    options = Options()
    options.add_argument("--headless=new")  # nouveau mode headless Chrome 109+
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://app.shipper.market/login")
        driver.refresh()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))
        driver.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys(EMAIL)
        driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(PASSWORD)
        driver.find_element(By.TAG_NAME, "button").click()

        time.sleep(5)
        WebDriverWait(driver, 20).until(lambda d: "shipper.market" in d.current_url)
        driver.get("https://app.shipper.market/products/704b3a71-d020-47ad-a945-fffa62fd083e")

        WebDriverWait(driver, 20).until(
            lambda d: any(re.match(r"\d+", el.text.strip()) for el in d.find_elements(By.CLASS_NAME, "text-success"))
        )

        for el in driver.find_elements(By.CLASS_NAME, "text-success"):
            txt = el.text.strip()
            if txt.isdigit():
                return int(txt)
        return None
    except Exception as e:
        print("Erreur scraper:", e)
        return None
    finally:
        driver.quit()