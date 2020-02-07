# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
    
    def test_sellIn(self):
        items = [Item("foo", 4,7),Item("Sulfuras, Hand of Ragnaros", 4,4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(4, items[1].sell_in)
   
    def test_quality(self):
        items = [Item("foo", 4,4),Item("Sulfuras, Hand of Ragnaros", 4,4), Item("Backstage passes to a TAFKAL80ETC concert", 0,4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)
        self.assertEqual(4, items[1].quality)
        self.assertEqual(0, items[2].quality)
    
    def test_quality_zero(self):
        items = [Item("foo", 4,7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality) 
    
    def test_quality_50(self):
        items = [Item("Aged Brie", 4,50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality) 
        
    
    def test_conjured_quality(self):
        items = [Item("Conjured Mana Cake", 4,7),Item("Conjured Mana Cake", 4,2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)
        self.assertEqual(0, items[1].quality)
    
    def test_AgedBrie_quality(self):
        items = [Item("Aged Brie", 4,7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality) 

if __name__ == '__main__':
    unittest.main()
