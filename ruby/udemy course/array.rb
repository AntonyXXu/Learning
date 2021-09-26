arr = [1,2,3,4,5]
puts arr
p arr

puts arr.last

x = 1..5
puts x.class
arr2 = x.to_a
arr2.reverse
p arr2
# exclamation mark changes the original data structure
arr2.reverse!
p arr2
p arr2.length
arr2 << 10
p arr2
arr2.unshift('a')
arr2.append('a')
p arr2
arr2.uniq!
p arr2

p arr2.empty?
p [].empty?

puts arr2.include?('a')

arr2.push("new_item")
p arr2
p arr2.pop
string_data = arr2.join(",")
p string_data
p string_data.split(",")

arr2.each do |var|
    print var.to_s + ' '
    end
puts
arr.each {|var| print var * 10}
puts

arr3 = (1..100).to_a.shuffle
p arr3.select {|num| num.odd?}