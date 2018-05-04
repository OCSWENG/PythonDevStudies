import Tkinter
root = Tkinter.Tk()
root.title("Keysysm Logger")

def reportEvent(event):
	print 'keysym={} , keysym_num={}'.format(event.keysym, event.keysym_num)

text = Tkinter.Text(root, width=20, height=5, highlightthickness=2)
text.bind('<KeyPress>', reportEvent)

text.pack(expand=1, fill="both")
text.focus_set()
root.mainloop()

