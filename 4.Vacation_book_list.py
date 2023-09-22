from math import floor

book_pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())

read_hours = book_pages / pages_per_hour
must_read = read_hours / days_for_reading

print(floor(must_read))