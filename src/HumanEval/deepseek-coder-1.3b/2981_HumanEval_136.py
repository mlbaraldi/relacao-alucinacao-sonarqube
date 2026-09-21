
def largest_smallest_integers(lst):
    neg_nums = [i for i in lst if i < 0]
    pos_nums = [i for i in lst if i > 0]
    return (max(neg_nums) if neg_nums else None, min(pos_nums) if pos_nums else None)
