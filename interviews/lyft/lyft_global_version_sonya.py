"""



设计2个database:
    1) dictionary{key: value}
    # most up-to-date data
    2) history list: list of  list [[key1, value1], [key2, value2], ...]]
    3) key_history dictionary {key1: [2, 5, 7]}, key2: [3, 4, 8]}

PUT key1 value1
history list: [[key1, value1]]


put key1, value2
history list: [[key1, value1], [key1, value2], .....]

get key1, version 3

for GET function:
    just get from dictionary

for PUT function:
    1. check if this key already in the dictionary
    2. if in dictionary:
        just update the new info into the ditionary
    3. if NOT in dictionary:
        just update into the ditionary
    (2 and 3 are same)
    4. update the histroy with .append([new_key, new_value])
    5. key_history

for GET key version#:
    1. find the version#index (index-1) in the history list
    2. from that (version#-1)th history, find the most before recent list
        2.1 if found:
        value = list[#][1]
        return print("{}:{}".format(command, value))



"""


from collections import defaultdict

class Database:
    def __init__(self):
        self.dict = {}
        self.history = []
        self.key_history = defaultdict(list)

    def find_version(self, key, target_version):
        """
        input key: str
        input target_version: int
        return ouput latest_closest version: int

        """
        key_list = self.key_history[key]

        # corner case:
        # key_list has only 1 item
        if len(key_list) < 2:
          # if target_version < existing only version
          # return "None"
          if target_version < key_list[0]:
            return "None"
          else:
            return key_list[0]

        l = 0
        r = len(key_list) - 1
        while l <= r:
            mid = (l + r) // 2
            print("l", l, "r", r, "mid",mid)

            if key_list[mid] == target_version:
                return key_list[mid]
            elif key_list[l] < target_version < key_list[mid]:
                if key_list[mid - 1] < target_version < key_list[mid]:
                    return key_list[mid - 1]
                else:
                    r = mid - 1
                print("left")
            elif key_list[mid] < target_version < key_list[r]:
                if key_list[mid] < target_version < key_list[mid + 1]:
                    return key_list[mid]
                else:
                    l = mid + 1
                print("right")
            print("after: l", l, "r", r)
        if key_list[l] < target_version < key_list[r]:
            print("l", l, key_list[l], "r", r, key_list[r])
            return key_list[l]

    def run(self, commands):
        i = 0
        while i < len(commands):
            command = commands[i]
            tokens = command.split()
            op = tokens[0]
            if op == "PUT":
                print("PUT", command)
                key = tokens[1]
                value = int(tokens[2])
                self.dict[key] = value
                self.history.append([key, value])
                version = len(self.history)
                self.key_history[key].append(version)
                print("PUT(#{}):{} = {}".format(version, key, value))
                i += 1
            if op == "GET":
                print("ENTER")
                key = tokens[1]
                print("key", key)
                # simple get
                if key not in self.key_history:
                    print("NOT find")
                    print("{}:{}".format(command, "NULL"))
                    i += 1
                elif len(tokens) == 2:
                    value = self.dict.get(key, "NULL")
                    print("{}: {}".format(command, value))
                    i += 1
                # else "GET KEY VERSION"
                else:
                    print("search version")
                    version = int(tokens[2])
                    latest_version = self.find_version(key, version)
                    print("latest_version", latest_version)
                    if latest_version == "None":
                      print("latest_versin", ":Does Not Exist")
                    else:
                      value = self.history[latest_version - 1][1]
                      print("latest_version", latest_version, value)
                      print("GET {} (#{}) = {}".format(key, version, value))
                    i += 1

####################### Test Case #################


# commands = [
#   "PUT key1 5",
#   "PUT key2 6",
#   "GET key1",
#   "GET key3",
#   "GET key3 1",
#   "GET key1 1"
# ]

# 例如我在你的输入中加入 "PUT key3 5", 则会在"GET key3 1"进入无限循环.
# FIXED
commands = [
  "PUT key1 5",
  "PUT key2 6",
  "PUT key3 5",
  "GET key1",
  "GET key3",
  "GET key3 1",
  "GET key1 1"
]

db = Database()
db.run(commands)
print("Finished")
