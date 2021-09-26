users = [
    { username: "mashrur", password: "password1" },
    { username: "jack", password: "password2" },
    { username: "arya", password: "password3" },
    { username: "jonshow", password: "password4" },
    { username: "heisenberg", password: "password5" }
  ]

MAX_ATTEMPTS = 5

def authenticate(username, password, users)
    users.each do |user|
        if username == user[:username] && password == user[:password]
            return user
        end
    end
    return nil
end

def main(users) 
    puts "Authenticator:"
    25.times {print '-' }
    puts
    attempts = 0
    while attempts < MAX_ATTEMPTS
        puts "input your username"
        username = gets.chomp
        puts "input your password"
        password = gets.chomp
        user = authenticate(username, password, users)
        if user != nil
            p user[:username]
            return user
        end
        attempts += 1
    end
    puts "you have reached the maximum authentification"
end

main(users)