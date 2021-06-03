from Libraries.Database import Database
import UI
from PyQt5 import QtWidgets
import logging
from Libraries.Sound import Sound
from Libraries.Spectrogram import Spectrogram
class Main(UI.Ui_MainWindow):

    def __init__(self,MainWindow):
        super(Main,self).setupUi(MainWindow)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.Loadbtns = [self.openSong1, self.openSong2]
        self.Text = [self.Text1, self.Text2]
        self.audFiles = [None, None]    # List Containing both songs
        for i in range(2):
            self.Loadbtns[i].clicked.connect(lambda checked, i=i:self.loadFile(i))

    def loadFile(self,flag):
        self.statusBar.showMessage("Loading Song {}".format(flag+1))
        audFile,_ = QtWidgets.QFileDialog.getOpenFileName(None, "Load Song {}".format(flag+1),
                                                                   filter="*.mp3")
        self.logger.debug("Song {} Loaded".format(flag+1))

        if audFile == "":
            self.logger.debug("loading cancelled")
            self.statusBar.showMessage("Loading cancelled")
        else:
            self.logger.debug("starting extraction of data")
            audData, audRate = Sound.ReadFile(audFile)
            self.logger.debug("extraction successful")
            self.audFiles[flag] = audData
            self.Text[flag].setText(audFile.split('/')[-1])
            self.statusBar.showMessage("Loading Done")
            self.logger.debug("Loading done")

    def __extract(self):
        """
        Responsible for the following :
        - Read the slider value and mix the loaded songs if any with the selected ratio
        - Extract the spectrogram of the resulted mix and it`s features
        - hash the resulted extractions
        """
        print("Slider Value is %s" % self.ratioSlider.value())
        self.statusBar.showMessage("Finding Matches ...")
        self.logger.debug("starting searching process")

        if (self.audFiles[0] is not None) and (self.audFiles[1] is not None):
            self.logger.debug("loaded two different songs ")
            self.audMix = Sound.mix(
                self.audFiles, self.Slider.value()/100)

        else:
            self.logger.debug("loaded only one song")
            if self.audFiles[0] is not None:
                self.audMix = self.audFiles[0]
            if self.audFiles[1] is not None:
                self.audMix = self.audFiles[1]
            if self.audFiles[0] is None and self.audFiles[1] is None:
                self.showMessage("Warning", "You need to at least load one Audio File",
                                 QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Warning)

        if self.audMix is not None:
            self.logger.debug("starting Extraction")

            self.spectro = self.spectrogram(self.audMix, self.audRates[0])[-1]
            self.testHash = Spectrogram.Hash(self.spectro)

            for feature in self.extractFeatures(self.audMix, self.spectro, self.audRates[0]):
                self.featureMixHash.append(Spectrogram.Hash(feature))

            self.__compareHash()
        self.statusBar.clearMessage()

    def __compareHash(self):
        """
        Responsible for the following :

        - Reading the database's saved hashes
        - Compare the resulted hashesh with those saved in database
        - Sorting the results and sending data to Table
        """
        self.logger.debug("staring comparisons ... ")
        self.statusBar.showMessage("Loading results .. ")

        for songName, songHashes in Database.read(self.dbPath):
            self.spectroDiff = Spectrogram.getHammingDistance(
                songHashes[self.spectroHashKey], self.testHash)
            self.featureDiff = 0

            for i, feature in enumerate(songHashes[self.featureKey]):
                self.featureDiff += Spectrogram.getHammingDistance(
                    feature, Spectrogram.featureMixHash[i])

            self.avg = (self.spectroDiff + self.featureDiff)/4
            self.results.append(
                (songName, (abs(1 - Spectrogram.AdjustRange(self.avg, 0, 255, 0, 1)))*100))

        self.results.sort(key=lambda x: x[1], reverse=True)

        self.statusBar.clearMessage()

        self.__startTable()

    def __startTable(self):
        """
        Responsible for the following :

        - Setting TableWidget Parameters, Columns and Rows
        - Clearing the Results Buffer
        """
        self.label_2.show()
        self.resultsTable.setColumnCount(2)
        self.resultsTable.setRowCount(len(self.results))

        for row in range(len(self.results)):
            self.resultsTable.setItem(
                row, 0, QtWidgets.QTableWidgetItem(self.results[row][0]))
            self.resultsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(
                str(round(self.results[row][1], 2))+"%"))
            self.resultsTable.item(row, 0).setBackground(
                QtGui.QColor(57, 65, 67))
            self.resultsTable.item(row, 1).setBackground(
                QtGui.QColor(57, 65, 67))
            self.resultsTable.verticalHeader().setSectionResizeMode(
                row, QtWidgets.QHeaderView.Stretch)

        self.resultsTable.setHorizontalHeaderLabels(
            ["Found Matches", "Percentage"])

        for col in range(2):
            self.resultsTable.horizontalHeader().setSectionResizeMode(
                col, QtWidgets.QHeaderView.Stretch)
            self.resultsTable.horizontalHeaderItem(
                col).setBackground(QtGui.QColor(57, 65, 67))

        self.resultsTable.show()

        self.results.clear()

    def showMessage(self, header, message, button, icon):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(header)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(button)
        self.logger.debug("messege shown with %s %s " % (header, message))
        msg.exec_()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
