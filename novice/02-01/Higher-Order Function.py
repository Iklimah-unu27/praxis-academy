#Higher-Order Function

# #kodingan asli js
# const strArray = ['JavaScript', 'Python', 'PHP', 'Java', 'C'];
# function mapForEach(arr, fn) {  const newArray = [];
#   for(let i = 0; i < arr.length; i++) {
#     newArray.push(
#       fn(arr[i])
#     );
#   }  return newArray;
# }const lenArray = mapForEach(strArray, function(item) {
#   return item.length;
# });// prints [ 10, 6, 3, 4, 1 ]
# console.log(lenArray);


#kodingan python
strArray = ['JavaScript', 'Python', 'PHP', 'Java', 'C']
def mapForEach(arr, fn):
    newArray = []
    for i in range(len(arr)):
        newArray.append(fn(arr[i]))
    return newArray

lenArray = mapForEach(strArray, lambda x: len(x))
print(lenArray)