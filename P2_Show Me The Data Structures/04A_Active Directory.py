#!/usr/bin/env python
# coding: utf-8

# ## Active Directory
# 
# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

# In[1]:


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


# Write a function that provides an efficient look up of whether the user is in a group.

# In[2]:


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()
    if user in users:
        return True
    else:
        #check user membership to see if the user exists in any group
        group_list = group.get_groups()
        for group in group_list:
            if is_user_in_group(user, group):
                return True
    return False


# In[10]:


print("Testcase 1")
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child_user_b = "sub_child_user_b"
child.add_group(sub_child)
parent.add_group(child)

print("Is sub_child_user in parent group?", is_user_in_group(sub_child_user, parent))
print("Is sub_child_user in child group?", is_user_in_group(sub_child_user, child))
print("Is sub_child_user in sub_child group?", is_user_in_group(sub_child_user, sub_child))
print("is sub_child_user_b in sub_child group?", is_user_in_group(sub_child_user_b, sub_child))


# In[8]:


print("Testcase 2")
group2 = Group("test_group")
group2b = Group("test_group_b")
user1 = "user1"
user2 = "user2"
user3 = ""
group2.add_user(user1)
group2b.add_user(user2)
group2.add_group(group2b)

print("Is user1 in group2?", is_user_in_group(user1, group2))
print("Is user 2 in group2b?", is_user_in_group(user2, group2b))
print("Is user 2 in group2?", is_user_in_group(user2, group2))
#Edge case
print("Is user 3 in group 2?", is_user_in_group(user3, group2))
print("Is user 3 in group 2?", is_user_in_group(user3, group2b))


# In[11]:


print("Testcase 3")
empty = Group("Edge case group")
user1 = "user1"

print("Edge case group has user?", is_user_in_group(user1, empty))


# In[16]:


print("Testcase 4")
Edge_case = Group("")
user1 = "user1"
user2 = ""
Edge_case.add_user(user1)
print("Edge case group has user1?", is_user_in_group(user1, Edge_case))
print("Edge case group has user2?", is_user_in_group(user2, Edge_case))


# In[ ]:




