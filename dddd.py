
def bang():
    import winsound
    duration = 50  # Set Duration To 1000 ms == 1 second

    for j in range(1, 10):
        extra = j * 100
        for i in range(1, 10):
            frequency = extra + 37*i  # Set Frequency To 2500 Hertz
            winsound. Beep(frequency, duration)
        for i in range(1,10):
            frequency = extra + 37* (11-i)  # Set Frequency To 2500 Hertz
            winsound.Beep(frequency, duration)


from tkinter import *

window = Tk()
window.title('my window')

mylable=Label(window, width=25, height=1, text="foo")
mylable.grid(row=0, column=0)


b=Button(window, text='hi there', width = 10, command = bang)
b.grid(row=1, column = 0)
window.mainloop()




#
# def greet(name):
#     answer = input('hello ' + name + ' what is your age?')
#     try:
#         age = int(answer)
#     except:
#         print("i dont understand " +answer)
#         age = -1
#     return age
#
# def multiple(number):
#     for i in range(1,6):
#         print(number * i)
#
#
# multiple(5)
#
# r=greet('gracie')
#
# print('gracie is ' + str(r))
# #greet('jiohn')
# #greet('johny')



