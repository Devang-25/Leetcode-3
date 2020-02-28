from collections import defaultdict

_debug = True

def dprint(*args, **kwargs):
    if _debug:
      print(*args, ** kwargs)

class Database:
    def __init__(self):
        self.data_ = {}
        self.val_count_ = defaultdict(int)

    def execute(self, command):
        """
        execute a single command
        """
        tokens = command.split() #split the single command text into words
        op = tokens[0] #the first word is the operaion
        if op == "SET":
            name, value = tokens[1:]

            # update val_counter dict
            # deduct the old value count -=1
            # if original value is already in the self.data_
            self.val_count_[value] += 1
            if name in self.data_:
                old_value = self.data_[name]
                self.val_count_[old_value] -= 1

            # perform set
            self.data_[name] = value
        elif op == "GET":
            name = tokens[1]
            value = self.data_.get(name, "NULL")
            print('{}: {}'.format(command, value))
        elif op == "UNSET":
            name = tokens[1]

            # update the counter
            # if name in self.data_
            if name in self.data_:
                old_value = self.data_[name]
                self.val_count_[old_value] -= 1

            # unset the data
            self.data_.pop(name, None)

        elif op == "NUMWITHVALUE":
            value = tokens[1]
            count = self.val_count_[value]
            print("{}: {}".format(command, count))
        elif op == "END":
            pass
        else:
            raise Exception("Unsupported command: {}".format(command))

    def run(self, commands):
        """
        input commands: list of commands
        output: nothing, just execute the commands
        """
        def transaction(i):
            """
            input i: int, the ith line of commands
            ouput (i+1_th, status): (int, str)
            i+1_th: the next line ith index of commands
            status: str ,th status of the given transaction block
            """
            trans = []
            while i < len(commands):
                command = commands[i]
                tokens = command.split()
                op = tokens[0]
                if op in {"SET", "GET", "UNSET", "NUMWITHVALUE"}:
                    trans.append(command)
                    i += 1
                elif op == "COMMIT":
                    dprint("commit")
                    for command in trans:
                        self.execute(command)
                    return i + 1, "COMMIT"
                elif op == "BEGIN":
                    dprint("begin")
                    i, status = transaction(i + 1)

                    # if the status returned above is commit
                    # then commit all the command in the upper (which is current) layer
                    if status == "COMMIT":
                        dprint("commit")
                        for command in trans:
                            self.execute(command)
                        return i, "COMMIT"
                elif op == "ROLLBACK":
                    return i + 1, "ROLLBACK"
                elif op == "END":
                    i += 1
                    assert i == len(commands)
                else:
                    raise Exception("UNSUPPORTED COMMAND: {}".format(command))
            return i, "UNFINISHED"

        i = 0
        while i < len(commands):
            command = commands[i]
            tokens = command.split()
            op = tokens[0]
            if op == "BEGIN":
                dprint("begin")
                i, status = transaction(i + 1)
            else:
                self.execute(command)
                i += 1


################## Test code below. ##################

# Basic test.
commands0 = [
  'SET ex 10',
  'GET ex', # print: GET ex: 10
  'NUMWITHVALUE 10',

  # Set val to same value.
  'SET ex 10',
  'NUMWITHVALUE 10',

  # Set val to different value.
  'SET ex 12',
  'NUMWITHVALUE 10',
  'NUMWITHVALUE 12',
  'UNSET ex',
  'GET ex',
  'NUMWITHVALUE 10',
  'NUMWITHVALUE 12',
  'END'
]


commands1 = [
  'SET ex 5',
  'GET ex',
  'BEGIN',
  'SET ex 10',
  'GET ex',
    'BEGIN',
    'SET ex 15',
    'GET ex',
    'ROLLBACK',
  'COMMIT',
  'GET ex',
  'END'
]

db = Database()
db.run(commands1)
print('Done.')
