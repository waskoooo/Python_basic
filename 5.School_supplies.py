PEN_PACKET = 5.80
MARKER_PACKET = 7.20
CLEANING_LIQUID = 1.20

number_pen_packet = int(input())
number_marker_packet = int(input())
liters_cleaning_liquid = int(input())
discount = int(input())

end_sum = number_pen_packet * PEN_PACKET + number_marker_packet * MARKER_PACKET + liters_cleaning_liquid *\
          CLEANING_LIQUID
end_sum_with_discount = end_sum * (100 - discount) / 100

print(end_sum_with_discount)