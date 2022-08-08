from pyquery import PyQuery

def get_exchange_table():
    # Data source
    url = 'https://rate.bot.com.tw/xrt?Lang=en-US'
    # the output dictionary
    table = {}
    # Crawl the entire webpage
    html = PyQuery(url)
    # All currency names
    original_names = html('div.hidden-phone.print_show').text().split()
    names = []
    temp = []
    i = 0
    while i < len(original_names) - 1:
        temp.append(original_names[i])
        if original_names[i + 1][0] == '(':
            names.append(' '.join(temp))
            temp = []
            i += 2
            continue
        else:
            i += 1

    # the price of buying
    bids = html(
        'td.rate-content-cash.text-right.print_hide[data-table="Cash Buying"]').text().split()
    # the price of selling
    offers = html(
        'td.rate-content-cash.text-right.print_hide[data-table="Cash Selling"]').text().split()
    # store the bids and offers in names
    ind = 0
    for name in names:
        table[name] = {
            "bid": bids[ind],
            "offer": offers[ind]
        }
        ind += 1
    return table




