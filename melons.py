"""Classes for melon orders."""

from random import randint
from datetime import datetime


class AbstractMelonOrder(object):
    """ An abstract base class that other Melon Orders inherit from. """

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        if qty > 100:
            raise TooManyMelonsError

        self.species = species
        self.qty = qty
        self.shipped = False
        self.date_time = datetime.now()

    def get_base_price(self):
        """ Splurge / Random pricing."""
        base_price = randint(5, 9)

        if (self.date_time.weekday() < 5 and
            self.date_time.hour >= 8 and
            self.date_time.hour <= 10):

            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species.startswith("Christmas"):
            base_price = base_price * 1.5

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
    passed_inspection = None
    inspected = False

    def mark_inspection(self, passed):
        """ Documents results of inspection. """
        self.inspected = True
        self.passed_inspection = passed


class TooManyMelonsError(ValueError):
    """ Raises error when quantity is more than 100 melons. """

    def __init__(self):
        """ Displays TooManyMelonsError from ValueError class. """
        super(TooManyMelonsError, self).__init__('No more than 100 melons!')
