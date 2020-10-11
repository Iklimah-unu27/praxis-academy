#integer
a = 9
print (a)

#float
a = 1.11
print (a) 

#string
x = 'Iklimah'
y = 'Safira'
print(x + ' & ' + y)

#boolean
x = 4
y = 2
print (x == y)

#list
list_num = [1,2,45,6,7,2,90,23,435]
list_char = ['i','k','l','i','m','a']
list_num.append(11)
print(list_num)
print(list_char)
list_num.insert(0, 11)
print(list_num)
list_char.remove('a') 
print(list_char)
list_char.pop(-2)
print(list_char)
list_num.sort()
print(list_num)
list.reverse(list_num)
print(list_num)

#stack
yaudah = [1,2,3,4,5] 
yaudah.append(6) 
print(yaudah)

#graphs
graph = { "a" : ["c", "d"],
          "b" : ["d", "e"],
          "c" : ["a", "e"],
          "d" : ["a", "b"],
          "e" : ["b", "c"]
        }

def define_edges(graph):
    edges = []
    for vertices in graph:
        for neighbour in graph[vertices]:
            edges.append((vertices, neighbour))
    return edges

print(define_edges(graph))

#trees
class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left  = left
        self.right = right

    def __str__(self):
        return (str(self.info) + ', Left child: ' + str(self.left) + ', Right child: ' + str(self.right))

tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
print(tree)

#sets
coba = set('Iklimah')
lagi = set('Safira')
print(coba)
print(lagi)
print(coba - lagi)

