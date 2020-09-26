from django.db import models
from django.utils.translation import ugettext_lazy as _


class Exchange(models.Model):
    GROUP_STATUS = (
        ('n1', 'N1'),
        ('n2', 'N2'),
    )

    # m = Main Board
    # f = First List
    # s = Sub  Board
    BOARD_STATUS = (
        ('m', 'تابلو اصلی'),
        ('f', 'فهرست اولیه'),
        ('s', 'تابلو فرعی')
    )
    symbol_code = models.CharField(_("Symbol Code"),
                                   max_length=12,
                                   unique=True)
    group = models.CharField(_("Symbol Group"),
                             max_length=2,
                             choices=GROUP_STATUS)
    group_industry = models.CharField(_("Group of industries"),
                                      max_length=128)
    board = models.CharField(_("Symbol Board"),
                             max_length=1,
                             choices=BOARD_STATUS)
    latin_symbol = models.CharField(_("Latin Symbol"),
                                    max_length=5,
                                    unique=True,
                                    db_index=True)
    latin_name = models.CharField(_("Latin Name"),
                                  max_length=128)
    persian_symbol = models.CharField(_("Persian symbol"),
                                      max_length=24,
                                      unique=True,
                                      db_index=True)
    persian_name = models.CharField(_("Persian name"),
                                    max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.latin_symbol} - {self.latin_name}'

    class Meta:
        ordering = ('-created', )
