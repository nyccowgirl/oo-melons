"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """ An abstract base class that other Melon Orders inherit from. """

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        if self.species.startswith("Christmas"):
            base_price = 7.5
        else:
            base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    def get_total(self):
        """ To add shipping fee to Christmas melons if order is less than 10. """

        total = super(InternationalMelonOrder, self).get_total()
        if self.species.startswith("Christmas") and self.qty < 10:
            total += 3

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A governmental melon order."""

    order_type = "government"
    tax = 0.0
    passed_inspection = False
    inspected = False

    def mark_inspection(self, passed):
        """ Pass 'True' if passed inspection."""
        self.inspected = True
        self.passed_inspection = passed
