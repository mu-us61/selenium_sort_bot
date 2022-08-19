from booking import booking
from booking import constants as const
from booking.booking import Booking

# bot1 = booking.Booking(executable_path=const.DRIVER_PATH)

# bot1.homepage()
# bot1.se

with booking.Booking(breakdown=False) as bot:
    bot.homepage()
    bot.select_currency("USD")
    bot.select_city("LONDON")
    bot.select_date(start="2022-08-28", end="2022-09-16")
    bot.select_adult_number(number=3)
    bot.search()
    bot.filter_fun()
