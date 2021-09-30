class Student
    @fname
    @lname
    @email
    @username
    @password

    def initialize(fname, lname, email, username, password)
        @fname = fname
        @lname = lname
        @email = email
        @username = username
        @password = password   
    end
    
    def fname=(fname)
        @fname = fname
    end

    def fname
        return @fname
    end
    
    def to_s
        "Fname: #{@fname}, Lname: #{@lname}"
    end
end

a = Student.new("antony", "xu", "a@a.ca", "a", "a")
puts a

class Student2
    attr_accessor :fname, :lname, :email
    attr_reader :username, :password
    @fname
    @lname
    @email
    @username
    @password
    
    def initialize(fname, lname, email, username, password)
        @fname = fname
        @lname = lname
        @email = email
        @username = username
        @password = password   
    end

    def to_s
        "Fname: #{@fname}, Lname: #{@lname}, username: #{@username}"
    end
end

a = Student2.new("antony", "xu", "a@a.ca", "a", "a")
puts a