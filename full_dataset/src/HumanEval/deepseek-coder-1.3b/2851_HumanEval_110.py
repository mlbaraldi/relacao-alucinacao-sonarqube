
def exchange(lst1, lst2):
    # Count the number of odd numbers in lst1
    odd_count1 = sum(x % 2 != 0 for x in lst1)
    # Count the number of even numbers in lst2
    even_count2 = sum(x % 2 == 0 for x in lst2)
    # If the number of odd numbers in lst1 is greater than the number of even numbers in lst2,
    # it is impossible to make lst1 a list of only even numbers.
    if odd_count1 > even_count2:
        return "NO"
    # Otherwise, it is possible to make lst1 a list of only even numbers.
    else:
        return "YES"
