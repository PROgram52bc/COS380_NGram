class SortedCounter:
    def add(self, word):
        raise NotImplementedError("method not implemented")
    def getCount(self, word):
        raise NotImplementedError("method not implemented")
    def getTotalCount(self):
        raise NotImplementedError("method not implemented")
    def getMax(self):
        raise NotImplementedError("method not implemented")
    def getAll(self):
        raise NotImplementedError("method not implemented")
    def __contains__(self, word):
        raise NotImplementedError("method not implemented")
    def getProbability(self, key):
        return self.getCount(key)/self.getTotalCount()

class SortedCounterDictionary(SortedCounter):
    def __init__(self):
        self.hashtable = {  }
        self.count = 0
    def __contains__(self, word):
        return word in self.hashtable
    def add(self, word):
        self.count += 1
        if word not in self.hashtable:
            self.hashtable[word] = 1
        else:
            self.hashtable[word] += 1
    def getCount(self, word):
        return self.hashtable[word]
    def getTotalCount(self):
        return self.count
    def getMax(self):
        return sorted(self.hashtable.items(), key=lambda kv:kv[1], reverse=True)
    def getAll(self):
        return self.hashtable.keys()

class SortedCounterLinkedList(SortedCounter):
    class Node:
        def __init__(self, count=None, value=None, nxt=None):
            self.count = count
            self.value = value
            self.nxt = nxt
        def swap(self, other):
            """ exchange the content of self and other """
            tmp = self.count
            self.count = other.count
            other.count = tmp
            tmp = self.value
            self.value = other.value
            other.value = tmp
        def __repr__(self):
            return "({},{})".format(self.count, self.value)
    def __init__(self):
        self.head = None
        self.tail = None
        self.hashtable = {  }
        self.count = 0
    def __contains__(self, word):
        return word in self.hashtable
    def add(self, word):
        self.count += 1
        if word not in self.hashtable:
            # Add new node, replace tail
            node = self.Node(1, word, self.tail)
            self.tail = node
            self.hashtable[word] = node
            if not self.head:
                # if self is the first element
                self.head = node # set head to self element
        else:
            # if node already exists
            node = self.hashtable[word]
            node.count += 1
            while node.nxt and node.count > node.nxt.count:
                # swap the node mapping in hash
                next_word = node.nxt.value
                self.hashtable[word] = node.nxt
                self.hashtable[next_word] = node
                # swap the content
                node.swap(node.nxt)
                node = node.nxt
    def getCount(self, word):
        return self.hashtable[word].count
    def getTotalCount(self):
        return self.count
    def getMax(self):
        return self.head.value
    def getAll(self):
        return self.hashtable.keys()

    def check_coherency(self):
        for k in self.hashtable:
            if k != self.hashtable[k].value:
                raise Exception("Incoherent key [{}] pointing to node {}".format(k, self.hashtable[k]))
    def display(self):
        node = self.tail
        while node:
            print(node, end=" => ")
            node = node.nxt
        print("NULL")

class SortedCounterHeap(SortedCounter):
    class Node:
        def __init__(self, count=None, value=None, idx=None):
            self.count = count
            self.value = value
            self.idx = idx
        def swap(self, other):
            """ exchange the content of self and other """
            tmp = self.count
            self.count = other.count
            other.count = tmp
            tmp = self.value
            self.value = other.value
            other.value = tmp
            tmp = self.idx
            self.idx = other.idx
            other.idx = tmp
        def __repr__(self):
            return "({},{})".format(self.count, self.value)
    def __init__(self):
        self.heap = [None]
        self.hashtable = {  }
        self.count = 0
    def add(self, word):
        if word not in self.hashtable:
            node = self.Node(1, word, len(self.heap)+1)
            self.heap.append(node)
            self.hashtable[word] = node
        else:
            # if word already in
            node = self.hashtable[word]
            node.count += 1
            while True:
                if node.idx == 1:
                    break
                parent = self.heap[node.idx//2]
                if node.count <= parent.count:
                    break
                # if has parent and violates the heap structure
                # then swap the node mapping in hash
                parent_word = parent.value
                self.hashtable[word] = parent
                self.hashtable[parent_word] = node
                # swap the content
                node.swap(parent)
                node = parent
            
    def getCount(self, word):
        return self.hashtable[word].count
    def getTotalCount(self):
        return self.count
    def getMax(self):
        return self.heap[1].value
    def getAll(self):
        return self.hashtable.keys()
    def __contains__(self, word):
        return word in self.hashtable


sc = SortedCounterLinkedList()
sc.add("a")
sc.add("a")
sc.add("a")

sc.add("b")
sc.add("b")
sc.add("b")
