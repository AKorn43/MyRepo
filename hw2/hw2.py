# Arielle Korn
# Professor Malone, Sean Gallagher, Jess Esch

def exchange(str):
    char1 = str[0]
    char2 = str[-1]
    new_string = char2 + str[1:-1] + char1
    if len(str) > 1:
        return new_string
    else:
        return char1
    

    """
    Given a string, return a new string where the first and last chars
    have been exchanged.
    """


def remove_range(alist, min, max):
    new_range = [x for x in alist if x > max or x < min]
    return new_range

    """
    Use comprehension to write a method named removeRange that accepts a list of
    integers and two integer values min and max as parameters and removes all elements
    values in the range min through max (inclusive).
    For example, if a alist named list stores
    [7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], the call of remove_range(alist, 5, 7);
    should change the list to store [9, 4, 2, 3, 1, 8].

   *** Important: your code must use comprehensions and should not be more than
   two lines of code including the return statement ***
    """


def word_count_in_set(words):
    new_set = set(words)
    return len(new_set)
     

    
    """
    Write a function named wordCount that accepts a list of strings as a parameter and
    returns a count of the number of unique words in the list. Do not worry about
    capitalization and punctuation; for example, "Hello" and "hello" and "hello!!" are
    different words for this problem.
    *** Solution should not be more than 3 lines of code (can be less)
     including the return statement ***
    """



def topping1(dictionary):

    if "ice cream" in dictionary:
        dictionary["ice cream"] = "cherry"
        
    dictionary["bread"] = "butter"

    return dictionary



    """
    Given a dictionary of food keys and topping values, modify and return the dictionary
    as follows:
    if the key "ice cream" is present, set its value to "cherry".
    In all cases, set the key "bread" to have the value "butter".
    Examples:
    topping1({"ice cream": "peanuts"}) returns {"bread": "butter", "ice cream": "cherry"}
    topping1({})  {"bread": "butter"} returns {"bread": "butter"}
    topping1({"pancake": "syrup"}) returns {"bread": "butter", "pancake": "syrup"}
    """


def word_count(strings):

    word_count = {key: strings.count(key) for key in strings}
    return word_count
    """
    The classic word-count algorithm: given an array of strings, return a dictionary with
    a key for each different string, with the value the number of times that string appears in the
    list.
    Examples:
    word_count(["a", "b", "a", "c", "b"]) returns {"a": 2, "b": 2, "c": 1}
    word_count(["c", "b", "a"]) returns {"a": 1, "b": 1, "c": 1}
    word_count(["c", "c", "c", "c"]) returns {"c": 4}
    *** Important: your code must use comprehensions and should not be more than two
    lines of code including the return statement ***
    """


def friend_list(friend_dictionary):
    friend_relationships = {}
    for key, value in friend_dictionary.items():
        if key not in friend_relationships:
            friend_relationships[key] = []
        if value not in friend_relationships:
            friend_relationships[value] = []

        friend_relationships[key].append(value)
        friend_relationships[value].append(key)

    return friend_relationships
    """
    Write a method named friendList that accepts a dictionary as a parameter and reads
    friend relationships and stores them into a new dictionary that is returned.
    You should create a new dictionary where each key is a person's name from the original
    simple dictionary, and the value associated with that key is a list of all friends of
    that person. Friendships are bi-directional:
    if Marty is friends with Danielle, Danielle is friends with Marty.

    The dictionary parameter contains one friend relationship per key/value pair,
    consisting of two names. If the dictionary parameter,friendMap looks like this:
    Marty: Cynthia
    Danielle: Marty
    Then the call of friendList(friendMap) should return a dictionary with the following
    contents:
    {Cynthia:[Marty], Danielle:[Marty], Marty:[Cynthia, Danielle]}
    """
    pass


# Test functions
assert exchange("code") == "eodc", 'exchange("code") expected eodc'
print("correct")
assert exchange("ba") == 'ab', 'exchange("ba") expected ab'
print("correct")
assert exchange("a") == 'a', 'exchange("a") expected a'
print("correct")

assert remove_range([7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], 5, 7) == [9, 4, 2, 3, 1, 8] , '[9, 4, 2, 3, 1, 8] expected'
print("correct")
assert remove_range([7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], 2, 3) == [7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], '[7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7] expected'
print("correct")
assert remove_range([7, 9, 7], 7, 9) == [], '[] expected'
print("correct")

assert word_count_in_set(["the", "quick", "brown", "fox", "brown"]) == 4, 'expected 4'
print("correct")
assert word_count_in_set(["brown", "brown"]) == 1, 'expected 1'
print("correct")

assert topping1({"ice cream": "peanuts"}) == {"bread": "butter", "ice cream": "cherry"}, 'expected {"bread": "butter", "ice cream": "cherry"}'
print("correct")
assert topping1({"bread": "butter"}) == {"bread": "butter"}, 'expected {"bread": "butter"}'
print("correct")
assert topping1({"pancake": "syrup"}) == {"bread": "butter", "pancake": "syrup"}, '{"bread": "butter", "pancake": "syrup"}'
print("correct")

assert word_count(["a", "b", "a", "c", "b"]) == {"a": 2, "b": 2, "c": 1}, 'expected {"a": 2, "b": 2, "c": 1}'
print("correct")
assert word_count(["c", "b", "a"]) == {"a": 1, "b": 1, "c": 1}, 'expected {"a": 1, "b": 1, "c": 1}'
print("correct")
assert word_count(["c", "c", "c", "c"]) == {"c": 4}, 'expected {"a": 1, "b": 1, "c": 1}'
print("correct")

assert friend_list({"Marty": "Cynthia", "Danielle": "Marty"})== {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}, 'expected {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}'
print("correct")


# Problems found on https://codingbat.com/python
