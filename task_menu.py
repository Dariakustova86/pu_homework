from abc import ABCMeta, abstractmethod

class CommandException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class ShowCommand(Command):
    def __init__(self, task_id):
        pass

    def execute(self):
        pass

class ListCommand(Command):
    def __init__(self):
        pass

    def execute(self):
        pass

class TaskCompleted(Command):
    def __init__(self):
        pass

    def execute(self):
        pass

class TaskNotCompleted(Command):
    def __init__(self):
        pass

    def execut(self):
        pass

class Menu(object):
    commands = {}
    counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.commands.items()):
            ret_val = list(self.commands.items())[self.counter]
            self.counter += 1
            return ret_val

        else:
            self.counter = 0
            raise StopIteration

    @classmethod
    def add_command(cls, name, klass):
        if not name:
            raise CommandException('Command must have a name!')

        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))

        cls.commands[name] = klass


    @classmethod
    def execute(cls, name, *args, **kwargs):
        klass = cls.commands.get(name)
        if klass is None:
            raise CommandException('Command with name "{}" not found'.format(name))
        return klass.execute(name, *args, **kwargs)


if __name__ == '__main__':
    menu = Menu()
    menu.add_command('show', ShowCommand)
    menu.add_command('list', ListCommand)
    menu.add_command('task_completed', TaskCompleted)
    #menu.execute('Completed')

    for i in menu:
        print(i)








