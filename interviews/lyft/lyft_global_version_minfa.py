"""
Build a simple key-value store for storing integers (keys are strings, values are integers) and global version (integer). You will store data in memory.

Version increases every time any key is written with a value. The first write is version number 1.

Three operations:
1) PUT <key> <value> -- returns the version number of this write.
   Print format: PUT(#<version number>) <key> = <value>
2) GET <key> -- returns the LAST value mapped to the key.
   Prints out the key and the last value of the key, or <NULL>. Format: GET <key> = <value>
3) GET <key> <version number> -- returns the value mapped to the key at the time of the version number.
   Format: GET <key>(#version) = <value>
"""


from collections import defaultdict


class VersionedDb:
    def __init__(self):
        self.version_ = 0
        self.data_ = defaultdict(list)

    def run(self, commands):
        for command in commands:
            tokens = command.split()
            op = tokens[0]
            if op == 'PUT':
                key, value = tokens[1:]
                self._put(key, int(value))
            elif op == 'GET' and len(tokens) == 2:
                key = tokens[1]
                self._get(key)
            elif op == 'GET' and len(tokens) == 3:
                key, version = tokens[1:]
                self._versioned_get(key, int(version))
            else:
                raise Exception('Unknown command: {}'.format(command))

    def _put(self, key, value):
        self.version_ += 1
        self.data_[key].append({
            'version': self.version_,
            'value': value
        })
        print('PUT {} {}'.format(key, value))
        return self.version_

    def _get(self, key):
        if key not in self.data_:
            print('GET {} = {}'.format(key, '<NULL>'))
            return

        value = self.data_[key][-1]['value']
        print('GET {} = {}'.format(key, value))
        return value

    def _versioned_get(self, key, version):
        # Do binary search to find the value whose version <= input version
        records = self.data_[key]
        i, j = 0, len(records)
        while i < j:
            m = (i + j) // 2
            version_m = records[m]['version']
            if version_m > version:
                j = m
            else:
                i = m + 1

        if key not in self.data_ or i == 0:
            print('GET(#{}) {} = {}'.format(version, key, '<NULL>'))
            return

        value = records[i-1]['value']
        print('GET(#{}) {} = {}'.format(version, key, value))
        return value


commands = [
    'PUT key1 5',
    'PUT key2 6',
    'GET key1',
    'GET key1 1',
    'GET key2 2',
    'PUT key1 7',
    'GET key1 1',
    'GET key1 2',
    'GET key1 3',
    'GET key4',
    'GET key2 1',
]

db = VersionedDb()
db.run(commands)
