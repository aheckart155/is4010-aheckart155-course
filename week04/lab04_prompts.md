## Problem 1: Finding Common Items

Prompt:
I have two very large lists of product IDs. I need to find items present in both lists efficiently. The order doesn't currently matter. Which data structure should I use and why?

AI Recommendation:
Use a hash set (a set).

Reasoning:
Membership checks in a set are O(1) average time (hash lookup), so it scales well for “very large lists.”
    The intersection is then fast:
        Build a set from one list: S = set(listA) → O(n)
        Scan the other list and keep matches: [x for x in listB if x in S] → O(m)
        Total: O(n + m) average, which is about as good as it gets in practice.

## Problem 2: User Profile Lookup

Prompt:
I have a list of user dictionaries. I need to look up users by their unique username very frequently. Performance is critical. How should I structure this data for the fastest lookups?

AI Recommendation:
Turn the list into a hash table keyed by username

Reasoning:
Hash table lookups are O(1) average time, vs scanning a list which is O(n) per lookup.
Since you’re doing this very frequently and performance matters, you want constant-time membership/lookup.

## Problem 3: Listing Even Numbers

Prompt:
I have a list of integers. I need a new list with only the even numbers, keeping the original order. What is the most Pythonic way to do this?

AI Recommendation:
Use a list comprehension

Reasoning:
Readable: enough detail to explain the idea without feeling heavy
Memorable: people naturally remember things in 3s (it’s a classic communication rule)
Scannable: quick to skim, especially for technical answers