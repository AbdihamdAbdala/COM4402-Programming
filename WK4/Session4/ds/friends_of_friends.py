friends = {
    "Alice": {"Bob", "Chen"},
    "Bob": {"Alice", "Dina"},
    "Chen": {"Alice"},
    "Dina": {"Bob"}
}

def friends_of_friends(friends, name):
    """
    Return a set of friends-of-friends for 'name'.
    friends: dict mapping names (str) to sets of friend names (str)
    name: str
    Steps:
    - Start with result = empty set
    -  For each friend f in friends[name], add all friends[f] to result
    - Remove 'name' from result (if present)
    - Remove any direct friends of 'name' from result
    If name is not in friends, return an empty set.
    Raise TypeError if 'friends' is not a dict or 'name' is not a str.
    """

    result = set()
    for friend in friends[name]:

        result.add(friend)

