def merge(list1: list, list2: list) -> list:
  return [x for n in (list1, list2) for x in n]