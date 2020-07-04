'''
You're given an array of integers where each integer represents a jump of its value in the array. For instance, the integer 2 represents a jump of two indices forward in the array; the integer -3 represents a jump of three indices backward in the array.

If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at the last index in the array brings us to index 0.

Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle occurs if, starting at any index in the array and following the jumps, every element in the array is visited exactly once before landing back on the starting index.

Sample Input
array = [2, 3, 1, -4, -4, 2]
Sample Output
true
'''

def has_single_cycle(input_list):
	n_visited_elements = 0
	current_idx = 0
	while n_visited_elements < len(input_list):
		if n_visited_elements > 0 and current_idx == 0:
			return False
		n_visited_elements += 1
		current_idx = find_new_current_idx(input_list, current_idx)
	return current_idx == 0


def find_new_current_idx(input_list, current_idx):
	jump = input_list[current_idx]
	next_idx = (current_idx + jump) % len(input_list)
	return next_idx if next_idx >= 0 else next_idx + len(input_list)

my_list = [2, 3, 1, -4, -4, 2]
print(has_single_cycle(my_list))


'''
Time: O(n)
Space: O(1)
'''