a = {'a' => 1, 'b' => 2, 'c' => 3}
p a['a']

# symbols for hashing - key is immutable
b = {a: 1, b: 2, c: 3}
p b
p b['a']
p b[:a]

p a.values
p a.keys

a.each {|key, value| p "key: #{key}, value: #{value}"}
b.each {|key, value| p "key: #{key.class}, value: #{value.class}"}

b[:e] = 5
b[:c] = "3"
p b

p b.select {|key, value| value.is_a?(String)}

b.each {|k, v| b.delete(k) if v.is_a?(String)}
p b