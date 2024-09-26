import time
import requests

# Inefficient sorting algorithm (Bubble Sort)
def inefficient_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Hardcoded credentials (bad security practice)
def connect_to_service():
    username = "admin"
    password = "password123"
    try:
        # Insecure HTTP request (no HTTPS)
        response = requests.get(f'http://example.com/api?user={username}&pass={password}')
        if response.status_code == 200:
            print("Connection Successful")
        else:
            print("Connection Failed")
    except Exception as e:
        print("Something went wrong, but I won't tell you much.")
        # Poor exception handling, no details on error

# Inefficient and unnecessary usage of loops
def inefficient_loop_operation():
    result = []
    for i in range(10000):
        for j in range(10000):
            if i == j:
                result.append(i)

if __name__ == "__main__":
    # Testing inefficient sorting
    arr = [64, 34, 25, 12, 22, 11, 90]
    inefficient_sort(arr)
    print(f'Sorted array: {arr}')

    # Testing bad security practice
    connect_to_service()

    # Testing inefficient loop operation
    start_time = time.time()
    inefficient_loop_operation()
    end_time = time.time()
    print(f"Inefficient loop took {end_time - start_time} seconds to complete")
