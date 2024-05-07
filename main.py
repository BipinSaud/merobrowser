import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Mero Browser")
        self.setWindowIcon(QIcon(".venv/icons/Bicon.png"))

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction(QIcon(".venv/icons/back.png"), 'Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon(".venv/icons/forward.png"), 'Forward',
                              self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon(".venv/icons/reload.png"), 'Reload',
                             self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon(".venv/icons/Home.png"), 'Home', self) 
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Adjusting spacing for icons
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        navbar.addWidget(spacer)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Adjusting spacing for URL bar
        url_spacer = QWidget()
        url_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        navbar.addWidget(url_spacer)

        self.browser.urlChanged.connect(self.update_url)

        # Apply stylesheet to navbar and url_bar
        navbar.setStyleSheet("""
            QToolBar {
                background-color: #37474f;
                border: none;
            }

            QLineEdit {
                background-color: #455a64;
                border: 1px solid #37474f;
                border-radius: 3px;
                padding: 5px;
                color: white;
            }

            /* Adjust icon size */
            QToolButton {
                width: 30px;
                height: 30px;
            }

            /* Adjust spacing between icons and URL bar */
            QToolBar::icon {
                margin-right: 10px;
            }
        """)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.merodestiny.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def closeEvent(self, event):
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
