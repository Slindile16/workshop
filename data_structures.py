def split_coords(coordinates):
    
    return tuple(list(i) for i in zip(*coordinates) )
# print(split_coords([(12, 45), (15, 48), (18, 51)]))

def flatten_list(nested_list):
    li = []
    for i in nested_list:
        if isinstance(i,list):
            li.extend(flatten_list(i))
        else:
            li.append(i)
    return li    
# print(flatten_list([[['a']], ['b', 'c']]))

def create_id_lookup(user_data):
    return {student: index for index , student in enumerate(user_data)}
# print(create_id_lookup(["Sipho", "Lerato", "Thandi", "Kobane"]))

def top_performer(student_data):
    new = max(student_data,key = student_data.get)
    return new
# print(top_performer({'A': 85, 'B': 90, 'C': 78, 'D': 92, 'E': 88}))


def group_by_category(items):
    grouped = {}
    for item in items:
        name = item["name"]
        type = item["type"]
        if type not in grouped:
            grouped[type] = []
        grouped[type].append(name)
    return grouped


def sort_by_length(names):
    sorted_list = sorted(names,key=len)
    return sorted_list
# print(sort_by_length(["Christopher", "Ava", "Joe", "Bernadette"]))

def sort_dict_by_value(data):
    return dict(sorted(data.items(), key=lambda item: item[1]))

# print(sort_dict_by_value({'x': 10, 'y': 5, 'z': 7}))

def rotate_list(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums
    return nums[-k:] + nums[:-k]


def sort_emails_by_domain(emails):
    return sorted(emails, key=lambda email: email.split("@")[1])

def is_subset(list_a, list_b):
    return all(item in list_b for item in list_a)

def remove_dictionary_key(data, keys_to_remove):
    if keys_to_remove not in data:
        return "Key not found"
    new_data = data.copy()
    new_data.pop(keys_to_remove)
    return new_data

def invert_dictionary(data):
    return {value: key for key, value in data.items()}

def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

def fibonacci_generator(n):
    if n <= 0:
        return []
    result = [0, 1]
    while len(result) < n:
        result.append(result[-1] + result[-2])
    return result[:n]