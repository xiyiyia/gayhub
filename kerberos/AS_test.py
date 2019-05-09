from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
import sys
import kerberos.des_encryption as des_en
import kerberos.Tstr as tostr
import redis
import time
import socket
import kerberos.UI as ui

class QW(QWidget):
    message2_Plaintext = ''
    message2_Ciphertext = ''
    Key_client = ''
    ticket_tgs_Plaintext = ''
    ticket_tgs_Ciphertext = ''
    Key_tgs = ''

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #reply = QMessageBox.critical(self, '提醒', '这是一个提醒消息对话框', QMessageBox.Retry , QMessageBox.Retry)
        """msgBox = QMessageBox()
        msgBox.setWindowTitle('提醒')
        msgBox.setText("这是一条来自AS发送到Client的报文！！！")
        msgBox.setStandardButtons(QMessageBox.Retry)
        msgBox.setDefaultButton(QMessageBox.Ignore)
        msgBox.setDetailedText('message2_Plaintext = '+self.message2_Plaintext+ '\n'+ 'Key_client = '+self.Key_client +'message2_Ciphertext = '+self.message2_Ciphertext +'\n\n'+'ticket_tgs_plaintext = '+self.ticket_tgs_Plaintext+'\n'+'ticket_tgs_ciphertext = '+self.ticket_tgs_Ciphertext)
        reply = msgBox.exec()

        if reply == QMessageBox.Ignore:
            self.la.setText('你选择了Ignore！')"""

        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('ASASASASASAS')
        self.la = QLabel('这里是kerberos验证的加密解密细节呈现'+'\n'+'AS发送到Client的报文', self)
        self.la.move(20, 20)
        self.bt1 = QPushButton('明文密文', self)
        self.bt1.move(120, 80)
        self.bt2 = QPushButton('细节显示', self)
        self.bt2.move(120, 140)
        self.bt3 = QPushButton('来向去向', self)
        self.bt3.move(120, 200)
        self.bt1.clicked.connect(self.aboutMC)
        self.bt2.clicked.connect(self.aboutdetail)
        self.bt3.clicked.connect(self.fromandgoto)

        self.show()
    def aboutMC(self):
        self.form = QWidget()
        self.ui = ui.show_Kerberos()
        self.ui.setupUi(self.form,'message2_Ciphertext = '+self.message2_Ciphertext + '\n'+'message2_Plaintext = '+self.message2_Plaintext)
        self.form.show()
    def aboutdetail(self):
        self.form = QWidget()
        self.ui = ui.show_Kerberos()
        self.ui.setupUi(self.form,
                        'message2_Plaintext = '+self.message2_Plaintext+ '\n'+ 'Key_client = '+self.Key_client +'message2_Ciphertext = '+self.message2_Ciphertext +'\n\n'+'ticket_tgs_plaintext = '+self.ticket_tgs_Plaintext+'\n'+'ticket_tgs_ciphertext = '+self.ticket_tgs_Ciphertext)
        self.form.show()
    def fromandgoto(self):
        QMessageBox.about(self,'来源和去向','这是一条来自AS发送到Client的报文！！！')


def get_ticket(Key_ctgs, ip_Client, ip_TGS, ts2, lifetime2, r):
    # 在此要从数据库获取E_tgs，是TGS和AS之间使用的对称密钥
    Key_tgs = (r.get('Key_TGS')).decode()
    QW.Key_tgs = Key_tgs
    AD_c = ip_Client
    ticket = Key_ctgs + ip_Client + ip_Client + ip_TGS + ts2 + lifetime2
    QW.ticket_tgs_Plaintext = ticket
    ticket = des_en.test(ticket, Key_tgs)
    QW.ticket_tgs_Ciphertext = ticket
    print("ticket = ", ticket)
    return ticket


def AS_to_Client(ip_Client, r):
    Key_c = (r.get('Key_Client')).decode()
    Key_c = tostr.key_tostr(Key_c)
    QW.Key_client = Key_c

    Key_ctgs = (r.get('Key_ctgs')).decode()  # 理论上从数据库获取
    Key_ctgs = tostr.key_tostr(Key_ctgs)
    print("Key_ctgs = ", Key_ctgs)

    ip_TGS = (r.get('ip_TGS')).decode()  # 从数据库获取TGS的IP地址
    ip_TGS = tostr.ip_tostr(ip_TGS)
    ts2 = time.time()
    ts2 = tostr.ts_tostr(ts2)

    lifetime2 = 666
    lifetime2 = tostr.lifetime_tostr(lifetime2)

    ip_Client = tostr.ip_tostr(ip_Client)

    ticket_tgs = get_ticket(Key_ctgs, ip_Client, ip_TGS, ts2, lifetime2, r)

    message = Key_ctgs + ip_TGS + ts2 + lifetime2 + ticket_tgs
    QW.message2_Plaintext = message
    message = des_en.test(message, Key_c)
    QW.message2_Ciphertext = message
    return message


def get_Client_Authentication(ip_C, r):
    ip_Client = r.get('ip_Client').decode()
    if ip_Client == ip_C:
        print("The right Client!!!")
    else:
        print("The wrong Client!!!")


def AS():
    r = redis.Redis(host='localhost', port=6379, db=0)
    # 接受Client发送的报文
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localhost = socket.gethostname()
    port = 10000
    s.bind((localhost,port))
    s.listen(5)

    cs,address = s.accept()
    print("got connection : ",address)

    message1 = cs.recv(1024)
    # message1 = '192.168.43.202*192.168.43.203*1556868720.719386*'
    receive = message1.decode()
    ip_Client = receive[0:15]
    ip_Client = tostr.takeout(ip_Client)
    print("ip_Client = ", ip_Client)  # 数据库判断是否合法的ip

    get_Client_Authentication(ip_Client, r)

    ip_TGS = receive[15:30]
    ip_TGS = tostr.takeout(ip_TGS)
    print("ip_TGS = ", ip_TGS)

    ts1 = receive[30:48]
    ts1 = tostr.takeout(ts1)
    print("ts1 = ", ts1)
    ip_c = (r.get('ip_Client')).decode()
    print("ip_c = ", ip_c)
    if ip_c == ip_Client:
        message2 = AS_to_Client(ip_Client, r)
        print("message2 = ", message2)
            # 发送message给Client
        cs.send(message2.encode())
    else:
        print("There is not ",ip_Client)
        s.close()

    cs.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    AS()
    qw = QW()
    sys.exit(app.exec_())