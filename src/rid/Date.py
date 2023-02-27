_format ={
    "ymd" :'{d.year}-{d.month}-{d.day}',
    "dmy" : '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
            if format_spec == "":
                format_spec = "ymd"
                fmt = _format[format_spec]
                return fmt.format(d=self)



d = Date(2023, 2, 1)
print(format(d, "dmy"))