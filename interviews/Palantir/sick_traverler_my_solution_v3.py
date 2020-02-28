############ Version 1 without Enum ############

from collections import defaultdict

def parseInfo(travelers_info):
  """
  input:
    travelers_info type: [str]

  output:
    names: [str]
    people_health : [str]
    travel_plan {name: cities} : {str:[str]}
  """

  names = []
  people_health = []
  travel_plan = defaultdict(list)

  for line in travelers_info:
    info = line.split()

    name = info[0]
    health = info[1]
    cities = info[2:]

    names.append(name)
    people_health.append(health)
    travel_plan[name] = cities

  return names, people_health, travel_plan

def get_location(names, travel_plan, day):
  """"
  inputs:
    names : [str]
    travel_plan {name: [cities]} : {str : [str]}
    day : int

  output:
    location : [str]

  """
  location = []
  for name in names:
    index = day % len(travel_plan[name]) - 1
    city = travel_plan[name][index]
    location.append(city)

  return location

def update_cities_status(names, people_health, location):
    """
    inputs:
        names: [str]
        people_health : [str]
        location: [str]


    output:
        cities_status {city: status} : {str : str "G" or "B"}
    """

    cities_status = defaultdict(str)

    for city in location:
        cities_status[city] = "G"

    for i, name in enumerate(names):
        health = people_health[i]
        city = location[i]

        if cities_status[city] == "G" and (health != "HEALTHY"):
            cities_status[city] = "B"

    return cities_status

def update_people_health(names, people_health, travel_plan, cities_status, day):
    """
    inputs:
        names: [str]
        people_health : [str]
        travel_plan {name: [citeis]} : {str : [citeis]}
        cities_status : {str : str}
        day : int

    output:
        new_health : [str]
    """
    new_health = []

    for i, name in enumerate(names):
        health = people_health[i]

        city_i = day % len(travel_plan[name])-1
        city = travel_plan[name][city_i]

        city_status = cities_status[city]

        if health == "SICK":
            h = "RECOVERING"
        elif health == "RECOVERING":
            h = "HEALTHY"
        elif health == "HEALTHY":
            if city_status == "G":
                h = "HEALTHY"
            elif city_status == "B":
                h = "SICK"

        new_health.append(h)

    return new_health



def traceDisease(travelers_info):
  """
  input:
    travelers_info type: [str]

  output:
    results: [str]
  """

  results = []

  names, people_health, travel_plan = parseInfo(travelers_info)

  results.append(" ".join(name for name in names))

  print(names)

  day = 1


  while day <= 365:
    results.append(" ".join(h for h in people_health))

    all_healthy = all([h == "HEALTHY" for h in people_health])

    if all_healthy or day == 365:
      break

    # get current location
    location = get_location(names, travel_plan, day)

    # update cities_status
    cities_status = update_cities_status(names, people_health, location)

    print(day, [(h, "/", l) for h, l in zip(people_health, location)])
    print([(city, "/", status) for city, status in cities_status.items()])
    print("\n")

    # for city, status in cities_status:
    #     print(city, "/", status)

    # update people_health
    people_health = update_people_health(names, people_health, travel_plan, cities_status, day)

    day += 1


  results.append(str(day))
  return results



# travelers_info = ["Michael HEALTHY PALOALTO","YUN RECOVERING PALOALTO DC"]

travelers_info = [
"Wilson SICK PaloAlto DC London PaloAlto",
"Yun HEALTHY PaloAlto",
"Ali RECOVERING DC DC DC London",
"Jasmin HEALTHY London"
]

print(traceDisease(travelers_info))


################### Version2 with Enum Implemented ############

# Complete the traceDisease function below.
# initialStates is an array of strings, each string a line of input.
# Your return value should also be a list of strings (see the prompt for the expected output format)
# Content sent to stdout (i.e. any print statements) will be sent to a separate output that is ignored by the test checker.
from collections import defaultdict
from enum import Enum

State = Enum("State", "HEALTHY RECOVERING SICK")
# class State(Enum):
#     HEALTHY = 1
#     RECOVERING = 2
#     SICK = 3
    


def stateFromString(state_str):
    if state_str == 'HEALTHY':
        return State.HEALTHY
    if state_str == 'RECOVERING':
        return State.RECOVERING
    if state_str == 'SICK':
        return State.SICK
    assert False


def parseInfo(initialStates):
    names = []
    people_health = []
    travel_plans = defaultdict(list)
    for line in initialStates:
        info = line.split()
        name = info[0]
        health_str = info[1]
        health = stateFromString(health_str)
        travel_plan = info[2:]

        names.append(name)
        people_health.append(health)
        travel_plans[name] = travel_plan

    return names, people_health, travel_plans

def getLocations(names, travel_plans, day):
    """
    inputs:
        names : [str]
        travel_plans : {str: [str]}

    output:
        locations: [str]
    """
    locations = []

    for i, name in enumerate(names):
        cur_city_index = day % len(travel_plans[name]) - 1
        cur_city = travel_plans[name][cur_city_index]
        locations.append(cur_city)

    return locations


def updateCitiesStatus(names, people_health, locations):
    """
    inputs:
        names
    """
    cities_status = defaultdict(str)

    for city in locations:
      cities_status[city] = State.HEALTHY

    for i, name in enumerate(names):
        h = people_health[i]
        city = locations[i]
        status = cities_status[city]

        if status == State.HEALTHY:
          if h != State.HEALTHY:
            cities_status[city] = State.SICK

    return cities_status

def updateHealthStatus(names, people_health, locations, cities_status):
    """
    inputs:

    outputs:
        new_health
    """
    new_health = []

    for i, name in enumerate(names):
        h = people_health[i]
        city = locations[i]
        new_h = None

        if h == State.SICK:
            new_h = State.RECOVERING
        elif h == State.RECOVERING:
            new_h = State.HEALTHY
        elif h == State.HEALTHY:
            if cities_status[city] == State.HEALTHY:
                new_h = State.HEALTHY
            elif cities_status[city] == State.SICK:
                new_h = State.SICK

        new_health.append(new_h)

    return new_health


def stateToStr(state):
    if state == State.HEALTHY:
        return 'HEALTHY'
    if state == State.RECOVERING:
        return 'RECOVERING'
    if state == State.SICK:
        return 'SICK'
    assert False


def traceDisease(initialStates):
    """
    inputs:
        initialStates: [str]

    outputs:
        results: [str]
    """
    results = []

    # parse information
    names, people_health, travel_plans = parseInfo(initialStates)

    results.append(" ".join(names))

    day = 1

    while day <= 365:
        results.append(" ".join([stateToStr(health) for health in people_health]))

        all_healthy = all([h == State.HEALTHY for h in people_health])
        if all_healthy or day == 365:
            break

        # if not all healthy and day not yet 365:
        # get each person's location
        # use locations information to update the cities_status_dict
        # use cities_status to update people's health stutus
        locations = getLocations(names, travel_plans, day)
        cities_status = updateCitiesStatus(names, people_health, locations)

        daily_result = ([stateToStr(health) for health in people_health])
        print("day", day, ["%s/%s" % (r, l) for r, l in zip(daily_result, locations)], ["%s:%s" % (c, stateToStr(s)) for c, s in cities_status.items()])

        people_health = updateHealthStatus(names, people_health, locations, cities_status)

        day += 1

    results.append(str(day))

    return results


# travelers_info = ["Michael HEALTHY PALOALTO","YUN RECOVERING PALOALTO DC"]

travelers_info = [
"Wilson SICK PaloAlto DC London PaloAlto",
"Yun HEALTHY PaloAlto",
"Ali RECOVERING DC DC DC London",
"Jasmin HEALTHY London"
]

results = traceDisease(travelers_info)

for result in results:
  print(result)
