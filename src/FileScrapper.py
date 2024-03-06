import time

from src.Model import Model
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class FileScraper:

  html_folder = '/project/files'

  def __init__(self) -> None:
    self.driver = self.get_driver()

  def setHtmlFolder(self, folder: str) -> None:
    self.html_folder = folder

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


  def download_file(self, item: Model):
    return self.__download_html(item.url, item.name, item.ext)

  def __download_html(self, url: str, filename: str, extention: str = 'html'):
    filepath = f"{self.html_folder}/{extention}/{filename}.{extention}"
    try:
      self.driver.get(url)
      time.sleep(1)
      html = self.driver.page_source
      with open(filepath, 'w+') as f:
        f.write(html)
        f.close()
      
      return filepath
    
    except Exception:
      # print(Exception.__base__)
      return None
    finally:
      self.driver.close()
      self.driver.quit()
    