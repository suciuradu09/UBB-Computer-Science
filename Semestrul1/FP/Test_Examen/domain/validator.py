
class EventValidator:
    def validate(self, event):
        errors = []
        if event.getName() == '':
            errors.append("Evenimentul nu poate avea nume nul.")
        if event.getDate() == '':
            errors.append("Data nu poate fi nula.")
        if event.getDescription() == '':
            errors.append("Evenimentul nu poate avea descrierea nula.")
        if len(errors) > 0:
            errors_string = '\n'.join()
            raise errors_string