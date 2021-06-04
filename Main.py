import UI
import numpy
import logging
from Sound import Sound
from PyQt5 import QtWidgets
from Database import Database
from Spectrogram import Spectrogram

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
        
        self.audFiles = [None, None]    # List Containing both songs
        self.SamplingRate = [0, 0]
        self.similarityResults = []
        for i in range(2):
            self.Loadbtns[i].clicked.connect(lambda checked, i=i:self.loadFile(i))
        self.Mix.clicked.connect(self.Searching)
        self.Slider.valueChanged.connect(self.updateratio)
    
    def updateratio(self):
        self.label.setText("{s} : {n}".format(
            n=self.Slider.value(), s=(100-self.Slider.value())))

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
                self.statusBar.showMessage("Error Uploading File")
                logger.warning("Error Uploading File")
                return
                
            logger.info("extraction successful")
            self.audFiles[flag] = audData
            self.SamplingRate[flag] = audRate
            self.Loadbtns[flag].setText(audFile.split('/')[-1])
            self.statusBar.showMessage("Loading Done")
            logger.info("Loading done")
            self.Mix.setEnabled(True)
            self.mixing()
            
    def mixing(self):

        if any(type(element) != numpy.ndarray for element in self.audFiles):
            for i in range(2):
                if self.audFiles[i] is not None:
                    logger.info("loaded only one song")
                    self.audMix = self.audFiles[i]
        elif all(type(element) == numpy.ndarray for element in self.audFiles):
            logger.info("loaded 2 songs")
            logger.info("starting Mixing")
            self.Slider.setEnabled(True)
            self.label.show()
            self.audMix = Sound.mix(self.audFiles, max(self.SamplingRate), self.Slider.value()/100)

    def Searching(self):
        self.mixing()
        self.statusBar.showMessage("Finding Matches ...")
        logger.info("starting searching process")

        self.spectrogram = Spectrogram.Features(self.audMix, max(self.SamplingRate))[0]
        self.testHash = Spectrogram.Hash(self.spectrogram)

        logger.info("Mixing Done")
        self.statusBar.clearMessage()

        self.check_similarity()

    def check_similarity(self):

        logger.info("Searching similarities")
        self.statusBar.showMessage("Searching Similarities")
        for songName, songHashes in Database.read("DataBase.json"):
            spectroDiff = Spectrogram.getSimilarity(
                songHashes["spectrogram_hash"], self.testHash)
            self.similarityResults.append((songName, spectroDiff*100))

        self.similarityResults.sort(key=lambda x: x[1], reverse=True)
        # print(self.similarityResults)        
        logger.info("Searching similarities Done")
        self.statusBar.showMessage("Searching Similarities Done")
        self.createTable()

    def createTable(self):

        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Song Name", "Similarity"])
        self.tableWidget.setFont(self.font)
        logger.info("Showing Results")
        self.statusBar.showMessage("Showing Results")
        for row in range(len(self.similarityResults)):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(
                self.similarityResults[row][0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(
                str(round(self.similarityResults[row][1], 2))+"%"))
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
