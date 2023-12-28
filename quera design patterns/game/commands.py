from interfaces import Command


class MoveForwardCommand(Command):
    def execute(self):
        self.character.move_forward()


class MoveBackwardCommand(Command):
    def execute(self):
        self.character.move_backward()

class MoveDownCommand(Command):
    def execute(self):
        self.character.move_down()

class JumpCommand(Command):
    def execute(self):
        self.character.jump()

