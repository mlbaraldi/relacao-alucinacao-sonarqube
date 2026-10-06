import datetime
import dateutil.parser


def isoparse(self, dt_str):
    # Parse the datetime string using the dateutil parser
    dt = dateutil.parser.parse(dt_str)

    # If the datetime string does not contain a time zone offset,
    # assume UTC and add the offset
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=dateutil.tz.tzutc())

    # Return the parsed datetime object
    return dt
