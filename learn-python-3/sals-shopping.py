# for 41.5 pounds

weight = 41.5

# groundshipping

if weight <= 2:
  cost_ground = (weight*1.5 + 20.00)
elif 2 < weight <= 6:
  cost_ground = (weight*3.00 + 20.00)
elif 6 < weight <= 10:
  cost_ground = (weight*4.00 + 20.00)
else:
  cost_ground = (weight*4.75 + 20.00)
print("Ground Shipping: $", cost_ground)

# groundshippingpremium

cost_ground_premium = 125.00
print("Ground Shipping Premium: $", cost_ground_premium)

# droneshipping

if weight <= 2:
  cost_drone = (weight*4.50)
elif 2 < weight <= 6:
  cost_drone = (weight*9.00)
elif 6 < weight <= 10:
  cost_drone = (weight*12.00)
else:
  cost_drone = (weight*14.25)
print("Drone Shipping: $", cost_drone)

# for 4.8 pounds

weight = 4.8

# groundshipping

if weight <= 2:
  cost_ground = (weight*1.5 + 20.00)
elif 2 < weight <= 6:
  cost_ground = (weight*3.00 + 20.00)
elif 6 < weight <= 10:
  cost_ground = (weight*4.00 + 20.00)
else:
  cost_ground = (weight*4.75 + 20.00)
print("Ground Shipping: $", cost_ground)

# groundshippingpremium

cost_ground_premium = 125.00
print("Ground Shipping Premium: $", cost_ground_premium)

# droneshipping

if weight <= 2:
  cost_drone = (weight*4.50)
elif 2 < weight <= 6:
  cost_drone = (weight*9.00)
elif 6 < weight <= 10:
  cost_drone = (weight*12.00)
else:
  cost_drone = (weight*14.25)
print("Drone Shipping: $", cost_drone)
