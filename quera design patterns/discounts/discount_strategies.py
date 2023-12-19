from discount_interfaces import DiscountStrategy, Season


class NoDiscount(DiscountStrategy):
    def apply_discount(self, price, context):
        return price

class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, price, context):
        if context.season == Season.WINTER:
            return int(price * 0.9)
        return price

class BulkPurchaseDiscount(DiscountStrategy):
    def apply_discount(self, price, context):
        if context.quantity > 9:
            return int(price * 0.85)
        return price

class MemberDiscount(DiscountStrategy):
    def apply_discount(self, price, context):
        if context.is_member:
            return int(price * 0.8)
        return price

