from cli import CLI

def testFunction():
    print "hello, world. testing, testing..."
    return 22

cli_test = CLI()
cli_test.addFunction("test", testFunction, 0)
result = cli_test.executeCommand("test")
print result
