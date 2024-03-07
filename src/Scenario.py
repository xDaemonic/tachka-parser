import lxml
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod 

class Scenario(ABC):
  _soup: BeautifulSoup

  def __init__(self, html_content: str) -> None:
    self._soup = BeautifulSoup(html_content, 'lxml')

  @abstractmethod
  def run(self):
    pass