puts "new line"
print "Hello world"
print "same line"
puts
# vars
testVar = "abc"

# data types
stringVar = "test"
numberVar = 123
decimalVar = 12.3
boolVar = true
nullType = nil

stringVar.upcase()
stringVar.downcase()
stringVar.length()
stringVar.strip()
puts stringVar.include? "t"
puts stringVar[0, 2]
puts stringVar.index('s')
stringVar.index('s   ')

# data structures
arr = Array.new
arr2 = Array["test"]
arr.reverse()
arr.include? "test"
puts arr
puts arr2