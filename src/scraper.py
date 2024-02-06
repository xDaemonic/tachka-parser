import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Scraper:

  def __init__(self) -> None:
    self.driver = self.get_driver()


  def get_driver(self):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--start-maximized')

    return webdriver.Chrome(options=options)
  

  def test_fullpage_screenshot(self, url: str, filename: str):
    try:
      self.driver.get(url)
      time.sleep(2)

      ele = self.driver.find_element(By.TAG_NAME, 'body')
      height = self.driver.execute_script("return document.body.scrollHeight")
      self.driver.set_window_size(1920, height)

      self.driver.save_screenshot(f"screenshots/{filename}")
    except Exception:
      pass
    finally:
      self.driver.close()
      self.driver.quit()

  def download_html(self, url: str, filename: str, extention: str = 'html'):
    try:
      self.driver.get(url)
      time.sleep(2)
      html = self.driver.page_source
      with open(f"/files/{filename}.{extention}", 'w+') as f:
        f.write(html)
        f.close()
    except Exception:
      print(Exception.message())
      pass
    finally:
      self.driver.close()
      self.driver.quit()