# import lines
import tkinter as tk
import tkinter.ttk as ttk
import turtlefigure
import turtle
import random
import colorsys


class TurtleGenerator(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.parent = parent

        self.makeUI()
        self.centerApplication()

    # end __init__

    def makeUI(self):

        self.parent.title("Turtle Generator Application")
        self.pack(fill=tk.BOTH, expand=True)

        self.fractalNames = ["Binary Tree", "Dandelion", "Fern",
                             "Snowflake", "Antiflake", "Sierpinski Carpet",
                             "Sierpinski Gasket", "Swiss Gasket", "Pentagon",
                             "Lévy C Curve", "Crocheted Circles", "Diamond Eye",
                             "Diamond Cube", "Star", "Pinwheel"]

        self.fractalFunctionNames = [turtlefigure.tree, turtlefigure.tree4, turtlefigure.fern,
                                     turtlefigure.flake, turtlefigure.antiflake, turtlefigure.s_carpet,
                                     turtlefigure.s_gasket, turtlefigure.swiss_gasket, turtlefigure.pent,
                                     turtlefigure.c_curve, turtlefigure.circles, turtlefigure.diamond_eye,
                                     turtlefigure.diamond_cube, turtlefigure.star,
                                     turtlefigure.pinwheel]

        self.fractalDescription = ["""The Binary Tree is a deterministic and self-similar fractal and starts with a simple line.
        
    With each increase of the order, the line gets split into two at an angle of 45 degrees in both directions, and two new lines with half the length of the line before get drawn, giving the impression of a tree.
        
    For this fractal, the recommended length is of no longer than 300.""",
                                   """The Dandelion is a deterministic and self-similar fractal and starts with a simple line.
                                   
    With each increase of the order, the line gets split into four further lines, with an angle of 60 degrees between them. The new lines are half the length of the line before, giving the appearance of a dandelion.
                                   
    For this fractal, the recommended length is of no longer than 300.""",
                                   """The Fern is a deterministic self-affine fractal and starts with a simple line.
                                   
    At three different points multiplied by the order, lines branch off with varying angles, which then also branch again depending on the order, giving the appearance of a fern.
                                   
    Recommend length depends highly on the chosen order, although a length of 50 can be a good starting point.""",
                                   """The Snowflake, also called the Koch Snowflake, is a deterministic and self-similar fractal based on the Koch curve. 
    With an order of 1, the Koch curve is a simple line, which the Snowflake iterates three times to create a triangular shape.
                                   
    With each increase of the order, the Koch curve gets split in three and the middle section is replaced by a peak with each side the same length as the replaced section, to which the same process will be applied.
With a higher number of iterations, i.e. a high order number, the fractal will take on the shape of a snowflake.
                                   
    For this fractal, the recommended length is of no longer than 300.""",
                                   """The Antiflake is a deterministic and self-similar fractal based on the Koch curve. It is very similar to the Snowflake fractal, of which description can offer more detail on how it is made.
                                   
    In comparison to the Snowflake, the Antiflake creates its triangular shape with opposite angles, resulting in valleys rather than the peaks described in the description of the Snowflake fractal.
                                   
    For this fractal, the recommended length is of no longer than 300.""",
                                   """The Sierpinski Carpet, also called the Sierpinski Square Snowflake, is a deterministic self-similar fractal based on the Sierpinski Curve.
                                   
    This curve has a very distinctive pattern, which when repeated four times with a 90 degrees angle, could be imagined as the pattern of a carpet.
                                   
    As the size of the carpet grows exponentially with increase of the order, a small length like 5 is recommended.""",
                                   """The Sierpinski Gasket is a self-similar deterministic fractal in a triangular shape to start with.
                                   
    With each increase of the order, triangles are drawn within the corner of the previous triangle(s) drawn, with their sides half the length of the previous triangle(s).
                                   
    For this fractal, the recommended length is of no longer than 300.""",
                                   """The Swiss Gasket is a self-similar deterministic fractal that starts off with a simple square.
                                   
    With each increase of the order, further squares are drawn in the corner of the previous square(s), with their sides a third the length of the previous square(s).
This leaves an empty space in the middle of each square looking like a cross, similar to the Swiss Flag.
                                   
    For this fractal, the recommended length is of no longer than 300.""",
                                   """The Pentagon is a self-similar deterministic fractal that starts off with a simple line.
                                   
    With each increase of the order, further pentagons are drawn in the corner of the previous pentagon(s), with their sides a little more than a third the length of the previous pentagon(s).
                                   
    For this fractal, the recommended length is of no longer than 300.""",
                                   """The Lévy C Curve, often just called C Curve, is a self-similar, deterministic fractal that starts off with a simple pentagon.
                                   
    With each increase of the order, a further line is added with the same length and an angle of 90 degrees, which quickly gives the impression of the letter 'C'. 
                                   
    As the size of the curve grows with each increase of the order, a small length like 5 is recommended.""",
                                   """The Crocheted Circles fractal is a self-similar, deterministic fractal and starts off with a simple circle.
                                   
    With each increase of the order, six more circles are placed tangentially within the previously drawn circle(s) at each sixth of the circumference with a third of the radius of the previous circle(s).
For aesthetic purposes, three smaller circles are placed tangentially between each of the bigger circles, which gives of the impression of a finely crocheted tablecloth.
                                   
    For this fractal, the recommended length is of no longer 300.""",
                                   """The Diamond Eye is a self-similar deterministic fractal based on a diamond lozenge shape.
    With each increase of the order, the basic diamond shape is used as a guideline for the placement of further diamonds.
If the the order is not too high, it is easy to imagine seeing an eye in the middle.
                                   
    For this fractal, the recommended length if of no longer than 400.""",
                                   """The Diamond Cube is a self-similar deterministic fractal based on a diamond lozenge shape, repeated three times at an angle of 90 degrees. 
                                   
    This results in the illusion of a three-dimensional object in the shape of a cube. With each increase of the order, each side of the cube gets split into more diamonds. 
                                   
    For this fractal, the recommended length is of no longer 300.""",
                                   """The Star is a self-similar deterministic fractal based on a diamond lozenge shape repeated six times in a circular pattern.
                                   
    With each increase of the order, this is repeated with a little more than half the length than previously and an offset of 30 degrees, resulting in a beautiful star pattern.
                                   
    For this fractal, the recommended length is of no longer 300.""",
                                   """The Pinwheel is a self-similar deterministic fractal based on a diamond lozenge shape.
                                    
    It is similar to the star, but the pattern is only repeated four times.
With each increase of the order, this is repeated with a little more than half the length than previously and an offset of 30 degrees, resulting in a pattern not unlike a pinwheel.
                                   
    For this fractal, the recommended length is of no longer 300."""]

        self.columnconfigure(0, minsize=300)
        self.columnconfigure(1, minsize=500)

        self.darkcolor = tk.StringVar()
        self.darkcolor.set("#6c476c")
        self.darkercolor = tk.StringVar()
        self.darkercolor.set("#3e283e")
        self.lightcolor = tk.StringVar()
        self.lightcolor.set("#b188b1")
        self.lightercolor = tk.StringVar()
        self.lightercolor.set("#f4d3f8")

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure(".", background=self.darkcolor.get(), foreground="#ffffff")
        self.style.configure("Title.TLabel", font=("default", "16", "bold"))
        self.style.configure("TLabelframe", relief="groove", padding="10 5 5 10")
        self.style.configure("Canvas.TLabelframe", relief="groove", padding="0 0 0 0")
        self.style.configure("TLabelframe.Label", font=("default", 12), foreground=self.lightercolor.get())
        self.style.map("TButton", background=[("active", self.lightcolor.get())])
        self.style.configure("Control.TLabel", width=5, anchor=tk.E, padx=5, font=("default", "12"),
                             foreground=self.lightercolor.get())
        self.style.configure("Status.TLabel", anchor=tk.W, background=self.darkercolor.get(),
                             foreground=self.lightercolor.get(), width=7)
        self.style.configure("Progress.TLabel", anchor=tk.W, background=self.darkercolor.get(),
                             foreground=self.lightercolor.get(),
                             font=("default", "13", "italic"), padx=(0, 20))
        self.style.configure("TEntry", foreground="#ffffff", fieldbackground=self.darkercolor.get(), padding="3 1 1 1")
        self.style.map("TMenubutton", background=[("active", self.lightcolor.get())])
        self.style.configure("Random.TButton", borderwidth=0, font=("default", "11"),
                             padding="0 0 0 0", width=8, anchor=tk.E + tk.W)
        self.style.configure("Horizontal.TScale", background="white", troughcolor="#362f36",
                             sliderthickness=5, sliderlength=10, sliderrelief="ridge",
                             borderwidth=0)

        # make the first label
        label = ttk.Label(self, text="Turtle Fractal Generator", style="Title.TLabel")
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # make the canvas panel
        canvasPanel = ttk.LabelFrame(self, text=" Canvas ", style="Canvas.TLabelframe")
        canvasPanel.grid(row=1, column=1, rowspan=3, padx=(0, 15))

        self.canvas = tk.Canvas(canvasPanel, width=500, height=500, bd=1,
                                relief="ridge", highlightthickness=0, bg=self.darkercolor.get())
        self.canvas.pack(padx=(23, 21), pady=(16, 21))

        # get the canvas pen and screen
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor(self.darkercolor.get())

        self.pen = turtle.RawPen(self.screen)
        self.pen.color(self.lightercolor.get())
        self.pen.speed(0)
        self.pen.width(1)

        # make the control panel
        controlPanel = ttk.LabelFrame(self, text=" Control Panel ")
        controlPanel.grid(row=1, column=0, padx=(15, 15)
                          , sticky=tk.W + tk.E)

        # make the fractal selection widgets
        fractalLabel = ttk.Label(controlPanel, text="FRACTAL", style="Control.TLabel")
        fractalLabel.grid(row=0, column=0, sticky=tk.W + tk.E, padx=5)

        self.fractalStr = tk.StringVar()
        fractalOptionMenu = ttk.OptionMenu(controlPanel, self.fractalStr, self.fractalNames[0],
                                           *self.fractalNames, command=self.descriptionF)
        fractalOptionMenu.grid(row=0, column=1, pady=5, sticky=tk.W + tk.E)

        # make the order widgets
        orderLabel = ttk.Label(controlPanel, text="ORDER", style="Control.TLabel")
        orderLabel.grid(row=1, column=0, sticky=tk.W + tk.E, padx=5)

        self.orderStr = tk.StringVar()
        orderEntry = ttk.Entry(controlPanel, textvariable=self.orderStr)
        orderEntry.grid(row=1, column=1, sticky=tk.W + tk.E, pady=1)

        # randomise order widgets
        randomOrderButton = ttk.Button(controlPanel, text="Randomise", command=self.randomOrderF,
                                       style="Random.TButton", cursor="hand2")
        randomOrderButton.grid(row=1, column=1, sticky=tk.E, padx=3)

        # make the length widgets
        lengthLabel = ttk.Label(controlPanel, text="LENGTH", style="Control.TLabel")
        lengthLabel.grid(row=2, column=0, sticky=tk.W + tk.E, padx=5)

        self.lengthStr = tk.StringVar()
        lengthEntry = ttk.Entry(controlPanel, textvariable=self.lengthStr)
        lengthEntry.grid(row=2, column=1, sticky=tk.W + tk.E, pady=1)

        # randomise Length widgets
        randomLengthButton = ttk.Button(controlPanel, text="Randomise", command=self.randomLengthF,
                                        style="Random.TButton", cursor="hand2")
        randomLengthButton.grid(row=2, column=1, sticky=tk.E, padx=3)

        # make the clear button
        clearButton = ttk.Button(controlPanel, text="Clear", command=self.clearF, cursor="hand2")
        clearButton.grid(row=3, column=0, padx=5)

        # make the draw button
        drawButton = ttk.Button(controlPanel, text="Draw", command=self.drawF, cursor="hand2")
        drawButton.grid(row=3, column=1, pady=10, sticky=tk.E + tk.W)

        # make the description panel
        descriptionPanel = ttk.LabelFrame(self, text=" Description ")
        descriptionPanel.grid(row=2, column=0, padx=(15, 15), pady=10,
                              sticky=tk.E + tk.W + tk.N + tk.S)
        descriptionPanel.columnconfigure(0, minsize=293)

        # make the description widget
        self.descriptionStr = tk.StringVar()
        self.descriptionStr.set(self.fractalDescription[0])
        self.description = tk.Text(descriptionPanel, state=tk.DISABLED, font=("default", "14"),
                                   width=13, height=13, bd=1, relief="ridge", wrap=tk.WORD,
                                   padx=10, pady=5, highlightthickness=0, bg=self.darkercolor.get(),
                                   fg="white", cursor="left_ptr")
        self.description.grid(row=0, column=0, padx=6, pady=10,
                              sticky=tk.E + tk.W + tk.N + tk.S)
        self.description.configure(state=tk.NORMAL)
        self.description.insert("end", self.descriptionStr.get())
        self.description.configure(state=tk.DISABLED)

        scrollbar = ttk.Scrollbar(descriptionPanel, orient=tk.VERTICAL,
                                  command=self.description.yview, width=5, cursor="hand2")
        scrollbar.grid(row=0, column=0, pady=10.5, padx=(0, 5),
                       sticky=tk.E + tk.N + tk.S)
        self.description["yscrollcommand"] = scrollbar.set

        # make the appearance panel
        appearancePanel = ttk.LabelFrame(self, text=" Appearance ")
        appearancePanel.grid(row=3, column=0, padx=(15, 15), ipadx=5, sticky=tk.E + tk.W + tk.N + tk.S)
        appearancePanel.columnconfigure(0, minsize=102)

        # make the color mode widgets
        colorModeLabel = ttk.Label(appearancePanel, text="MODE", style="Control.TLabel")
        colorModeLabel.grid(row=0, column=0, sticky=tk.E + tk.W, padx=5, pady=5)

        self.colorModeInt = tk.IntVar()
        self.darkColorModeButton = tk.Radiobutton(appearancePanel, text="DARK", indicatoron=0,
                                                  variable=self.colorModeInt, value=0, command=self.colorModeF,
                                                  background=self.darkercolor.get(), foreground=self.darkcolor.get(),
                                                  borderwidth=1, selectcolor=self.darkcolor.get(),
                                                  activebackground=self.lightercolor.get(),
                                                  font=("default", 13, "bold"),
                                                  cursor="hand2")
        self.darkColorModeButton.grid(row=0, column=1, sticky=tk.E + tk.W, pady=5)
        self.lightColorModeButton = tk.Radiobutton(appearancePanel, text="LIGHT", indicatoron=0,
                                                   variable=self.colorModeInt, value=1, command=self.colorModeF,
                                                   background=self.darkcolor.get(), foreground=self.lightercolor.get(),
                                                   borderwidth=1, selectcolor=self.darkcolor.get(),
                                                   activebackground=self.lightercolor.get(),
                                                   font=("default", 13, "bold"),
                                                   cursor="hand2")
        self.lightColorModeButton.grid(row=0, column=2, sticky=tk.E + tk.W, pady=5)

        # make the background color widgets
        colorLabel = ttk.Label(appearancePanel, text="COLOUR", style="Control.TLabel")
        colorLabel.grid(row=1, column=0, sticky=tk.E + tk.W, padx=5)

        self.darkhueImg = tk.PhotoImage(file="dark_hue_gradient.png")
        self.lighthueImg = tk.PhotoImage(file="light_hue_gradient.png")
        self.hueImgLabel = ttk.Label(appearancePanel, image=self.darkhueImg, relief="ridge")
        self.hueImgLabel.grid(row=1, column=1, columnspan=2)

        self.hueInt = tk.IntVar()
        hueScale = ttk.Scale(appearancePanel, from_=0, to=360, orient=tk.HORIZONTAL,
                             value=300, variable=self.hueInt, command=self.hueF, cursor="hand2")
        hueScale.grid(row=1, column=1, sticky=tk.W + tk.E, columnspan=2, padx=(1, 1))
        self.hueInt.set(300)

        # make the status frame
        statusFrame = ttk.Frame(self)
        statusFrame.grid(row=4, column=0, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)
        statusFrame.columnconfigure(0, minsize=25)
        statusFrame.columnconfigure(1, minsize=850)

        statusSeparator = ttk.Separator(statusFrame, orient=tk.HORIZONTAL)
        statusSeparator.grid(row=0, column=0, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S, pady=(20, 0))

        # make the status widgets
        statusLabel = ttk.Label(statusFrame, text="     Status:", style="Status.TLabel")
        statusLabel.grid(row=1, column=0, sticky=tk.E + tk.W + tk.N + tk.S, ipady=2)

        self.progressStr = tk.StringVar()
        progressLabel = ttk.Label(statusFrame, textvariable=self.progressStr, style="Progress.TLabel")
        progressLabel.grid(row=1, column=1, columnspan=2, sticky=tk.W + tk.N + tk.E + tk.S, ipady=2)
        self.progressStr.set("Waiting on Instructions...")

    # end makeUI

    # define the handlers

    def hueF(self, hue):
        hue = self.hueInt.get()

        rgbDarker = colorsys.hls_to_rgb((hue + 3) / 360, 20 / 100, 22 / 100)
        rgbDark = colorsys.hls_to_rgb((hue + 3) / 360, 35 / 100, 21 / 100)
        rgbLight = colorsys.hls_to_rgb(hue / 360, 69 / 100, 23 / 100)
        rgbLighter = colorsys.hls_to_rgb((hue - 3) / 360, 90 / 100, 73 / 100)

        self.darkercolor.set("#%02x%02x%02x" % (int(255 * rgbDarker[0]), int(255 * rgbDarker[1]), int(255 * rgbDarker[2])))
        self.darkcolor.set("#%02x%02x%02x" % (int(255 * rgbDark[0]), int(255 * rgbDark[1]), int(255 * rgbDark[2])))
        self.lightcolor.set("#%02x%02x%02x" % (int(255 * rgbLight[0]), int(255 * rgbLight[1]), int(255 * rgbLight[2])))
        self.lightercolor.set("#%02x%02x%02x" % (int(255 * rgbLighter[0]), int(255 * rgbLighter[1]), int(255 * rgbLighter[2])))

        if self.colorModeInt.get() == 1:
            self.style.configure(".", background=self.lightcolor.get(), foreground="#ffffff")
            self.style.configure("TLabelframe.Label", foreground="#ffffff")
            self.style.configure("Control.TLabel", foreground=self.darkcolor.get())
            self.style.map("TButton", background=[("active", self.darkcolor.get())])
            self.style.configure("TEntry", foreground=self.lightcolor.get(), fieldbackground="#ffffff")
            self.style.map("TMenubutton", background=[("active", self.darkcolor.get())])
            self.style.configure("Status.TLabel", background=self.darkcolor.get(), foreground=self.lightercolor.get())
            self.style.configure("Progress.TLabel", background=self.darkcolor.get(), foreground=self.lightercolor.get())
            self.style.configure("Horizontal.TScale", background="#362f36", troughcolor="#ffffff")
            self.description["bg"] = "#ffffff"
            self.description["fg"] = self.darkcolor.get()
            self.screen.bgcolor("#ffffff")
            self.pen.color(self.darkcolor.get())
            self.canvas["bg"] = "#ffffff"
            self.hueImgLabel["image"] = self.lighthueImg
            self.darkColorModeButton["background"] = self.lightcolor.get()
            self.darkColorModeButton["foreground"] = self.darkcolor.get()
            self.lightColorModeButton["background"] = self.darkcolor.get()
            self.lightColorModeButton["foreground"] = self.lightercolor.get()
        else:
            self.style.configure(".", background=self.darkcolor.get(), foreground="#ffffff")
            self.style.configure("TLabelframe.Label", foreground=self.lightercolor.get())
            self.style.configure("Control.TLabel", foreground=self.lightercolor.get())
            self.style.map("TButton", background=[("active", self.lightcolor.get())])
            self.style.configure("TEntry", foreground="#ffffff", fieldbackground=self.darkercolor.get())
            self.style.map("TMenubutton", background=[("active", self.lightcolor.get())])
            self.style.configure("Status.TLabel", background=self.darkercolor.get(),
                                 foreground=self.lightercolor.get())
            self.style.configure("Progress.TLabel", background=self.darkercolor.get(),
                                 foreground=self.lightercolor.get())
            self.style.configure("Horizontal.TScale", background="white", troughcolor="#362f36")
            self.description["bg"] = self.darkercolor.get()
            self.description["fg"] = "#ffffff"
            self.screen.bgcolor(self.darkercolor.get())
            self.pen.color(self.lightercolor.get())
            self.canvas["bg"] = self.darkercolor.get()
            self.hueImgLabel["image"] = self.darkhueImg
            self.darkColorModeButton["background"] = self.darkercolor.get()
            self.darkColorModeButton["foreground"] = self.darkcolor.get()
            self.lightColorModeButton["background"] = self.darkcolor.get()
            self.lightColorModeButton["foreground"] = self.lightercolor.get()

    # end hueF

    def colorModeF(self):
        if self.colorModeInt.get() == 1:
            self.style.configure(".", background=self.lightcolor.get(), foreground="#ffffff")
            self.style.configure("TLabelframe.Label", foreground="#ffffff")
            self.style.configure("Control.TLabel", foreground=self.darkcolor.get())
            self.style.map("TButton", background=[("active", self.darkcolor.get())])
            self.style.configure("TEntry", foreground=self.lightcolor.get(), fieldbackground="#ffffff")
            self.style.map("TMenubutton", background=[("active", self.darkcolor.get())])
            self.style.configure("Status.TLabel", background=self.darkcolor.get(), foreground=self.lightercolor.get())
            self.style.configure("Progress.TLabel", background=self.darkcolor.get(), foreground=self.lightercolor.get())
            self.style.configure("Horizontal.TScale", background="#362f36", troughcolor="#ffffff")
            self.description["bg"] = "#ffffff"
            self.description["fg"] = self.darkcolor.get()
            self.screen.bgcolor("#ffffff")
            self.pen.color(self.darkcolor.get())
            self.canvas["bg"] = "#ffffff"
            self.hueImgLabel["image"] = self.lighthueImg
            self.darkColorModeButton["background"] = self.lightcolor.get()
            self.darkColorModeButton["foreground"] = self.darkcolor.get()
            self.lightColorModeButton["background"] = self.darkcolor.get()
            self.lightColorModeButton["foreground"] = self.lightercolor.get()
        else:
            self.style.configure(".", background=self.darkcolor.get(), foreground="#ffffff")
            self.style.configure("TLabelframe.Label", foreground=self.lightercolor.get())
            self.style.configure("Control.TLabel", foreground=self.lightercolor.get())
            self.style.map("TButton", background=[("active", self.lightcolor.get())])
            self.style.configure("TEntry", foreground="#ffffff", fieldbackground=self.darkercolor.get())
            self.style.map("TMenubutton", background=[("active", self.lightcolor.get())])
            self.style.configure("Status.TLabel", background=self.darkercolor.get(), foreground=self.lightercolor.get())
            self.style.configure("Progress.TLabel", background=self.darkercolor.get(),
                                 foreground=self.lightercolor.get())
            self.style.configure("Horizontal.TScale", background="white", troughcolor="#362f36")
            self.description["bg"] = self.darkercolor.get()
            self.description["fg"] = "#ffffff"
            self.screen.bgcolor(self.darkercolor.get())
            self.pen.color(self.lightercolor.get())
            self.canvas["bg"] = self.darkercolor.get()
            self.hueImgLabel["image"] = self.darkhueImg
            self.darkColorModeButton["background"] = self.darkercolor.get()
            self.darkColorModeButton["foreground"] = self.darkcolor.get()
            self.lightColorModeButton["background"] = self.darkcolor.get()
            self.lightColorModeButton["foreground"] = self.lightercolor.get()

    # end colorModeF

    def descriptionF(self, state):
        self.descriptionStr.set(self.fractalDescription[self.fractalNames.index(self.fractalStr.get())])
        self.description.configure(state=tk.NORMAL)
        self.description.delete("1.0", "end")
        self.description.insert("end", self.descriptionStr.get())
        self.description.configure(state=tk.DISABLED)

    # end descriptionF

    def randomOrderF(self):
        if self.fractalStr.get() == self.fractalNames[9]:
            randOrder = str(random.randint(5, 10))
        else:
            randOrder = str(random.randint(2, 5))
        self.orderStr.set(randOrder)

    # end randomOrderF

    def randomLengthF(self):
        if self.fractalStr.get() == self.fractalNames[5] or self.fractalStr.get() == self.fractalNames[9]:
            randLength = str(random.randint(5, 20))
        elif self.fractalStr.get() == self.fractalNames[2]:
            randLength = str(random.randint(10, 60))
        else:
            randLength = str(random.randint(20, 300))
        # endif
        self.lengthStr.set(randLength)

    # end randomOrderF

    def drawF(self):
        # get the values of order and length as int
        self.length = int(float(self.lengthStr.get()))
        self.order = int(float(self.orderStr.get()))

        # get the function name through fractal selection index
        self.fractal = self.fractalFunctionNames[self.fractalNames.index(self.fractalStr.get())]

        # move pen to a better position

        if self.fractal == self.fractalFunctionNames[0] or self.fractal == self.fractalFunctionNames[1]:
            self.pen.up()
            self.pen.backward(self.length)
            self.pen.down()
        # endif

        if self.fractal == self.fractalFunctionNames[2]:
            self.pen.up()
            self.pen.backward(2 * self.length)
            self.pen.down()
        # endif

        if self.fractal == self.fractalFunctionNames[3]:
            self.pen.up()
            self.pen.backward(self.length / 2)
            self.pen.right(90)
            self.pen.backward(self.length / 2)
            self.pen.left(90)
            self.pen.down()
        # endif

        if self.fractal == self.fractalFunctionNames[4] or self.fractal == self.fractalFunctionNames[
            6] or self.fractal == self.fractalFunctionNames[7]:
            self.pen.up()
            self.pen.backward(self.length / 2)
            self.pen.right(90)
            self.pen.forward(self.length / 2)
            self.pen.left(90)
            self.pen.down()
        # endif

        if self.fractal == self.fractalFunctionNames[5]:
            self.pen.up()
            if self.order == 1:
                self.pen.backward(self.length * 1.207)
            else:
                self.pen.backward(self.length * 4.121 * ((2 ** (self.order - 1)) / 2))
            # endif
            self.pen.right(90)
            if self.order == 1:
                self.pen.backward(self.length * 1.914)
            else:
                self.pen.backward(self.length * 4.4745 * ((2 ** (self.order - 1)) / 2))
            # endif
            self.pen.left(90)
            self.pen.down()
        # endif

        if self.fractal == self.fractalFunctionNames[8]:
            self.pen.up()
            self.pen.backward(self.length / 2)
            self.pen.right(90)
            self.pen.forward(1.5388 * self.length / 2)
            self.pen.left(90)
            self.pen.down()
        # endif

        if self.fractal == self.fractalFunctionNames[10]:
            self.pen.up()
            self.pen.backward(self.length)
            self.pen.down()
            self.pen.right(90)
        # endif

        if self.fractal == self.fractalFunctionNames[11] or self.fractal == self.fractalFunctionNames[12]:
            self.pen.up()
            self.pen.backward(self.length * 0.45)
            self.pen.down()
        # endif

        # pen draws fractal
        self.progressStr.set("Drawing...")
        self.fractal(self.order, self.length, self.pen)
        self.progressStr.set("Finished!")

    # end drawF

    def clearF(self):
        # reset the entries using their textvars
        self.lengthStr.set("")
        self.orderStr.set("")
        # reset option menus
        self.fractalStr.set(self.fractalNames[0])
        # reset description
        self.descriptionStr.set(self.fractalDescription[0])
        # clear and reset screen canvas
        self.screen.reset()
        if self.colorModeInt.get() == 1:
            self.pen.color(self.darkercolor.get())
        else:
            self.pen.color(self.lightercolor.get())
        # end if
        self.pen.speed(0)
        self.pen.width(1)
        # reset the status bar
        self.progressStr.set("Waiting on Selection...")

    # end clearF

    def centerApplication(self):
        w = 915
        h = 642
        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()
        appPosX = (screenWidth - w) / 2
        appPosY = (screenHeight - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, appPosX, appPosY))
    # end centerApplication


# end class


def main():
    root = tk.Tk()
    app = TurtleGenerator(root)
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
