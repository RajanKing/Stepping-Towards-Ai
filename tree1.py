class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

    def pre_order_traversal(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order_traversal()

        if self.right_child:
            self.right_child.pre_order_traversal()

    def in_order_traversal(self):
        if self.left_child:
            self.left_child.in_order_traversal()

        print(self.value)

        if self.right_child:
            self.right_child.in_order_traversal()

    def post_order_traversal(self):
        if self.left_child:
            self.left_child.post_order_traversal()

        if self.right_child:
            self.right_child.post_order_traversal()

        print(self.value)

bst = BinarySearchTree(15)

bst.insert_node(10)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)

print(bst.find_node(15)) # True
print(bst.find_node(10)) # True
print(bst.find_node(8)) # True
print(bst.find_node(12)) # True
print(bst.find_node(20)) # True
print(bst.find_node(17)) # True
print(bst.find_node(25)) # True
print(bst.find_node(19)) # True

print(bst.find_node(0)) # False

print
print(bst.find_minimum_value())

print
bst.pre_order_traversal()
print
bst.in_order_traversal()
print
bst.post_order_traversal()

print
print(bst.remove_node(8, None))
print
bst.pre_order_traversal()

print
print(bst.remove_node(17, None))
print
bst.pre_order_traversal()

print
print(bst.remove_node(15, None))
print
bst.pre_order_traversal()

print
print(bst.remove_node(20, None))
print
bst.pre_order_traversal()