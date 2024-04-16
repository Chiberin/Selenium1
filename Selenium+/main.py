# name = input()
# with open(name, 'r') as file:
#     lines = file.readlines()
#     num_lines = len(lines)
# print(num_lines)

failename = input()
with open(failename, "r") as file:
    lines = file.readlines()
    for i in range(1, len(lines), 2):
        print(lines[i].strip())
        

# matrix = [[1,2,3],[4,5,6],[10,11,20]]

# max_element = matrix[0][0]
# min_element = matrix[0][0]
# for row in matrix:
#     for elem in row:
#         if elem > max_element:
#             max_element = elem
#         if elem < min_element:
#             min_element = elem
# print(max_element)
# print(min_element)

# Стихотворение

