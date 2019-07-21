import tkinter as tk
import serial


L_duty_array = {"-4":"150","-3":"145", "-2":"105", "-1":"080","0":"000", "1":"080", "2":"105","3":"145", "4":"150"}
R_duty_array = {"-4":"115","-3":"110", "-2":"080", "-1":"060","0":"000", "1":"060", "2":"080","3":"110", "4":"115"}

ser = serial.Serial('/dev/rfcomm8', 9600)

class Application(tk.Frame):
    def __init__(self,master,left_duty='0',right_duty='0'):
        super().__init__(master)
        #self.pack()
        master.geometry("600x400")
        master.title("Tank Controller")
        master.bind('<Up>', self.forward)
        master.bind('<space>', self.stop)
        master.bind('<Down>', self.backward)
        master.bind('<Right>', self.right)
        master.bind('<Left>', self.left)
        master.bind('<z>', self.LL)
        master.bind('<x>', self.RR)
        self.create_widgets(master,left_duty,right_duty)

    def create_widgets(self,master,left_duty,right_duty):
        self.left_duty = tk.Label(master, text=left_duty, relief=tk.FLAT, bd=2,background="white")
        self.right_duty = tk.Label(master, text=right_duty, relief=tk.FLAT, bd=2,background="white")
        forward = tk.Button(master, text="↑", fg="blue", command=self.forward)
        backward = tk.Button(master, text="↓", fg="blue", command=self.backward)
        right = tk.Button(master, text="→", fg="green", command=self.right)
        left = tk.Button(master, text="←", fg="green", command=self.left)
        RR = tk.Button(master, text=">>", fg="purple", command=self.RR)
        LL = tk.Button(master, text="<<", fg="purple", command=self.LL)
        stop = tk.Button(master, text="STOP", fg="red", command=self.stop)

        self.left_duty.grid(row=0, column=0, columnspan=2, sticky="we")
        self.right_duty.grid(row=0, column=3, columnspan=2, sticky="we")
        forward.grid(row=1, column=1, columnspan=3, sticky="we")
        LL.grid(row=2, column=0)
        left.grid(row=2, column=1)
        stop.grid(row=2, column=2)
        right.grid(row=2, column=3)
        RR.grid(row=2, column=4)
        backward.grid(row=3, column=1, columnspan=3, sticky="we")

    def send_command(self,command):
        arg = str(command) + ";"
        print(arg)
        arg_byte=arg.encode('utf-8')
        ser.write(arg_byte)
        return

    def forward(self,event=None):
        print("FORWARD")
        #command = ('F100085')
        L = self.left_duty["text"]
        R = self.right_duty["text"]

        if R!=L:
            i=0
        else:
            i=int(R)
        i=i+1

        if i > 3:
            i=4;
        L_level = self.left_duty["text"] = str(i);
        R_level = self.right_duty["text"] = str(i);

        if i>0:
            direction ="F"
        else:
            direction ="B"

        command = direction + str(L_duty_array[L_level]) + str(R_duty_array[R_level])
        self.send_command(command)
        return

    def stop(self, event=None):
        print("STOP")
        L_level = self.left_duty["text"] = "0";
        R_level = self.right_duty["text"] = "0";
        direction ="S"
        command = direction + str(L_duty_array[L_level]) + str(R_duty_array[R_level])
        self.send_command(command)
        return

    def backward(self, event=None):
        print("BACKWARD")
        L = self.left_duty["text"]
        R = self.right_duty["text"]

        if R!=L:
            i=-1
        else:
            i=int(R)
        i=i-1

        if i < -3:
            i=-4;
        L_level = self.left_duty["text"] = str(i);
        R_level = self.right_duty["text"] = str(i);

        if i>0:
            direction ="F"
        else:
            direction ="B"

        command = direction + str(L_duty_array[L_level]) + str(R_duty_array[R_level])
        self.send_command(command)
        return

    def left(self, event=None):
        print("LEFT")
        i = int(self.left_duty["text"])
        i = i-1

        if i<0:
            i=0

        L_level = self.left_duty["text"] = str(i)
        R_level = self.right_duty["text"]

        direction ="F"
        command = direction + str(L_duty_array[L_level]) + str(R_duty_array[R_level])
        self.send_command(command)
        return

    def right(self, event=None):
        print("RIGHT")
        i = int(self.right_duty["text"])
        i = i-1

        if i<0:
            i=0

        L_level = self.left_duty["text"]
        R_level = self.right_duty["text"] = str(i)

        direction ="F"
        command = direction + str(L_duty_array[L_level]) + str(R_duty_array[R_level])
        self.send_command(command)
        return

    def LL(self, event=None):
        print("LL")
        L_level = self.left_duty["text"] = "-2";
        R_level = self.right_duty["text"] = "2";
        direction ="L"
        command = direction + str(L_duty_array[L_level]) + str(R_duty_array[R_level])
        self.send_command(command)
        return

    def RR(self, event=None):
        print("RR")
        L_level = self.left_duty["text"] = "2";
        R_level = self.right_duty["text"] = "-2";
        direction ="R"
        command = direction + str(L_duty_array[L_level]) + str(R_duty_array[R_level])
        self.send_command(command)
        return

def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()
