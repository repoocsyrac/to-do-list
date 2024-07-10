import csv
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel

class ToDo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 300)
        
        self.tasks = self.get_tasks_from_csv()
        
        self.layout = QVBoxLayout()
        
        self.title = QLabel("To-do List")
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.remove_button = QPushButton("Remove Selected Task")
        self.task_list = QListWidget()

        for task in self.tasks:
            self.task_list.addItem(task)        
        
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.remove_button)
        
        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)
        
        self.setLayout(self.layout)
    
    def add_task(self):
        task = self.input_field.text()
        if task:
            f = open("tasks.csv", "a")
            f.write("\"" + task + "\"\n")
            f.close()
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.input_field.clear()

    def remove_task(self):
        task = self.task_list.currentItem()
        if task:
            self.tasks.remove(task.text())
            self.task_list.takeItem(self.task_list.row(task))
            self.remove_task_from_csv(task.text())

    def get_tasks_from_csv(self):
        tasks = list()

        with open('tasks.csv', 'r') as readFile:
            reader = csv.reader(readFile)

            for row in reader:
                for field in row:
                    tasks.append(field)

        return tasks
    
    def remove_task_from_csv(self, t):
        lines = list()

        with open('tasks.csv', 'r') as readFile:
            reader = csv.reader(readFile)

            for row in reader:
                lines.append(row)
                for field in row:
                    if field == t:
                        lines.remove(row)

        with open('tasks.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDo()
    window.show()
    sys.exit(app.exec_())