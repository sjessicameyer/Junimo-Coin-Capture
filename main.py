import turtle, random, time

t_time = turtle.Turtle()
t_time.up()
t_time.hideturtle()
t_time.goto(0, 150)
start = time.time()

sc = turtle.Screen()
sc.setup(400, 400)
sc.title("Junimo Coin Capture")
sc.bgpic("grass.gif")
sc.bgcolor("green")
sc.register_shape("coin.gif")
sc.register_shape("junimo.gif")
sc.tracer(0)

jeffrey = turtle.Turtle()
jeffrey.shape("junimo.gif")
jeffrey.up()
jeffrey.speed(0)

mariocoin = turtle.Turtle()
mariocoin.shape("coin.gif")
mariocoin.up()
mariocoin.hideturtle()

all_coins = []
def random_coin():
  global all_coins
  new_coin = mariocoin.clone()
  new_coin.showturtle()
  randx = random.randint(-190, 190)
  randy = random.randint(-190, 190)
  new_coin.goto(randx, randy)
  all_coins.append(new_coin)

for i in range(20):
  random_coin()

score = 0
sk = turtle.Turtle()
sk.ht()
sk.up()
sk.goto(-180, 160)
def display_score():
  sk.clear()
  sk.write(f"Coins: {score}", align = "left", font=("Courier", 15, "normal"))

def detect_coin():
  global score
  for c in all_coins:
    if jeffrey.distance(c) < 30:
      all_coins.remove(c)
      c.hideturtle()
      random_coin()
      score +=  1
      display_score()

def up():
  jeffrey.sety(jeffrey.ycor()+10)
  detect_coin()
  sc.update()
def down():
  jeffrey.sety(jeffrey.ycor()-10)
  detect_coin()
  sc.update()
def left():
  jeffrey.setx(jeffrey.xcor()-10)
  detect_coin()
  sc.update()
def right():
  jeffrey.setx(jeffrey.xcor()+10)
  detect_coin()
  sc.update()

sc.listen()
sc.onkey(up, "Up")
sc.onkey(down, "Down")
sc.onkey(left, "Left")
sc.onkey(right, "Right")
sc.update()
display_score()

limit = 60
while (time.time() - start) < limit:
  seconds = int(limit - (time.time() - start))
  t_time.clear()
  t_time.write(f"{seconds}", align="center", font = ("Courier", 15, "normal"))
  sc.update()

sc.onkey(None, "Up")
sc.onkey(None, "Down")
sc.onkey(None, "Left")
sc.onkey(None, "Right")

t_time.goto(0,0)
t_time.color("red")
t_time.write("GAMEOVER!", align="center", font=("Courier", 20, "bold"))
