from os import write
from turtle import title
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class OpeningScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        title = Text("What are Scalars and Vectors?", font_size=48, color=WHITE)
        
        # Center the title on the screen
        title.move_to(ORIGIN)
        with self.voiceover(text="Hey there, future physicists! Today we're diving into Scalars and Vectors. ") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        # Fade in the title
         # Display for 2 seconds
        
        self.play(FadeOut(title))
       



        title = Text("Scalars And Vector", font_size=60, color=WHITE)
          # Shift the title upwards
          # Center the title on the screen

        
        # Fade in the title
        self.play(Create(title) )
        self.wait(2)
          
        
        # Fade out the title
        self.play(FadeOut(title))
        
        # Transition to a different design
        self.wait(1)

        circle = Circle(radius=2, color=BLUE)
        center_dot = Dot(color=RED).move_to(circle.get_center())

        self.play(Create(circle), Create(center_dot))
        
        circle_name = Text("Scalar having magnitude\n But not Specified Direction", font_size=24)
        circle_name.next_to(circle, DOWN, buff=0.5)
        self.play(Create(circle_name))

        # Draw a random line (scalar) from the center to the circumference
        random_line = Line(circle.get_center(), circle.point_from_proportion(np.random.random()), color=YELLOW)
       
        
         # Draw a random line (scalar) from the center to the circumference
        random_line1 = Line(circle.get_center(), circle.point_from_proportion(np.random.random()), color=YELLOW)
        
      
         # Draw a random line (scalar) from the center to the circumference
        random_line2 = Line(circle.get_center(), circle.point_from_proportion(np.random.random()), color=YELLOW)
        
         # Draw a random line (scalar) from the center to the circumference
        random_line3 = Line(circle.get_center(), circle.point_from_proportion(np.random.random()), color=YELLOW)
        line = VGroup(random_line,random_line1,random_line2,random_line3)
        with self.voiceover(text="Scalar having magnitude But not have Direction like east west south and north") as tracker:
            self.play(FadeIn(line), run_time=tracker.duration)
        
        circle_name1 = Text("Vector having magnitude and Specified Direction\n(East,nort,west and south)", font_size=24)
        circle_name1.next_to(circle, DOWN, buff=0.5)
        self.play(Transform(circle_name,circle_name1))
           # Draw a specific line (vector) at 0 degrees (east)
        vector_line = Arrow(  # Use the Arrow class to add an arrowhead
            circle.get_center(),
            circle.point_at_angle(0),
            color=GREEN

        )
       
        # Draw a line at 90 degrees (north) with an arrowhead
        vector_line_90 = Arrow(
            circle.get_center(),
            circle.point_at_angle(np.deg2rad(90)),
            color=GREEN
        )
       
        

        # Draw a line at 180 degrees (west) with an arrowhead
        vector_line_180 = Arrow(
            circle.get_center(),
            circle.point_at_angle(np.deg2rad(180)),
            color=GREEN
        )
       

        # Draw a line at 270 degrees (south) with an arrowhead
        vector_line_270 = Arrow(
            circle.get_center(),
            circle.point_at_angle(np.deg2rad(270)),
            color=GREEN
        )
        vector = VGroup(vector_line,vector_line_90,vector_line_180,vector_line_270)
        with self.voiceover(text="vector having magnitude and also specified Direction like east west south and north") as tracker:
            self.play(Transform(line,vector), run_time=tracker.duration)
        
    
        self.play(FadeOut(line,circle_name,circle,center_dot))

        


        title = Text("Scalars Example", font_size=60, color=WHITE)
        with self.voiceover(text="some of scalar quantity example are:") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.play(title.animate.shift(UP*2).scale(0.8))
        self.wait(1)
        self.play(FadeOut(title))
        # Create thermometer image
        thermometer = ImageMobject("thermometer.png.png")
        thermometer.scale(0.5)
       
        
        # Create speedometer image
        speedometer = ImageMobject("speedometer.png")
        speedometer.scale(2)
       
        
        # Create weight scale image
        weight_scale = ImageMobject("weight-scale.png")
        weight_scale.scale(0.5)
       
        # Display the images
        self.add((thermometer))
        # Display for 2 seconds
        
        # Animate the thermometer
        self.play(thermometer.animate.shift(UP*1.5).scale(1.2))
        narration_text = Text("Thermometer", font_size=30)
        narration_text.next_to(thermometer, DOWN, buff=1)
        with self.voiceover(text="Thermometer") as tracker:
            self.play(Write(narration_text), run_time=tracker.duration)
       
         # Fade everything away
        
        self.play(FadeOut(thermometer,narration_text))
        self.add((speedometer))
        
        
        # Animate the speedometer
        self.play(speedometer.animate.shift(UP*1.5).scale(1.5))
        narration_text = Text("Speedometer", font_size=30)
        narration_text.next_to(speedometer, DOWN, buff=1)
        with self.voiceover(text="speedometer") as tracker:
            self.play(Write(narration_text), run_time=tracker.duration)
       
         # Fade everything away
    
        self.play(FadeOut(speedometer,narration_text))
        self.add((weight_scale))
        
        # Animate the weight scale
        self.play(weight_scale.animate.shift(UP*1.5).scale(1.2))
        narration_text = Text("Weight Scale", font_size=30)
        narration_text.next_to(weight_scale, DOWN, buff=1)
        with self.voiceover(text="Weight scale") as tracker:
            self.play(Write(narration_text), run_time=tracker.duration)
         # Fade everything away
        
        self.play(FadeOut(weight_scale,narration_text))
       

        # Text "Vectors" with popping animation
        vectors_text = Text("Vectors", font_size=72)
        with self.voiceover(text="Introduction to vector") as tracker:
            self.play(Write(vectors_text), run_time=tracker.duration)
        self.play(vectors_text.animate.shift(UP*2).scale(0.8))
        

        # Create arrows forming around the text
        arrows = VGroup(*[Arrow(ORIGIN, 0.5 * RIGHT) for _ in range(8)])
        arrows.arrange( buff=0.5)
        arrows.next_to(vectors_text, DOWN, buff=0.5)
        self.play(Create(arrows))

        # Narration
        narration_text = Text("Vectors, on the other hand, are a bit more demanding.\nThey have both magnitude and direction.", font_size=24)
        narration_text.next_to(vectors_text, DOWN, buff=1)
        with self.voiceover(text="Vectors, on the other hand, are a bit more demanding.They have both magnitude and direction.") as tracker:
            self.play(Write(narration_text), run_time=tracker.duration)
         # Fade everything away
        self.wait(1)
        self.play( FadeOut(vectors_text), FadeOut(narration_text))
       
        # Create points A and B
        point_a = Dot(point=LEFT, color=BLUE)
        point_b = Dot(point=RIGHT, color=BLUE)
        label_a = Text("A", color=WHITE).next_to(point_a, DOWN)
        label_b = Text("B", color=WHITE).next_to(point_b, DOWN)

        # Create an arrow from A to B with a label
        arrow = Arrow(point_a.get_center(), point_b.get_center(), buff=0.1, color=YELLOW)
        distance_label = always_redraw(lambda:MathTex(r"\vec{AB}").next_to(arrow, UP))

        # Show everything
        self.play(Create(point_a), Create(point_b), Write(label_a), Write(label_b))
        self.play(Create(arrow), Write(distance_label))

        # You can animate the arrow as desired
        self.play(FadeOut(label_a),FadeOut(label_b),FadeOut(point_a),FadeOut(point_b))
        self.play(arrow.animate.shift(2 * RIGHT))
        self.play(FadeOut(arrow,distance_label))
        


        # Text description
        description = Text(" Vector Examples", font_size=36)
        with self.voiceover(text="some of example of vector are:") as tracker:
            self.play(Write(description), run_time=tracker.duration)
        self.play(description.animate.shift(UP*2),run_time=2)
        

        # Create a list of wind flows
        wind_flows = VGroup()
        num_wind_flows = 5  # Number of wind flows

        # Calculate the speed of all wind flows
        wind_speed = 3  # Speed of all wind flows

        for _ in range(num_wind_flows):
            wind = Arrow(LEFT, RIGHT, color=BLUE, buff=0.1)
            wind.next_to(wind_flows, DOWN, buff=0.2)
            wind_flows.add(wind)
# Narration with the common speed
        narration = Text(f" Wind Flows in the East Direction\nSpeed: {wind_speed} m/s", font_size=24)
        narration.next_to(wind_flows, UP, buff=0.5)
        with self.voiceover(text="wind flows in specified direction") as tracker:
            self.play(Write(narration), run_time=tracker.duration)
        

        self.wait(1)
        # Set initial positions to the left of the screen
        wind_flows.shift(LEFT * 2)

        # Animate the wind flows to move to the right (east)
        self.play(wind_flows.animate.shift(RIGHT * 5), run_time=3)

        

        # Fade out
        self.play(FadeOut(wind_flows), FadeOut(narration))


        # Create a dot (target)
        dot = Dot(color=RED, radius=0.1)
        dot.shift(RIGHT * 2)  # Position the dot to the right

       

        # Title
        title = Text("Arrow Shot in a Circular Dot", font_size=24)
        title.next_to(description,DOWN)

        # Speed information
        speed_info = MathTex(r"\text{Speed:} \, 5 \, \text{m/s} \, \text{East}", font_size=28)
        speed_info.next_to(title, DOWN, buff=0.5)

        # Group the title, speed information, and dot
        title_group = VGroup(title, speed_info, dot)

        # Show the title, speed information, and dot
        with self.voiceover(text="Arrow moving toward target") as tracker:
            self.play(Write(title_group), run_time=tracker.duration)
        
        # Create an arrow
        arrow = Arrow(LEFT, RIGHT, color=GREEN)
        arrow.scale(1.5)  # Scale the arrow size

        # Set the initial position of the arrow at the left side
        arrow.move_to(LEFT * 5)

        # Calculate the final position of the arrow
        final_position = dot.get_center() + dot.radius * RIGHT
        arrow_end = arrow.get_end()
        move_vector = final_position - arrow_end

        self.wait(2)
         # Animate the arrow to move to the dot (target) without exceeding it
        self.play(arrow.animate.shift(move_vector), run_time=2)

        # Fade out
        self.play(FadeOut(arrow), FadeOut(title_group,title,speed_info,description))


        
        vectors_text = Text("Notation Difference" )
        self.play(Create(vectors_text))
        self.play(vectors_text.animate.shift(UP*3),run_time=2)
        # Create a straight line labeled as "Magnitude"
        magnitude_label = Text("Magnitude\n (Scalar)", font_size=26)
        magnitude_line = Line(LEFT, RIGHT, color=BLUE)
        magnitude_label.next_to(magnitude_line, DOWN)

        
        # Create a custom arrowhead on the same line
        direction_label = Text("Direction (Vector)", font_size=26)
        direction_arrowhead =  Arrow(color=RED)
        
        
        # Create a new label "Magnitude with Direction (Vector Quantity)"
        magnitude_with_direction_label = Text("Magnitude with Direction\n (Vector Quantity)", font_size=26)
        magnitude_with_direction_label.next_to(direction_arrowhead, DOWN)
        
       
        
        # Display the elements
        self.play(Create(magnitude_line))
        
        with self.voiceover(text="the line represent the numerical value called magnitude") as tracker:
            self.play(Write(magnitude_label), run_time=tracker.duration)
        
        self.wait(1)
        with self.voiceover(text=" arrow represent the direction") as tracker:
            self.play(Transform(magnitude_label, magnitude_with_direction_label), run_time=tracker.duration)
        
        
        # Add animation to the arrowhead, decrease the font size of the text, and fade away the old label
        self.play(

           Transform(magnitude_line,direction_arrowhead)
        )
        self.wait(1)
        self.play(FadeOut(magnitude_line,magnitude_label,vectors_text))

        vectors_text = Text("Scalar Addition")
        with self.voiceover(text="Scalar addition is a algerabic addition") as tracker:
            self.play(vectors_text.animate.shift(UP*2), run_time=tracker.duration)
    
        self.wait(2)
        # Create text objects
        text_1 = Text("5 kilogram", color=WHITE).shift(LEFT*3)
        plus_sign = Text("+", color=WHITE).next_to(text_1,RIGHT)
        text_2 = Text("3 kilogram", color=WHITE).next_to(plus_sign,RIGHT)
        equal = Text("=").next_to(text_2,RIGHT)
        result = Text("8 kilogram", color=WHITE).next_to(equal, RIGHT)

        # Display the text objects
        self.play(Write(text_1), Write(text_2))
        self.wait(1)
        self.play(Write(plus_sign), Write(equal))
        self.wait(1)
        self.play(Write(result))
        self.wait(1)
        self.play(FadeOut(plus_sign,equal,result,text_1,text_2,vectors_text))

      


        vectors_text = Text("Vector Addition")
        with self.voiceover(text="Addition of vector A and B is:") as tracker:
            self.play(vectors_text.animate.shift(UP*3), run_time=tracker.duration)

        
        
        # Create two vectors
        vector1 = Vector(2 * RIGHT, color=BLUE)
        vector2 = Vector(UP, color=GREEN)

        # Label the vectors
        label1 = MathTex("\\vec{A}", color=BLUE)
        label2 = MathTex("\\vec{B}", color=GREEN)

        # Position the vectors and labels
        vector1.next_to(ORIGIN, LEFT)
        vector2.next_to(ORIGIN, UP)
        label1.next_to(vector1, LEFT)
        label2.next_to(vector2, UP)

        # Create the result vector (addition of vector1 and vector2)
        result_vector = Vector(vector1.get_vector() + vector2.get_vector(), color=ORANGE).shift(LEFT*2.3,UP*0.2)
        label_result = MathTex("\\vec{A} + \\vec{B}", color=ORANGE)
        label_result.next_to(result_vector, UP)

        # Show the vectors and labels
        self.play(Create(vector1), Create(vector2))
        self.play(Write(label1), Write(label2))
        self.wait(1)
        with self.voiceover(text="In vector addition, the resultant vector is equal to the tail of first vector to the tip of second vector.") as tracker:
            self.play(Create(result_vector), run_time=tracker.duration)
        # Show the result vector and label
        with self.voiceover(text="line represent resultant magnititude and arrow represent direction") as tracker:
            self.play(Write(label_result), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(label1),FadeOut(label2),FadeOut(label_result),FadeOut(vector1),FadeOut(vector2),FadeOut(result_vector),FadeOut(vectors_text),run_time = 2)




        vectors_text = Text("Scalar Multiplication")
        self.play(Create(vectors_text))
        self.play(vectors_text.animate.shift(UP*3),run_time=2)
        self.wait(1)
        
        # Create a vector
        original_vector = Arrow(start=ORIGIN, end=4*RIGHT, color=BLUE)
        original_label = Tex("2 unit ,east", color=BLUE).next_to(original_vector, UP)
        narration1 = Text("On multiple the above vector with scalar 2 unit", font_size=24)

      
        # Show the original vector and label
        self.play(Create(original_vector), Write(original_label))
        narration1.next_to(original_vector, DOWN)
        
       
        with self.voiceover(text=" On multiple the above vector with scalar 2 unit") as tracker:
            self.play(Write(narration1), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(narration1))
        # Apply scalar multiplication
        scalar = 3
        stretched_vector = Arrow(start=ORIGIN, end=scalar*2*RIGHT, color=RED)
        stretched_label = Tex("4 unit,east", color=RED).next_to(stretched_vector, UP)

        # Show the stretched vector and label
        self.play(Transform(original_vector, stretched_vector), Transform(original_label, stretched_label))

        # Add narration
        narration = Text("You can stretch vectors\nby multiplying them with scalars.", font_size=24)
        narration.next_to(stretched_vector, DOWN)
       
       
        with self.voiceover(text=" vector magnitude increase by 2 times") as tracker:
            self.play(Write(narration), run_time=tracker.duration)

        self.wait(1)
        self.play(FadeOut(narration))
        # Apply scalar multiplication
        scalar = 1
        stretched_vector = Arrow(start=ORIGIN, end=scalar*2*RIGHT, color=RED)
        stretched_label = Tex("1 unit,east", color=RED).next_to(stretched_vector, UP)

        # Show the stretched vector and label
        self.play(Transform(original_vector, stretched_vector), Transform(original_label, stretched_label))

        # Add narration
        narration = Text("You can decrease vectors magnitude\nby multiplying them with scalars between 0 to 1.", font_size=24)
        narration.next_to(stretched_vector, DOWN)
      
        with self.voiceover(text=" similarly, vector magnitude decrease by multiplying them with scalars between 0 to 1 ") as tracker:
            self.play(Write(narration), run_time=tracker.duration)

        self.wait(1)
        self.play(FadeOut(vectors_text,narration,stretched_label,original_vector,original_label))

        # Create a vector
        vector = Arrow(start=ORIGIN, end=3*RIGHT, color=BLUE)

        # Show the original vector
        self.play(Create(vector))
        narration = Text("Multiplying by a negative scalar", font_size=24)
        narration.next_to(vector, DOWN)
   
        with self.voiceover(text=" Its direction change in opposite direction ") as tracker:
            self.play(Write(narration), run_time=tracker.duration)
        
        self.wait(1)
        self.play(FadeOut(narration))

        # Apply negative scalar multiplication
        negative_scalar = -1
        flipped_vector = Arrow(start=ORIGIN, end=negative_scalar*3*RIGHT, color=RED)

        # Show the flipped vector
        self.play(Transform(vector, flipped_vector))

        # Add narration
        narration = Text("That'll flip your vector the other way!", font_size=24)
        narration.next_to(flipped_vector, DOWN)
        with self.voiceover(text="  on multiply by negative scalar ") as tracker:
            self.play(Write(narration), run_time=tracker.duration)

        self.wait(1)
        self.play(FadeOut(vector,narration))
     


        # Create two vectors with the same magnitude but different directions
        vector1 = Arrow(start=ORIGIN, end=2*RIGHT, color=BLUE)
        vector2 = Arrow(start=ORIGIN, end=2*UP, color=GREEN)

        # Show the vectors
        self.play(Create(vector1))
        self.play(Create(vector2))
        

        # Add narration
        narration = Text("Remember, direction matters in vectors.\nSame magnitude but different directions means they're different vectors.", font_size=24)
        narration.next_to(ORIGIN, DOWN,buff=2)
        with self.voiceover(text=" Same magnitude but different directions means they're different vectors. ") as tracker:
            self.play(Write(narration), run_time=tracker.duration)
        self.play(Write(narration))

        self.wait(2)
        self.play(FadeOut(narration,vector1,vector2))
        self.play(Create(vector1))
        narration = Text(" blue vector represent \n you are moving in a east direction with some magnitude", font_size=24)
        narration.next_to(vector1, DOWN,buff=2)
        with self.voiceover(text=" This blue vector represent  you are moving in a east direction with some magnitude") as tracker:
            self.play(Write(narration), run_time=tracker.duration)
        self.play(FadeOut(narration,vector1))
        self.play(Create(vector2))
        narration = Text("This yellow vector represent \n you are moving in a north direction with same magnitude", font_size=24)
        narration.next_to(vector2, DOWN,buff=2)
        with self.voiceover(text="yellow vector represent you are moving in a north direction with same magnitude") as tracker:
            self.play(Write(narration), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(narration,vector2))
       
 
