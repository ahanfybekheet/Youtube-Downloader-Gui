from re import U
import sys
import os
from youtube import Downloader,ApiSearch
from mainWindow import Ui_MainWindow
from playlistVideos import Ui_Dialog
from PyQt5.QtWidgets import QFileDialog
from youtube import Downloader,ApiSearch
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QCheckBox,
)

from PyQt5.QtCore import (
    QObject, QThread, pyqtSignal
)



class Window(QMainWindow,Ui_MainWindow):
    downloader = Downloader()
    searcher = ApiSearch()
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.connectSignalsSlots()


    def connectSignalsSlots(self):
        self.search_btn.clicked.connect(self.check_input)
        


    def check_input(self):
        if self.downloader.is_valid_video(self.search_input.text()):
            self.download_video()
        elif self.downloader.is_valid_playlist(self.search_input.text()):
            self.download_playlist()
        else:
            self.download_search()
            
    def download_video(self):
        os.chdir(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
        if self.video_btn.isChecked():
            QMessageBox.about(self, "Message", f"The Video started downloading.. ")
            self.downloader.download_video_mp4(self.search_input.text(),self.qualitybox.currentText())
            QMessageBox.about(self, "Message", f"Download Finished ")
        if self.audio_btn.isChecked():
            QMessageBox.about(self, "Duration", f"The Audio started downloading.. ")
            self.downloader.download_video_mp3(self.search_input.text())
            QMessageBox.about(self, "Message", f"Download Finished ")

    def download_playlist(self):
        if self.video_btn.isChecked():
            self.downloader.define_playlist(self.search_input.text())
            playlist_videos = PlaylistVideos(self.downloader.playlist,self.qualitybox.currentText(),0)
        if self.audio_btn.isChecked():
            self.downloader.define_playlist(self.search_input.text())
            playlist_videos = PlaylistVideos(self.downloader.playlist,self.qualitybox.currentText(),1)
        playlist_videos.exec()


    def download_search(self):
        if self.video_btn.isChecked():
            self.searcher.search(self.search_input.text())
            playlist_videos = PlaylistVideos(self.searcher.videos,self.qualitybox.currentText(),0)
        if self.audio_btn.isChecked():
            self.searcher.search(self.search_input.text())
            playlist_videos = PlaylistVideos(self.searcher.videos,self.qualitybox.currentText(),1)
        playlist_videos.exec()



class PlaylistVideos(QDialog,Ui_Dialog):
    downloader = Downloader()
    searcher = ApiSearch()
    def __init__(self,playlist:list,quality:str,type):
        super().__init__()
        self.setupUi(self)
        self.playlist = playlist
        self.quality = quality
        self.type = type
        self.addPlaylistVideos()
        try: self.title.setText(self.playlist.title)
        except: self.title.setText("Search Result")
        self.connectSignalsSlots()


    def addPlaylistVideos(self):
        self.checkbox_btns=[]
        self.selected_checkbox=[]
        for url in self.playlist:
            self.checkbox_btns.append(QCheckBox(self.scrollAreaWidgetContents))
            self.checkbox_btns[-1].setObjectName(f"{self.downloader.get_title(url)}")
            self.verticalLayout.addWidget(self.checkbox_btns[-1])
            self.checkbox_btns[-1].setText(f"{self.downloader.get_title(url)}")

    def connectSignalsSlots(self):
        self.download_btn.clicked.connect(self.download_selected_videos)
        self.cancel_btn.clicked.connect(self.close)
        

    def download_selected_videos(self):
        os.chdir(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
        for i in range(len(self.checkbox_btns)):
            if self.checkbox_btns[i].isChecked():
                if self.type==0:
                    self.downloader.download_video_mp4(self.playlist[i],self.quality)
                else:
                    self.downloader.download_video_mp3(self.playlist[i])







if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
