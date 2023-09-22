start_range = int(input())
end_range = int(input())

for barcode in range(start_range, end_range + 1):
    barcode_str = str(barcode)
    has_even_digit = any(int(digit) % 2 == 0 for digit in barcode_str)

    if not has_even_digit:
        print(barcode, end=" ")
