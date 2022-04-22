# -*- coding: utf-8 -*-

from ItemHandler import ItemHandler


class GildedRose(object):

    non_degrading_items = ("Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros")

    def __init__(self, items):
        self.items = items

    @classmethod
    def update_quality(cls, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if 5 < item.sell_in <= 10:
                ItemHandler.increase_quality_if_possible(item, 2)
            elif 0 < item.sell_in <= 5:
                ItemHandler.increase_quality_if_possible(item, 3)
            else:
                ItemHandler.set_quality_to_zero(item)
        else:
            base_quality_change = 1 if not item.sell_in <= 0 else 2
            if item.name == "Aged Brie":
                ItemHandler.increase_quality_if_possible(item, base_quality_change)
            elif item.name.startsWith("Conjured"):
                ItemHandler.decrease_quality_if_possible(item, 2*base_quality_change)
            elif item.name not in cls.non_degrading_items:
                ItemHandler.decrease_quality_if_possible(item, base_quality_change)

    @classmethod
    def update_sellin(cls, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            ItemHandler.decrease_sellin(item)

    def update_items(self):
        for item in self.items:
            self.update_quality(item)
            self.update_sellin(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
