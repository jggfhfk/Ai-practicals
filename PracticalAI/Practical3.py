# # 1> SELECTION SORT

# def selection_sort(arr):
#     n = len(arr)
    
#     for i in range(n):
#         # Find the index of the minimum element in the remaining unsorted array
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
                
#         # Swap the found minimum element with the first element
#         arr[i], arr[min_index] = arr[min_index], arr[i]
    
#     return arr

# # Example usage:
# arr = [64, 25, 12, 22, 11]
# sorted_arr = selection_sort(arr)
# print("Sorted array:", sorted_arr)




n = int(input("Enter the number of jobs: "))
jobs = []
for i in range(n):
    job_id = input(f"Enter the job ID for job {i+1}: ")
    deadline = int(input(f"Enter the deadline for job {i+1}: "))
    profit = int(input(f"Enter the profit for job {i+1}: "))
    jobs.append((job_id, deadline, profit))


jobs.sort(key=lambda x: x[2], reverse=True)


max_deadline = max(jobs, key=lambda x: x[1])[1]


schedule = [None] * max_deadline


for job in jobs:
    for i in range(job[1]-1, -1, -1):
        if schedule[i] is None:
            schedule[i] = job[0]
            break

print("Job schedule:")
print(", ".join(job for job in schedule if job is not None))



