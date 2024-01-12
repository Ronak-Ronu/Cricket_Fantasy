from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
import sys
from database import insert_new_team,display_all_players_name,display_BWL_players_name,display_AR_players_name,display_WK_players_name,insert_new_stats,insert_new_match,check_player_role,get_player_value,display_BAT_players_specific_data


class MainWindow(QMainWindow):
  
     def __init__(self):

        super(MainWindow,self).__init__()
        self.BAT_count = 0
        self.WK_count = 0
        self.AR_count = 0
        self.BLW_count = 0
        self.is_player_selected = set()
        self.points_used=0
        self.default_team_name="Default_Team"
        # self.team_added_count=0

        loadUi("app.ui",self)
        self.actionnew_team.triggered.connect(self.new_team_win_func)
        self.actionsave_team.triggered.connect(self.save_team)
        self.actionevaluate_team.triggered.connect(self.eval_team)
        self.actionopen_team.triggered.connect(self.open_team)
        
        # setting  default value as 0
        self.batman_value.setText("0")
        self.allrounde_value.setText("0")
        self.bowler_value.setText("0")
        self.wicketkeeper_value.setText("0")

        self.BAT_radio_btn.toggled.connect(self.display_BAT_players_name_radio)
        self.BOW_radio_btn.toggled.connect(self.display_BWL_players_name_radio)
        self.AR_radio_btn.toggled.connect(self.display_AR_players_name_radio)
        self.WK_radio_btn.toggled.connect(self.display_WK_players_name_radio)
        self.selections_list_widget.itemClicked.connect(self.add_item_to_selected_list)
    
     def new_team_win_func(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

     def receive_name_data(self, name):
        self.Team_name_value.setText(name)
     
     def save_team(self):
        #  insert_new_team()
         players_name=self.get_team_data()
         players_value = []
         if self.Team_name_value.text()=='':
            self.default_team_name="Default_Team"
         else:
             self.default_team_name= self.Team_name_value.text()
         print("Team Name : {}".format(self.default_team_name))
         for i in range(len(players_name)): 
            players_value.append(get_player_value(players_name[i]))
         print(players_value,players_name)
         for j in range(len(players_name)):
            insert_new_team(self.default_team_name,players_name[j],players_value[j])
         self.showmessage("saved")



     def eval_team(self):
         self.showmessage("team evalutation")
     def open_team(self):
         self.showmessage("open team")

     def display_players_from_db(self,selected):
         if selected:
            list_players = display_all_players_name()
            self.selections_list_widget.addItems(list_players)
            print(list_players)
         else:
            self.selections_list_widget.clear()

     def display_BAT_players_name_radio(self,selected):
        if selected:
            stas_player = display_BAT_players_specific_data()
            stats_player_name=[i[0] for i in stas_player]
            stats_player_value_bat=[i[1] for i in stas_player]
            print(stats_player_name)
            avail_score_bat=sum(stats_player_value_bat)
            self.selections_list_widget.addItems(stats_player_name)
            print(self.selections_list_widget.count())
            print(stas_player)
            self.points_available_value.setText(str(avail_score_bat))
        else:
            self.selections_list_widget.clear()

     def display_BWL_players_name_radio(self,selected):
        if selected:
            stas_player = display_BWL_players_name()
            stats_player_name=[i[0] for i in stas_player]
            stats_player_value_bwl=[i[1] for i in stas_player]
            avail_score_bwl=sum(stats_player_value_bwl)
            print("stats player value :{}".format(sum(stats_player_value_bwl)))
            self.selections_list_widget.addItems(stats_player_name)
            print(self.selections_list_widget.count())
            print(stas_player)
            self.points_available_value.setText(str(avail_score_bwl))

        else:
            self.selections_list_widget.clear()
        

     def display_WK_players_name_radio(self,selected):
        if selected:
            stas_player = display_WK_players_name()
            stats_player_name=[i[0] for i in stas_player]
            stats_player_value_wk=[i[1] for i in stas_player]
            avail_score_wk=sum(stats_player_value_wk)
            print("stats player value :{}".format(sum(stats_player_value_wk)))

            self.selections_list_widget.addItems(stats_player_name)
            self.selections_list_widget.count()
            print(stas_player)
            self.points_available_value.setText(str(avail_score_wk))

            
        else:
            self.selections_list_widget.clear()

     def display_AR_players_name_radio(self,selected):
        if selected:
            stas_player = display_AR_players_name()
            stats_player_name=[i[0] for i in stas_player]
        
            stats_player_value_ar=[i[1] for i in stas_player]
            avail_score_ar=sum(stats_player_value_ar)

            print("stats player value :{}".format(sum(stats_player_value_ar)))
            self.selections_list_widget.addItems(stats_player_name)
            print(self.selections_list_widget.count())
            self.points_available_value.setText(str(avail_score_ar))

            print(stas_player)
        else:
            self.selections_list_widget.clear()
    
     def add_item_to_selected_list(self,item):
         print(item.text())
            
         player_role=check_player_role(item.text())
         player_value=get_player_value(item.text())
         print("value: {}".format(player_value))
         print(player_role)
         if item.text() in self.is_player_selected:
            self.showmessage("Player already selected")
            return
         self.is_player_selected.add(item.text())
         
         if player_role=="BAT" :
                self.BAT_count+=1
                if self.BAT_count>6:
                    self.showmessage("Batsmen not more than 5")
                    return
                self.batman_value.setText(str(self.BAT_count))

         if player_role=="BWL" :
             self.BLW_count+=1
             if self.BLW_count>6:
                self.showmessage("bowlers not more than 5")
                return
             self.bowler_value.setText(str(self.BLW_count))

         if player_role=="AR" :
             self.AR_count+=1
             if self.AR_count>4:
                self.showmessage("Allrounders not more than 3")
                return
             self.allrounde_value.setText(str(self.AR_count))

         if player_role=="WK":
             self.WK_count+=1
             if self.WK_count>1:
                self.showmessage("Wicketkeepers not more than 1")
                return
             self.wicketkeeper_value.setText(str(self.WK_count))

        #  if self.BAT_count>=5:
        #      self.showmessage("Batsmen not more than 5")
        #      return

        #  if self.BLW_count>=5:
        #      self.showmessage("bowlers not more than 5")
        #      return
        #  if self.AR_count>3:
        #      self.showmessage("Allrounders not more than 3")
        #      return
         
         
         total_player_count= self.BAT_count+self.WK_count+self.AR_count+self.WK_count
         
         print(total_player_count)

         if total_player_count > 12:
             self.showmessage("All players added,cant include more players")
             return
         
         self.points_used+=player_value
         self.team_added_list_widget.addItem(item.text())
         team_added_count = self.team_added_list_widget.count()
         self.points_used_value.setText(str(self.points_used))
         print("team_added_list_widget {}".format(team_added_count))



     def showmessage(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Hey Its Warning !")
        ret=Dialog.exec()

     def get_team_data(self):
         team_data = []
         for row in range(self.team_added_list_widget.count()):
            item = self.team_added_list_widget.item(row)
            team_data.append(item.text())
         return team_data




class New_Team_Add_UI(QMainWindow):
    name_data_signal = QtCore.pyqtSignal(str) 
    def __init__(self):
        super(New_Team_Add_UI,self).__init__()
        loadUi("newteam.ui",self)
        self.addteam.clicked.connect(self.add_team_data_func)
        self.Home.clicked.connect(self.Home_page)
        self.addstats_btn.clicked.connect(self.add_stats_data_func)
        self.addMatch_btn.clicked.connect(self.insert_new_match)

    def Home_page(self):
       widget.setCurrentIndex(0)

    def add_team_data_func(self):
        name=self.teamname.text()
        players=self.players.text()
        value=self.value.text()
        self.is_data_added.setText("team Added Successfully")
        print(name,players,value)
        self.name_data_signal.emit(name)
        insert_new_team(name,players,value)

    def add_stats_data_func(self):
        player=self.player_inp.text()
        matches=self.metches_inp.text()
        runs=self.runs_inp.text()
        hundreds=self.hundreds_inp.text()
        fifties=self.fifties_inp.text()
        value=self.value_inp.text()
        ctg=self.ctg_inp.text()
        self.is_data_added.setText("stats Added Successfully")
        print(player,ctg)
        insert_new_stats(player,matches,runs,hundreds,fifties,value,ctg)


    def insert_new_match(self):
        players=self.players_match_inp.text()
        scored=self.players_scored_inp.text()
        faced=self.players_faced_inp.text()
        fours= self.players_fours_inp.text()
        sixes=self.players_sixes_inp.text()
        bowled=self.players_bowled_inp.text()
        wkts=self.players_wkts_inp.text()
        given=self.players_given_inp.text()
        maiden=self.players_maiden_inp.text()
        catches=self.players_catches_inp.text()
        stumping=self.players_stumping_inp.text()
        ro=self.players_ro_inp.text()
        insert_new_match(players,scored,faced,fours,sixes,bowled,wkts,given,maiden,catches,stumping,ro)
        self.is_data_added.setText("match Added Successfully")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    MainWindow = MainWindow() 
    new_Team_Window = New_Team_Add_UI()
    # i transfer the data from add new team window to main window to display the team name 
    new_Team_Window.name_data_signal.connect(MainWindow.receive_name_data)

    widget.addWidget(MainWindow)
    widget.addWidget(new_Team_Window)

    widget.setFixedHeight(700)
    widget.setFixedWidth(900)

    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Application terminated")

