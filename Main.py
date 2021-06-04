import UI
import logging
from PyQt5 import QtWidgets ,QtGui
from Sound import Sound
from Database import Database
from Spectrogram import Spectrogram
import numpy
# Create and configure logger
logging.basicConfig(filename="app.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
logger.setLevel(20)
class Main(UI.Ui_MainWindow):

    def __init__(self,MainWindow):
        super(Main,self).setupUi(MainWindow)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        self.Loadbtns = [self.openSong1, self.openSong2]
        self.Text = [self.Text1, self.Text2]
        self.audFiles = [None, None]    # List Containing both songs
        self.SamplingRate = [0, 0]
        self.similarityResults = []
        for i in range(2):
            self.Loadbtns[i].clicked.connect(lambda checked, i=i:self.loadFile(i))
        self.Mix.clicked.connect(self.Searching)

    def loadFile(self,flag):
        self.statusBar.showMessage("Loading Song {}".format(flag+1))
        audFile,_ = QtWidgets.QFileDialog.getOpenFileName(None, "Load Song {}".format(flag+1),
                                                                   filter="*.mp3")
        logger.info("Song {} Loaded".format(flag+1))

        if audFile == "":
            logger.info("loading cancelled")
            self.statusBar.showMessage("Loading cancelled")
        else:
            logger.info("starting extraction of data")
            try:
               audData , audRate = Sound.ReadFile(audFile)
               
            except:
                self.showWarring("Warning", "Error Uploading File")
                self.statusBar.showMessage("Error Uploading File")
                logger.warning("Error Uploading File")
                return
                
            logger.info("extraction successful")
            self.audFiles[flag] = audData
            self.SamplingRate[flag] = audRate
            self.Text[flag].setText(audFile.split('/')[-1])
            self.statusBar.showMessage("Loading Done")
            logger.info("Loading done")


    def Searching(self):

        self.statusBar.showMessage("Finding Matches ...")
        logger.info("starting searching process")
        if any(type(element) != numpy.ndarray for element in self.audFiles):
            for i in range(2): 
                if self.audFiles[i] is not None:
                    logger.info("loaded only one song")
                    self.audMix = self.audFiles[i]    

        elif all(type(element) == numpy.ndarray for element in self.audFiles):
            logger.info("loaded 2 songs")
            self.audMix = Sound.mix(self.audFiles, max(self.SamplingRate), self.Slider.value()/100)

        logger.info("starting Mixing")

        self.spectrogram = Spectrogram.Features(self.audMix, max(self.SamplingRate))[0]
        self.testHash = Spectrogram.Hash(self.spectrogram)
        print(self.testHash)
        logger.info("Mixing Done")
        self.statusBar.clearMessage()
        # for i in self.database:
        #     print(self.database[i]['spectrogram_hash'])
        self.check_similarity()


    def check_similarity(self):
        logger.info("Searching similarities")
        self.statusBar.showMessage("Searching Similarities")
        for songName, songHashes in Database.read("db.json"):

            spectroDiff = Spectrogram.getSimilarity(
                songHashes["spectrogram_Hash"], self.testHash)
            self.similarityResults.append((songName, spectroDiff*100))

        self.similarityResults.sort(key=lambda x: x[1], reverse=True)
        logger.info("Searching and getting similarities Done")
        self.statusBar.showMessage("Getting Similarities Done")
        print(self.similarityResults)
        # self.similarityResults.sort(key=lambda x: x[1], reverse=True)
        # logger.info("Searching similarities Done")
        # self.statusBar.showMessage("Searching Similarities Done")
        # self.fill_table()

    def fill_table(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Found Matches", "Percentage"])

        logger.info("Showing Results")
        self.statusBar.showMessage("Showing Results")
        for row in range(len(self.similarityResults)):
            self.tableWidget.insertRow(row)

            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(
                self.similarityResults[row][0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(
                str(round(self.similarityResults[row][1], 2))+"%"))

        for col in range(2):
            self.tableWidget.horizontalHeader().setSectionResizeMode(
                col, QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeaderItem(
                col).setBackground(QtGui.QColor(57, 65, 67))
        self.similarityResults.clear()

        logger.info("Results Done")
        self.statusBar.showMessage("Results Done")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
