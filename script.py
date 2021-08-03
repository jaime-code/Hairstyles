hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# setting variable to help us determine the sum total of prices
total_price = 0 

# creating loop to be able to tally up total prices
for price in prices:
  total_price += price
#print(total_price)

# creating an average price that is total prices divided by the number of digits in prices, which can be simplied using len()
average_price = total_price / len(prices)
print("Average Haircut Prices: " + str(average_price))

#The average price is too high, client would like all prices to be lowered by $5.  Throwing in a comprhensive list
new_prices = [price - 5 for price in prices]
#print(new_prices)

# creating a total_revenue variable
total_revenue = 0

# creating a for loop that uses i as the variable/element that goes through the range provided by the length of the hairsytles list, this will set i equal to index values
for i in range(len(hairstyles)):
  #print(i)
  total_revenue =+ prices[i] * last_week [i]
print("Total Revenue: " + str(total_revenue))

# Finding out the daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# creating a list that shows all cuts under 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("These are the hairstles under 30: " + str(cuts_under_30))