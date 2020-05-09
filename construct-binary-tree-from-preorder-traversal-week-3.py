# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, arr: List[int]) -> TreeNode:
        
        def insert(root,node):

            if(root):

                if(node.val > root.val):

                    if(root.right):
                        insert(root.right,node)

                    else:
                        root.right = node


                elif(node.val < root.val):

                    if(root.left):
                        insert(root.left,node)

                    else:
                        root.left = node




        root = TreeNode(arr[0])




        for i in range(1,len(arr)):
            insert(root,TreeNode(arr[i]))



#         tree = []

#         stack = [root]

#         while(stack):

#             c = len(stack)

#             while(c > 0):

#                 p = stack.pop(0)

#                 tree.append(p.val)
#                 # print(p.val)

#                 if(p.left):
#                     stack.append(p.left)

#                 if(p.right):
#                     stack.append(p.right)


#                 c -= 1


        return(root)
