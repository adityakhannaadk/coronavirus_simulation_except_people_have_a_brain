import math
def collect(death_toll, infected, cured, reponse_radius):
  return [[death_toll,infected,cured],[response_radius]]
  # The neural network features are death toll infected and cured
  # The neural network outputs a response radius (move distance) in units
  # the angle is random for now but that will change

def strat_rad(radius):
  # Use pythagoras theorem to find a plausible movement 
  def_ = math.round(1/3*radius)
  m = radius**2-def_
  v = math.sqrt(m)
  return [math.round(v),def_] 
