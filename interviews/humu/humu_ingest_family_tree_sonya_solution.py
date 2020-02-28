from collections import defaultdict
from datetime import datetime


class Person:

  def __init__(self, line):
    l = line.split(", ")
    # print(l)
    self.id = l[0]
    self.name = l[1]
    self.gender = l[2]
    self.birth = l[3]
    self.death = l[4]
    self.parent1 = l[5]
    self.parent2 = l[6]
    self.age = None
    self.descendants_num = 0


def parseInfo(data, today):
  """
    outputs:
        header : [str]
        people_dict: {id: person} {str: person_object}
        family_graph: {parent_id: [children_id]} {str: [str]}
    """
  header = data[0]

  people_dict = defaultdict()
  family_graph = defaultdict(list)

  for line in data[1:]:
    person = Person(line)
    people_dict[person.id] = person

    if person.parent1:
      family_graph[person.parent1].append(person.id)
    if person.parent2:
      family_graph[person.parent2].append(person.id)

    age = getAge(person.birth, person.death, today)
    person.age = age

  return header, people_dict, family_graph


def parseDate(date_str):
  if not date_str:
    return ""

  try:
    return datetime.strptime(date_str, '%m/%d/%Y').date()
  except:
    pass

  try:
    return datetime.strptime(date_str, '%Y-%m-%d').date()
  except:
    return "error"


def getAge(birth, death, today):
  """
    birth: str
    death: str
    today = str
    """

  # if death = str "ymd" or "smething wrong"
  if birth and death:
    birth = parseDate(birth)
    death = parseDate(death)
    if death != "error":
      return (death - birth).days
    elif death == "error":
      return ""
  # death = empty str ""
  elif birth and not death:
    birth = parseDate(birth)
    today = parseDate(today)
    return (today - birth).days


def countDescendants(people_dict, family_graph):

  def recursivelyCountDescendants(id_str, family_graph):
    # if no descendents
    print("family_graph", family_graph)
    print(type(id_str))
    if not family_graph[id_str]:
      return 0

    # if Has descendents
    # find the descendants of each children
    direct_children = family_graph[id_str]
    total = sum([
        recursivelyCountDescendants(child_id, family_graph)
        for child_id in direct_children
    ])
    return total + 1

  for id_str in people_dict:
    count = recursivelyCountDescendants(id_str, family_graph)
    people_dict[id_str].descendants_num = count

  return people_dict


def ingestFamilyTree(data, today):
  """
    inputs:
        data: [str]
    """

  results = []
  # append(header, )

  # paseInfomation into the Person object
  # calculate the age of each person
  # build the connection tree
  # use family_graph, find the number of descendants of each person
  header, people_dict, family_graph = parseInfo(data, today)
  # print("family", family_graph, "people", people_dict)
  people_dict = countDescendants(people_dict, family_graph)

  results.append(header + ", age" + ", descendants")

  results_missing_age = []

  for id_str in people_dict:
    p = people_dict[id_str]
    # ", ".join([str(item) for item in [person.name]])
    # ", ".join(str(pitem) for item in [id_str, name, gender, birth, death, parent1, parent2, age, descendants_num])
    r = ", ".join(
        str(item) for item in [
            p.id, p.name, p.gender, p.birth, p.death, p.parent1, p.parent2,
            p.age, p.descendants_num
        ])
    if p.age:
      results.append(r)
    elif not p.age:  # p.age == ""
      results_missing_age.append(r)

  results = results + results_missing_age
  return results


csv = [
    "id, name, gender, birth, death, parent1, parent2",
    "1, Mary, female, 1906-12-05, 00013=-23, 2, p2",
    "2, S, female, 1906-12-05, 1916-12-06, 3, p2"
]

r = ingestFamilyTree(csv, "2018-10-22")
print("result", r)

###################

import math
import os
import random
import re
import sys

import collections
from datetime import datetime


def parseDate(date_str):
  """
  inputs:
    date_str: str. It could be any of the following format:
    YYYY-MM-DD
    MM/DD/YYYY
    <empty>
    Invalid
  
  returns:
    one of: datetime.date | '' | None
    valid: return datetime.date
    empty: return empty str ''
    invalid: return None
  """
  if not date_str:
    return ''

  if len(date_str) != 10:
    return None

  try:
    return datetime.strptime(date_str, '%Y-%m-%d').date()
  except:
    pass

  try:
    return datetime.strptime(date_str, '%m/%d/%Y').date()
  except:
    pass

  return None


def computeAge(birth, death, today):
  """
  inputs:
    birth: datetime.date or None
    death: dateimte.date or None.
    today: datetime.date or None.
  
  returns:
    age: int
  """
  if not birth or not today:
    return -1

  if death is None:
    return -1

  if death is "":
    return (today - birth).days

  if death and today > death:
    return (death - birth).days

  return -1


class FamilyGraph(object):

  def __init__(self, data):
    """
    inputs:
      date: List[List[str]]. properly parsed csv data.
    
    the idea is to create a graph (dictionary) from teh data.
    """
    graph = collections.defaultdict(set)
    unique_ids = set([row[0] for row in data])

    for row in data:
      id, name, gender, birth, death, parent1, parent2 = row
      if parent1 and parent1 in unique_ids:
        unique_ids[parent1].add(id)
      if parent2 and parent2 in unique_ids:
        unique_ids[parent2].add(id)

      self.graph = graph
      self.desc_count_ = collections.Counter()

  def _getDescIds(self, id):
    if not self.graph[id]:
      return []

      desc_ids = list(self.graph[id])
      for child_id in self.graph[id]:
        desc_ids += self._getDescIds(child_id)

      return desc_ids

  def getDescendants(self, id):
    """
    inputs:
      id: str. root per id.
    
    return:
      int. the numbef of descendents.
    """

    if not self.graph[id]:
      return 0

    if id not in self.desc_count_:
      self.desc_count_[id] = len(set(self._getDescIds(id)))

    return self.desc_count_[id]


def ingestFamilyTree(csv, today):
  """
  inputs;
    csv: List[str]
    today: str. Representing a date.
  
  returns:
    out: List[str].Same as input csv with two extra colums: age and descendants.
  """
  today = parseDate(today)
  out = []
  out_missing_birth = []

  data = [[col for col in line.split(",")] for line in csv[1:]]

  family_graph = FamilyGraph(data)
  for row in data:
    id, name, gender, birth_str, death_str, parent1, parent2 = row
    birth, death = parseDate(birth), parseDate(death)
    age = computeAge(birth, death, today)
    descendants = family_graph.getDescendants(id)

    out_row = row + [str(age), str(descendants)]
    out_list = out if birth else out_missing_birth
    out_list.append(out_row)

  header = csv[0].split(',') + ['age', 'descendants']
  out = sorted(out, key=lambda row: parseDate(row[3]))
  out = [header] + out + out_missing_birth
  out = [",".join(row) for row in out]
  return out
