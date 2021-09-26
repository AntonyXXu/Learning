# string interpolation can't be done on single quotes
a = "fname"
b = "lname"
puts a + " " + b

puts "interpolation #{a} t#{b}"

puts a.class
puts 20.0.class
puts 10.class

puts a.sub('name', "lalala")

# inputs

first_name = gets.chomp
puts first_name