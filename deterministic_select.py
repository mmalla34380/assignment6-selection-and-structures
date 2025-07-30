def deterministic_select(arr, k):
    def select(lst, k):
        if len(lst) <= 5:
            return sorted(lst)[k]
        chunks = [lst[i:i + 5] for i in range(0, len(lst), 5)]
        medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]
        pivot = select(medians, len(medians) // 2)
        lows = [el for el in lst if el < pivot]
        highs = [el for el in lst if el > pivot]
        pivots = [el for el in lst if el == pivot]
        if k < len(lows):
            return select(lows, k)
        elif k < len(lows) + len(pivots):
            return pivot
        else:
            return select(highs, k - len(lows) - len(pivots))
    return select(arr, k)
