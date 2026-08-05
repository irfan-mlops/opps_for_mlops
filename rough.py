# from oops_project import chatbook


# ls = [1, 2, 3, 4, 5]
# str = "Hello, World!"
# my_int = 1555

# print(type(ls))
# print(type(str))
# print(type(my_int))

# # ls.clear()
# print(ls)

from oops_project import chatbook

usser1 = chatbook()
print(usser1.id)

chatbook.set_id(11)

usser2 = chatbook()
print(usser2.id)

usser3 = chatbook()
print(usser3.id)

usser4 = chatbook()
print(usser4.id)

# print(usser1.get_name())
# (usser1.set_name("Agent XY"))
# print(usser1.get_name())
