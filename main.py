import text as bot
import stockquotes

def main():
    #Get the current price of the stocks desired
    verizon = stockquotes.Stock('VZ').current_price
    norCruise = stockquotes.Stock('NCLH').current_price
    jpm = stockquotes.Stock('JPM').current_price
    aflac = stockquotes.Stock('AFL').current_price
    att = stockquotes.Stock('T').current_price
    exxon = stockquotes.Stock('XOM').current_price

    #Get the change in percentage of the stock for the day
    verizonChange = str(stockquotes.Stock('VZ').increase_percent)
    norCruiseChange = str(stockquotes.Stock('NCLH').increase_percent)
    jpmChange  = str(stockquotes.Stock('JPM').increase_percent)
    aflacChange = str(stockquotes.Stock('AFL').increase_percent)
    attChange = str(stockquotes.Stock('T').increase_percent)
    exxonChange = str(stockquotes.Stock('XOM').increase_percent)

    #Construct the message to be sent
    message = "Verizon: $" + str(verizon) + "(" + verizonChange + "%)" + "\nJPM: $" + str(jpm) + "(" + jpmChange + "%)" + "\nAflac: $" + str(aflac) + "(" + aflacChange + "%)" + "\nAT&T: $" + str(att) + "(" + attChange + "%)" + "\nExxon: $" + str(exxon) + "(" + exxonChange + "%)" + "\nNorwegian: $" + str(norCruise) + "(" + norCruiseChange + "%)" + "\nTotal Value: $" + str(totalVal)
    
    #Send text message via email
    bot.sendMessage(message, "(email to send message from)", "(email access code)", "(input phone number)@(your cell carrier)")

if __name__ == "__main__":
    main()
