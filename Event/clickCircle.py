import matplotlib.pyplot as plt
import time
plt.style.use('ggplot')

class Callbacks:
    def __init__(self):
        fig,ax = plt.subplots()
        ax.set_aspect(1)
        fig.canvas.mpl_connect('button_press_event',self.press)
        fig.canvas.mpl_connect('button_release_event',self.release)

        plt.show()
    def start(self):
        plt.show()

    def press(self,ev):
        self.start_time = time.time()
        
    def release(self,ev):
        self.end_time = time.time()
        self.draw_click(ev)
        
    def draw_click(self,ev):
        size = 4*(self.end_time - self.start_time)**2
        c1 = plt.Circle([ev.xdata,ev.ydata],0.0002)
        c2 = plt.Circle([ev.xdata,ev.ydata],0.02*size,alpha=0.2)
        ev.canvas.figure.gca().add_artist(c1)
        ev.canvas.figure.gca().add_artist(c2)
        ev.canvas.figure.show()
        
        
cbs = Callbacks()
cbs.start()
