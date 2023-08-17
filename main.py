from manim import *

class BlockID(ThreeDScene):
    def construct(self):
        # Create cube 27 times larger than default size
        cube = Cube(side_length=3)

        # rotate camera to view cube from different angle
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Create array of squares within the cube
        squares = VGroup()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    square = Square(side_length=0.8).shift([k-1, j-1, i-1])
                    squares.add(square)

        # create cube instantly
        self.add(cube)
        self.play(Create(squares))

        # show length of cube
        self.wait(2)
        text1 = MathTex("GridDim.x").shift(cube.get_center() + [0, -2, -2])
        text2 = MathTex("GridDim.y").shift(cube.get_center() + [2, 0, -2]).rotate(PI/2)
        text3 = MathTex("GridDim.z").shift(cube.get_center() + [2, 2, 0]).rotate(PI/2, axis=[1, 0, 0]).rotate(-PI/2, axis=[0, 1, 0])
        self.play(Write(text1), Write(text2), Write(text3))

        # rotate camera to view cube top
        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES)
        self.wait(1)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(1)

        # display text for square 15 at the top of the screen facing the camera
        text4 = Text("Block at (2,1,1)").shift([0, 3, 0])
        self.add_fixed_in_frame_mobjects(text4)
        # self.play(Write(text4))

        # change "(2,1,1)" and corresponding square to red
        self.play(text4[-7:].animate.set_color(RED), squares[14].animate.set_color(RED))

        texts = VGroup()
        for i, square in enumerate(squares):
            texts.add(MathTex(str(i)).shift(square.get_center()))
        self.play(Write(texts))

        # hide text1-3
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(texts), FadeOut(text4))

        formula = Text("Block ID = 14").scale(0.6).rotate(PI/2, axis = [1, 0, 0]).rotate(PI/4, axis = [0, 0, 1]).shift([-3, 3, -5])
        self.play(Write(formula))
        self.wait(1)

        formula2 = Text("Block ID = 9 + 3 + 2").scale(0.6).rotate(PI/2, axis = [1, 0, 0]).rotate(PI/4, axis = [0, 0, 1]).shift([-3, 3, -5.5])
        self.play(ReplacementTransform(formula, formula2))
        self.wait(1)

        color1 = YELLOW

        # make a copy of squares 0-8 and convert them to the formula in fixed frame
        self.play(formula2[8:9].animate.set_color(color1), squares[:9].animate.set_color(color1))
        squares2 = squares[:9].copy()
        self.wait(0.5)
        self.play(ReplacementTransform(squares2, formula2[8:9]))

        self.play(FadeIn(text1), FadeIn(text2))
        formula3 = Text("Block ID = BlockIdx.z * GridDim.x * GridDim.y + 3 + 2").scale(0.6).rotate(PI/2, axis = [1, 0, 0]).rotate(PI/4, axis = [0, 0, 1]).shift([-3, 3, -5.5])
        # setcolor of formula3 to red
        formula3[8:38].set_color(color1)
        text1copy = text1.copy()
        text2copy = text2.copy()
        self.play(ReplacementTransform(text1copy, formula3[19:28]), ReplacementTransform(text2copy, formula3[29:38]), ReplacementTransform(formula2, formula3))
        self.wait(1)
        self.play(FadeOut(text1), FadeOut(text2), squares[:9].animate.set_color(WHITE), formula3.animate.set_color(WHITE))

        color2 = YELLOW

        self.play(formula3[39:40].animate.set_color(color2), squares[9:12].animate.set_color(color2))
        squares2 = squares[9:12].copy()
        self.wait(0.5)
        self.play(ReplacementTransform(squares2, formula3[39:40]))

        self.play(FadeIn(text1))
        formula4 = Text("Block ID = BlockIdx.z * GridDim.x * GridDim.y + BlockIdx.y * GridDim.x + 2").scale(0.6).rotate(PI/2, axis = [1, 0, 0]).rotate(PI/4, axis = [0, 0, 1]).shift([-3, 3, -5.5])
        formula4[39:59].set_color(color2)
        text1copy = text1.copy()
        self.play(ReplacementTransform(text1copy, formula4[50:59]), ReplacementTransform(formula3, formula4))
        self.wait(1)
        self.play(FadeOut(text1), squares[9:12].animate.set_color(WHITE), formula4.animate.set_color(WHITE))

        color3 = YELLOW

        self.play(formula4[60:61].animate.set_color(color3), squares[12:14].animate.set_color(color3))
        squares2 = squares[12:14].copy()
        self.wait(0.5)
        self.play(ReplacementTransform(squares2, formula4[60:61]))
        
        formula5 = Text("Block ID = BlockIdx.z * GridDim.x * GridDim.y + BlockIdx.y * GridDim.x + BlockIdx.x").scale(0.6).rotate(PI/2, axis = [1, 0, 0]).rotate(PI/4, axis = [0, 0, 1]).shift([-3, 3, -5.5])
        formula5[60:80].set_color(color3)
        self.play(ReplacementTransform(formula4, formula5))
        self.wait(1)
        self.play(squares[12:14].animate.set_color(WHITE), formula5.animate.set_color(WHITE))

        self.wait(1)

class ThreadID(Scene):
    def construct(self):
        # draw a rectangle with 12 vertical lines inside it
        rectangle = Rectangle(height=3, width=4)
        squiggles = VGroup()
        for i in range(3):
            for j in range(4):
                squiggle = ParametricFunction(lambda t: np.array([np.sin(5*t)/60, t/6, 0]), t_range=[0, PI], color=WHITE)
                squiggle.shift([j-1.5, -i+0.75, 0])
                squiggles.add(squiggle)
        self.play(Create(rectangle), Create(squiggles))
        self.wait(1)

        
        text3 = Text("BlockId = 14").shift([0, 3, 0]).scale(0.8)
        self.play(Write(text3))

        text1 = MathTex("BlockDim.x").shift([0, 2, 0]).scale(0.8)
        text2 = MathTex("BlockDim.y").shift([-2.5, 0, 0]).rotate(PI/2).scale(0.8)

        self.play(Write(text1), Write(text2))
        
        self.play(FadeOut(text3), FadeOut(text1), FadeOut(text2))

        text4 = Text("Thread at position (2, 2)").shift([0, 3, 0]).scale(0.6)
        self.play(Write(text4))
        self.play(text4[16:21].animate.set_color(RED), squiggles[10].animate.set_color(RED))
        self.wait(1)
        # self.play(FadeOut(text4))

        formula = Text("Local Thread ID = 10").shift([0, -2.5, 0]).scale(0.6)
        self.play(Write(formula))

        formula2 = Text("Local Thread ID = 8 + 2").shift([0, -2.5, 0]).scale(0.6)
        self.play(ReplacementTransform(formula, formula2))
        self.wait(1)

        self.play(formula2[14:15].animate.set_color(YELLOW), squiggles[:8].animate.set_color(YELLOW))
        squiggles2 = squiggles[:8].copy()
        self.wait(0.5)
        self.play(ReplacementTransform(squiggles2, formula2[14:15]))
        self.wait(1)

        self.play(FadeIn(text1))
        text1copy = text1.copy()
        formula3 = Text("Local Thread ID = ThreadIdx.y * BlockDim.x + 2").shift([0, -2.5, 0]).scale(0.6)
        formula3[14:36].set_color(YELLOW)
        self.play(ReplacementTransform(formula2, formula3), ReplacementTransform(text1copy, formula3[26:36]))
        self.wait(1)
        self.play(FadeOut(text1), squiggles[:8].animate.set_color(WHITE), formula3.animate.set_color(WHITE))


        self.play(formula3[37:38].animate.set_color(YELLOW), squiggles[8:10].animate.set_color(YELLOW))
        squiggles2 = squiggles[8:10].copy()
        self.wait(0.5)
        self.play(ReplacementTransform(squiggles2, formula3[37:38]))
        self.wait(1)

        formula4 = Text("Local Thread ID = ThreadIdx.y * BlockDim.x + ThreadIdx.x").shift([0, -2.5, 0]).scale(0.6)
        formula4[37:59].set_color(YELLOW)
        self.play(ReplacementTransform(formula3, formula4))
        self.wait(1)
        self.play(squiggles[8:10].animate.set_color(WHITE), formula4.animate.set_color(WHITE))

        self.play(FadeIn(text3), FadeOut(rectangle), FadeOut(squiggles), formula4.animate.shift([0, 2.5, 0]))

        text3copy = text3[:-2].copy()
        formula4copy = formula4[:13].copy()
        text5 = Text("Global Thread ID = BlockId * BlockDim.x * BlockDim.y * BlockDim.z + Local Thread ID").shift([0, -2, 0]).scale(0.4)
        self.play(Write(text5), ReplacementTransform(text3copy, text5[10:15]), ReplacementTransform(formula4copy, text5[31:]))
        self.wait(1)
