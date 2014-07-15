# Price-haggler for python
import math
print "What do you think is a reasonable monthly price for this kind of service?";
InitialPrice = int(input())
# Establish a base price that the customer is willing to pay
MinimumPrice=50
# Set your lowest price
GoalPrice=100
# Set your target price
if InitialPrice < MinimumPrice:
  ResultPrice = MinimumPrice + ((MinimumPrice / 2) + InitialPrice) 
  print "We're sorry, but we can't offer you a price that low. \
  We need to make a living, too. We can give you this price:";
  print "%r kr per month" % (ResultPrice)
elif InitialPrice > GoalPrice:
  ResultPrice = int(GoalPrice + ((InitialPrice - GoalPrice) - math.sqrt(InitialPrice)))
  print "We're pleased that you value our work so high! \
  Here's an even better offer for you:";
  print "%r kr per month" % (ResultPrice)
elif InitialPrice == GoalPrice:
  ResultPrice = InitialPrice
  print "We're pleased that you value our work, \
and we think you have a good sense of value. \
We're willing to offer you your price, and hope you will be satisfied:";
  print "%r kr per month" % (ResultPrice)
elif InitialPrice >= MinimumPrice and InitialPrice < GoalPrice:
  ResultPrice = InitialPrice + ((GoalPrice - InitialPrice) / 2)
  print "We're pleased that you value our work, \
  but please consider a slighty higher price. \
  Here's an offer for you, that we think will please all parts of the deal:";
  print "%r kr per month" % (ResultPrice)
# Calculate resulting price from given variables. If between minimum and goal
# price -> Push price toward goal price and make offer. If below minimum or 
# negative -> Explain and give a higher offer. If above goal price ->
# give offer.
print "Do you accept this monthly price? (y/n)"

# Ask if satisfactory haggling has been made. If yes -> proceed to checkout. 
# If no -> Cancel.
print "Your monthly price will be %r kr." % (ResultPrice)
# Display price
