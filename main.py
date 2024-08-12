from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()

text_edit_QTextEdit()
list_notes_lbl = QLable()
notes_list = QListWidget()
create_note_btn = QPushButton()
create_note_btn = QPushButton()
delete_note_btn = QPushButton()
add_teg = QPushButton()
teg_list = QListWidget
create_teg_btn = QLineEdit()
delete_teg = QPushButton()
search_note_btn = QPushButton()
tags_list = QHBoxLayout()
tag_input = QLineEdit()

main_line = QHBoxLayout()
main_line = AddWidget(text_edit)

v1 = QVBoxLayout()
v1.addWidget(list_notes_lbl)
v1.addWidget(notes_list)
v1.addWidget(create_note_btn)
v1.addWidget()
v1.addWidget()
v1.addWidget()
v1.addWidget()
v1.addWidget()
v1.addWidget()
v1.addWidget()
main_line.addLayout(v1)

window.setLayout(main_line)
window.show()
app.exec()