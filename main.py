# def quick_sort(array):
#     sort(array, 0, len(array)-1)
#     return array
#
#
# def swap(array, a, b):
#     tmp = array[a]
#     array[a] = array[b]
#     array[b] = tmp
#
#
# def sort(array, start, end):
#     if start >= end:
#         return
#     original_end = end
#     original_start = start
#     ref_value = array[start]
#     while start < end:
#         while start < end and array[start] < ref_value:
#             start += 1
#         while start < end and array[end] > ref_value:
#             end -= 1
#         if start < end:
#             swap(array, end, start)
#             start += 1
#             end -= 1
#
#     sort(array, original_start, end)
#     sort(array, start, original_end)
#
#
# print(quick_sort([1, 2, 2, 2, 2, 1, 1, 99, 99, 5, 5, 4, 3, 2, 1, 2, 4]))


def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin, end):
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)


array = [1, 2, 2, 2, 2, 1, 1, 99, 99, 5, 5, 4, 3, 2, 1, 2, 4]
quicksort(array, 0, len(array) - 1)
print(array)
