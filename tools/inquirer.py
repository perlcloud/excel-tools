from PyInquirer import prompt, Separator
from PyInquirer import style_from_dict, Token


class Inquire:
    """Helper class used with PyInquirer to make asking questions simpler"""

    # Question types available
    LIST = "list"
    RAWLIST = "rawlist"
    EXPAND = "expand"
    CHECKBOX = "checkbox"
    CONFIRM = "confirm"
    INPUT = "input"
    PASSWORD = "password"
    EDITOR = "editor"

    # Styles taken from the PyInquirer samples
    STYLE_1 = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })
    STYLE_2 = style_from_dict({
        Token.Separator: '#6C6C6C',
        Token.QuestionMark: '#FF9D00 bold',
        # Token.Selected: '',  # default
        Token.Selected: '#5F819D',
        Token.Pointer: '#FF9D00 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#5F819D bold',
        Token.Question: '',
    })
    STYLE_3 = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })

    questions = []

    def __init__(self, style=None):
        self.style = style

    def question(
            self,
            question_type="input",
            message=None,
            name=None,
            default=None,
            choices=None,
            validate=None,
            filter=None,
            when=None,
            page_size=None,
            eargs=None,
    ):
        question = {}
        question.update({"type": question_type}) if question_type else None
        question.update({"name": name}) if name else None
        question.update({"message": message}) if message else None
        question.update({"default": default}) if default else None
        question.update({"choices": choices}) if choices else None
        question.update({"validate": validate}) if validate else None
        question.update({"filter": filter}) if filter else None
        question.update({"when": when}) if when else None
        question.update({"pageSize": page_size}) if page_size else None
        question.update({"eargs": eargs}) if eargs else None
        self.questions.append(question)

    def ask(self):
        return prompt(self.questions, self.style)


if __name__ == "__main__":
    # Some examples
    q = Inquire()
    q.question(
        question_type=q.INPUT,
        name="bio",
        message="Please write a short bio of at least 3 lines.",
        default="Hello World",
        # validate=lambda text: len(text.split('\n')) >= 3 or 'Must be at least 3 lines.',
    )
    q.question(
        question_type=q.EXPAND,
        name="overwrite",
        message="Conflict on `file.js`: ",
        default="a",
        choices=[
            {"key": "y", "name": "Overwrite", "value": "overwrite"},
            {
                "key": "a",
                "name": "Overwrite this one and all next",
                "value": "overwrite_all",
            },
            {"key": "d", "name": "Show diff", "value": "diff"},
            Separator(),
            {"key": "x", "name": "Abort", "value": "abort"},
        ],
    )
    q.question(
        question_type=q.LIST,
        name="theme",
        message="What do you want to do?",
        choices=[
            "Order a pizza",
            "Make a reservation",
            Separator(),
            "Ask for opening hours",
            {"name": "Contact support", "disabled": "Unavailable at this time"},
            "Talk to the receptionist",
        ],
    )
    q.question(
        question_type=q.PASSWORD, name="password", message="Enter your git password",
    )
    a = q.ask()

    print(a)
