base_url = 'https://tachka.ru'

def url(path: str) -> str:
  global base_url
  return f"{base_url}{path}"

def remove_base_url(url: str) -> str:
  global base_url
  return url.replace(f"{base_url}/", '')

def page_url(url: str, page: int) -> str:
  global base_url
  return f"{url}?page={page}" if 'https' in url else f"{base_url}{url}?page={page}"
