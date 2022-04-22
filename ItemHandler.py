class ItemHandler(object):
    @staticmethod
    def increase_quality_if_possible(item, amount=1):
        if amount < 0:
            raise ValueError("Cannot increase quality by a negative amount")
        elif item.quality + amount > 50:
            amount = max(item.quality, 50)
        item.quality += amount

    @staticmethod
    def decrease_quality_if_possible(item, amount=1):
        if amount < 0:
            raise ValueError("Cannot decrease quality by a negative amount")
        elif item.quality - amount < 0:
            item.quality = min(item.quality, 0)
        else:
            item.quality -= amount

    @staticmethod
    def set_quality_to_zero(item):
        item.quality = 0

    @staticmethod
    def decrease_sellin(item, amount=1):
        if amount < 0:
            raise ValueError("Cannot decrease sell-in by a negative amount")
        item.sell_in -= amount
