"""
Write a function contiguous_inplace(L) that (analougosly to the previous exercise)
takes a list L as a parameter and modifies the list L such that a series of equal
contiguous values is replaced by one single entry of the value followed by the number
of occurrences of the equal contiguous values in A.

The function does not return anything. It modifies L without modyfing the id and
without using auxiliary structures like other lists or tuples.

To check that the modified list is actually the same as the one passed as a parameter,
the test will check that the id (of the two lists) match, and that list L has been modified
correctly. However, you will not see any results in the automatic tests.
"""

def contiguous_inplace(A: list):
    if len(A) != 0:
        read_index = 0
        write_index = 0 

        while read_index < len(A):
            current_letter = A[read_index]

            while write_index < len(A) and current_letter == A[write_index]:
                write_index += 1

            count = write_index - read_index

            if count > 1:
                A[read_index + 1] = count
                del A[read_index + 2: write_index]
                read_index += 1

            read_index += 1
            write_index = read_index

        return A

    return []


A = ['a','b','b','z','o','o','b','b','b','b','k']
AR = ['a', 'b', 2, 'z', 'o', 2, 'b', 4, 'k']

id_before = id(A)

contiguous_inplace(A)

print((id_before == id(A)) and (A == AR))