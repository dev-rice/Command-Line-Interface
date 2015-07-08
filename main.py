from function_holder import FunctionHolder
from cli import CLI

def testFunction():
    print("hello, world. testing, testing...")
    return 22

function_holder = FunctionHolder()
# Add a simple function to the function_holder
function_holder.addFunction("test", testFunction, 0)

cli = CLI(function_holder)
cli.run()
