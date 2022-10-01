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
class Worker(QObject):
    downloader = Downloader()
    searcher = ApiSearch()
    finished = pyqtSignal() #Initialize signal To use it as thing to tell thread that worker has finished
    def __init__(self,url="",quality="",videos=[]) :
        super().__init__()
        self.url = url
        self.quality = quality
        self.videos = videos

    def download_video_mp4(self):
        self.downloader.download_video_mp4(self.url,self.quality)
        self.finished.emit()

    def download_video_mp3(self):
        self.downloader.download_video_mp3(self.url)
        self.finished.emit()

    def download_playlist_mp4(self):
        self.downloader.download_playlist_mp4(self.videos , self.quality)
        self.finished.emit()

    def download_playlist_mp3(self):
        self.downloader.download_playlist_mp3(self.videos)
        self.finished.emit()




class Window(QMainWindow,Ui_MainWindow):
    downloader = Downloader()
    searcher = ApiSearch()
    thread = QThread()
    worker = Worker()
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
            QMessageBox.about(self, "Message", f"{self.downloader.get_title(self.search_input.text())} started downloading.. ")
            self.worker.url = self.search_input.text()
            self.worker.quality = self.qualitybox.currentText()
            self.thread.started.connect(self.worker.download_video_mp4)
            
        if self.audio_btn.isChecked():
            QMessageBox.about(self, "Message", f"{self.downloader.get_title(self.search_input.text())} started downloading as Audio.. ")
            self.worker.url = self.search_input.text()
            self.thread.started.connect(self.worker.download_video_mp3)

        self.worker.finished.connect(lambda : QMessageBox.about(self, "Message", f"{self.downloader.get_title(self.search_input.text())} Has Been Finished!!")) 
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.worker.deleteLater) 
        self.worker.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater) 
        self.thread.start()

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
    thread = QThread()
    worker = Worker()
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
        self.select_all = QCheckBox(self.scrollAreaWidgetContents)
        self.select_all.setObjectName("select_all")
        self.verticalLayout.addWidget(self.select_all)
        self.select_all.setText("Select All")
        for url in self.playlist:
            self.checkbox_btns.append(QCheckBox(self.scrollAreaWidgetContents))
            self.checkbox_btns[-1].setObjectName(f"{self.downloader.get_title(url)}")
            self.verticalLayout.addWidget(self.checkbox_btns[-1])
            self.checkbox_btns[-1].setText(f"{self.downloader.get_title(url)}")

    def connectSignalsSlots(self):
        self.download_btn.clicked.connect(self.download_selected_videos)
        self.select_all.toggled.connect(self.select_all_videos)
        self.cancel_btn.clicked.connect(self.close)

    def select_all_videos(self):
        if self.select_all.isChecked():
            for checkbox in self.checkbox_btns:
                checkbox.setChecked(True)
        else:
            for checkbox in self.checkbox_btns:
                checkbox.setChecked(False)

    def download_selected_videos(self):
        os.chdir(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

        for i in range(len(self.checkbox_btns)):
            if self.checkbox_btns[i].isChecked():
                self.selected_checkbox.append(self.playlist[i])

        if self.type == 0:
            self.worker.videos = self.selected_checkbox
            self.worker.quality = self.quality
            self.thread.started.connect(self.worker.download_playlist_mp4)

        else:
            self.worker.videos = self.selected_checkbox
            self.thread.started.connect(self.worker.download_playlist_mp3)

        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.close)
        self.worker.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()








if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
