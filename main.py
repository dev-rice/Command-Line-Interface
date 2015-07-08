from cli import CLI

def testFunction():
    print("hello, world. testing, testing...")
    return 22

cli_test = CLI()

# Add a simple function to the cli
cli_test.addFunction("test", testFunction, 0)
while not cli_test.isEnabled():
    # Take the users input as a command and send it to the cli instance
    users_input = input('>? ')
    result = cli_test.executeCommand(users_input)

    # If something was returned, print it
    if result:
        print(result)
