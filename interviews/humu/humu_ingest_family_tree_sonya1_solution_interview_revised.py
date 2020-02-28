#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'ingestFamilyTree' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY csv
#  2. STRING today
#

import collections
from datetime import datetime


def parseDate(date_str):
  """
    Inputs:
        date_str: Str. It could be any of the following format:
            * YYYY-MM-DD
            * MM/DD/YYYY
            * <empty>
            * Invalid

    Returns:
        One of: datetime.date | '' | None
            Valid: returns datetime.date
            Empty string: returns empty string.
            Invalid: returns None.
    """
  # Empty string.
  if not date_str:
    return ''

  # Invalid data: length error.
  if len(date_str) != 10:
    return None

  # String in format YYYY-MM-DD.
  try:
    return datetime.strptime(date_str, '%Y-%m-%d').date()
  except:
    pass

  # String in format MM/DD/YYYY.
  try:
    return datetime.strptime(date_str, '%m/%d/%Y').date()
  except:
    pass

  # Invalid/unknown string format.
  return None


def computeAge(birth, death, today):
  """
    Inputs:
        birth: datetime.date or None.
        death: datetime.date or None.
        today: datetime.date or None.

    Returns:
        age: Int.
    """
  if not birth or not today:
    return -1

  # Invalid death date format.
  if death is None:
    return -1

  # Still alive.
  if death == '':
    return (today - birth).days

  if death and today > death:
    return (death - birth).days

  return -1


class FamilyGraph(object):

  def __init__(self, data):
    """
        Inputs:
            data: List[List[str]]. Properly parsed csv data.

        The idea is to create a graph (dictionary) from the data where key is the parent_id, and value is a set of its direct descendants.
        """
    graph = collections.defaultdict(set)
    self.unique_ids = set([row[0] for row in data])

    for row in data:
      id, name, gender, birth, death, parent1, parent2 = row
      if parent1 and parent1 in self.unique_ids:
        graph[parent1].add(id)
      if parent2 and parent2 in self.unique_ids:
        graph[parent2].add(id)

    self.graph_ = graph
    self.desc_count_ = collections.Counter()

  def _getDescIds(self, id):
    if not self.graph_[id]:
      return []

    desc_ids = list(self.graph_[id])
    for child_id in self.graph_[id]:
      desc_ids += self._getDescIds(child_id)

    return desc_ids

  def getDescendants(self, id):
    """
        Inputs:
            id: Str. Root person id.

        Returns:
            Int. Number of descendants.

        The function uses dynamic programming. If the person is already in self.desc_count_, then just returns its desc count. Otherwise, recursively finds its children's desc count, caches the result in self.desc_count_.
        """
    if not self.graph_[id]:
      return 0

    if id not in self.desc_count_:
      self.desc_count_[id] = len(set(self._getDescIds(id)))

    return self.desc_count_[id]


def ingestFamilyTree(csv, today):
  """
    Inputs:
        csv: List[Str].
        today: Str. Representing a date.

    Returns:
        out: List[Str]. Same as csv with two extra columns: age and descendants.
    """
  today = parseDate(today)
  out = []
  out_missing_birth = []
  gender_age = defaultdict(list)
  gender_age["female"] = []
  gender_age["male"] = []

  data = [[col for col in line.split(',')] for line in csv[1:]]

  family_graph = FamilyGraph(data)
  unique_ids = family_graph.unique_ids
  for row in data:
    id, name, gender, birth_str, death_str, parent1, parent2 = row
    if parent1 not in unique_ids:
      parent1 = -1
    if parent2 not in unique_ids:
      parent2 = -1
    birth, death = parseDate(birth_str), parseDate(death_str)
    age = computeAge(birth, death, today)
    descendants = family_graph.getDescendants(id)

    gender_age[gendre].append(age)

    out_row = row + [str(age), str(descendants)]
    out_list = out if birth else out_missing_birth
    out_list.append(out_row)

  header = csv[0].split(',') + ['age', 'descendants']
  out = sorted(out, key=lambda row: parseDate(row[3]))
  out = [header] + out + out_missing_birth
  out = [','.join(row) for row in out]

  out_gender = [
      gender + '.' + agv_age for gender,
      average(gender_age[gender]) in gender_age
  ]
  return out, out_gender


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  csv_count = int(input().strip())

  csv = []

  for _ in range(csv_count):
    csv_item = input()
    csv.append(csv_item)

  today = input()

  result = ingestFamilyTree(csv, today)

  fptr.write('\n'.join(result))
  fptr.write('\n')

  fptr.close()
