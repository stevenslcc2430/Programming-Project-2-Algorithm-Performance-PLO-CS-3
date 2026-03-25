"""
Team #5

Team Members
- Steven Benjamin
- Alex Gonzalez
- Carlos Recinos

CS-2430-502
Project 2: Algorithm Performance
"""

import itertools


def generate_permutations(n):
    """Generate all n! permutations of [1, 2, ..., n].
    Returns a list of lists where each inner list is one permutation."""
    #build the base list [1, 2, ..., n]
    base = list(range(1, n + 1))
    #itertools.permutations gives tuples so convert each to a list
    perms = [list(p) for p in itertools.permutations(base)]
    return perms


# Example usage
if __name__ == "__main__":
    #verify n=3 produces exactly 6 permutations
    result = generate_permutations(3)
    print("n=3 permutations (" + str(len(result)) + " total):")
    for perm in result:
        print("  ", perm)

    #show counts for n=4, 6, 8
    for n in [4, 6, 8]:
        count = len(generate_permutations(n))
        print("n=" + str(n) + " -> " + str(count) + " permutations")
