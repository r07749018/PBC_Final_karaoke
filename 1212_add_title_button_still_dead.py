import wx.grid as gridlib
import pygame
import sys
import os
import random
import wx


class PanelOne(wx.Panel):

    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundColour(wx.Colour(251, 226, 81))
        # self.musicUrlList = []
        # self.song_cat = ''

        self.titleName = wx.StaticText(self, label="Pick One!", pos=(0, 20),
                                       size = (800, 250), style = wx.ALIGN_CENTER)
        font = wx.Font(40, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD)
        self.titleName.SetFont(font)



        # button_font = wx.Font(24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD)
        # self.CatButton1 =wx.Button(self, label="懷舊老歌", pos=(0, 100), size=(400, 300))
        # self.CatButton1.SetFont(button_font)
        # self.CatButton2 =wx.Button(self, label="聽嘻哈的小孩不會變壞", pos=(400, 100), size=(400, 300))
        # self.CatButton2.SetFont(button_font)
        # self.CatButton3 =wx.Button(self, label="小時候我都聽周杰倫", pos=(0, 400), size=(400, 300))
        # self.CatButton3.SetFont(button_font)
        # self.CatButton4 =wx.Button(self, label="KTV必點金曲", pos=(400, 400), size=(400, 300))
        # self.CatButton4.SetFont(button_font)

        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(self.CatButton1, 0, 0, 0)
        # sizer.Add(self.CatButton3, 0, 0, 0)
        # # sizer.SetSizeHints(self)
        # self.SetSizer(sizer)


        # self.StartButton = wx.Button(self, label="準備好了!", pos=(300,300), size=(150,200))
        bmp_start = wx.Bitmap("karaoke.png", wx.BITMAP_TYPE_ANY)

        self.StartButton = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp_start, pos=(325, 595), size=(150, 120))
        self.Bind(wx.EVT_BUTTON, parent.onSwitchPanels, self.StartButton)

        bmp1 = wx.Bitmap("cate1.png-1.png", wx.BITMAP_TYPE_ANY)
        bmp2 = wx.Bitmap("cate1.png-2.png", wx.BITMAP_TYPE_ANY)
        bmp3 = wx.Bitmap("cate1.png-3.png", wx.BITMAP_TYPE_ANY)
        bmp4 = wx.Bitmap("cate1.png-4.png", wx.BITMAP_TYPE_ANY)

        self.CatButton1 = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp1, pos=(0, 100),size=(400,250))
        self.CatButton2 = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp2, pos=(400, 100),size=(400, 250))
        self.CatButton3 = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp3, pos=(0, 350),size=(400, 250))
        self.CatButton4 = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp4, pos=(400, 350),size=(400, 250))

        self.Bind(wx.EVT_BUTTON, self.ClickCat1, self.CatButton1)
        self.Bind(wx.EVT_BUTTON, self.ClickCat2, self.CatButton2)
        self.Bind(wx.EVT_BUTTON, self.ClickCat3, self.CatButton3)
        self.Bind(wx.EVT_BUTTON, self.ClickCat4, self.CatButton4)

        # self.Bind(wx.EVT_BUTTON, parent.onSwitchPanels, self.CatButton1)
        # self.Bind(wx.EVT_BUTTON, parent.onSwitchPanels, self.CatButton2)
        # self.Bind(wx.EVT_BUTTON, parent.onSwitchPanels, self.CatButton3)
        # self.Bind(wx.EVT_BUTTON, parent.onSwitchPanels, self.CatButton4)


    def ClickCat(self, content):
        # PanelTwo.count = -1
        # print(PanelTwo.score)
        # musicUrlList = []
        # PanelTwo.ScoreBox1.SetLabel('得分: %s' % PanelTwo.score)
        # PanelTwo.CorrectOrNot.SetLabel('')
        music_list_reset()
        musicUrlLoader(content)
        self.titleName.SetLabel("已選擇 %s" % content)


        global song_cat
        song_cat = content + '/'
        # self.ShowInfoText.SetLabel("播放%s流行音樂" % content)

        print(song_cat)
        print("press clickcat", musicUrlList)


    def ClickCat1(self, event):
        # self.ClickCat(self.CatButton1.GetLabel())
        self.ClickCat("懷舊老歌")

    def ClickCat2(self, event):
        # self.ClickCat(self.CatButton2.GetLabel())
        self.ClickCat("聽嘻哈的小孩不會變壞")

    def ClickCat3(self, event):
        # self.ClickCat(self.CatButton3.GetLabel())
        self.ClickCat("小時候我都聽周杰倫")

    def ClickCat4(self, event):
        # self.ClickCat(self.CatButton4.GetLabel())
        self.ClickCat("KTV必點金曲")


    # def musicUrlLoader(self, cat):
    #
    #     fileList = os.listdir(file_path + cat)
    #     for filename in fileList:
    #         if filename.endswith(".mp3"):
    #             print("找到音訊檔案", filename)
    #             musicUrlList.append(filename)


class PanelTwo(wx.Panel):

    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundColour(wx.Colour(251, 226, 81))
        self.player_num = 1
        self.count = -1
        self.score_1 = 0
        self.score_2 = 0
        # self.musicUrlList =[]

        self.SongName = wx.StaticText(self, label="請在以下空白框輸入歌名", pos=(325, 100))
        self.GuessBox = wx.TextCtrl(self, pos=(300,150), size=(185, 25))
        self.ShowInfoText = wx.StaticText(self, label='播放未開始', pos=(325, 125)
                                          , size=(185, 25), style=wx.ALIGN_CENTER_VERTICAL)

        self.isPaused = False  # 是否被暫停
        self.StartPlayButton = wx.Button(self, label='開始/下一首', pos=(300, 200))
        self.Bind(wx.EVT_BUTTON, self.OnStartClicked, self.StartPlayButton)
        # self.StartPlayButton.SetBackgroundColour(wx.Colour(270, 240, 240))

        self.PauseOrContinueButton = wx.Button(self, label='停止/繼續', pos=(400, 200))
        self.Bind(wx.EVT_BUTTON, self.OnPauseOrContinueClicked, self.PauseOrContinueButton)
        self.PauseOrContinueButton.Enable(False)

        self.SubmitAnsButton = wx.Button(self, label='送出', pos=(300, 250))
        self.Bind(wx.EVT_BUTTON, self.CheckAns, self.SubmitAnsButton)

        self.RestartButton = wx.Button(self, label='換人來', pos=(400, 250))
        self.Bind(wx.EVT_BUTTON, self.RestartFunction, self.RestartButton)

        self.ChangePlaylistButton = wx.Button(self, label='回目錄', pos=(400, 300))
        self.ChangePlaylistButton.Bind(wx.EVT_BUTTON, parent.onSwitchPanels)
        # self.Bind(wx.EVT_BUTTON, parent.onSwitchPanels, self.ChangePlaylistButton)


        self.ScoreBox1 = wx.StaticText(self, label='Player 1 得分: %s' % '', pos=(100, 300)
                                      , size=(185, 25), style=wx.ALIGN_CENTER_VERTICAL)
        self.ScoreBox2 = wx.StaticText(self, label='Player 2 得分: %s' % '', pos=(600, 300)
                                      , size=(185, 25), style=wx.ALIGN_CENTER_VERTICAL)

        self.CorrectOrNot = wx.StaticText(self, label='', pos=(300, 300)
                                          , style=wx.ALIGN_CENTER_VERTICAL)

        pygame.mixer.init()

    def ResetCount(self):
        self.count = -1


    def OnStartClicked(self, event):
        self.isPaused = False
        self.PauseOrContinueButton.Enable(True)
        self.ShowInfoText.SetLabel("現在是 '%s' player %d" % (song_cat[:-1], self.player_num))


        if self.count == len(musicUrlList) - 1:
            pygame.mixer.music.stop()
            self.ShowInfoText.SetLabel("結束, 請重新選擇分類")
        else:
            self.count += 1

            self.willPlayMusic = file_path + song_cat + musicUrlList[self.count]
            # self.willPlayMusic = random.choice(musicUrlList)

            pygame.mixer.music.load(self.willPlayMusic.encode())
            pygame.mixer.music.play(1, random.randint(30, 180))
            # pygame.mixer.music.fadeout(5000)
            # time.sleep(5)
            # pygame.mixer.music.stop()

            # self.ShowInfoText.SetLabel("請猜猜歌名~~")
            # self.ShowInfoText.SetLabel("當前播放:"+self.willPlayMusic)
            self.CorrectOrNot.SetLabel('加油~~!')

    def OnPauseOrContinueClicked(self, event):
        if not self.isPaused:
            self.isPaused = True
            pygame.mixer.music.pause()
            self.PauseOrContinueButton.SetLabel('停止/繼續')
        # self.ShowInfoText.SetLabel('播放已暫停')
        else:
            self.isPaused = False
            pygame.mixer.music.unpause()
            self.PauseOrContinueButton.SetLabel('停止/繼續')

        # self.ShowInfoText.SetLabel("請猜猜歌名~~")
        # self.ShowInfoText.SetLabel("當前播放:" + self.willPlayMusic)

    def CheckAns(self, event):
        ans = self.GuessBox.GetLineText(0) + '.mp3'
        self.GuessBox.Clear()
        pygame.mixer.music.pause()

        if ans == musicUrlList[self.count]:
            if self.player_num == 1:
                self.score_1 += 1
            else:
                self.score_2 += 1
            self.CorrectOrNot.SetLabel('恭喜正確!')
        else:
            self.CorrectOrNot.SetLabel('答錯了QQ')

        self.ScoreBox1.SetLabel('Player 1 得分: %s' % self.score_1)
        self.ScoreBox2.SetLabel('Player 2 得分: %s' % self.score_2)

        if self.count == len(musicUrlList) - 1:
            pygame.mixer.music.stop()
            self.ShowInfoText.SetLabel("結束, 請重新選擇分類")
        else:
            self.count += 1

            self.willPlayMusic = file_path + song_cat + musicUrlList[self.count]
            pygame.mixer.music.load(self.willPlayMusic.encode())
            pygame.mixer.music.play(1, random.randint(30, 180))
        # pygame.mixer.music.fadeout(5000)
        # time.sleep(5)
        # pygame.mixer.music.stop()

    def RestartFunction(self, event):
        # self.count = -1
        # self.score = 0
        self.GuessBox.Clear()
        pygame.mixer.music.pause()
        self.ScoreBox1.SetLabel('Player 1 得分: %s' % self.score_1)
        self.ScoreBox2.SetLabel('Player 2 得分: %s' % self.score_2)
        self.CorrectOrNot.SetLabel('')

        if self.player_num == 1:
            self.player_num = 2
        else:
            self.player_num = 1

        self.ShowInfoText.SetLabel("現在是 '%s' player %d" % (song_cat[:-1],self.player_num))


class MyMusicPlayer(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,"PCB KTV", size=(800,730))

        MainPanel = wx.Panel(self)
        MainPanel.SetBackgroundColour(wx.Colour(251, 226, 81))

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        self.panel_two.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    # def SwitchtoPanelOne(self, event):
    #
    #     self.SetTitle("PCB KTV")
    #     self.panel_one.Show()
    #     self.panel_two.Hide()
    #     self.Layout()
    #     pygame.mixer.music.stop()
    #
    # def SwitchtoPanelTwo(self, event):
    #
    #     self.SetTitle("PCB KTV")
    #     self.panel_one.Hide()
    #     self.panel_two.Show()
    #     self.Layout()


    def onSwitchPanels(self, event):
        if self.panel_one.IsShown():
            self.SetTitle("PCB KTV")
            self.panel_one.Hide()
            self.panel_two.Show()
        else:
            self.SetTitle("PCB KTV")
            self.panel_one.Show()
            self.panel_two.Hide()
            pygame.mixer.music.stop()
            # 底下這行還是改不成功QQ
            PanelTwo.ResetCount(panel_2)
        self.Layout()


file_path = os.getcwd() + '/'
musicUrlList = []
song_cat = ''
#載入工作目錄下的所有.mp3檔案

def music_list_reset():
    global musicUrlList
    musicUrlList = []

def musicUrlLoader(cat):
    fileList = os.listdir(file_path + cat)
    for filename in fileList:
        if filename.endswith(".mp3"):
            print("找到音訊檔案",filename)
            musicUrlList.append(filename)
    print("in musicUrlloader", musicUrlList)


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyMusicPlayer()
    panel_1 = PanelOne(frame)
    panel_2 = PanelTwo(frame)
    frame.Show()
    app.MainLoop()
