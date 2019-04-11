import easygui as g
import sys
g.msgbox("杨宏兴,come on! you can do it!")

g.egdemo()
# while 1:
#     g.msgbox("嗨，欢迎进入第一个游戏界面！^_^")
#     msg = "请问你想成为什么样的人呢？"
#     title = "小游戏互动"
#     choices = ["科学家", "工程师", "医生", "程序员"]
#     choice = g.choicebox(msg, title, choices) #改行是将之前的msg，title,choice合并成一个选择窗口进行显示
#     g.msgbox("你的选择是:" + str(choice), "结果") #将choice的值显示出来
#     msg = "你想重新开始游戏吗？"
#     title = "请选择"
#     if g.ccbox(msg, title): #ccbox将msg和title合并，并提供继续和取消选择
#         pass     # 选择继续，到while第一行
#     else:       #选择取消
#         sys.exit(0)
