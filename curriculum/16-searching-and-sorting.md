# 16 — Searching and sorting

Linear search is O(n); binary search is O(log n) and requires sorted data. Insertion sort is O(n²), useful for small/nearly sorted data; merge sort is O(n log n), stable, and uses extra memory; quicksort is average O(n log n), worst O(n²); heapsort is O(n log n), in-place, not stable. Prefer standard library sorting in production.
