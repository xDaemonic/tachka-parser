import time
from fake_useragent import UserAgent

from src.Model import Model
from src.Bag import Bag
from models.FileItem import FileItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class FileScraper:

  html_folder = '/project/files'
  driver = None

  def __init__(self) -> None:
    pass

  def setHtmlFolder(self, folder: str) -> None:
    self.html_folder = folder

  def init_driver(self):
    ua = UserAgent()
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    options.add_argument(f"user-agent={ua.chrome}")

    self.driver = webdriver.Chrome(options=options)
  
  def destroy_driver(self):    
    self.driver.close()
    self.driver.quit()


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
      self.destroy_driver()

  def download_file(self, item: FileItem):
    self.init_driver()
    result = self.__download_html(item.url, item.name, item.ext)
    self.destroy_driver()

    return result
  
  def download_files(self, bag: Bag) -> Bag:
    if (self.driver == None): self.init_driver()
          
    for item in bag.getItems():
      if isinstance(item, FileItem):
        filepath = self.__download_html(item.url, item.name, item.ext)
        item.setAttribute('filepath', filepath)
        item.setAttribute('downloaded', True)
        
    self.destroy_driver()
    
    return bag

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
      pass
    