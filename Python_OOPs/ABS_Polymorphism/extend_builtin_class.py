class InputText(str):
    def get_unique(self):
        return list(self.split())

    def word_count(self):
        return len(self.split())


text = InputText("This is a text")
print(text.get_unique())
print(text.word_count())
