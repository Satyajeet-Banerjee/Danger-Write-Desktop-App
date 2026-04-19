class MainController:
    def __init__(self, model, view, timer_service):
        self.model = model
        self.view = view
        self.timer = timer_service

        self.view.editor.textChanged.connect(self.on_text_change)

    def on_text_change(self):
        self.timer.reset()

    def clear_text(self):
        self.view.editor.clear()
        self.view.label.setText("💀 You stopped writing — everything erased!")