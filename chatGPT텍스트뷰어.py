import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog


class TextFileViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("텍스트 파일 뷰어")
        self.setGeometry(100, 100, 800, 600)

        # 메인 위젯과 레이아웃 설정
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)

        # 텍스트 뷰어 (QTextEdit)
        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        self.layout.addWidget(self.textEdit)

        # 파일 열기 버튼
        self.openButton = QPushButton("파일 열기", self)
        self.openButton.clicked.connect(self.openFile)
        self.layout.addWidget(self.openButton)

    def openFile(self):
        # 파일 열기 대화상자
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 열기", "", "텍스트 파일 (*.txt);;모든 파일 (*)", options=options)
        if filePath:
            try:
                with open(filePath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.textEdit.setText(content)
            except Exception as e:
                self.textEdit.setText(f"파일을 열 수 없습니다: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = TextFileViewer()
    viewer.show()
    sys.exit(app.exec_())