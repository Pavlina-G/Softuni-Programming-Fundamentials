days = int(input())
day_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0
counter = 0

while counter < days:
    counter += 1
    total_plunder += day_plunder
    if counter % 3 == 0:
        total_plunder += 0.5 * day_plunder
    if counter % 5 == 0:
        total_plunder *= 0.70

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    diff = (1 - (expected_plunder - total_plunder)/expected_plunder) * 100
    print(f"Collected only {diff:.2f}% of the plunder.")