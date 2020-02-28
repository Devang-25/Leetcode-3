"""
https://www.1point3acres.com/bbs/thread-451570-1-1.html

1. 给的输入是一个String的数组，String的大致格式是“xiaoming SICK cityA cityB cityC”，包含了姓名，初始健康状态，和去的城市
2. 之前有的帖子提到每个人去的citylist可能长度不一样，题目的说明是每个人会在自己的citylist里面循环，也就是A->B->C，回到A然后重新开始，A->B->C.....
3. 关于传染的话recovering和sick状态都是具有传染性的
4. 然后让你算直到所有人都recovered的期间所有人每天的状态
5. Healthy 遇 sick 或 recovering，状态改变.
sick 和 recovering 则不需要，自动进入下一个状. recovering 不会变sick
6. 状态改变发生在当前状态的下一天

https://www.1point3acres.com/bbs/thread-453065-1-1.html

Output Format:
输出的格式：
Alex Ben Crystal
Healthy Sick  Recovering
Healthy  Recovering Healthy
Healthy Healthy Healthy
3





"""

from collections import defaultdict

class Person:
  def __init__(self, name, health, cities):
    self.name = name
    self.health = [health]
    self.cities = cities

class SickTravelers:
  def __init__(self):
    self.cities = defaultdict()
    self.people = []
    self.results = []

  def traceDiseases(self, travelers_info):
    """
    input: [str, str, ...]
    for each str:
      “Traverl health_state cityA cityB cityC”
      eg. “xiaoming SICK cityA cityB cityC”

    return: [str] health_state of each individual until they are all healthy/recovered
    让你算直到所有人都recovered的期间所有人每天的状态
    """
    # update cities
    for traveler in travelers_info:
      traveler = traveler.split()
      name = traveler[0]
      health = traveler[1]
      cities = traveler[2:]
      print("name{}, health{}, cities{}".format(name, health, cities))

      person = Person(name, health, cities)
      print("Person object", person.name, person.health, person.cities)
      self.people.append(person)
      print(self.people)

      for city in cities:
        self.cities[city] = None
      print("initial city dict", self.cities)

    self.results.append(" ".join([person.name for person in self.people]))
    print("names in result", self.results)

    day = 1

    while day < 365:
      today_health = True

      # 看谁在那个城市：city: p1, p2, ..
      # 就每个城市的每个人，看他的健康状况，跟新城市的健康状况
      # 根据城市今天的情况及每个人今天的状况--》算出她明天的健康状况
      for city in self.cities:
        daily_location_tracker  = defaultdict(list)

      for person in self.people:
        cur_city_i = day % len(person.cities) - 1
        cur_city = person.cities[cur_city_i]
        daily_location_tracker[cur_city].append(person)

      # update each city's status
      self.update_city_status(daily_location_tracker)

      # update each person's status
      for person in self.people:
        my_health = self.update_my_health(person, day)
        print("my_health", my_health)
        if my_health != "HEALTHY":
          today_health = False

      print("today health", today_health)

      if today_health == True:
        for person in self.people:
          health_record = " ".join([h for h in person.health])
          self.results.append(health_record)
        self.results.append(day + 1)
        print("results1", "day:{}, results:{}".format(day+1, self.results))
        return self.results


      elif today_health == False:
        day += 1

    # NOT people are healthy within 365 days
    for person in self.people:
      health_record = " ".join([h for h in person.health])
      # print(type(health_record))
      self.results.append(health_record)
    self.results.append(day)
    print("result 2", self.results)
    return self.results



  def update_my_health(self, person, day):
    cur_health = person.health[-1]
    cur_city_i = day % len(person.cities) - 1
    cur_city = person.cities[cur_city_i]

    if cur_health == "SICK":
      person.health.append("RECOVERING")
    elif cur_health == "RECOVERING":
      person.health.append("HEALTHY")
    elif cur_health == "HEALTHY":
      if self.cities[cur_city] == "BAD":
        person.health.append("SICK")
      elif self.cities[cur_city] == "GOOD":
        person.health.append("HEALTHY")

    print("person:{}, health{}".format(person.name, person.health))
    return person.health[-1]

  def update_city_status(self, daily_location_tracker):
    """
    purpose: update health status of a city

    input daily_location_tracker: dict of list of Person object
    {city1:[person, ], city2:[]}

    Person:
      person.name str
      person.health []
      person.cities []
    """
    for city, people in daily_location_tracker.items():
      self.cities[city] = "GOOD"
      for person in people:
        cur_health = person.health[-1]
        if cur_health == "RECOVERING" or cur_health == "SICK":
          self.cities[city] = "BAD"
          break

# travelers_info = ["Michael SICK PALOALTO"]

# travelers_info = ["Michael HEALTHY PALOALTO","YUN RECOVERING DC"]

# travelers_info = ["Michael HEALTHY PALOALTO","YUN RECOVERING DC","JASMINE SICK LONDON, DC"]

########### test case from Hacker Rank ########
traverler_info = [
'Ali SICK PA DC NY',
'Isabella HEALTHY DC NY PA',
'Lee HEALTHY NY PA DC',
'Yun SICK PA',
'Michael HEALTHY DC',
'Jamal HEALTHY NY',
'A RECOVERING DC NY',
'B RECOVERING PA DC',
'C HEALTHY NY PA'
]

s = SickTravelers()
print(s.traceDiseases(travelers_info))
