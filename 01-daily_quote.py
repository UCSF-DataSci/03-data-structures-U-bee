#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date

quotes = [
    # Create a list of quotes here
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
    "If you look at what you have in life, you'll always have more. - Oprah Winfrey",
    "Don't judge each day by the harvest you reap but by the seeds that you plant. - Robert Louis Stevenson",
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson"
]

def get_quote_of_the_day(quotes):
    todays_quote = None

    # Your code here
    random.seed(date.today().weekday())
    todays_quote = random.choice(quotes)
    print("0 8 * * * C:/Users/borau/AppData/Local/Programs/Python/Python312/python.exe C:/Users/borau/Documents/Datasci217 Git/03-data-structures-U-bee/01-daily-quote.py >> C:/Users/borau/Documents/daily_quotes.log 2>&1")
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * C:/Users/borau/AppData/Local/Programs/Python/Python312/python.exe C:/Users/borau/Documents/Datasci217 Git/03-data-structures-U-bee/01-daily-quote.py >> C:/Users/borau/Documents/daily_quotes.log 2>&1    