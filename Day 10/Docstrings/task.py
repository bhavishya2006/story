# # # def format_name(f_name, l_name):
# # #     formated_f_name = f_name.title()
# # #     formated_l_name = l_name.title()
# # #     return f"{formated_f_name} {formated_l_name}"
# # #
# # #
# # # formatted_name = format_name("AnGeLa", "YU")
# # #
# # # length = len(formatted_name)
# # #
# # #
# # #
# #
# # def add(n1, n2):
# #     return n1 + n2
# #
# #
# # def subtract(n1, n2):
# #     return n1 - n2
# #
# #
# # def multiply(n1, n2):
# #     return n1 * n2
# #
# #
# # def divide(n1, n2):
# #     return n1 / n2
# #
# #
# # print(add(2, multiply(5, divide(8, 4))))
#
# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#
#     return inner_function(a, b)
#
#
# result = outer_function(5, 10)
# print(result)
#


def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))




















































































































