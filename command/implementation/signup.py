from command.interface.command import *
from service.auth import *

class SignupCommand(ICommand):
    def __init__(self, request):
        self.request = request
        
    def execute(self):
        result = AuthService().signup(self.request)
        return result