class BugValidator:

    def bug_val(self, bug):
        errors = []
        if bug.getID() == '':
            errors.append("Id-ul nu poate fi nul.")
        elif bug.getID() < 0:
            errors.append("Id-ul nu poate fi negativ.")

        if bug.getName() == '':
            errors.append("Numele nu poate fi nul")
        if not isinstance(bug.getPriority(), int):
            errors.append("Prioritatea trebuie sa fie numar intreg.")
        errors_string = '\n'.join(errors)

        if len(errors_string) > 0:
            raise errors_string
       