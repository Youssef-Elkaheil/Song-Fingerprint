import UI
from PyQt5 import QtWidgets


class Main(UI.Ui_MainWindow):

    def __init__(self,MainWindow):
        super(Main,self).setupUi(MainWindow)
        
        self.audFiles = [None, None]    # List Containing both songs
        self.audRates = [None, None]    # List contains Songs Rates which must be equal
        for i in range(2):
            self.Loadbtns[i].clicked.connect(lambda i=i:self.loadFile(i))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
