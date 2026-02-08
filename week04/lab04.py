def find_common_elements(list1, list2):
    """Find the common elements between two lists.

    This function takes two lists and returns a new list containing
    only the elements that are present in both input lists.
    """
    set1 = set(list1)
    set2 = set(list2)
    
    return list(set1 & set2)


def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.

    Parameters
    ----------
    users : list of dict
        A list of dictionaries, where each dictionary represents a user.
    name : str
        The name of the user to find.
    """
    user_lookup = {user['name']: user for user in users}
    
    return user_lookup.get(name)


def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    The order of the numbers in the output list must be the same as the
    order of the even numbers in the input list.
    """
    return [x for x in numbers if x % 2 == 0]