# Taking input from the user
A = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Greedy search algorithm for Selection Sort
for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print("Sorted array using Greedy search algorithm for Selection Sort:")
for i in range(len(A)):
    print("%d" %A[i], end="\n")

 

# Taking input from the user
n = int(input("Enter the number of jobs: "))
jobs = []
for i in range(n):
    job_id = input(f"Enter the job ID for job {i+1}: ")
    deadline = int(input(f"Enter the deadline for job {i+1}: "))
    profit = int(input(f"Enter the profit for job {i+1}: "))
    jobs.append((job_id, deadline, profit))

# Sort jobs in decreasing order of profit
jobs.sort(key=lambda x: x[2], reverse=True)

# Find the maximum deadline
max_deadline = max(jobs, key=lambda x: x[1])[1]

# Initialize the schedule
schedule = [None] * max_deadline

# Fill the schedule
for job in jobs:
    for i in range(job[1]-1, -1, -1):
        if schedule[i] is None:
            schedule[i] = job[0]
            break

# Print the schedule
print("Job schedule:")
print(", ".join(job for job in schedule if job is not None))