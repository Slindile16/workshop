# workshop
# fun-003 - Data Structures



---

## Coding Assessment

This assessment consists of five Python functions ordered from easiest to most difficult. Each function must be implemented from scratch.

---

### Question 1 - split_coords(coordinates)

A team of eco-adventurers is mapping out a new hiking trail along the Wild Coast in the Eastern Cape. Their GPS device records the path as a series of coordinates, stored as pairs of (latitude, longitude); or in our case, *$(x, y)$* values.The navigation team at the base camp in Chintsa needs these coordinates separated. They need one list containing only the $x$ values (to calculate horizontal distance) and another list containing only the $y$ values (to track the vertical path). Instead of looking at them as pairs, they need two distinct "tracks" of data.

Apply your logic to the split_coords() function. You will receive a list of tuples, where each tuple contains two numbers. Your goal is to "unzip" or split these pairs into two separate lists.

- *Input:*

```python
[(12, 45), (15, 48), (18, 51)]
```


- *Output:*

```python
([12, 15, 18], [45, 48, 51])
```

### Question 2 - flatten_list(nested_list)

User Story:
As a data engineer, I need to flatten nested lists into a single list to simplify data processing and analysis.

Test Cases:
Input: [[1, 2], [3, 4]] → Output: [1, 2, 3, 4]
Input: [[['a']], ['b', 'c']] → Output: ['a', 'b', 'c']

### Question 3 - create_id_lookup(user_data)

It’s registration day for the Comrades Marathon in Durban! Thousands of runners are arriving to collect their race numbers. The volunteers at the desk have a list of runner names in the order they signed up (their "index" in the system).

To speed up the process, the organisers want a quick "lookup" system. Instead of scrolling through a long list every time a runner arrives, they want a digital folder (a dictionary) where they can type in a runner's name and immediately get their ID/Index number.

Apply your logic to the create_id_lookup() function. The function takes a list of names and should return a dictionary where each runner's name acts as the key and their position in the list (index) is the value.

- *Input:*

```python
["Sipho", "Lerato", "Thandi", "Kobane"]
```


- *Output:*

```python
{"Sipho": 0, "Lerato": 1, "Thandi": 2, "Kobane": 3}
```




### Question 4 - `top_performer(student_data)`

**User Story:**
As a school administrator, I need to identify the student with the highest marks in a class to award them the "Top Performer" certificate for the term.

```
input 1:
```python
top_performer({'A': 85, 'B': 90, 'C': 78, 'D': 92, 'E': 88})
```
output:
```python
'D'
```
input 2:
```python
top_performer({'Tom': 67, 'Jerry': 89, 'Mickey': 95, 'Donald': 80})
```
output: 
```python
'Mickey'
```
input 3:
```python
top_performer({'Raj': 60, 'Simran': 60, 'Aman': 59})
```
output: 
Returns: 'Raj' or 'Simran'
```
### Question 5 - `sort_by_length(names)`

User Story:
As a graduation ceremony coordinator, I need to sort student names by their length so that the printer can organize name tags from the smallest size to the largest.

```
input:
```python
names = ["Christopher", "Ava", "Joe", "Bernadette"]
```
output:
```python
["Ava", "Joe", "Bernadette", "Christopher"]
```



### Question 6 - group_by_category(items)

A major South African supermarket chain in Johannesburg is preparing for the "Braai Day" rush. Their online shopping app receives a messy list of items from a customer’s trolley, but the personal shoppers at the store need the list organised by Aisle Category so they can pick the items quickly without walking back and forth across the shop.

Apply your logic to the group_by_category() function. You will take a list of dictionaries, each containing a name and a type, and transform them into a single dictionary where each type is a key, and its value is a list of all item names belonging to that category.

- *Input:*

```python
[{"name": "Boerewors", "type": "Meat"}, {"name": "Charcoal", "type": "Hardware"}, {"name": "Lamb Chops", "type": "Meat"}, {"name": "Chakalaka", "type": "Canned Goods"}]
```


- *Output:*

```python
{"Meat": ["Boerewors", "Lamb Chops"], "Hardware": ["Charcoal"], "Canned Goods": ["Chakalaka"]}
```
#### Question 7 - `sort_dict_by_value(data)`

User Story:
As a data analyst, I often receive frequency maps or scoreboards in dictionary format. To generate reports, I need to reorganize these dictionaries so that the items are ordered from the lowest value to the highest value.

```
input 1:
```python
{'a': 3, 'b': 1, 'c': 2}
```
output 1:
```python
{'b': 1, 'c': 2, 'a': 3}
```

input 2:
```python
sort_dict_by_value({'x': 10, 'y': 5, 'z': 7})
```
output 2:
```python
{'y': 5, 'z': 7, 'x': 10}
```


### Question 8 - `rotate_list(nums, k)`

User Story:
As a developer building a digital carousel for a website, I need to rotate the items in my list to the right by a specific number of positions. This will allow the items at the end of the list to "wrap around" to the front.

Handle empty lists by returning an empty list.
input 1:
```python
rotate_list([1, 2, 3, 4, 5], 2)
```
output 2:
```python
[4, 5, 1, 2, 3]
```

input 2:
```python
rotate_list([10, 20, 30], 1)
```
output 2: 
```python
[30, 10, 20]
```

input 3: (k > length)
```python
rotate_list([1, 2], 3)
```
output 3:
```python
[2, 1]
```

### Question 9 - `sort_emails_by_domain(emails)`

User Story:
As a system administrator, I need to group our user mailing list by their email providers. By sorting the list alphabetically by the domain name (the part after the '@'), I can easily identify how many users belong to Gmail, Outlook, or Yahoo.

input:
```python
["alice@yahoo.com", "bob@gmail.com", "charlie@outlook.com", "dave@gmail.com"]
```

output:
```python
["bob@gmail.com", "dave@gmail.com", "charlie@outlook.com", "alice@yahoo.com"]
```
(Note: gmail.com < outlook.com < yahoo.com)

### Question 10 - `is_subset(list_a, list_b)`

User Story:
As a security administrator, I need to check if a list of requested permissions (List A) is entirely contained within a user's assigned permissions (List B) to ensure they are authorized to perform an action.
input 1:
```python
is_subset([1, 2], [1, 2, 3, 4])
```
output 1:
```python
True
```

input 2:
```python
is_subset([5, 6], [1, 2, 3])
```
output 2: 
```python
False
```
input 3:
```python
is_subset(['a'], ['a', 'b', 'c'])
```
output 3:
```python
True
```

### Question 11 - `remove_dictionary_key(data, key_to_remove)`

User Story:
As a database administrator, I need a tool that can remove specific user attributes from a record. However, if I try to remove a piece of information that doesn't exist, the system should notify me rather than breaking.
input 1:
```python
({'a': 1, 'b': 2, 'c': 3}, 'b')
```
output 1: 
```python
{'a': 1, 'c': 3}
```
input 2:
```python
remove_dictionary_key({'x': 10}, 'x')
```
output:
```python
{}
```
input 3:
```python
remove_dictionary_key({'p': 5, 'q': 6}, 'z')
```
output 3: 
```python
"Key not found"
```


### Question 12 - `invert_dictionary(data)`

User Story:
As a data architect, I sometimes need to reverse a lookup table. For example, if I have a dictionary mapping usernames to ID numbers, I may need to invert it to find which username belongs to a specific ID.

input 1:
```python
{'a': 1, 'b': 2}
```
output 1: 
```python
{1: 'a', 2: 'b'}
```

input 2:
```python
{'x': 5, 'y': 5}
```
output 2:
```python
{5: 'y'}
```

input 3:
```python
{'p': True, 'q': False}
```
output 3:

{True: 'p', False: 'q'}

### Question 13 - `recursive_sum(n)`

User Story:
As a software engineer optimizing a mathematical engine, I need a way to calculate the sum of all integers from 1 up to a given number n. Using recursion allows me to express this calculation as a clean, self-referential mathematical sequence.

input:
```python
recursive_sum(5)
```
output: 
```python
15
```

### Question 14 - fibonacci_generator(n)

Scientists at the Kirstenbosch National Botanical Garden in Cape Town are studying the growth patterns of various indigenous succulents and flowers, like the Protea. In nature, many plants follow a mathematical sequence where each new stage of growth is the sum of the two previous stages, this is known as the Fibonacci Sequence. The research team needs a tool to predict the number of petals or seed spirals a plant might develop over $n$ generations. To help them, you need to provide a list of the sequence up to the $n^{th}$ number.

Apply your solution to the fibonacci_generator(n) function. The function should take an integer $n$ and return a list containing the first $n$ numbers of the Fibonacci sequence.

- *Input:*

python
n = 7


- *Output:*

python
[0, 1, 1, 2, 3, 5, 8]


### Extras
### Question 15 - `lists_to_dict(keys, values)`

User Story:
As a data engineer, I often receive headers and data rows as separate lists. I need a reliable way to map these together into a dictionary format for easier searching and data manipulation.
input 1:
```python
(['a', 'b', 'c'], [1, 2, 3])
```
output 1:
```python
{'a': 1, 'b': 2, 'c': 3}
```
input 2:
```python
(['x', 'y'], [10])
```
output 2:
```python
{'x': 10}
```
input 3:
```python
([], [])
```
output 3:
```python
{}
```

### Question 16 - `count_frequencies(items)`

User Story:
As a social media analyst, I need to count how many times different hashtags appear in a list so that I can determine which topics are trending.
input 1:
```python
count_frequencies([1, 2, 2, 3, 3, 3])
```
output 1:
```python
{1: 1, 2: 2, 3: 3}
```

input 2:
```python
count_frequencies(['a', 'b', 'a'])
```
output 2:
```python
{'a': 2, 'b': 1}
```

input 3:
```python
count_frequencies([])
```
output 3:
```python
{}
```

### Question 17 - `tuples_to_dict(tuple_list)`

User Story:
As a data scientist, I often receive coordinates or paired observations as a list of tuples. I need to convert these into a dictionary so I can quickly look up a specific observation using its unique label.
input 1:
```python
tuples_to_dict([('a', 1), ('b', 2)])
```
output 1:
```python
{'a': 1, 'b': 2}
```

input 2:
```python
tuples_to_dict([('x', 10), ('x', 20)])
```
output 2:
```python
{'x': 20}
```

input 3:
```python
tuples_to_dict([])
```
output 3:
```python
{}
```