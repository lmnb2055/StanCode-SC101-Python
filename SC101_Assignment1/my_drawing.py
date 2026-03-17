"""
File: Love Taiwan Image
Name:Sidney
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    When the Portuguese sailed to Taiwan in the 16th century,
    they shouted "Ilha formosa!“
    I love Taiwan!!!
    """
    window = GWindow(width=400, height=700, title='Taiwan')
    background = GRect(400, 700)
    background.filled = True
    background.fill_color = 'skyblue'
    background.color = 'skyblue'
    window.add(background)


    taiwan = GPolygon()
    taiwan.add_vertex((245, 660))   #台灣尾端1
    taiwan.add_vertex((260, 640))   # 2
    taiwan.add_vertex((250, 630))   # 3
    taiwan.add_vertex((244, 620))   # 4
    taiwan.add_vertex((240, 600))   # 5
    taiwan.add_vertex((240, 580))   # 6
    taiwan.add_vertex((240, 562))   # 7
    taiwan.add_vertex((250, 535))   # 8
    taiwan.add_vertex((255, 520))   # 9
    taiwan.add_vertex((260, 500))   # 10
    taiwan.add_vertex((270, 490))   # 11
    taiwan.add_vertex((275, 485))   # 12
    taiwan.add_vertex((280, 480))  # 13
    taiwan.add_vertex((281, 460))  # 14
    taiwan.add_vertex((285, 440))  # 15
    taiwan.add_vertex((290, 430))  # 16
    taiwan.add_vertex((290, 415))  # 17
    taiwan.add_vertex((300, 380))  # 18
    taiwan.add_vertex((301, 360))  # 19
    taiwan.add_vertex((302, 345))  # 20
    taiwan.add_vertex((303, 330))  # 21
    taiwan.add_vertex((304, 320))  # 22
    taiwan.add_vertex((305, 315))  # 23
    taiwan.add_vertex((306, 300))  # 24
    taiwan.add_vertex((305, 285))  # 25
    taiwan.add_vertex((303, 270))  # 26
    taiwan.add_vertex((300, 255))  # 27
    taiwan.add_vertex((290, 235))  # 28

    taiwan.add_vertex((289, 215))  # 29
    taiwan.add_vertex((285, 200))  # 30
    taiwan.add_vertex((280, 180))  # 31
    taiwan.add_vertex((265, 150))  # 32
    taiwan.add_vertex((260, 140))  # 33
    taiwan.add_vertex((265, 125))  # 34
    taiwan.add_vertex((275, 121))  # 35
    taiwan.add_vertex((280, 110))  # 36
    taiwan.add_vertex((285, 95))  # 37
    taiwan.add_vertex((280, 80))  # 38
    taiwan.add_vertex((270, 78))  # 39
    taiwan.add_vertex((255, 80))  # 40
    taiwan.add_vertex((245, 90))  # 41
    taiwan.add_vertex((235, 100))  # 42
    taiwan.add_vertex((230, 95))  # 43

    taiwan.add_vertex((220, 95))  # 44
    taiwan.add_vertex((215, 80))  # 45
    taiwan.add_vertex((210, 65))  # 46
    taiwan.add_vertex((203, 55))  # 47
    taiwan.add_vertex((190, 50))  # 48
    taiwan.add_vertex((180, 60))  # 49
    taiwan.add_vertex((175, 70))  # 50
    taiwan.add_vertex((165, 80))  # 51
    taiwan.add_vertex((163, 90))  # 52
    taiwan.add_vertex((165, 110))  # 53
    taiwan.add_vertex((180, 130))  # 54
    taiwan.add_vertex((175, 135))  # 55
    taiwan.add_vertex((160, 155))  # 56
    taiwan.add_vertex((155, 165))  # 57
    taiwan.add_vertex((140, 180))  # 58
    taiwan.add_vertex((130, 190))  # 59
    taiwan.add_vertex((120, 210))  # 60

    taiwan.add_vertex((110, 230))  # 61
    taiwan.add_vertex((100, 240))  # 62
    taiwan.add_vertex((90, 260))  # 63
    taiwan.add_vertex((85, 275))  # 64
    taiwan.add_vertex((80, 290))  # 65
    taiwan.add_vertex((75, 305))  # 66
    taiwan.add_vertex((74, 320))  # 67
    taiwan.add_vertex((73, 340))  # 68
    taiwan.add_vertex((70, 360))  # 69
    taiwan.add_vertex((71, 380))  # 70
    taiwan.add_vertex((72, 400))  # 71
    taiwan.add_vertex((73, 430))  # 72
    taiwan.add_vertex((75, 450))  # 73
    taiwan.add_vertex((80, 475))  # 74
    taiwan.add_vertex((85, 495))  # 75
    taiwan.add_vertex((100, 510))  # 76
    taiwan.add_vertex((115, 525))  # 77
    taiwan.add_vertex((125, 535))  # 78
    taiwan.add_vertex((140, 545))  # 79
    taiwan.add_vertex((158, 560))  # 80

    taiwan.add_vertex((162, 562))  # 81
    taiwan.add_vertex((175, 575))  # 82
    taiwan.add_vertex((185, 585))  # 83
    taiwan.add_vertex((198, 598))  # 84
    taiwan.add_vertex((203, 603))  # 85
    taiwan.add_vertex((205, 620))  # 86
    taiwan.add_vertex((210, 625))  # 87
    taiwan.add_vertex((225, 640))  # 88
    taiwan.add_vertex((230, 650))  # 89

    taiwan.filled = True
    taiwan.color = 'seagreen'
    taiwan.fill_color = 'seagreen'
    window.add(taiwan)

    left_eye = GArc(40, 120, 180, 180, x=120, y=240)
    left_eye.color = 'black'
    window.add(left_eye)
    # left_eye = GOval(40, 40, x=220, y=280)
    # left_
    right_eye = GArc(40, 120, 180, 180, x=220, y=240)
    right_eye.color = 'black'
    window.add(right_eye)

    nose = GOval(10, 10, x=180, y=290)
    nose.filled = 'black'
    nose.fill_color = 'black'
    window.add(nose)
    nose1 = GPolygon()
    nose1.add_vertex((185, 295))
    nose1.add_vertex((185, 340))
    nose1.color = 'black'
    window.add(nose1)

    mouth = GArc(50, 30, 180, 180, x=160, y=325)
    window.add(mouth)

    left_face = GOval(50, 50, x=80, y=325)
    right_face = GOval(50, 50, x=240, y=325)
    left_face.color = 'mistyrose'
    right_face.color = 'mistyrose'
    left_face.filled = True
    right_face.filled = True
    left_face.fill_color = 'mistyrose'
    right_face.fill_color = 'mistyrose'
    window.add(left_face)
    window.add(right_face)

    t = GLabel('LOVE', x=0, y=60)
    t.font = '-60'
    t.color = 'red'
    window.add(t)
    t1 = GLabel('LOVE', x=0, y=100)
    t1.font = '-55'
    t1.color = 'orangered'
    window.add(t1)
    t2 = GLabel('LOVE', x=0, y=132)
    t2.font = '-45'
    t2.color = 'tomato'
    window.add(t2)
    t3 = GLabel('LOVE', x=0, y=157)
    t3.font = '-35'
    t3.color = 'salmon'
    window.add(t3)
    t3 = GLabel('LOVE', x=0, y=178)
    t3.font = '-27'
    t3.color = 'lightsalmon'
    window.add(t3)
    t4 = GLabel('LOVE', x=0, y=193)
    t4.font = '-20'
    t4.color = 'mistyrose'
    window.add(t4)

    label = GLabel('Taiwan', x=270, y=700)
    label.font = '-40'
    label.color = 'navy'
    window.add(label)
    label1 = GLabel('Taiwan', x=285, y=670)
    label1.font = '-35'
    label1.color = 'mediumblue'
    window.add(label1)
    label2 = GLabel('Taiwan', x=300, y=640)
    label2.font = '-30'
    label2.color = 'blue'
    window.add(label2)
    label3 = GLabel('Taiwan', x=315, y=615)
    label3.font = '-25'
    label3.color = 'dodgerblue'
    window.add(label3)
    label4 = GLabel('Taiwan', x=330, y=590)
    label4.font = '-20'
    label4.color = 'royalblue'
    window.add(label4)
    label5 = GLabel('Taiwan', x=343, y=570)
    label5.font = '-15'
    label5.color = 'steelblue'
    window.add(label5)
    label6 = GLabel('Taiwan', x=357, y=555)
    label6.font = '-10'
    label6.color = 'lightcyan'
    window.add(label6)
    label7 = GLabel('Taiwan', x=366, y=542)
    label7.font = '-7'
    label7.color = 'aliceblue'
    window.add(label7)




    # window = GWindow(width=800, height=600, title='iron_man')
    # back = GRect(800, 600, x=0, y=0)
    # back.filled = True
    # back.fill_color = 'light yellow'
    # back.color = 'light yellow'
    # window.add(back)
    #
    # l_back = GRect(200, 550, x=15, y=25)
    # l_back.filled = True
    # l_back.fill_color = 'maroon'
    # l_back.color = 'maroon'
    # window.add(l_back)
    #
    # r_back = GRect(200, 550, x=window.width - 215, y=25)
    # r_back.filled = True
    # r_back.fill_color = 'cornflowerblue'
    # r_back.color = 'cornflowerblue'
    # window.add(r_back)
    #
    # r2_back = GRect(180, 550, x=window.width - 400, y=25)
    # r2_back.filled = True
    # r2_back.fill_color = 'cornflowerblue'
    # r2_back.color = 'cornflowerblue'
    # window.add(r2_back)
    #
    # l_back = GRect(200, 550, x=15, y=25)
    # l_back.filled = True
    # l_back.fill_color = 'maroon'
    # l_back.color = 'maroon'
    # window.add(l_back)
    #
    # l2_back = GRect(180, 550, x=220, y=25)
    # l2_back.filled = True
    # l2_back.fill_color = 'maroon'
    # l2_back.color = 'maroon'
    # window.add(l2_back)
    #
    # r_back = GRect(200, 550, x=window.width - 215, y=25)
    # r_back.filled = True
    # r_back.fill_color = 'cornflowerblue'
    # r_back.color = 'cornflowerblue'
    # window.add(r_back)
    #
    # polygon = GPolygon()
    # polygon.add_vertex((400, 25))  # left head point
    # polygon.add_vertex((415, 25))  # forehead
    # polygon.add_vertex((475, 45))  # face
    # polygon.add_vertex((510, 180))  # face
    # polygon.add_vertex((490, 340))  # face
    # polygon.add_vertex((475, 350))  # neck
    # polygon.add_vertex((465, 370))  # neck
    # polygon.add_vertex((520, 420))  # neck
    # polygon.add_vertex((550, 430))  # shoulder
    # polygon.add_vertex((580, 440))  # shoulder
    # polygon.add_vertex((580, 575))  # shoulder
    # polygon.add_vertex((220, 575))  # border
    # polygon.add_vertex((220, 430))  # border
    # polygon.add_vertex((220, 420))  # left shoulder
    # polygon.add_vertex((240, 380))  # left shoulder
    # polygon.add_vertex((260, 370))  # left shoulder
    # polygon.add_vertex((270, 360))  # left shoulder
    # polygon.add_vertex((300, 350))  # left shoulder
    # polygon.add_vertex((310, 340))  # left shoulder
    # polygon.add_vertex((300, 310))  # face
    # polygon.add_vertex((295, 280))  # face
    # polygon.add_vertex((290, 260))  # face
    # polygon.add_vertex((290, 240))  # face
    # polygon.add_vertex((288, 200))  # face
    # polygon.add_vertex((290, 150))  # face
    # polygon.add_vertex((300, 100))  # face
    # polygon.add_vertex((310, 55))
    # polygon.add_vertex((359, 25))  # face
    # polygon.filled = True
    # polygon.fill_color = 'midnightblue'
    # polygon.color = 'midnightblue'
    # window.add(polygon)
    #
    # yellowface = GPolygon()
    # yellowface.add_vertex((356, 33))
    # yellowface.add_vertex((313, 58))
    # yellowface.add_vertex((303, 103))
    # yellowface.add_vertex((313, 155))
    # yellowface.add_vertex((320, 158))
    # yellowface.add_vertex((353, 161))
    # yellowface.add_vertex((383, 164))
    # yellowface.add_vertex((413, 168))
    # yellowface.add_vertex((450, 164))
    # yellowface.add_vertex((480, 161))
    # yellowface.add_vertex((481, 185))
    # yellowface.add_vertex((450, 193))
    # yellowface.add_vertex((440, 190))  # right eye
    # yellowface.add_vertex((420, 185))
    # yellowface.add_vertex((380, 185))  # nose
    # yellowface.add_vertex((360, 185))
    # yellowface.add_vertex((350, 190))
    # yellowface.add_vertex((320, 193))
    # yellowface.add_vertex((310, 185))  # left eye
    # yellowface.add_vertex((300, 220))
    # yellowface.add_vertex((305, 230))
    # yellowface.add_vertex((310, 240))
    # yellowface.add_vertex((313, 253))
    # yellowface.add_vertex((320, 260))
    # yellowface.add_vertex((325, 270))
    # yellowface.add_vertex((330, 280))
    # yellowface.add_vertex((340, 290))
    # yellowface.add_vertex((340, 303))
    # yellowface.add_vertex((350, 310))
    # yellowface.add_vertex((338, 315))
    # yellowface.add_vertex((330, 320))
    # yellowface.add_vertex((320, 325))
    # yellowface.add_vertex((310, 310))
    # yellowface.add_vertex((315, 340))
    # yellowface.add_vertex((330, 350))
    # yellowface.add_vertex((340, 355))
    # yellowface.add_vertex((350, 345))  # 下巴上升
    # yellowface.add_vertex((370, 330))
    # yellowface.add_vertex((380, 325))
    # yellowface.add_vertex((390, 325))
    # yellowface.add_vertex((400, 323))
    # yellowface.add_vertex((410, 325))
    # yellowface.add_vertex((420, 323))
    # yellowface.add_vertex((430, 325))
    # yellowface.add_vertex((440, 325))
    # yellowface.add_vertex((450, 330))
    # yellowface.add_vertex((460, 345))  # 下巴結束
    # yellowface.add_vertex((475, 320))
    # yellowface.add_vertex((475, 320))
    # yellowface.add_vertex((465, 310))  # 進入嘴巴
    # yellowface.add_vertex((445, 315))
    # yellowface.add_vertex((430, 310))
    # yellowface.add_vertex((380, 310))
    # yellowface.add_vertex((365, 318))
    # yellowface.add_vertex((350, 310))
    # yellowface.add_vertex((366, 312))  # 上面嘴唇
    # yellowface.add_vertex((373, 303))
    # yellowface.add_vertex((435, 303))
    # yellowface.add_vertex((445, 307))
    # yellowface.add_vertex((465, 304))
    # yellowface.add_vertex((460, 290))  # 右邊臉頰
    # yellowface.add_vertex((465, 280))
    # yellowface.add_vertex((475, 275))
    # yellowface.add_vertex((480, 265))
    # yellowface.add_vertex((485, 255))
    # yellowface.add_vertex((490, 240))
    # yellowface.add_vertex((493, 230))
    # yellowface.add_vertex((485, 150))
    # yellowface.add_vertex((483, 100))
    # yellowface.add_vertex((473, 55))
    # yellowface.add_vertex((430, 33))
    # yellowface.add_vertex((415, 120))
    # yellowface.add_vertex((363, 120))
    # yellowface.filled = True
    # yellowface.fill_color = 'lemonchiffon'
    # yellowface.color = 'lemonchiffon'
    # window.add(yellowface)
    #
    # face1 = GPolygon()
    # face1.add_vertex((430, 33))
    # face1.add_vertex((415, 28))
    # face1.add_vertex((400, 28))
    # face1.add_vertex((356, 33))
    # face1.add_vertex((313, 58))
    # face1.add_vertex((303, 103))
    # face1.add_vertex((313, 155))
    # face1.add_vertex((320, 158))
    # face1.add_vertex((353, 161))
    # face1.add_vertex((360, 103))
    # face1.add_vertex((358, 70))
    # face1.add_vertex((380, 68))
    # face1.add_vertex((420, 70))
    # face1.filled = True
    # face1.fill_color = 'maroon'
    # face1.color = 'maroon'
    # window.add(face1)
    #
    # forehead = GPolygon()
    # forehead.add_vertex((363, 120))
    # forehead.add_vertex((393, 123))
    # forehead.add_vertex((413, 120))
    # forehead.add_vertex((420, 80))
    # forehead.add_vertex((390, 78))
    # forehead.add_vertex((360, 80))
    # forehead.filled = True
    # forehead.fill_color = 'maroon'
    # forehead.color = 'maroon'
    # window.add(forehead)
    #
    # left_eye = GPolygon()
    # left_eye.add_vertex((365, 173))
    # left_eye.add_vertex((310, 163))
    # left_eye.add_vertex((305, 173))
    # left_eye.add_vertex((310, 181))
    # left_eye.add_vertex((350, 186))
    # left_eye.add_vertex((365, 182))
    # left_eye.filled = True
    # left_eye.fill_color = 'white'
    # left_eye.color = 'white'
    # window.add(left_eye)
    #
    # right_eye = GPolygon()
    # right_eye.add_vertex((420, 175))
    # right_eye.add_vertex((475, 165))
    # right_eye.add_vertex((478, 175))
    # right_eye.add_vertex((475, 180))
    # right_eye.add_vertex((445, 185))
    # right_eye.add_vertex((423, 180))
    #
    #
    #
    #
    # right_eye.filled = True
    # right_eye.fill_color = 'white'
    # right_eye.color = 'white'
    # window.add(right_eye)
    #
    #
    #
    #
    #
    # face = GOval(200, 200, x=30, y=60)
    # face.filled = True
    # face.fill_color = 'peachpuff'
    # window.add(face)
    # l_eye = GOval(30, 30, x=100, y=150)
    # window.add(l_eye)
    # l_eye.filled = True
    # l_eye.fill_color = 'snow'
    # r_eye = GOval(30, 30, x=170, y=150)
    # window.add(r_eye)
    # r_eye.filled = True
    # r_eye.fill_color = 'snow'
    # mouth = GRect(50, 50, x=120, y=200)
    # mouth.filled = True
    # mouth.fill_color = 'snow'
    # window.add(mouth)
    # label = GLabel('OMG')
    # label.font = '-60'
    # label.filled = True
    # label.fill_color = 'hotpink'
    # window.add(label, x=50, y=70)


if __name__ == '__main__':
    main()
