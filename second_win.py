from PyQt5.QtCore import Qt, QTimer, QTime

def timer_test(self):
  global time
  time= Qtime(0, 0, 15)
  self.timer = QTimer
  self.timer.tmeout.connect(self.timer1Event)
  self.timer.start(1000)
  
def timer_sits(self):
  global time
  time = QTime(0, 0, 30)
  self.timer = QTimer()
  self.timer.tmeout.connect(self.timer2Event)
  self.timer.start(1500)
  
def timer_sits(self):
  global time
  time = QTime(0, 1, 0)
  self.timer = QTimer()
  self.timer.tmeout.connect(self.timer3Event)
  self.timer.start(1000)
  
def timer1Event(self):
  global time
  time = timeaddSecs(-1)
  self.text_time.setText(time.toString('hh:mm:ss'))
  self.text_time.setFont(QFont('Times', 36, QFont.Bold))
  self.text_time.setStyleSheet('color': rgb(0, 0, 0)')
  if time.toString('hh:mm:ss') == "00:00:00":
     self.timer.stop()
                               
def timer2Event(self):
  global time
  time = timeaddSecs (-1)
  self.text_time.setText(time.toString('hh:mm:ss'))
  self.text_time.setFont(QFont('Time', 36, QFont.Bold))
  self.text_time.setStyleSheet('color': rgb(0, 0, 0)')
  if time.toString('hh:mm:ss') == "00:00:00":
     self.timer.stop()
                                
                               
def timer2Event(self):
  global time
  time = timeaddSecs(-1)
  self.text_time.setText(time.toString('hh:mm:ss'))
  if int(time.toString('hh:mm:ss')[6:8] >= 45:
    self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
  elif int(time.toString('hh:mm:ss')[6:8] >= 15:
    self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
  else:
    self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
  self.text_time.setFont(QFont('Time', 36, QFont.Bold))
  self.text_time.setStyleSheet('color': rgb(0, 0, 0)')
  if time.toString('hh:mm:ss') == "00:00:00":
     self.timer.stop()

def connects(self):
self.btn_next.clicked.connect(self.next_click)
self.btn_next1.clicked.connect(self.next_test)
self.btn_next2.clicked.connect(self.next_sits)
self.btn_next3.clicked.connect(self.next_final)
