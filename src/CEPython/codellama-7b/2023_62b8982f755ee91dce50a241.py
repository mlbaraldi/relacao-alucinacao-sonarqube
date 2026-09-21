from datetime import timedelta


def normalized(self):
    # Convert all attributes to integers
    days = int(self.days)
    hours = int(self.hours)
    minutes = int(self.minutes)
    seconds = int(self.seconds)
    microseconds = int(self.microseconds)
    milliseconds = int(self.milliseconds)
    weeks = int(self.weeks)

    # Calculate the total number of seconds
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

    # Calculate the number of weeks
    weeks = total_seconds // (7 * 24 * 60 * 60)

    # Calculate the remaining seconds
    remaining_seconds = total_seconds % (7 * 24 * 60 * 60)

    # Calculate the number of days
    days = remaining_seconds // (24 * 60 * 60)

    # Calculate the number of hours
    hours = remaining_seconds % (24 * 60 * 60) // (60 * 60)

    # Calculate the number of minutes
    minutes = remaining_seconds % (60 * 60) // 60

    # Calculate the number of seconds
    seconds = remaining_seconds % 60

    # Create a new relativedelta object with the normalized values
