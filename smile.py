import turtle

bot = turtle.Turtle()

bot.up()
bot.goto(0,-100)
bot.down()

bot.begin_fill()
bot.pendown()
bot.fillcolor('yellow')
bot.circle(100)
bot.end_fill()

bot.up()
bot.goto(-67,-40)
bot.setheading(-60)
bot.width(5)
bot.down()
bot.circle(80,120)
bot.fillcolor('black')

for i in range(-35,105,70):
    bot.up()
    bot.goto(i,35)
    bot.setheading(0)
    bot.down()
    bot.begin_fill()
    bot.circle(10)
    bot.end_fill()
bot.penup()
bot.goto(0,-150)

turtle.mainloop()