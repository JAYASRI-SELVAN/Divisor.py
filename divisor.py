# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def count_divisibles(arr,divisor):
    count=0
    for x in arr:
        if x%divisor==0:
            count+=1
    return count
arr=[10,45,20,67,11,42]
divisor=2
count= count_divisibles(arr,divisor)
print(f"Number of elements divisible by {divisor}:{count}")
    

