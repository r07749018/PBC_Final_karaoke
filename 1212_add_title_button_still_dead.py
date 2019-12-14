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
        font = wx.Font(40, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, 'Arial')
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

        music_list_reset()
        musicUrlLoader(content)
        self.titleName.SetLabel("已選擇 %s" % content)

        global song_cat
        song_cat = content + '/'

        print(song_cat)
        print("press clickcat", musicUrlList)

    def ClickCat1(self, event):
        self.ClickCat("懷舊老歌")

    def ClickCat2(self, event):
        self.ClickCat("聽嘻哈的小孩不會變壞")

    def ClickCat3(self, event):
        self.ClickCat("小時候我都聽周杰倫")

    def ClickCat4(self, event):
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
        self.player_num = 0
        self.count = -1
        self.score_1 = 0
        self.score_2 = 0

        self.ShowInfoText = wx.StaticText(self, label='播放未開始', pos=(300, 100))

        self.isPaused = False  # 是否被暫停
        self.StartPlayButton = wx.Button(self, label='開始/下一首', pos=(300, 125))
        self.Bind(wx.EVT_BUTTON, self.OnStartClicked, self.StartPlayButton)

        self.PauseOrContinueButton = wx.Button(self, label='停止/繼續', pos=(400, 125))
        self.Bind(wx.EVT_BUTTON, self.OnPauseOrContinueClicked, self.PauseOrContinueButton)
        self.PauseOrContinueButton.Enable(False)

        self.SongName = wx.StaticText(self, label="請在以下空白框輸入歌名", pos=(300, 175))

        self.GuessBox = wx.TextCtrl(self, pos=(300,200), size=(185, 25), value='')
        self.GuessBox.Bind(wx.EVT_KEY_DOWN, parent.OnKeyDown)
        self.Bind(wx.EVT_KEY_DOWN, parent.OnKeyDown)

        self.SubmitAnsButton = wx.Button(self, label='送出', pos=(350, 250))
        self.Bind(wx.EVT_BUTTON, self.CheckAns, self.SubmitAnsButton)

        self.RestartButton = wx.Button(self, label='重來', pos=(350, 350))
        self.Bind(wx.EVT_BUTTON, self.ResetCount, self.RestartButton)

        self.ChangePlaylistButton = wx.Button(self, label='回目錄', pos=(350, 300))
        self.ChangePlaylistButton.Bind(wx.EVT_BUTTON, parent.onSwitchPanels)

        score_font = wx.Font(24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Arial')
        self.ScoreBox1 = wx.StaticText(self, label='Player 1 得分: %s' % '', pos=(50, 300)
                                      , size=(185, 25), style=wx.ALIGN_CENTER_VERTICAL)
        self.ScoreBox2 = wx.StaticText(self, label='Player 2 得分: %s' % '', pos=(525, 300)
                                      , size=(185, 25), style=wx.ALIGN_CENTER_VERTICAL)
        # self.ScoreBox1.SetForegroundColour((255, 0, 0))
        self.ScoreBox1.SetFont(score_font)
        self.ScoreBox2.SetFont(score_font)

        self.CorrectOrNot = wx.StaticText(self, label='', pos=(0, 400), size = (800, 250)
                                          , style=wx.ALIGN_CENTER)
        CON_font = wx.Font(36, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, 'Arial')
        self.CorrectOrNot.SetFont(CON_font)

        pygame.mixer.init()

    # def OnKeyDown(self, event):
    #     kc = event.GetKeyCode()
    #     # event.DoAllowNextEvent()
    #     if kc == 316:
    #         self.ChangePlayer(player=1)
    #     elif kc == 396:
    #         # self.player_num = 2
    #         self.ChangePlayer(player=2)
    #     print('key')
    #     event.Skip()

    def SetInfoText(self):
        self.ShowInfoText.SetLabel("點一下開始播放 '%s'" % (song_cat[:-1]))

    def ResetCount(self, event):
        self.count = -1
        self.score_1 = 0
        self.score_2 = 0
        self.ScoreBox1.SetLabel('Player 1 得分: %s' % self.score_1)
        self.ScoreBox2.SetLabel('Player 2 得分: %s' % self.score_2)
        self.CorrectOrNot.SetLabel('')

    def OnStartClicked(self, event):
        self.isPaused = False
        self.PauseOrContinueButton.Enable(True)
        self.ShowInfoText.SetLabel("播放 '%s'" % (song_cat[:-1]))

        if self.count == len(musicUrlList) - 1:
            self.count = 0
            # pygame.mixer.music.stop()
            # self.ShowInfoText.SetLabel("結束, 請重新選擇分類")
        else:
            self.count += 1

        self.willPlayMusic = file_path + song_cat + musicUrlList[self.count]
        # self.willPlayMusic = random.choice(musicUrlList)

        pygame.mixer.music.load(self.willPlayMusic.encode())
        pygame.mixer.music.play(1, random.randint(30, 180))
        # pygame.mixer.music.fadeout(5000)
        # time.sleep(5)

        self.CorrectOrNot.SetLabel('加油~~!')

        self.player_num = 0
        self.ScoreBox1.SetForegroundColour('black')
        self.ScoreBox2.SetForegroundColour('black')


    def OnPauseOrContinueClicked(self, event):
        if not self.isPaused:
            self.isPaused = True
            pygame.mixer.music.pause()
            self.PauseOrContinueButton.SetLabel('停止/繼續')
            self.ShowInfoText.SetLabel('播放已暫停')
        else:
            self.isPaused = False
            pygame.mixer.music.unpause()
            self.PauseOrContinueButton.SetLabel('停止/繼續')
            self.ShowInfoText.SetLabel("播放 '%s'" % (song_cat[:-1]))


    def CheckAns(self, event):
        ans = self.GuessBox.GetLineText(0) + '.mp3'
        self.GuessBox.Clear()

        if ans == musicUrlList[self.count]:
            if self.player_num == 1:
                self.score_1 += 1
                self.CorrectOrNot.SetLabel('恭喜正確!')
            elif self.player_num == 2:
                self.score_2 += 1
                self.CorrectOrNot.SetLabel('恭喜正確!')
            else:
                self.CorrectOrNot.SetLabel('沒人搶答!')

        else:
            self.CorrectOrNot.SetLabel('答錯了QQ')

        self.ScoreBox1.SetLabel('Player 1 得分: %s' % self.score_1)
        self.ScoreBox2.SetLabel('Player 2 得分: %s' % self.score_2)

        if self.count == len(musicUrlList) - 1:
            self.count = 0
            # pygame.mixer.music.stop()
            # self.ShowInfoText.SetLabel("結束, 請重新選擇分類")
        else:
            self.count += 1

        self.willPlayMusic = file_path + song_cat + musicUrlList[self.count]
        pygame.mixer.music.load(self.willPlayMusic.encode())
        pygame.mixer.music.play(1, random.randint(30, 180))
        self.isPaused = False
        self.ShowInfoText.SetLabel("播放 '%s'" % (song_cat[:-1]))

        # pygame.mixer.music.fadeout(5000)
        # time.sleep(5)

        self.player_num = 0
        self.ScoreBox1.SetForegroundColour('black')
        self.ScoreBox2.SetForegroundColour('black')

    def ChangePlayer(self, player):
        # self.count = -1
        # self.score = 0
        self.GuessBox.Clear()
        pygame.mixer.music.pause()
        self.isPaused = True
        self.ScoreBox1.SetLabel('Player 1 得分: %s' % self.score_1)
        self.ScoreBox2.SetLabel('Player 2 得分: %s' % self.score_2)
        self.CorrectOrNot.SetLabel('')

        if player == 1:
            self.player_num = 2
            self.ScoreBox2.SetForegroundColour((255, 0, 0))
            self.ScoreBox1.SetForegroundColour('black')
        else:
            self.player_num = 1
            self.ScoreBox1.SetForegroundColour((255, 0, 0))
            self.ScoreBox2.SetForegroundColour('black')

        self.ShowInfoText.SetLabel("現在是 '%s' %d" % (song_cat[:-1], self.player_num))

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

        MainPanel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Centre()
        self.Show(True)

    def onSwitchPanels(self, event):
        if self.panel_one.IsShown():
            self.SetTitle("PCB KTV")
            self.panel_one.Hide()
            self.panel_two.Show()
            PanelTwo.SetInfoText(self.panel_two)

        else:
            self.SetTitle("PCB KTV")
            self.panel_one.Show()
            self.panel_two.Hide()
            pygame.mixer.music.stop()

        self.Layout()

    def OnKeyDown(self, event):
        kc = event.GetKeyCode()
        # event.DoAllowNextEvent()

        if kc == 316:
            PanelTwo.ChangePlayer(self.panel_two, player=1)
        elif kc == 396:
            PanelTwo.ChangePlayer(self.panel_two, player=2)
            print("changed!")

        event.Skip()


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
    frame.Show()
    app.MainLoop()
