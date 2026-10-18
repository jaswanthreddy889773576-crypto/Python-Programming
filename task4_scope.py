
message = "I am a global variable"

def show_scope():
    local_message = "I am a local variable"

    print("Inside the function:")
    print(message)
    print(local_message)

show_scope()

print("\nOutside the function:")
print(message)

# local_message is not available outside the function
# print(local_message) would cause a NameError
