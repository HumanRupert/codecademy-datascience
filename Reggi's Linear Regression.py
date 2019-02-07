datapoints = [[1, 2], [2, 0], [3, 4], [4, 4], [5, 3]]
def get_y(m, b, x):
  y = m*x + b
  return y
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y = get_y(m,b,x_point)
    return abs(y - y_point)
def calculate_all_error(m, b, points):
  total_error = 0
  for point in points:
    error = calculate_error(m,b,point)
    total_error += error
  return total_error
m_range = [i*0.1 for i in range(-100, 100)]
m_values = [float("{0:.2f}".format(i)) for i in m_range]
b_range = [i * 0.1 for i in range(-200, 200)]
b_values = [float("{0:.2f}".format(i)) for i in b_range]
errors = []
def smallest_finder(m):
  for b in b_values:
    total_error = calculate_all_error(m, b, datapoints)
    errors.append([float("{0:.2f}".format(total_error)), m, b])
for m in m_values:
    smallest_finder(m)
errors.sort()           
best_m = errors[0][1]
best_b = errors[0][2]
def height(cm):
  bounce_height = best_m * cm + best_b
  return bounce_height
print(height(6))
