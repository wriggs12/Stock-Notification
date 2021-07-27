import text as bot
import stockquotes

def main():
    verizon = stockquotes.Stock('VZ').current_price
    norCruise = stockquotes.Stock('NCLH').current_price
    jpm = stockquotes.Stock('JPM').current_price
    aflac = stockquotes.Stock('AFL').current_price
    att = stockquotes.Stock('T').current_price
    exxon = stockquotes.Stock('XOM').current_price

    verizonChange = str(stockquotes.Stock('VZ').increase_percent)
    norCruiseChange = str(stockquotes.Stock('NCLH').increase_percent)
    jpmChange  = str(stockquotes.Stock('JPM').increase_percent)
    aflacChange = str(stockquotes.Stock('AFL').increase_percent)
    attChange = str(stockquotes.Stock('T').increase_percent)
    exxonChange = str(stockquotes.Stock('XOM').increase_percent)

    totalVal = (exxon * 10.76) + (att * 45.184) + (aflac * 2.126) + (jpm * 5.112) + (norCruise * 24) + (verizon * 12.132)

    message = "Verizon: $" + str(verizon) + "(" + verizonChange + "%)" + "\nJPM: $" + str(jpm) + "(" + jpmChange + "%)" + "\nAflac: $" + str(aflac) + "(" + aflacChange + "%)" + "\nAT&T: $" + str(att) + "(" + attChange + "%)" + "\nExxon: $" + str(exxon) + "(" + exxonChange + "%)" + "\nNorwegian: $" + str(norCruise) + "(" + norCruiseChange + "%)" + "\nTotal Value: $" + str(totalVal)
    bot.sendMessage(message, "botjohnny648@gmail.com", "msbqsxvtevmmaaem", "5166471969@sms.myboostmobile.com")

if __name__ == "__main__":
    main()