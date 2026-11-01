# Selected solutions

Exactly two true:
```python
def exactly_two_true(a, b, c):
    return int(a) + int(b) + int(c) == 2
```

First repeated:
```python
def first_repeated(values):
    seen = set()
    for value in values:
        if value in seen:
            return value
        seen.add(value)
    return None
```
Average time O(n), auxiliary space O(n).

Two Sum:
```python
def two_sum(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return None
```
