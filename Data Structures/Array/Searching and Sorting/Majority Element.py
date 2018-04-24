
def majority_element_2loops(arr):
    maj_element = None
    for i in range(len(arr)):
        count = 1
        for j in range(len(arr)):
            if i != j:
                if arr[j] == arr[i]:
                    count += 1
        if count > len(arr)/2:
            maj_element = (arr[i])
    if maj_element == None:
        print("No majority element!")
    else:
        print(maj_element)

#Using Moore's Voting Algorithm
def majority_element(arr):
    majority_index = 0
    count = 1
    for i in range(len(arr)):
        if arr[majority_index] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority_index = i
            count = 1
    return arr[majority_index]

# Function to check if the candidate occurs more than n/2 times
def is_majority(arr, cand):
    count =0
    for i in range(len(arr)):
        if arr[i] == cand:
            count += 1
    if count > len(arr)/2:
        print('Majority element is ', cand)
    else:
        print('Majority element does not exist!')

def main():
    arr = [2,2,3,2,3]
    majority_element_2loops(arr)
    cand = majority_element(arr)
    is_majority(arr, cand)
main()
