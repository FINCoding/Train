import _thread, queue, time
dataQueue = queue.Queue()

def producer(i):
    while True:
        i += 1
        if i > 100000000:
            break
        dataQueue.put( i )

def makethreads():
    _thread.start_new_thread(producer, (1,))

def print_into(root):
    try:
        data = dataQueue.get(block=False)
    except queue.Empty:
        pass
    else:
        root.insert('end', 'consumer got => %s\n' % str(data))
        root.see('end')


if __name__ == '__main__':
    from tkinter.scrolledtext import ScrolledText
    root = ScrolledText()
    root.pack()
    root.bind('<Button-1>', lambda event: makethreads())
    root.bind('<Button-3>', lambda event: print_into(root))
    root.mainloop()