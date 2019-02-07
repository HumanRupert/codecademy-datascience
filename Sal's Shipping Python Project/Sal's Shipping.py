try:
    pack = int(input("W: "))
except ValueError:
    print ('Please enter a NUMBER')
    try:
        pack = int(input("W: "))
    except ValueError:
        print ('Please enter a NUMBER')
        try:
            pack = int(input("W: "))
        except ValueError:
            print ('GO OUT!')

### GROUND SHIPPING
def gs(weight):
  cost = 20
  if weight <= 2:
    cost += 1.5 * weight
  elif weight > 2 and weight <= 6:
    cost += 3.0 * weight
  elif weight > 6 and weight <= 10:
    cost += 4.0 * weight
  else:
    cost += 4.75 * weight
  return cost

### GROUND SHIPPING
def pgs(weight):
  cost = 145.0
  if weight <= 2:
    cost += 1.5 * weight
  elif weight > 2 and weight <= 6:
    cost += 3.0 * weight
  elif weight > 6 and weight <= 10:
    cost += 4.0 * weight
  else:
    cost += 4.75 * weight
  return cost

### Drone SHIPPING
def ds(weight):
  cost = 0
  if weight <= 2:
    cost += 4.5 * weight
  elif weight > 2 and weight <= 6:
    cost += 9.0 * weight
  elif weight > 6 and weight <= 10:
    cost += 12.0 * weight
  else:
    cost += 14.25 * weight
  return cost

### MOST ECONOMIC OPTION
def economic(ground, premium, drone):
    costs = [ground, premium, drone]
    return min(costs)

### VARIABLES
ground = gs(pack)
premium = pgs(pack)
drone = ds(pack)
economic = economic(ground, premium, drone)
economic_name = ''
if economic == ground:
    economic_name = 'ground shipping'
elif economic == drone:
    economic_name  = 'drone shipping'
elif economic == premium:
    economic_name = 'premium ground shipping'


### PRINT RESULTS
print ("""The cost of the ground shipping is %1.1f, the cost of the premium ground shipping is %1.1f, and the cost of the drone shipping is %1.1f.
The most economic option is %s which costs: %1.1f""" % (ground, premium, drone, economic_name, economic))


### PREFER
try:
    choice = int(input("PLEASE CHOOSE YOUR SHIPPING PLAN: ENTER 1 FOR GROUND SHIPPING, 2 FOR PREMIUM SHIPPING, AND 3 FOR DRONE SHIPPING: "))
except ValueError:
    print ("PLEASE CHOOSE YOUR SHIPPING PLAN: ENTER 1 FOR GROUND SHIPPING, 2 FOR PREMIUM SHIPPING, AND 3 FOR DRONE SHIPPING: ")
    try:
        choice = int(input("PLEASE CHOOSE YOUR SHIPPING PLAN: ENTER 1 FOR GROUND SHIPPING, 2 FOR PREMIUM SHIPPING, AND 3 FOR DRONE SHIPPING: "))
    except ValueError:
        print ("PLEASE CHOOSE YOUR SHIPPING PLAN: ENTER 1 FOR GROUND SHIPPING, 2 FOR PREMIUM SHIPPING, AND 3 FOR DRONE SHIPPING: ")
turns = 0
while turns < 3:
    if choice ==1:
        print ("YOU'VE CHOSEN GROUND SHIPPING")
        turns +=10
    elif choice == 2:
        print("YOU'VE CHOSEN PREMIUM GROUND SHIPPING")
        turns +=10
    elif choice == 3:
        print("YOU'VE CHOSEN DRONE SHIPPING")
        turns +=10
    else:
        print ("INVALID RANGE!")
        turns +=1
        choice = int(input("PLEASE CHOOSE YOUR SHIPPING PLAN: ENTER 1 FOR GROUND SHIPPING, 2 FOR PREMIUM SHIPPING, AND 3 FOR DRONE SHIPPING: "))

        
        
           


