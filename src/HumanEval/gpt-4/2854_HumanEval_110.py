
def exchange(lst1, lst2):
    # Count the number of odd numbers in lst1
    odd_count_lst1 = sum(1 for num in lst1 if num % 2 != 0)
    # Count the number of even numbers in lst2
    even_count_lst2 = sum(1 for num in lst2 if num % 2 == 0)
    # If the number of odd numbers in lst1 is less than or equal to the number of even numbers in lst2
    # then it is possible to exchange elements to make lst1 a list of only even numbers
    if odd_count_lst1 <= even_count_lst2:
        return "YES"
    else:
        return "NO"
