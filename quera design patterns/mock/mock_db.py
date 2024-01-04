
class MockDatabase:
    class FakeResult:
        def __init__(self, user, email) -> None:
            self.user = user
            self.email = email

        def fetchone(self):
            if self.user:
                return (self.email,)
            return None

    def __init__(self):
        self.user = None
        self.email = None

    def execute(self, query: str, params):
        if query.upper().startswith('INSERT'):
            self.user = params[0]
            self.email = params[1]
        elif query.upper().startswith('SELECT'):
            return self.FakeResult(self.user, self.email)
        elif query.upper().startswith('UPDATE'):
            if self.user == params[1]:
                self.email = params[0]
        elif query.upper().startswith('DELETE'):
            if self.user == params[0]:
                self.user = None
                self.email = None
