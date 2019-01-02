from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import os
"""
  Install firefox driver
    brew install geckodriver
  Use of docker
    https://hub.docker.com/u/selenium/
    https://www.kenst.com/2016/12/installing-marionette-firefoxdriver-on-mac-osx/
"""


def runCrawler(tag):
  try:
    driver = webdriver.Firefox()
    url = "%s/%s" % ("https://leetcode.com/tag", tag)
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "reactable-data")))
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    txt_lst = []
    txt_lst += ["Problem statement, Problem Link, Hint, Solution link, Priority"]
    try:
      for link in soup.find_all('a'):
        txt = link.get('href')
        if (txt != None and txt.startswith('/problems/')):
          #print(link)
          prfx = "https://leetcode.com"
          out = ("%s,%s,,") % (link.get_text(), prfx + link.get('href'))
          txt_lst += [out]
    except AttributeError:
      print("error")

    out_dir = 'target'

    if not os.path.exists(out_dir):
      os.makedirs(out_dir)

    fp = "%s/%s.csv" % (out_dir, tag)
    with open(fp, 'w') as fp:
      fp.write("\n".join(txt_lst))
  finally:
    driver.close()


def process():
  tags = getTags()
  for tag in tags:
    #print tag
    runCrawler(tag)


lst = [
    "array", "dynamic-programming", "string", "math", "tree", "hash-table",
    "depth-first-search", "binary-search", "two-pointers",
    "breadth-first-search", "greedy", "stack", "backtracking", "design",
    "linked-list", "bit-manipulation", "heap", "dynamic-programming", "string",
    "math", "tree", "hash-table", "depth-first-search", "binary-search",
    "two-pointers", "breadth-first-search", "greedy", "stack", "backtracking",
    "design", "linked-list", "bit-manipulation", "heap", "sort", "graph",
    "union-find", "divide-and-conquer", "binary-search-tree", "trie",
    "recursion", "queue", "segment-tree", "random", "binary-indexed-tree",
    "minimax", "topological-sort", "brainteaser", "geometry", "map",
    "rejection-sampling", "reservoir-sampling", "memoization"
]


def getTags():
  return lst


process()
