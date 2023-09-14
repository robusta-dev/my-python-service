# This code is intended to find the common elements between two lists and return them.
# However, it contains several issues that need to be addressed.

def find_common_elements(list1, list2):
    common = []  # Initialize an empty list for common elements

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                common.append(list1[i])  # Add the common element to the list

    return common


# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = find_common_elements(list1, list2)
print(f"Common elements: {result}")