from function_holder import FunctionHolder

def testFunction():
    print("hello, world. testing, testing...")
    return 22

function_holder_test = FunctionHolder()

# Add a simple function to the function_holder
function_holder_test.addFunction("test", testFunction, 0)
while not function_holder_test.isEnabled():
    # Take the users input as a command and send it to the FunctionHolder instance
    users_input = input('>? ')
    result = function_holder_test.executeCommand(users_input)

    # If something was returned, print it
    if result:
        print(result)
