import os
import sys
from enum import Enum
import random
import time

from selenium import webdriver


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


class Difficulty(Enum):
  easy = "Easy"
  medium = "Medium"
  hard = "Hard"


md_temp = """# {title}

{url}

## Solution:

```python

```

## Analysis:

Let $N$ be the number of elements in `arr`.

### Time Complexity:

$O(N)$

### Space Complexity:

$O(1)$

### Points to Note:

"""


def login_and_pick_one(login: str, password: str, difficulty: Difficulty):
  driver = webdriver.Firefox()
  driver.implicitly_wait(100)

  driver.get(f"https://leetcode.com/problemset/algorithms/?difficulty={difficulty.value}&status=Todo")

  elem = driver.find_element_by_link_text("Sign in")
  elem.click()

  elem = driver.find_element_by_xpath("//a[@data-icon='github-c']")
  elem.click()

  elem = driver.find_element_by_xpath("//input[@id='login_field']")
  elem.send_keys(login)

  elem = driver.find_element_by_xpath("//input[@id='password']")
  elem.send_keys(password)

  elem = driver.find_element_by_xpath("//input[@value='Sign in']")
  elem.click()

  elem = random.choice(driver.find_elements_by_class_name("reactable-page-button"))
  elem.click()

  time.sleep(0.2)

  elem = random.choice(driver.find_elements_by_xpath("//a[starts-with(@href, '/problems/')]"))
  elem.click()

  elem = driver.find_element_by_xpath("//div[@data-cy='question-title']")

  question_title = elem.text
  question_url = driver.current_url
  with open(get_script_path() + f"/{difficulty.value}/{question_title}.md", "w") as f:
    f.write(md_temp.format(**{"title": question_title, "url": question_url}))
  
  # driver.close()


if __name__ == "__main__":
  with open(get_script_path() + "/credientials.txt", "r") as f:
    login = f.readline()
    password = f.readline()

  login_and_pick_one(login, password, Difficulty.easy)
