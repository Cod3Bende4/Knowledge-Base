def modified(func):
    def modified_func():
        func()
        print("Yeah !")
        
    return modified_func

@modified
def print_test():
    print("Oh",end=" ")

print_test()

# Prints "Oh Yeah !"