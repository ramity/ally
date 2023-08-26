from django.db import models

class Exchange(models.Model):
    abbr = models.CharField(max_length=16)
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.abbr}"

class Symbol(models.Model):
    abbr = models.CharField(max_length=16)
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.abbr}"

class Stock(models.Model):
    symbol = models.ForeignKey(Symbol, on_delete = models.PROTECT)
    exchange = models.ForeignKey(Exchange, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.exchange}:{self.symbol}"

class YFExports(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    resolution = models.CharField(max_length=16)
    csv = models.TextField()

    def __str__(self):
        return f"{self.start} - {self.end} @ {self.resolution}"
