class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class Bst:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value=value)
            return

        current = self.root
        parent = None
        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return  # ignore duplicates

        new_node = Node(value=value, parent=parent)
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

    def find(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return None


def main():
    tree = Bst()
    cmd = input("P: ")
    while cmd != 'q':
        if cmd == 'i':
            value = int(input("val: "))
            tree.insert(value)
        elif cmd == 'f':
            value = int(input("val: "))
            node = tree.find(value)
            print("found" if node else "not found")
        cmd = input("P: ")


if __name__ == "__main__":
    main()
