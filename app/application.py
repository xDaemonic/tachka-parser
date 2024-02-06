from app.src.scraper import Scraper

class FileScrapper:
  urls = []

  def __init__(self) -> None:
    pass

  def add_url(self, url:str) -> None:
    self.urls.append(url)

  def run(self):
    scraper = Scraper()
    for url in self.urls: 
      scraper.download_html(url, 'tachka_global_categories')

class Detail:
  def __init__(self, filename) -> None:
    pass