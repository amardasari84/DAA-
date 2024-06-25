def ssort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
num_str=(input("Enter the comma separated integers:"))
user_list=[int(num) for num in num_str.split(",")]
result=ssort(user_list)
print(result)