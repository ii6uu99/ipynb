import turtle as t

class MyTurtle(t.Turtle):
	def big_circle(self):
		self.color('red')
		self.circle(100)

s = t.Screen()
t = MyTurtle()
t.big_circle()

s.mainloop()
