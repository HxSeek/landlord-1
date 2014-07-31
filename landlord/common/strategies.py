"""
    The validation strategies for applied meeting room.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from calendar import MONDAY, SUNDAY


class Strategy(object):
    """The base class of strategies."""

    ident = None
    label = None

    def __init__(self, room):
        self.room = room

    def __unicode__(self):
        return u'%d : %s' % (self.ident, self.label)

    def validate(self, application):
        raise NotImplementedError


class GeneralStrategy(Strategy):
    """The general rule."""

    ident = 1001
    label = 'General Rule'

    def validate(self, application):
        pass  # do nothing


class ReserveOnSunday(Strategy):
    """The rule to reserve meeting room on sunday."""

    ident = 1002
    label = 'Not reserve on Sunday 20:00 ~ 23:00'

    def validate(self, application):
        date = application.date
        times = application.time
        if date.weekday() == SUNDAY:
            for time in times:
                if (time in ['20:00:00', '20:30:00',
                             '21:00:00', '21:30:00',
                             '22:00:00', '22:30:00']):
                    raise ReservedError(self.label)


class ReserveOnMonday(Strategy):
    """The rule to reserve meeting room on monday."""

    ident = 1003
    label = 'Not reserve on Monday 12:00 ~ 14:00'

    def validate(self, application):
        date = application.date
        times = application.time
        if date.weekday() == MONDAY:
            for time in times:
                if (time in ['12:00:00', '12:30:00',
                             '13:00:00', '13:30:00']):
                    raise ReservedError(self.label)


class ReservedError(Exception):
    pass


_STRATEGY_SET = [GeneralStrategy, ReserveOnMonday, ReserveOnSunday]
_STRATEGY_MAP = {cls.ident: cls for cls in _STRATEGY_SET}


def make_strategy_by_ident(ident, room):
    """Creates the strategy instance for special room."""
    if ident not in _STRATEGY_MAP:
        raise ValueError('unknown strategy with ident %r' % ident)
    strategy_cls = _STRATEGY_MAP[ident]
    return strategy_cls(room)


def make_strategy_choices():
    """Creates the Django style choices list."""
    return tuple((cls.ident, cls.label) for cls in _STRATEGY_SET)
