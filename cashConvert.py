
nok = 5000
pounds = 36
dollars = 40


def exchange_nok_to_dollar(nok):
    rate = 8.7923852
    out = nok/rate

    print ("You get dollars " ,out)


exchange_nok_to_dollar(nok)


def exchange_nok_to_UKpounds(nok):
    rate = 11.840828
    out = nok/rate

    print ("You get Uk pounds " ,out)


exchange_nok_to_UKpounds(nok)


def exchange_UKpounds_to_nok(pounds):
    rate = 11.840828
    out = pounds * rate

    print ("You get nok " ,out)



def exchange_dollars_to_nok(dollars):
    rate = 8.7923852
    out = nok/rate
    print ("You get nok " ,out)


def exchange_UKpounds_to_dollars(pounds):
    rate = 1.3473644
    out = pounds * rate

    print("You get pounds ", out)


def exchange_dollars_to_UKpounds(dollars):
    rate = 0.74221567
    out = pounds * rate

    print("You get pounds ", out)
