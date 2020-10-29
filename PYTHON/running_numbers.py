def longest_run(num_list):
    longest = 0
    count = 0
    for i in range(len(num_list)-1):

        if not(num_list[i] == num_list[i+1]):
            count = 0
        else:
            count = count + 1
            if count > longest:
                longest = count
    return longest


def Total_run(num_list):
    longest = 0
    for i in range(len(num_list)-1):

        if num_list[i] == num_list[i+1]:
            longest = longest + 1
    return longest
