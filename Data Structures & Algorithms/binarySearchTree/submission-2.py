class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.right = None
        self.left = None

class TreeMap:
    def __init__(self):
        self.size = 0
        self.root = TreeNode(-1, -1)
    
    def insert(self, key, value):
        if self.size == 0:
            self.size += 1
            self.root = TreeNode(key, value)
        else:
            def insert(root):
                if not root:
                    self.size += 1
                    return TreeNode(key, value)
                if key > root.key:
                    root.right = insert(root.right)
                elif key < root.key:
                    root.left = insert(root.left)
                else:
                    root.val = value
                return root
            self.root = insert(self.root)
    
    def get(self, key:int)->int:
        if self.size == 0:
            return -1
        def search(root:TreeNode):
            if not root:
                return -1
            if key > root.key:
               return search(root.right)
            elif key < root.key:
                return search(root.left)
            else: return root.val
        return search(self.root)
    
    def remove(self, key:int):
        def delete(root, key):
            if not root:
                return None
            if key > root.key:
                root.right = delete(root.right, key)
            elif key < root.key:
                root.left = delete(root.left, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                else:
                    curr = root.right
                    while curr.left:
                        curr = curr.left
                    
                    root.key = curr.key
                    root.val = curr.val
                    root.right = delete(root.right, curr.key)
            return root
        self.root = delete(self.root, key)
        self.size -=1
    
    def getInorderKeys(self) -> List[int]:
        result = []
        if self.size == 0: return result
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result.append(root.key)
            inorder(root.right)
        inorder(self.root)
        return result

    def getMin(self):
        if self.size == 0:
            return -1
        return self.kthSmallestElement(1)
    
    def getMax(self):
        if self.size == 0:
            return -1
        return self.kthSmallestElement(self.size)
    
    def kthSmallestElement(self, k):
        count = 0
        queue = [self.root]
        curr = self.root

        while queue:
            while curr:
                queue.append(curr)
                curr = curr.left
            curr = queue.pop()
            count+=1
            if count == k:
                return curr.val
            curr = curr.right
    
    # def __init__(self):
    #     self.size = 0
    #     self.root = None

    # def insert(self, key: int, val: int) -> None:
    #     if self.size == 0:
    #         self.root = TreeNode(key, val)
    #     else:
    #         self.insert(self.root, key, val)
    
    # def insert(self, root, key, val):
    #     if not root:
    #         return TreeNode(key, val)
    #     if key > root.val:
    #         root.right = self.insert(root.right, key, val)
    #     elif key < root.left:
    #         root.left = self.insert(root.left, key, val)
    #     else:
    #         root.val = val
    #     self.size += 1

    # def get(self, key: int) -> int:
    #     if self.size == 0: return -1
    #     return search(self.root, key)
    
    # def search(root, key):
    #     if not root:
    #         return - 1
    #     if key > root.key:
    #         return search(root.right)
    #     elif key < root.key:
    #         return search(root.left)
    #     else:
    #         return root.val

    # def getMin(self) -> int:


    # def getMax(self) -> int:


    # def remove(self, key: int) -> None:


    # def getInorderKeys(self) -> List[int]:
    #     result = []
    #     def inorder(root):
    #         if not root:
    #             return
    #         inorder(root.left)
    #         result.append(root.key)
    #         inorder(root.right)
    #     inorder(self.root)
    #     return result
