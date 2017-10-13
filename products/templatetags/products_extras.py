from django import template
import decimal

register = template.Library()


def costformat(cost):
    return '{0:,}'.format(decimal.Decimal(cost)).replace(',', ' ')

register.filter('costformat', costformat)
