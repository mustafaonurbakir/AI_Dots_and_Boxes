"""
Mustafa Onur Bakır
150130059

Minimax with alpha beta
"""

import sys
import math
import datetime

# For calculate total node
number_of_node = 0

class Node():
	def __init__(self, parent_node, horizontal_values, vertical_values, first_player_score, second_player_score, current_player):
		self.parent_node = parent_node
		self.horizontal_values = horizontal_values.copy()
		self.vertical_values = vertical_values.copy()
		self.first_player_score = first_player_score
		self.second_player_score = second_player_score
		self.current_player = current_player

		global number_of_node
		number_of_node += 1


row_number = 0
column_number = 0

# This function open file and create first node
def read_file(file_name):
	# open the file
	try:
		input_file = open(file_name, "r")
	except:
		print("file doesn't open!")
		return -1
	
	# read the file
	content = input_file.read().splitlines()

	#close the file
	input_file.close()

	# check the content of the file

	global row_number
	global column_number
	try:
		row_number = int(content[0])
		column_number = int(content[1])
		
		if len(content) != (row_number) * (column_number + 1) + (column_number) * (row_number + 1) + 4:
			print("There is a problem on values")
			return -1
	except:
		print("There is problem on file!")
		return -1
	
	# parse occupied or not
	horizontal_values = []
	vertical_values = []

	for i in range(2, (column_number * (row_number + 1)) + 2):
		horizontal_values.append(int(content[i]))

	for i in range((column_number * (row_number + 1)) + 2, row_number * (column_number + 1) + (column_number * (row_number + 1)) + 2):
		vertical_values.append(int(content[i]))

	# current scores
	first_player_score = int(content[-2])
	second_player_score = int(content[-1])

	# create initial node
	initial_node = Node(None, horizontal_values, vertical_values, first_player_score, second_player_score, 1)
	
	return initial_node

def find_minimax(node):
	alpha = [-math.inf, -math.inf]
	beta = [math.inf, math.inf]
	return find_maximum(node, alpha, beta)

def find_maximum(node, alpha, beta):

	# if there no move anymore
	if node.horizontal_values.count(0) == 0 and node.vertical_values.count(0) == 0:
		return [node.first_player_score, node.second_player_score]

	max_val = [-math.inf, -math.inf]

	# choose horizontal values
	for i in range(len(node.horizontal_values)):
		if node.horizontal_values[i] == 0:
			new_horizontal_list = node.horizontal_values.copy()
			new_horizontal_list[i] = 1

			# check is there enclosed box
			how_many_box = check_box(new_horizontal_list, node.vertical_values) - (
			node.second_player_score + node.first_player_score)

			# create new node
			if how_many_box == 0:
				new_node = Node(node, new_horizontal_list, node.vertical_values,
								node.first_player_score, node.second_player_score,
								2 if node.current_player == 1 else 1)
			else:
				if node.current_player == 1:
					new_node = Node(node, new_horizontal_list, node.vertical_values,
									node.first_player_score + how_many_box, node.second_player_score,
									node.current_player)
				else:
					new_node = Node(node, new_horizontal_list, node.vertical_values,
									node.first_player_score, node.second_player_score + how_many_box,
									node.current_player)

			# if player find a box, it is gain one more turn
			if new_node.current_player == 1:
				max_val = find_maximum(new_node, alpha, beta)
			else:
				max_val = find_minimum(new_node, alpha, beta)

			# this part determine
			if max_val[0] <= alpha[0]:
				return max_val

			alpha[0] = max(max_val[0], alpha[0])


	# choose vertical values
	for i in range(len(node.vertical_values)):
		if node.vertical_values[i] == 0:
			new_vertical_list = node.vertical_values.copy()
			new_vertical_list[i] = 1

			# check is there enclosed box
			how_many_box = check_box(node.horizontal_values, new_vertical_list) - (
			node.second_player_score + node.first_player_score)

			# create new node
			if how_many_box == 0:
				new_node = Node(node, node.horizontal_values, new_vertical_list,
								node.first_player_score, node.second_player_score,
								2 if node.current_player == 1 else 1)
			else:
				if node.current_player == 1:
					new_node = Node(node, node.horizontal_values, new_vertical_list,
									node.first_player_score + how_many_box, node.second_player_score,
									node.current_player)
				else:
					new_node = Node(node, node.horizontal_values, new_vertical_list,
									node.first_player_score, node.second_player_score + how_many_box,
									node.current_player)

			# if player find a box, it is gain one more turn
			if new_node.current_player == 1:
				max_val = find_maximum(new_node, alpha, beta)
			else:
				max_val = find_minimum(new_node, alpha, beta)

			# this part determine
			if max_val[0] >= beta[0]:
				return max_val

			alpha[0] = max(max_val[0], alpha[0])

	return max_val

def find_minimum(node, alpha, beta):
	# if there no move anymore
	if node.horizontal_values.count(0) == 0 and node.vertical_values.count(0) == 0:
		return [node.first_player_score, node.second_player_score]

	min_val = [-math.inf, -math.inf]
	# choose horizontal values
	for i in range(len(node.horizontal_values)):
		if node.horizontal_values[i] == 0:
			new_horizontal_list = node.horizontal_values.copy()
			new_horizontal_list[i] = 1

			# check is there enclosed box
			how_many_box = check_box(new_horizontal_list, node.vertical_values) - (
			node.second_player_score + node.first_player_score)

			# create new node
			if how_many_box == 0:
				new_node = Node(node, new_horizontal_list, node.vertical_values,
								node.first_player_score, node.second_player_score,
								2 if node.current_player == 1 else 1)
			else:
				if node.current_player == 1:
					new_node = Node(node, new_horizontal_list, node.vertical_values,
									node.first_player_score + how_many_box, node.second_player_score,
									node.current_player)
				else:
					new_node = Node(node, new_horizontal_list, node.vertical_values,
									node.first_player_score, node.second_player_score + how_many_box,
									node.current_player)

			# if player find a box, it is gain one more turn
			if new_node.current_player == 1:
				min_val = find_maximum(new_node, alpha, beta)
			else:
				min_val = find_minimum(new_node, alpha, beta)

			# this part determine
			if min_val[0] <= alpha[1]:
				return min_val

			beta[1] = max(min_val[1], alpha[1])


	# choose vertical values
	for i in range(len(node.vertical_values)):
		if node.vertical_values[i] == 0:
			new_vertical_list = node.vertical_values.copy()
			new_vertical_list[i] = 1

			# check is there enclosed box
			how_many_box = check_box(node.horizontal_values, new_vertical_list) - (
				node.second_player_score + node.first_player_score)

			# create new node
			if how_many_box == 0:
				new_node = Node(node, node.horizontal_values, new_vertical_list,
								node.first_player_score, node.second_player_score,
								2 if node.current_player == 1 else 1)
			else:
				if node.current_player == 1:
					new_node = Node(node, node.horizontal_values, new_vertical_list,
									node.first_player_score + how_many_box, node.second_player_score,
									node.current_player)
				else:
					new_node = Node(node, node.horizontal_values, new_vertical_list,
									node.first_player_score, node.second_player_score + how_many_box,
									node.current_player)

			# if player find a box, it is gain one more turn
			if new_node.current_player == 1:
				min_val = find_maximum(new_node, alpha, beta)
			else:
				min_val = find_minimum(new_node, alpha, beta)

			# this part determine
			if min_val[0] >= alpha[1]:
				return min_val

			alpha[1] = max(min_val[1], alpha[1])

	return min_val

# this function check the number of box if exist
def check_box(horizontal_values, vertical_values):
	how_many_box = 0

	for i in range (row_number):
		for l in range (column_number):
			if horizontal_values[i + l] and horizontal_values[i + l + column_number] and vertical_values[l + (i * column_number)] and vertical_values[l + (i * column_number) + 1]:
				how_many_box += 1

	return how_many_box

if __name__ == "__main__":

	# read argument
	file_name = sys.argv[1]
	
	# check and read file
	initial_node = read_file(file_name)
	if initial_node == -1:
		sys.exit()

	# calculate minimax
	start_time = datetime.datetime.now()
	final_scores = find_minimax(initial_node)
	end_time = datetime.datetime.now()

	print ("First player score: ", final_scores[0])
	print ("Second player score: ", final_scores[1])
	print ("Number of Node: ", number_of_node)
	print ("Time: ", str((end_time - start_time).microseconds))


