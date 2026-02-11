users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

def calculate_average_age(users):
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users : list
        A list of user dictionaries.

    Returns
    -------
    float
        The average age of the users. Returns 0.0 if the list is empty
        or no valid ages are found.
    """
    total_age = 0
    count = 0
    
    try:
        for user in users:
            if isinstance(user.get("age"), int):
                total_age += user["age"]
                count += 1
        
        return total_age / count
        
    except ZeroDivisionError:
        print("Error: Cannot calculate average of an empty or invalid list.")
        return 0.0
    except TypeError:
        print("Error: Input must be a list of dictionaries.")
        return 0.0

def get_active_user_emails(users):
    """
    Retrieve a list of email addresses for active users.

    Parameters
    ----------
    users : list
        A list of user dictionaries.

    Returns
    -------
    list
        A list of strings containing emails of active users.
    """
    active_emails = []
    
    try:
        for user in users:
            if user.get("is_active") is True and user.get("email"):
                active_emails.append(user["email"])
        return active_emails
        
    except TypeError:
        print("Error: Input must be a list.")
        return []
    except AttributeError:
        print("Error: List must contain dictionaries.")
        return []

if __name__ == '__main__':
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")