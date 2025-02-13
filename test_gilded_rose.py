import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # Test 1: Logical error - Aged Brie quality behavior
    def test_aged_brie_quality_increases_correctly(self):
        items = [Item("Aged Brie", 6, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        brie_item = items[0]
        self.assertEqual(12, brie_item.quality)  # Expects double increase, which isn't implemented
        self.assertEqual(5, brie_item.sell_in)
        self.assertEqual("Aged Brie", brie_item.name)

    # Test 2: Logical error - Backstage pass quality increase
    def test_backstage_pass_quality_increase_boundaries(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        pass_item = items[0]
        self.assertEqual(22, pass_item.quality)  # Expecting base increase + extra increase
        self.assertEqual(9, pass_item.sell_in)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", pass_item.name)

    # Test 3: Logical error - Conjured item behavior
    def test_conjured_item_degrades_twice(self):
        items = [Item("Conjured Mana Cake", 3, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEqual(8, conjured_item.quality)  # Should decrease by 2
        self.assertEqual(2, conjured_item.sell_in)
        self.assertEqual("Conjured Mana Cake", conjured_item.name)

    # Test 4: Syntax error - Missing method
    def test_get_items_by_name(self):
        items = [
            Item("Aged Brie", 5, 10),
            Item("Sulfuras", 0, 80)
        ]
        gilded_rose = GildedRose(items)
        brie_items = gilded_rose.get_items_by_name("Aged Brie")  # Method doesn't exist
        self.assertEqual(1, len(brie_items))
        self.assertEqual("Aged Brie", brie_items[0].name)

if __name__ == '__main__':
    unittest.main()