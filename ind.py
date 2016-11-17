#   ind(e, L) takes in an element e and a sequence L where by "sequence" we mean either a list or a string;
#   fortunately indexing and slicing work the same for both lists and strings,
#   so your ind function should be able to handle both types of input!
#   Then, ind should return the index at which e is first found in L.
#   Counting begins at 0, as is usual with lists.
#   If e is NOT an element of L, then ind(e, L) should return an integer that is at least the length of L.
#   Remember, don't use the len function explicitly though!
#   Your recursive implementation can do this by itself.

def ind(e, L):
    #for i in range(len(L)):
     #   if e == L[i]:
      #      return i
    count = 0
    for num in L:
        count += 1

    for i in range(count):
        if e == L[i]:
            return i


    return len(L)

print ind(42, [ 55, 77, 42, 12, 42, 100 ])
print ind(42, range(0,100))
print ind('hi', [ 'hello', 42, True ])
print ind('hi', [ 'well', 'hi', 'there' ])
print ind('i', 'team')
print ind(' ', 'outer exploration')