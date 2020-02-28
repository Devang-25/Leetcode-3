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


test_case = [
"Wilson SICK PaloAlto DC London PaloAlto",
"Yun HEALTHY PaloAlto",
"Ali RECOVERING DC DC DC London",
"Jasmin HEALTHY LONDON"
]
"""

from collections import defaultdict

_debug = True
def dprint(*args, **kwargs):
  if _debug:

    print(*args, **kwargs)

class Person:
  def __init__(self, name, initial_health_cond, cities):
    self.name = name
    self.health = [initial_health_cond]
    self.cities = cities

def update_health(travelers_dict, cities_status_dict, day):
    """
        travelers_dict{name: person} type: {str: Person object}
    input day: int
        cities_status_dict {city: status} type: {str: str "GOOD" | "BAD" | "None"}
        day type: int

    outputs:
        travelers_dict{name: person} type: {str: Person object}
            updat the persons.health by appending updated health of a person
            updated_health is a str: "HEALTHY" | "SICK" | "RECOVERING"

    the purpose of this method:
        is to culculate the health of the each person

    Logic:
        my health on day_i depends on:
            1) my latest health condition
            2) the city I am in now
    """
    for name, person in travelers_dict.items():
        city_index = day % len(person.cities) - 1
        next_city = person.cities[city_index]
        city_status = cities_status_dict[next_city]

        latest_health = person.health[-1]

        if latest_health == "SICK":
            next_health = "RECOVERING"
            # update cur_city as not healthy
        elif latest_health == "RECOVERING":
            next_health = "HEALTHY"
            # update cur_city as not healthy
        elif latest_health == "HEALTHY":
            next_health = "HEALTHY" if city_status == "GOOD" else "SICK"

        person.health.append(next_health)

    return travelers_dict


def check_if_all_healthy(travelers_dict, day):
    """
    inputs:
        travelers_dict{name: person} type: {str: Person object}
        day type: int

    outputs:
        type: bool True/False
    """
    all_health = []

    for name, person in travelers_dict.items():
        health = person.health[-1]
        all_health.append(health)

    return all([h == "HEALTHY" for h in all_health])


def track_people_location(travelers_dict, cities_tracker_dict, day):
    """
    input:
        people_dict{name: person} type: {str: Person object}
        location_tracker_dict {city: [travelers]} type: {str: [Person Object]}
        day: int, indicating which day's status I am updating

    output:
        location_tracker_dict {city: [travelers]} type: {str: [Person Object]}

    """
    location_tracker_dict = defaultdict(list)

    for name, person in travelers_dict.items():
        person = travelers_dict[name]
        cur_city_i = day % len(person.cities) - 1
        cur_city = person.cities[cur_city_i]

        location_tracker_dict[cur_city].append(person)

    return location_tracker_dict

def update_city_status(location_tracker_dict, cities_status_dict):
    """
    input:
        location_tracker_dict {city: [person, ...]}: {str: [Person Object]}
        cities_status_dict {city: status} type: {str: str "GOOD" | "BAD"| "None"}

    return:
        cities_status_dict {city: status} type: {str: str "GOOD" | "BAD"| "None"}

    purpose of method:
        update the health status of a city based on the person's health

    CAUTION:

    since some cities might have have people there in previous day, so some cities are NOT in the location_tracker_dict BUT in cities_status_dict

    for these cities, update their status to "None"
    """
    for city in cities_status_dict.keys():
        dprint("city", city)
        if city not in location_tracker_dict:
          status = "GOOD"
        else:
          people = location_tracker_dict[city]
          health_list = [person.health[-1] for person in people]
          dprint("health_list", health_list)
          status = "GOOD" if all([h == "HEALTHY" for h in health_list]) else "BAD"
          dprint("status", status)

        cities_status_dict[city] = status
    # print([[city, status] for city, status in cities_status_dict.items()])
    print("\n")
    return cities_status_dict

def parseInfo(traverlers_info):
    """
    input:
        traverler_info: [str]
        for each str: name, initial_health, cities

    return:
        travelers_dict{name: person} type: {str: Person object}
        cities_status_dict {city: status} type: {str: str "GOOD" | "BAD" | "None"}
        travelers type: str "name1 name2 name3"
    """
    travelers_dict = defaultdict()
    cities_status_dict = defaultdict(str)
    travelers_names = []

    for line in travelers_info:
        # parse
        info = line.split()
        name = info[0]
        initial_health = info[1]
        cities = info[2:]
        # build person object
        person = Person(name, initial_health, cities)
        # track in to travelers_dict
        travelers_dict[name] = person

        travelers_names.append(name)

        for city in cities:
            cities_status_dict[city] = "None"

    travelers = " ".join(name for name in travelers_names)
    return travelers_dict, cities_status_dict, travelers


def traceDisease(traverlers_info):

    """
    input traverler_info: [str]

    for each str: name, initial_health, cities

    return:
        results type: [str, str1, ....]
    """
    # 1) parse the info and
    # build the traverlers_dict and cities_status dict

    results = []

    travelers_dict, cities_status_dict, travelers_names = parseInfo(travelers_info)

    day = 1
    dprint("day", day)

    while day <= 365:
        # 1. track if all people are healthy:
        all_healthy = check_if_all_healthy(travelers_dict, day) # return True / False
        dprint("all_healthy", all_healthy)
        if all_healthy or day == 365:
            break

        # else:
            # 2. track person's location_tracker
            # 3. use person's health and location to update city status
            # 4. use city's status and person's health to update health on day+1
        location_tracker_dict = track_people_location(travelers_dict, cities_status_dict, day)

        dprint("location_tracker_dict")
        for city, people in location_tracker_dict.items():
          dprint("city", city)
          dprint([person.name for person in people])

        cities_status_dict = update_city_status(location_tracker_dict, cities_status_dict)
        dprint("cities_status_dict", cities_status_dict)

        dprint("\n")
        dprint("day", day+1)

        travelers_dict = update_health(travelers_dict, cities_status_dict, day+1)
        dprint("travelers_dict")
        for name, person in travelers_dict.items():
          dprint(name, "'health:", person.health)

        day += 1

    results.append(travelers_names) #["name1, name2, ..."]
    for name, person in travelers_dict.items():
        health_record = " ".join([h for h in person.health])
        results.append(health_record)
    results.append(str(day))

    return results

######### test case 1####################

# travelers_info = ["Michael SICK PALOALTO"]

######### test case 2####################

# travelers_info = ["Michael HEALTHY PALOALTO","YUN RECOVERING DC"]
# reutrn ['Michael YUN', 'HEALTHY HEALTHY', 'RECOVERING HEALTHY', '2']


######### test case 3####################
"""
corner case:
  what if a city has no one there, does it status become "GOOD" or "Bad" or "None"
"""
# travelers_info = ["Michael HEALTHY PALOALTO","YUN RECOVERING PALOALTO DC"]
# return
# ['Michael YUN', 'HEALTHY SICK RECOVERING HEALTHY HEALTHY', 'RECOVERING HEALTHY SICK RECOVERING HEALTHY', '5']

######### test case 4####################

# travelers_info = ["Michael HEALTHY PALOALTO","YUN RECOVERING DC","JASMINE SICK LONDON, DC"]
# answer:
# ['Michael YUN JASMINE', 'HEALTHY HEALTHY HEALTHY HEALTHY HEALTHY HEALTHY','RECOVERINGHEALTHY SICK RECOVERING HEALTHY HEALTHY', 'SICK RECOVERING HEALTHY SICK RECOVERING HEALTHY', '6']

######### test case 5##########
travelers_info = [
"Wilson SICK PaloAlto DC London PaloAlto",
"Yun HEALTHY PaloAlto",
"Ali RECOVERING DC DC DC London",
"Jasmin HEALTHY London"
]
# return
# ['Wilson Yun Ali Jasmin',
# 'SICK RECOVERING HEALTHY SICK RECOVERING HEALTHY SICK RECOVERING HEALTHY SICK RECOVERING HEALTHY HEALTHY HEALTHY', 'HEALTHY SICK RECOVERING HEALTHYSICK RECOVERING HEALTHY HEALTHY SICK RECOVERING HEALTHY HEALTHY HEALTHY HEALTHY', 'RECOVERING HEALTHY SICK RECOVERING HEALTHY HEALTHY HEALTHY SICK RECOVERING HEALTHY SICK RECOVERING HEALTHY HEALTHY', 'HEALTHY HEALTHY HEALTHY HEALTHY SICK RECOVERING HEALTHY SICK RECOVERING HEALTHY HEALTHY SICK RECOVERING HEALTHY',
# '14'
# ]

print(traceDisease(travelers_info))
