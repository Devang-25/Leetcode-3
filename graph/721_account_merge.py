# from collections import defaultdict

# class Solution(object):

#   def accountsMerge(self, accounts):
#     """
#     :type accounts: List[List[str]]
#     :rtype: List[List[str]]
#     """
#     self.emails_dict = defaultdict(int)  # {em: id}
#     self.accounts_dict = defaultdict(int)  # {id: root_id}
#     self.roots_emails = defaultdict(list)  # {root: [emails]}
#     self.results = []

#     for i, account in enumerate(accounts):
#       # print("\nemails_dict", self.emails_dict)
#       # print("accounts_dict", self.accounts_dict)
#       # print("i:{}, account:{}".format(i, account))
#       # account = [str] = [name, email, ...]
#       emails = account[1:]
#       self.accounts_dict[i] = i
#       for email in emails:
#         if email not in self.emails_dict:
#           self.emails_dict[email] = i
#         else:
#           parent = self.emails_dict[email]
#           root = self.find_parent(parent)
#           self.union(root, i)

#     # 根据accounts_dict来merge result
#     for account, parent in self.accounts_dict.items():
#       root = self.find_parent(parent)
#       emails = accounts[account][1:]
#       self.roots_emails[root] += emails

#     for root, emails in self.roots_emails.items():
#       name = accounts[root][0]
#       emails_set = sorted(set(emails))
#       emails = list(emails_set)
#       info = [name] + emails
#       self.results.append(info)

#     return self.results

#   def find_parent(self, id):
#     if self.accounts_dict[id] == id:
#       return id
#     else:
#       return self.find_parent(self.accounts_dict[id])

#   def union(self, x, y):
#     x_set = self.find_parent(x)
#     y_set = self.find_parent(y)
#     self.accounts_dict[x_set] = y_set

########################################
"""
解题思路： 把是同一个账户的邮箱连接起来（取其中一个邮箱作为root). 
"""
from collections import defaultdict


class Solution(object):

  def accountsMerge(self, accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """

    self.em_dict = {}
    self.em_to_name = {}

    for acc in accounts:
      name = acc[0]
      for em in acc[1:]:
        self.em_to_name[em] = name
        if em not in self.em_dict:
          self.em_dict[em] = em
          self.em_dict[em] = self.find_parent(acc[1])
        elif em in self.em_dict:
          p1 = self.find_parent(em)
          p2 = self.find_parent(acc[1])
          self.union(p1, p2)

    self.em_merge = defaultdict(list)
    for em in self.em_dict:
      p = self.find_parent(em)
      self.em_merge[p].append(em)

    results = [
        [self.em_to_name[v[0]]] + sorted(v) for v in self.em_merge.values()
    ]

    return results

  def find_parent(self, em):
    if self.em_dict[em] == em:
      return em
    return self.find_parent(self.em_dict[em])

  def union(self, x, y):
    x_set = self.find_parent(x)
    y_set = self.find_parent(y)
    self.em_dict[x_set] = y_set


s = Solution()

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]
output = [[
    "John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'
], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
print("result", s.accountsMerge(accounts))

# accounts = [["David", "David0@m.co", "David4@m.co", "David3@m.co"],
#             ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
#             ["David", "David1@m.co", "David4@m.co", "David0@m.co"],
#             ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
#             ["David", "David4@m.co", "David1@m.co", "David3@m.co"]]

r = s.accountsMerge(accounts)
output = [[
    "David", "David0@m.co", "David1@m.co", "David3@m.co", "David4@m.co",
    "David5@m.co"
]]
print("result", r)
assert r == output