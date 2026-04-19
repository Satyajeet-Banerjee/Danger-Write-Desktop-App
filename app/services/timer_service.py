from PyQt5.QtCore import QTimer

class TimerService:
    def __init__(self, timeout_ms, callback):
        self.timer = QTimer()
        self.timer.setInterval(timeout_ms)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(callback)

    def reset(self):
        self.timer.stop()
        self.timer.start()

    def stop(self):
        self.timer.stop()