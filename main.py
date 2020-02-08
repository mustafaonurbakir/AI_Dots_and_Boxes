"""
Mustafa Onur Bakır
150130059

"""

import sys

class Node():
	
	def __init__(self, parent_node, horizontal_values, vertical_values, first_player_score, second_player_score, current_player):
		self.parent_node = parent_node
		self.horizontal_values = horizontal_values.copy()
		self.vertical_values = vertical_values.copy()
		self.first_player_score = first_player_score
		self.second_player_score = second_player_score
		self.current_player = current_player


"""

class BFSAgent(Agent):

	# Constants for frequently used variables.
	LEFT = "L"
	RIGHT = "R"
	UP = "U"
	DOWN = "D"
	APPLE = "A"
	FLOOR = "F"
	WALL = "W"
	PERSON = "P"
	
	def __init__(self):
		super().__init__()

	# this function find the number of apples in the matrix
	def findNumberOfApples(self, initial_level_matrix):
		appleNumber = 0
		for row in initial_level_matrix:
			for unit in row:
				if unit == self.APPLE:
					appleNumber += 1
		return appleNumber

	# This function create a new matrix for movement of player
	def createMap(self, tempNode, direction):
		newMatrix = [aa[:] for aa in tempNode.level_matrix]
		newMatrix[tempNode.player_row][tempNode.player_col] = self.FLOOR

		if direction == self.LEFT:
			newMatrix[tempNode.player_row][tempNode.player_col - 1] = self.PERSON
		elif direction == self.RIGHT:
			newMatrix[tempNode.player_row][tempNode.player_col + 1] = self.PERSON
		elif direction == self.UP:
			newMatrix[tempNode.player_row - 1][tempNode.player_col] = self.PERSON
		elif direction == self.DOWN:
			newMatrix[tempNode.player_row + 1][tempNode.player_col] = self.PERSON
		else:
			print("direction problem. line:67")

		return newMatrix

	# This function find route with BFS algorithm.
	def solve(self, level_matrix, player_row, player_column):
		super().solve(level_matrix, player_row, player_column)
		move_sequence = []

		# initial node
		initial_level_matrix = [list(row) for row in level_matrix]
		s0 = Node(None, initial_level_matrix, player_row, player_column, 0, "X", 0)

		#number of apples
		number_of_apples = self.findNumberOfApples(initial_level_matrix)
		print("elma: " + str(number_of_apples))
		
		# list as a queue for BFS
		queue = []
		queue.append(s0)

		max_collexted_apple = 0

		expandedNodeNumber = 0
		travelNodeNumber = 0
		maxNodeInMemory = 0
		
		while queue:

			if len(queue) > maxNodeInMemory:
				maxNodeInMemory = len(queue)

			currentNode = queue.pop(0)
			travelNodeNumber += 1

			#look at left
			if currentNode.level_matrix[currentNode.player_row][currentNode.player_col - 1] == self.FLOOR:
				#if currentNode.collected_apples == max_collexted_apple and currentNode.seq[-2:] != "LR":
				if currentNode.seq[-4:] != "LDRU" and currentNode.seq[-4:] != "LURD" and currentNode.seq[-2:] != "LR":
					queue.append(Node(currentNode, self.createMap(currentNode, self.LEFT), currentNode.player_row, currentNode.player_col - 1, currentNode.depth + 1, self.LEFT, currentNode.collected_apples))
					expandedNodeNumber += 1
			elif currentNode.level_matrix[currentNode.player_row][currentNode.player_col - 1] == self.APPLE:
				# This is an apple
				if currentNode.collected_apples + 1 == number_of_apples:
					#this is a solution
					solution_node = Node(currentNode, self.createMap(currentNode, self.LEFT), currentNode.player_row, currentNode.player_col - 1, currentNode.depth + 1, self.LEFT, currentNode.collected_apples + 1)
					expandedNodeNumber += 1
					move_sequence = list(solution_node.seq)
					break
				else:
					#queue.clear()
					queue.append(Node(currentNode, self.createMap(currentNode, self.LEFT), currentNode.player_row, currentNode.player_col - 1, currentNode.depth + 1, self.LEFT, currentNode.collected_apples + 1))
					expandedNodeNumber += 1
					max_collexted_apple += 1
					
			#look at right
			if currentNode.level_matrix[currentNode.player_row][currentNode.player_col + 1] == self.FLOOR:
				#if currentNode.collected_apples == max_collexted_apple and currentNode.seq[-2:] != "RL":
				if currentNode.seq[-4:] != "RULD" and currentNode.seq[-4:] != "RDLU" and currentNode.seq[-2:] != "RL":
					queue.append(Node(currentNode, self.createMap(currentNode, self.RIGHT), currentNode.player_row, currentNode.player_col + 1, currentNode.depth + 1, self.RIGHT, currentNode.collected_apples))
					expandedNodeNumber += 1
			elif currentNode.level_matrix[currentNode.player_row][currentNode.player_col + 1] == self.APPLE:
				# This is an apple
				if currentNode.collected_apples + 1 == number_of_apples:
					#this is a solution
					solution_node = Node(currentNode, self.createMap(currentNode, self.RIGHT), currentNode.player_row, currentNode.player_col + 1, currentNode.depth + 1, self.RIGHT, currentNode.collected_apples + 1)
					expandedNodeNumber += 1
					move_sequence = list(solution_node.seq)
					break
				else:
					#queue.clear()
					queue.append(Node(currentNode, self.createMap(currentNode, self.RIGHT), currentNode.player_row, currentNode.player_col + 1, currentNode.depth + 1, self.RIGHT, currentNode.collected_apples + 1))
					expandedNodeNumber += 1
					max_collexted_apple += 1

			#look at up
			if currentNode.level_matrix[currentNode.player_row - 1][currentNode.player_col] == self.FLOOR:
				#if currentNode.collected_apples == max_collexted_apple and currentNode.seq[-2:] != "UD":
				if currentNode.seq[-4:] != "ULDR" and currentNode.seq[-4:] != "URDL" and currentNode.seq[-2:] != "UD":
					queue.append(Node(currentNode, self.createMap(currentNode, self.UP), currentNode.player_row - 1, currentNode.player_col, currentNode.depth + 1, self.UP, currentNode.collected_apples))
					expandedNodeNumber += 1
			elif currentNode.level_matrix[currentNode.player_row - 1][currentNode.player_col] == self.APPLE:
				# This is an apple
				if currentNode.collected_apples + 1 == number_of_apples:
					#this is a solution
					solution_node = Node(currentNode, self.createMap(currentNode, self.UP), currentNode.player_row - 1, currentNode.player_col, currentNode.depth + 1, self.UP, currentNode.collected_apples + 1)
					expandedNodeNumber += 1
					move_sequence = list(solution_node.seq)
					break
				else:
					#queue.clear()
					queue.append(Node(currentNode, self.createMap(currentNode, self.UP), currentNode.player_row - 1, currentNode.player_col, currentNode.depth + 1, self.UP, currentNode.collected_apples + 1))
					expandedNodeNumber += 1
					max_collexted_apple += 1

			#look at down
			if currentNode.level_matrix[currentNode.player_row + 1][currentNode.player_col] == self.FLOOR:
				#if currentNode.collected_apples == max_collexted_apple and currentNode.seq[-2:] != "DU":
				if currentNode.seq[-4:] != "DLUR" and currentNode.seq[-4:] != "DRUL" and currentNode.seq[-2:] != "DU":
					queue.append(Node(currentNode, self.createMap(currentNode, self.DOWN), currentNode.player_row + 1, currentNode.player_col, currentNode.depth + 1, self.DOWN, currentNode.collected_apples))
					expandedNodeNumber += 1
			elif currentNode.level_matrix[currentNode.player_row + 1][currentNode.player_col] == self.APPLE:
				# This is an apple
				if currentNode.collected_apples + 1 == number_of_apples:
					#this is a solution
					solution_node = Node(currentNode, self.createMap(currentNode, self.DOWN), currentNode.player_row + 1, currentNode.player_col, currentNode.depth + 1, self.DOWN, currentNode.collected_apples + 1)
					expandedNodeNumber += 1
					move_sequence = list(solution_node.seq)
					break
				else:
					#queue.clear()
					queue.append(Node(currentNode, self.createMap(currentNode, self.DOWN), currentNode.player_row + 1, currentNode.player_col, currentNode.depth + 1, self.DOWN, currentNode.collected_apples + 1))
					expandedNodeNumber += 1
					max_collexted_apple += 1

		self.expanded_node_count = expandedNodeNumber
		self.generated_node_count = travelNodeNumber
		self.maximum_node_in_memory_count = maxNodeInMemory

		return move_sequence
"""

row_number = 0
column_number = 0

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

	# scores
	scores = []

	# if there no move anymore
	if node.horizontal_values.count(0) == 0 and node.vertical_values.count(0) == 0:
		return [node.first_player_score, node.second_player_score]

	# choose horizontal values
	for i in range(len(node.horizontal_values)):
		if node.horizontal_values[i] == 0:
			new_horizontal_list = node.horizontal_values.copy()
			new_horizontal_list[i] = 1

			# check is there enclosed box
			how_many_box = check_box(new_horizontal_list, node.vertical_values)

			# create new node
			if how_many_box == 0:
				new_node = Node(node, new_horizontal_list, node.vertical_values,
								node.first_player_score, node.second_player_score,
								2 if node.current_player == 1 else 1 )
			else:
				if node.current_player == 1:
					new_node = Node(node, new_horizontal_list, node.vertical_values,
									node.first_player_score + how_many_box, node.second_player_score,
									node.current_player)
				else:
					new_node = Node(node, new_horizontal_list, node.vertical_values,
									node.first_player_score, node.second_player_score + how_many_box,
									node.current_player)


			scores.append(find_minimax(new_node))

	# choose vertical values
	for i in range(len(node.vertical_values)):
		if node.vertical_values[i] == 0:
			new_vertical_list = node.vertical_values.copy()
			new_vertical_list[i] = 1

			# check is there enclosed box
			how_many_box = check_box(node.horizontal_values, new_vertical_list) - (node.second_player_score + node.first_player_score)

			# create new node
			if how_many_box == 0:
				new_node = Node(node, node.horizontal_values, new_vertical_list,
								node.first_player_score, node.second_player_score,
								2 if node.current_player == 1 else 1 )
			else:
				if node.current_player == 1:
					new_node = Node(node, node.horizontal_values, new_vertical_list,
									node.first_player_score + how_many_box, node.second_player_score,
									node.current_player)
				else:
					new_node = Node(node, node.horizontal_values, new_vertical_list,
									node.first_player_score, node.second_player_score + how_many_box,
									node.current_player)

			scores.append(find_minimax(new_node))

	final_score = [0, 0]
	for temp_val in scores:
		if node.current_player == 1:
			if temp_val[0] > final_score[0] or ( temp_val[0] == final_score[0] and temp_val[1] < final_score[1]) or final_score == [0, 0]:
				final_score = temp_val.copy()

		else:
			if temp_val[1] > final_score[1] or (temp_val[1] == final_score[1] and  temp_val[0] < final_score[0]) or final_score == [0, 0]:
				final_score = temp_val.copy()

		# if node.current_player == 1:
		# 	if temp_val[0] == 1:
		# 		if temp_val[1] >= final_score[1] or final_score[0] == 0:
		# 			final_score = temp_val
		# 	else:
		# 		if final_score[0] == 0 or final_score[0] == 2 or temp_val[1] <= final_score[1]:
		# 			final_score = temp_val
        #
		# else:
		# 	if temp_val[0] == 2:
		# 		if temp_val[1] <= final_score[1] or final_score[0] == 0:
		# 			final_score = temp_val
		# 	else:
		# 		if (final_score[0] == 0 or final_score[0] == 1) and temp_val[1] <= final_score[1]:
		# 			final_score = temp_val

	return final_score

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

	print(row_number)
	print(column_number)
	print(initial_node.horizontal_values)
	print(initial_node.vertical_values)
	print(initial_node.first_player_score)
	print(initial_node.second_player_score)

	# calculate minimax
	a = find_minimax(initial_node)

	print ("First player score: " ,a[0])
	print ("Second player score: " ,a[1])


