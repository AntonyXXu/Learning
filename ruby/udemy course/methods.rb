# methods must be above the line it's called

def multiply(x, y)
    x * y
end

puts multiply(10, 5)

def less_than_10(num)
    if num < 10
        return true
    elsif num < 20
        return nil
    else
        return false
    end
end

puts less_than_10(9)
puts less_than_10(15)

def case_test(input) 
    case input
    when 1
        puts "1"
    when 2
        puts "10"
    when 3
        puts "100"
    else
        puts "please input between 1 and 3"
    end
end
case_test(5)