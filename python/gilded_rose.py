# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                #double the decay of quality if conjured
                if item.name == "Conjured Mana Cake" and item.quality - 2 >= 0:
                    item.quality = item.quality - 2
                else:
                    item.quality = item.quality - 1
            else:
                if item.quality < 50 and item.name != "Sulfuras, Hand of Ragnaros":
                    
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11 and item.quality > 5:
                            item.quality = item.quality + 1
                        elif item.sell_in < 6 and item.quality >= 0:
                            item.quality = item.quality + 1
                        #quality drops to zero after the concert which is on day 0
                        elif item.sell_in < 0:
                            item.quality = 0
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name == "Aged Brie" and item.quality < 50: 
                    item.quality = item.quality + 1
 
                elif item.name != "Backstage passes to a TAFKAL80ETC concert" and item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                    #makes sure that an conjured's quality never goes past zero
                    if item.name == "Conjured Mana Cake" and item.quality - 2 >= 0:
                        item.quality = item.quality -2
                    else:
                        item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)