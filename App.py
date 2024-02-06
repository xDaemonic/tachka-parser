from src.scraper import Scraper

class App:
  urls = []

  def __init__(self) -> None:
    pass

  def add_url(self, url:str) -> None:
    self.urls.append(url)

  def run(self):
    scraper = Scraper()
    for url in self.urls: 
      scraper.download_html(url, 'tachka_global_categories')