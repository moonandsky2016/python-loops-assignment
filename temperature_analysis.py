# Name: Sindhu Kannan
# Roll Number: [Your Roll Number]
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
highesttemperature=temperatures[0]
lowesttemperature=temperatures[0]
for temp in temperatures:
    if(temp > highesttemperature):
        highesttemperature=temp
    if(temp < lowesttemperature):
        lowesttemperature=temp
print(f"Highest Temperature: {highesttemperature}°C")
print(f"Lowest Temperature: {lowesttemperature}°C")

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
hottemperaturedayscount=0
for temp in temperatures:
    if(temp<=30):
        continue
    else:
        hottemperaturedayscount+=1
print(f"Hot Days (>30°C): {hottemperaturedayscount}")

# print("\n===== Task 3: Alert System =====")
# temperatures = [28, 32, 35, 40, 31, 33, 30]
# # Write your code here
# hottemperaturedayscount=0
# for i in range(len(temperatures)):
#     if(temperatures[i]>30 and temperatures[i]<40):
#         hottemperaturedayscount+=1
#     elif(temperatures[i]>=40):
#         print(f"Hot Days before alert: {hottemperaturedayscount}")
#         print(f"Alert! Extreme temperature 40°C detected on Day {i+1}")
#         break

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
# Write your code here
hottemperaturedayscount=0
for day,temp in enumerate(temperatures):
    if(temp>30 and temp<40):
        hottemperaturedayscount+=1
    elif(temp>=40):
        print(f"Hot Days before alert: {hottemperaturedayscount}")
        print(f"Alert! Extreme temperature 40°C detected on Day {day+1}")
        break
