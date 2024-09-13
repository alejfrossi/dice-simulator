import random

# This program simulates the roll of a dice,
# allowing you to choose which number of die to roll and
# how many slides the dice has.

def dice_roll( dice_number ) :
  return random.randint( 1, dice_number )

def main() :
  print( "Welcome to the dice simulator!" )
  print( "How many sides does your dice have?" )
  dice_number = int( input() )
  print( "How many dice would you like to roll?" )
  dice_rolls = int( input() )
  
  dice_total = 0
  exput_text = ""
  for number in range( dice_rolls ) :
    dice_aux = dice_roll( dice_number )
    if number == dice_rolls - 1 :
      exput_text += str( dice_aux )
    else :
      exput_text += str( dice_aux ) + " + "
    dice_total += dice_aux
  print( str( dice_rolls ) + "d" + str( dice_number ) + ": " + str( dice_total ) + " ( " + exput_text + " ) " )

main()