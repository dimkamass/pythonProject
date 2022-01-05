def counter():
    count = 0

    def inner_func():
        nonlocal count
        count += 1
        return count

    return inner_func
