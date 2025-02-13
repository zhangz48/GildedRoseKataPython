# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Legendary item does not change

            self._update_item(item)
            item.sell_in -= 1
            if item.sell_in < 0:
                self._handle_expired_item(item)

    def _update_item(self, item):
        if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
            self._update_quality_increasing_item(item)
        elif item.name.startswith("Conjured"):
            self._decrease_quality(item, 2)
        else:
            self._decrease_quality(item, 1)

    def _update_quality_increasing_item(self, item):
        if item.sell_in > 10:
            self._increase_quality(item, 1)
        elif item.sell_in > 5:
            self._increase_quality(item, 2)
        elif item.sell_in > 0:
            self._increase_quality(item, 3)

    def _handle_expired_item(self, item):
        if item.name == "Aged Brie":
            self._increase_quality(item, 1)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        elif item.name.startswith("Conjured"):
            self._decrease_quality(item, 2)
        else:
            self._decrease_quality(item, 1)

    def _increase_quality(self, item, amount):
        item.quality = min(50, item.quality + amount)

    def _decrease_quality(self, item, amount):
        item.quality = max(0, item.quality - amount)

    def get_items_by_name(self, name):
        return [item for item in self.items if item.name == name]
