require 'bcrypt'

users = [
    { username: "mashrur", password: "password1" },
    { username: "jack", password: "password2" },
    { username: "arya", password: "password3" },
    { username: "jonshow", password: "password4" },
    { username: "heisenberg", password: "password5" }
  ]

def create_hash(password)
    BCrypt::Password.create(password)  
end


def verify_hash(password)
    BCrypt::Password.new(password)
end

def create_secure_users(list_of_users)
    list_of_users.each do |user|
        user[:password] = create_hash(user[:password])
    end
    return list_of_users
end

puts create_secure_users(users)