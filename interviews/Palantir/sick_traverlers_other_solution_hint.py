"""
Source: https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=484399

# Input : vector<string> name initial_health_stats cities

# Output: vector<string first line names
# After each line each person's healthy stats
# The last line outputs converge days\

#Use a hashmap to save each city Everyth. There is no pick and recovery. Then traverse and update everyone's state.
# That is, parse input and output are a bit of a hassle. Time is not enough.

# The infection condition is an office in a city, so I Use a map, the key is the city, and the value is the list of names.
# I divide the current situation and the change situation into two parts, so that I will know immediately if I am all healthy at first,
#

等I will deal with other edge cases in the latter.
# Basically look at the status quo and change the situation, you just write them as they say. At least I don't have time out.
# Pay special attention to the 365th Because there are two kinds of conditions, either full health or not all healthy,
# but they are the last number of 365, and it should be no problem if you pay attention to it.

# I scan every office every day to see If I am sick, and then change the status of each person.

# change the whole thing every time
# healthy, recovering, sick


#sick recovering always changes, healthy when sick

# Wilson Sick DC DC

"""


######################### other raw solution #####
# def test(input):
#
#
#
# people = {}
# cities = {}
# For employee in input:
# employee = employee.split()
# #initialize people with current condition
# people[employee[0]] = employee[1]
# for city in employee[2:]:
# #initialize a list for each city
# if city not in Cities :
# cities[city] = []
#
# #output
# res = []
# #add people for first line of output
# allPeople = []
# for person in people:
# allPeople.append(person)
# res.append(allPeople)
#
#
# dayNumber = 1
# #366
# while dayNumber < 366:
# #record output
# peopleStates = []
# for person in people:
# peopleStates.append(people[person])
# res.append(peopleStates)
#
#
#
#
#
#
# #clear cities
# for city in cities:
# cities[city] = []
#
# #add employees to each city
# for employee in input:
# employee = employee.split()
# schedule = Employee[2:]
# currentCity = schedule[(dayNumber-1)%len(schedule)] #fix
# cities[currentCity].append(employee[0])
#
#
# #new day
# #iterate each city
# allHealthy = True
# for city in cities:
# isSick = False
# employees = cities[city]
#
#
#
# for employee in employees:
# # print(employee,people[employee])
# if people[employee] == "SICK" or people[employee] == "RECOVERING":
# isSick = True
# allHealthy = False
#
# for employee in employees:
# if people[employee] == " SICK":
# people[employee] = "RECOVERING"
# elif people[employee] == "RECOVERING":
# people[employee] = "HEALTHY"
# elif people[employee] == "HEALTHY" and isSick:
# people[employee] = "SICK "
# allHealthy = False
#
#
#
# if allHealthy:
# Res.append(dayNumber)
# Return res
#
# dayNumber += 1
# allHealthy = True
#
# res.append(365)
# return res
#
#
#
#
#
#
# if __name__ == "__main__":
# input = ["Michael HEALTHY PALOALTO","YUN RECOVERING DC","JASMINE SICK LONDON"]
#
# input = [" Jasmine SICK DC DC DC DC DC DC","NICK HEALTHY DC NY NY NY NY PA","YUN HEALTHY PA DC PA PA PA PA"]
#
# print(test(input))


def test(input):

    people = {}
    cities = {}
    for employee in input:
        employee = employee.split()
        #initialize people with current condition
        people[employee[0]] = employee[1]

        for city in employee[2:]:
            #initialize a list for each city
            if city not in cities :
                cities[city] = []

    #output
    res = []

    #add people for first line of output
    allPeople = []

    for person in people:
        allPeople.append(person)
    res.append(allPeople)


    dayNumber = 1
    #366
    while dayNumber < 366:
    #record output
        peopleStates = []
        for person in people:
            peopleStates.append(people[person])
            res.append(peopleStates)

        #clear cities
        for city in cities:
            cities[city] = []

    #add employees to each city
    for employee in input:
    employee = employee.split()
    schedule = Employee[2:]
    currentCity = schedule[(dayNumber-1)%len(schedule)] #fix
    cities[currentCity].append(employee[0])


    #new day
    #iterate each city
    allHealthy = True
    for city in cities:
        isSick = False
        employees = cities[city]



        for employee in employees:
            # print(employee,people[employee])
            if people[employee] == "SICK" or people[employee] == "RECOVERING":
                isSick = True
                allHealthy = False

        for employee in employees:
            if people[employee] == " SICK":
                people[employee] = "RECOVERING"
            elif people[employee] == "RECOVERING":
                people[employee] = "HEALTHY"
            elif people[employee] == "HEALTHY" and isSick:
                people[employee] = "SICK "
                allHealthy = False



    if allHealthy:
        Res.append(dayNumber)
        Return res

    dayNumber += 1
    allHealthy = True

    res.append(365)
    return res






if __name__ == "__main__":
input = ["Michael HEALTHY PALOALTO","YUN RECOVERING DC","JASMINE SICK LONDON"]

input = [" Jasmine SICK DC DC DC DC DC DC","NICK HEALTHY DC NY NY NY NY PA","YUN HEALTHY PA DC PA PA PA PA"]

print(test(input))
