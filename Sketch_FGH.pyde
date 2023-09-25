def setup():
    size(500,500)
    colorMode(HSB)
    #colorMode(RGB)
  
def draw():
    # Greyscale
    # RGB
    # RGBA
    background(0) 
    
    f = 10.0
    g = 20.0
    h = 5
    
    #adding
    f = f + 1
    f += 1
    
    #subtracting
    g -= 30
    g = g - 27
    
    #multiplying
    
    g = f * h
    h *= 2
    
    #divide
    
    g = f / h
    h = h / 2.5
    
    f = pow(g, 2)
    
    h = h - 7
    g *= f
    f *= g
    h = f - (g +5)
    
    
    println("f: " + str(f))
    println("g: " + str(g))
    println("h: " + str(h))
    
    #Variable scope
    
    stroke(80,255,255)
    line(mouseX,10,100,mouseY)
    
    rectMode(CORNERS)
    rect(20,20,50,100)
    # first two values is point on 1st corner
    noStroke()
    circle(100,mouseX,5)
    fill(90,mouseY / 2,255)
    ellipse(200,200,100,10)
    point(90,100)
    
