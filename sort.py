def bubble_sort(values):
    values = list(values)

    n = len(values)
    for i in range(n):
        for j in range(n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]

    return values