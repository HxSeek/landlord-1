# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date

from django.db import models
from django.core.exceptions import ValidationError


class DateMixin(models.Model):

    date = models.DateField()

    class Meta:
        abstract = True

    def clean_date(self):
        now = datetime.now().date()
        if self.date < now:
            raise ValidationError(u'所填日期已过')
        if self.date >= now + timedelta(days=14):
            raise ValidationError(u'申请的场地使用时间距离现在不能超过14天')
        return date
