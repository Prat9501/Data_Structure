class Node:
	def __init__(self, item):
		self.data = item
		self.left = None
		self.right = None

def distance(root, x):
	if root == None:
		return -1

	dist = -1

	if root.data == x:
		return dist + 1
	else:
		dist = distance(root.left, x)
		if dist >= 0:
			return dist + 1
		else:
			dist = distance(root.right, x)
			if dist >= 0:
				return dist + 1

	return dist

if __name__ == '__main__': 
  
    root = Node(5)  
    root.left = Node(10)  
    root.right = Node(15)  
    root.left.left = Node(20)  
    root.left.right = Node(25)  
    root.left.right.right = Node(45)  
    root.right.left = Node(30)  
    root.right.right = Node(35)  
  
    print(distance(root, 45)) 