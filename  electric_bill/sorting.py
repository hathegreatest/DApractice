# sort a dictionary by value   
def sort_dict_by_value(d):
    sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict
# sort a dictionary by key
def sort_dict_by_key(d):
    sorted_dict = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
    return sorted_dict
# sort a list of dictionaries by a key
def sort_list_dict_by_key(l, key):
    sorted_list = sorted(l, key=lambda x: x[key], reverse=True)
    return sorted_list

# dictionary comprehension
def dict_comprehension(d):
    new_dict = {k: v for k, v in d.items() if v > 0}
    return new_dict 
# list comprehension
def list_comprehension(l):
    new_list = [x for x in l if x > 0]
    return new_list 

# lambda function
def lambda_function(l):
    new_list = list(filter(lambda x: x > 0, l))
    return new_list


