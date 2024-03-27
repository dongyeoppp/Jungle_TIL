arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = base
            last =i
    left = last
    for i in range(left,right): # 앞에서 뒤로 가며 정렬   
        if arr[i]< arr[i-1]:
            base = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = base
            last = i 
    right = last
