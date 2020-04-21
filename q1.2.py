def filter_long_words(arr, n):
    result = []
    for i in arr:
        if(len(i) > n):
            result.append(i)
    return result

input_arr = [x for x in input().split(" ")]
# print(input_arr)
n = int(input())
print(filter_long_words(input_arr, n))