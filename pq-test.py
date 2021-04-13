from pyquery import PyQuery as pq

with open("test.html", "r") as f:
    
    contents = f.read()
    
    doc = pq(contents)

    # print(doc)

    items = [item.text() for item in doc.items('td')]

    # print(items)

    # items2 = [item.text() for item in doc('[itemprop]')]

    print(doc('[itemprop=name]').text())

    print(doc('[itemprop=alternateName]').text())

    print(doc('[itemprop=taxID]').text())

    print(doc('[itemprop=address]').text())

    print(doc('[itemprop=alumni]').text())


    