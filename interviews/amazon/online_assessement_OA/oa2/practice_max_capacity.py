

def device_capacity(foreground, background, max_device_capacity):
    """
    inputs: forground : [[int]] eg. [[id, cap]]
    background : [[int]] eg [[id, cap]]

    max_device_capacity: int
    """
    max_capacity = 0
    max_ids = []

    for f_id , f_size in foreground:
        max_b_size = max_device_capacity - f_size

        # search max_b_size in background
        s = 0
        e = len(background) - 1

        while s <= e:
            mid = (s + e) // 2
            b_size = background[mid][1]
            b_id = background[mid][0]
            if b_size <= max_b_size:
                if b_size + f_size > max_capacity:
                    max_capacity = b_size + f_size
                    max_ids = [f_id, b_id]
                elif b_size + f_size == max_capacity:
                    max_ids.append([f_id, b_id])

                if b_size == max_b_size:
                    break
                elif b_size < max_b_size:
                    s = mid + 1

            elif b_size > max_b_size:
                e = mid - 1
    return max_ids

############ test case 1 ###########

# foreground = [[3, 4], [1, 2]]
# background = [[4, 1], [5, 6]]
# max_device_capacity = 8
# # return [[1,5]] b/c 2 + 6 = 8

############ test case 2 ###########
# foreground = [[1,3000],[2,5000],[3,4000],[4,10000]]
# background = [[1,2000],[2,3000],[3,4000]]
# max_device_capacity = 11000
# # return [[2, 3]]

############ test case 3 ###########
foreground = [[3, 4], [1, 2], [2, 3]]
background = [[4, 1], [5, 6], [8, 5]]
max_device_capacity = 8
# return [[1,5], [2, 8]] b/c 2 + 6 = 8


print(device_capacity(foreground, background, max_device_capacity))
