import sys
from PyQt5.QtWidgets import QApplication

from app.models.writing_model import WritingModel
from app.views.main_window import MainWindow
from app.controllers.main_controller import MainController
from app.services.timer_service import TimerService

app = QApplication(sys.argv)

model = WritingModel()
view = MainWindow()

controller = MainController(
    model,
    view,
    TimerService(5000, view.editor.clear)
)

view.show()
sys.exit(app.exec_())