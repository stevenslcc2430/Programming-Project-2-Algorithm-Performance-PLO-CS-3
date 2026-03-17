import itertools
from SortResults import Sort
class purmutationGenarator:
    def __init__(self):
        #store unsorted array first
        self.arry = Sort().unsortArray
        # Sort the input to ensure the generated sequence starts from the smallest permutation
        self.sorted_items = sorted(self.arry)
        # Generate permutations
        self.perms = itertools.permutations(self.sorted_items)
        #print out values to check
        for perm in self.perms:
            print (perm)

#example usage
if __name__ == "__main__":
    gen = purmutationGenarator()