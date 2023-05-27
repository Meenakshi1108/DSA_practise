# 18.	Program to Create Expression Tree from Infix Expression

class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def expressiontree_from_infix(s):
	node_stack=[]
	operator_stack=[]
	p=[0]*(128)
	p[ord('+')]=p[ord('-')]=1
	p[ord('/')]=p[ord('*')]=2
	p[ord('^')]=3
	p[ord('(')]=0

	for i in range(len(s)):
		if(s[i]=='('):
			operator_stack.append(s[i])
		elif(s[i].isalpha()):
			a=Node(s[i])
			node_stack.append(a)
		elif(p[ord(s[i])]>0):
			while(len(operator_stack)!=0 and s[i]!='^' and operator_stack[-1]!='('  and p[ord(operator_stack[-1])>=p[ord(s[i])]]):
				ele=Node(operator_stack[-1])
				operator_stack.pop()

				t1=node_stack[-1]
				node_stack.pop()
				t2=node_stack[-1]
				node_stack.pop()

				ele.left=t2
				ele.right=t1

				node_stack.append(ele)

			operator_stack.append(s[i])

		elif(s[i]==')'):
				while(len(operator_stack)!=0 and operator_stack[-1]!='('):
					ele=Node(operator_stack[-1])
					operator_stack.pop()

					t1=node_stack[-1]
					node_stack.pop()
					t2=node_stack[-1]
					node_stack.pop()

					ele.left=t2
					ele.right=t1

					node_stack.append(ele)
				operator_stack.pop() #pop (
	root=node_stack[-1]
	return root

def postorder(root):
    if (root != None):
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = "")
 
s = "(a^b^(c/d/e-f)^(x*y-m*n))"
s = "(" + s
s += ")"
root = expressiontree_from_infix(s)
 
# Function call
postorder(root)