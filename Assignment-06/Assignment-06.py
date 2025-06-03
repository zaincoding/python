

class Logger:

    def __init__(self,name):

        self.name = name

        print("Logger object {} has been created.".format(self.name))

    def __del__(self):
        print("Logger object {} has been destroyed".format(self.name))


greet = Logger('LoggerZain')

del greet