from collections import defaultdict


class Database:
  """
  In-memory database.

  Example usage:
    commands = [
      'SET ex 5',
      'GET ex',
      'BEGIN',
      'SET ex 10',
      'COMMIT',
      'GET ex',
      'END'
    ]

    db = Database()
    db.run(commands)
    print('Done.')
  """
  def __init__(self):
    self.data_ = {}
    self.val_count_ = defaultdict(int)

  def execute(self, command):
    """
    Execute a single command. The command is committed immediately.

    Input:
      command: str.

    Returns:
      Nothing.
    """
    tokens = command.split()
    op = tokens[0]
    if op == 'SET':
      name, value = tokens[1:]

      # Update counter.
      self.val_count_[value] += 1
      if name in self.data_:
        old_value = self.data_[name]
        self.val_count_[old_value] -= 1

      # Perform SET.
      self.data_[name] = value
    elif op == 'GET':
      name = tokens[1]
      value = self.data_.get(name, 'NULL')
      print('{}: {}'.format(command, value))
    elif op == 'UNSET':
      name = tokens[1]

      # Update counter.
      if name in self.data_:
        value = self.data_[name]
        self.val_count_[value] -= 1

      # Perform UNSET.
      self.data_.pop(name, None)
    elif op == 'NUMWITHVALUE':
      value = tokens[1]
      count = self.val_count_[value]
      print('{}: {}'.format(command, count))
    elif op == 'END':
      pass
    else:
      raise Exception('Unsupported command: {}'.format(command))

  def run(self, commands):
    """
    Inputs:
      commands: List[str]. A list of commands. Supported commands:
        Set name value
        Get name
        UNSET name
        NUMWITHVALUE value

    Returns:
      Nothing. Executes all commands.
    """
    def run_transaction(i):
      """
      Identify a transaction block from a command sequence, and execute the commands if a commit command is seen.

      Inputs:
        i: Int. start index of the transaction block from "commands".

      Returns:
        (new_i, status): (Int, Str). "new_i" is the index next to the end of the transaction block. "status" is the status code of the given transaction block.
      """
      trans = []
      while i < len(commands):
        command = commands[i]
        tokens = command.split()
        op = tokens[0]
        if op == 'BEGIN':
          i, status = run_transaction(i + 1)

          # COMMIT all open transactions.
          if status == 'COMMIT':
            for command in trans:
              self.execute(command)
            return i, 'COMMIT'
        elif op in { 'SET', 'GET', 'UNSET', 'NUMWITHVALUE' }:
          trans.append(command)
          i += 1
        elif op == 'ROLLBACK':
          return i + 1, 'ROLLBACK'
        elif op == 'COMMIT':
          for command in trans:
            self.execute(command)
          return i + 1, 'COMMIT'
        elif op == 'END':
          i += 1
          assert i == len(commands)
        else:
          raise Exception('Unsupported command: {}'.format(command))

      return i, 'UNFINISHED'

    i = 0
    while i < len(commands):
      command = commands[i]
      tokens = command.split()
      op = tokens[0]
      if op == 'BEGIN':
        i, trans = run_transaction(i + 1)
      else:
        self.execute(command)
        i += 1


################## Test code below. ##################

# # Basic test.
# commands = [
#   'SET ex 10',
#   'GET ex',
#   'NUMWITHVALUE 10',

#   # Set val to same value.
#   'SET ex 10',
#   'NUMWITHVALUE 10',

#   # Set val to different value.
#   'SET ex 12',
#   'NUMWITHVALUE 10',
#   'NUMWITHVALUE 12',

#   'UNSET ex',
#   'GET ex',
#   'NUMWITHVALUE 10',
#   'NUMWITHVALUE 12',
#   'END'
# ]

# # Basic transaction with rollback.
# commands = [
#   'BEGIN',
#   'SET ex 10',
#   'GET ex',
#   'ROLLBACK',
#   'GET ex',
#   'END'
# ]

# # Basic transaction with commit.
# commands = [
#   'BEGIN',
#   'SET ex 10',
#   'GET ex',
#   'COMMIT',
#   'GET ex',
#   'END'
# ]

# Nested transaction with rollback.
commands = [
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
db.run(commands)
print('Done.')
