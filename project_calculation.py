import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (
    QDialog, QApplication, QMainWindow, QMessageBox, QLineEdit, QLabel, QTableWidget, QTableWidgetItem
)

from main_window import Ui_MainWindow
from add_participants import Ui_Dialog
from dialog_command_result import Ui_Dialog_command_result

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.add_button_actions()
        self.tableWidget_participants.setColumnCount(6)
        # self.tableWidget_participants.insertRow(0)
        self.all_participants = []

        #make tableWidget Read-only
        self.tableWidget_participants.setEditTriggers(QTableWidget.NoEditTriggers)


    def add_button_actions(self) -> None:
        self.pushButton_add_participant.clicked.connect(self.add_participant)
        self.pushButton_calculate.clicked.connect(self.calculate_score)
        self.pushButton_delete.clicked.connect(self.delete_participant)
        self.pushButton_show.clicked.connect(self.show_individual_rating)

    def show_individual_rating(self) -> None:
        show_dialog = dialog_command_result()

        row = show_dialog.tableWidget_comand_result.rowCount()
        show_dialog.tableWidget_comand_result.insertRow(row)
       

        for i in range(len(self.all_participants)):
            show_dialog.tableWidget_comand_result.setItem(i, 0, QTableWidgetItem(str(self.all_participants[i]['num'])))
            show_dialog.tableWidget_comand_result.setItem(i, 1, QTableWidgetItem(str(self.all_participants[i]['name'])))
            show_dialog.tableWidget_comand_result.setItem(i, 2, QTableWidgetItem(str(self.all_participants[i]['team'])))
            show_dialog.tableWidget_comand_result.setItem(i, 3, QTableWidgetItem(str(self.all_participants[i]['zone'])))
            show_dialog.tableWidget_comand_result.setItem(i, 4, QTableWidgetItem(str(self.all_participants[i]['sector'])))
            show_dialog.tableWidget_comand_result.setItem(i, 5, QTableWidgetItem(str(self.all_participants[i]['weight'])))
            show_dialog.tableWidget_comand_result.setItem(i, 6, QTableWidgetItem(str(self.all_participants[i]['individual score'])))
            row = show_dialog.tableWidget_comand_result.rowCount()
            show_dialog.tableWidget_comand_result.insertRow(row)
            print('done')
        show_dialog.exec()


    #def show_command

    def calculate_score(self) -> None:
        zone=[]
        previous = 'nothing'
        size = len(self.all_participants)
        
        #get unique names of zone
        for i in range(size):
            if previous != self.all_participants[i]['zone']:
                previous = self.all_participants[i]['zone']
                zone.append(self.all_participants[i]['zone'])
        
        participants_by_zone = []
        temp = []
        
        #create list of participants for every zone
        for z in zone:
            temp = []
            for i in range(size):
                if self.all_participants[i]['zone'] == z:
                    temp.append(self.all_participants[i])
            participants_by_zone.append(temp)
            temp = sorted(temp, key=lambda k: k['weight'], reverse=True)
            score = 1
            for t in temp:
                t['command score'] = score
                score +=1

        
        all_participants_sorted = sorted(self.all_participants, key=lambda k: k['weight'])
        for i in all_participants_sorted:
            i['individual score'] = size
            size -=1
        all_participants_sorted = sorted(self.all_participants, key=lambda k: k['weight'], reverse=True)
        self.all_participants = all_participants_sorted
        print(all_participants_sorted)
        
    def delete_participant(self) -> None:
        #get row to delete
        row = self.tableWidget_participants.currentRow()
        
        
        #remove row from table
        self.tableWidget_participants.removeRow(row)
       
        #delete 
        for i in range(len(self.all_participants)):
            if self.all_participants[i]['id'] == row:
                del self.all_participants[i]
                break;

    def add_participant(self) -> None:
        dialog = Dialog_add()
        dialog.exec()
        
        #self.tableWidget_participants.setRowCount(0)
        #self.tableWidget_participants.setColumnCount(6)
        
        #set ?row? on the last changed row and put empty row
        row = self.tableWidget_participants.rowCount()
        self.tableWidget_participants.insertRow(row)
        
        #create dictionary for every participant
        participant = { 'id': row,
                        'num': dialog.lineEdit_num_participant.text(),
                        'name': dialog.lineEdit_name_participant.text(),
                        'team': dialog.lineEdit_team_participant.text(),
                        'zone': dialog.lineEdit_zone_participant.text(),
                        'sector': dialog.lineEdit_sector_participant.text(),
                        'weight': int(dialog.lineEdit_weight.text())}
        
        #add dict to list of all participants
        self.all_participants.append(participant)
        #print(self.all_participants)
        
        #send information from dialog window to Table
        self.tableWidget_participants.setItem(row, 0, QTableWidgetItem(participant['num']))
        self.tableWidget_participants.setItem(row, 1, QTableWidgetItem(participant['name']))
        self.tableWidget_participants.setItem(row, 2, QTableWidgetItem(participant['team']))
        self.tableWidget_participants.setItem(row, 3, QTableWidgetItem(participant['zone']))
        self.tableWidget_participants.setItem(row, 4, QTableWidgetItem(participant['sector']))
        self.tableWidget_participants.setItem(row, 5, QTableWidgetItem(str(participant['weight'])))



class Dialog_add(QDialog, Ui_Dialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.add_button_actions()

    def add_button_actions(self) -> None:
        self.pushButton_save.clicked.connect(self.close)


class dialog_command_result(QDialog, Ui_Dialog_command_result):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.tableWidget_comand_result.setColumnCount(7)
        #self.tableWidget_comand_result.insertRow(0)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())