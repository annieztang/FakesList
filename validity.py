from datascience import *
import numpy as np

headphone = Table().read_table('headphone.csv')
designer = Table().read_table('designer.csv')
makeup = Table().read_table('makeup.csv')
coin = Table().read_table('coin.csv')
jersey = Table().read_table('jersey.csv')
computer = Table().read_table('computer.csv')
laptop = Table().read_table('laptop.csv')
purse = Table().read_table('purse.csv')
watch = Table().read_table('watch.csv')
movie = Table().read_table('movie.csv')
shoe = Table().read_table('shoe.csv')
jewelry = Table().read_table('jewelry.csv')
wallet = Table().read_table('wallet.csv')
smartphone = Table().read_table('smartphone.csv')
wine = Table().read_table('wine.csv')

datasets = [headphone, designer, makeup, coin, jersey,
         computer, laptop, purse, watch, movie,
         shoe, jewelry, wallet, smartphone, wine]
items = ['headphone', 'designer', 'makeup', 'coin', 'jersey',
         'computer', 'laptop', 'purse', 'watch', 'movie',
         'shoe', 'jewelry', 'wallet', 'smartphone', 'wine']


def validity(item, price):
    item = item.lower()
    assert (item in items)

    for i in range(len(items)):
        if item == items[i]:
            lower_bound = np.median(datasets[i].column(1)) - (1 * np.std(datasets[i].column(1)))
            print(lower_bound)
            return bool(price >= lower_bound)
