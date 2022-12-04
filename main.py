#  A fuction that calculates the number of vowels in a password.

# Note functions RETURN values not printing
# to print a funtion return_value use:
#  print(function_name("input"))

def vowel_counter(password):
    vowel="aeiouAEIOU"
    count = 0
    for i in password:
        if i in vowel:
         count+=1
    return  count
print(vowel_counter("robinTheRocks"))
