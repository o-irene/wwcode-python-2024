# Task: Write a program to remove duplicates from a list.

def remove_list_duplicates(ls):
    unique_ls = list(set(ls))
    return unique_ls


assert sorted(remove_list_duplicates([5, 5, 6, 1, 1, 1, 0])) == [0, 1, 5, 6]
assert sorted(remove_list_duplicates(['a', 'a', 'a', 'x', 'y', 'z'])) == ['a', 'x', 'y', 'z']
