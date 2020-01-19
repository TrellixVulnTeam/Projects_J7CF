import Section_9_Package_Struct.common.validators as validators
import Section_9_Package_Struct.common.models


validators.is_boolean(1)
validators.is_integer(2)
validators.is_json('{}')


john_post = Section_9_Package_Struct.common.models.Post()
john_posts = Section_9_Package_Struct.common.models.Posts()
john = Section_9_Package_Struct.common.models.User()


print("\n\n**** self ****")
for k in dict(globals()).keys():
    print(k)

# print("\n\n **** Section_9_Package_Struct ****")
# for k in __dict__.keys():
#     print(k)

# print("\n\n **** common ****")
# for k in common.__dict__.keys():
#     print(k)

# print("\n\n **** validators ****")
# for k in common.validators.__dict__.keys():
#     print(k)
#
# print("\n\n **** numeric ****")
# for k in common.validators.numeric.__dict__.keys():
#     print(k)

# print("\n\n **** models ****")
# for k in models.__dict__.keys():
#     print(k)

print("\n\n **** models.post ****")
for k in Section_9_Package_Struct.common.models.posts.__dict__.keys():
    print(k)