from typing import List

class Solution:
  """"""

  # 23 min
  def is_unique(self, string: str) -> bool:
    """"""
    dict = {}
    for char in string:
      if char in dict:
        return False
      else:
        dict[char] = 1
    return True

  # 6 min
  def reverse(self, string: str) -> str:
    """"""
    rev_str = ""
    for i in range(len(string)-1, -1, -1):
      rev_str += string[i]
    return rev_str

  # 35 min
  def rm_duplicates(self, string: str) -> str:
    """"""
    if len(string) == 0 or len(string) == 1:
      return string
    dict = {}
    dict[string[0]] = 1
    count = 1
    length = len(string)
    while count <= length-1:
      if string[count] in dict:
        print(string[count])
        if count < length-1:
          string = string[:count] + string[count+1:]
          length -= 1
        elif count == length-1:
          string = string[:-1]
          length -= 1
      else:
        dict[string[count]] = 1
        count += 1
    return string
  
  # 16 min
  def is_anagram(self, string1: str, string2: str) -> bool:
    """"""
    dict = {}
    if not len(string1) == len(string2):
      return False
    for i in range(len(string1)):
      if string1[i] in dict:
        dict[string1[i]] += 1
      else:
        dict[string1[i]] = 1
      if string2[i] in dict:
        dict[string2[i]] -= 1
      else:
        dict[string2[i]] = -1
    for (key, item) in dict.items():
      if not item == 0:
        return False
    return True

  # 10 min
  def del_pattern(self, string1: str, pattern: str) -> str:
    """"""
    length = len(string1)
    pat_length = len(pattern)
    index = 0
    while index + len(pattern) < length:
      if string1[index:index+pat_length] == pattern:
        string1 = string1[:index] + string1[index+pat_length:]
        length -= pat_length
      else:
        index +=1
    return string1

  # 14 min
  def repl_pattern(self, string1: str, pattern: str, repl_str: str) -> str:
    """"""
    length = len(string1)
    pat_length = len(pattern)
    repl_length = len(repl_str)
    index = 0
    while index + len(pattern) < length:
      if string1[index:index+pat_length] == pattern:
        string1 = string1[:index] + repl_str + string1[index+pat_length:]
        length = length - pat_length + repl_length
        index += repl_length
      else:
        index +=1
    return string1

  # 1 min

  from math import ceil

  def rotate_image(self, img: List[List[int]]) -> list:
    """"""
    mat_dim = len(img)
    levels = math.ceil(mat_dim/2)
    for k in range(levels):
      for col in ranges(mat_dim):
        for row in range(mat_dim):
          for s in range(n_sides):
            # map cordinates for each rotation
            temp = img[col][mat_dim-col][row]
            img[]
    return img 
  