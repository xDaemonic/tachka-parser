import lxml
from bs4 import BeautifulSoup

class Scenario():
  __soup: BeautifulSoup

  def __init__(self, html_content: str) -> None:
    self.__soup = BeautifulSoup(html_content, 'lxml')