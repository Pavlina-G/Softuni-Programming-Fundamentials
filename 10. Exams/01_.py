from math import floor
biscuits_per_day_per_worker = int(input())
workers_count = int(input())
biscuits_other_30days = int(input())
days = 30
counter = 0
total_biscuits = 0

while counter < days:
    counter += 1
    daily_biscuits = workers_count * biscuits_per_day_per_worker

    if counter % 3 == 0:
        daily_biscuits = floor(daily_biscuits * 0.75)

    total_biscuits += daily_biscuits

print(f"You have produced {total_biscuits} biscuits for the past month.")
diff = abs(total_biscuits - biscuits_other_30days)
percentage = diff/biscuits_other_30days * 100

if total_biscuits > biscuits_other_30days:
    print(f"You produce {percentage:.2f} percent more biscuits.")
elif total_biscuits < biscuits_other_30days:
    print(f"You produce {percentage:.2f} percent less biscuits.")
