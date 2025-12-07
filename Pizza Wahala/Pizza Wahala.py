
import math
print("******Welcome to Scambirah Pizza joint*****")
print(""" 
----------------------------------------------------              
|  Pizza Type |  Number of Slices |  Price Per Box |
----------------------------------------------------
|Sapa Size    |4                 |2,000            |
----------------------------------------------------
|Small Money  |6                  |2,400           |
----------------------------------------------------
|Big Boys     |8                  |3,000           |
----------------------------------------------------
|Odogwu       |12                 |4,200           |
----------------------------------------------------


""")
guest_number=int(input("Enter the the amount of guest ypu are expecting: "))
pizza_type=input("Which type of pizza would you like to get: ").lower().strip()
price_per_box=0
number_of_slices=0
if pizza_type == "sapa size":
     number_of_slices=4
     price_per_box=2000

elif pizza_type == "small money":
     number_of_slices=6
     price_per_box=2400

elif pizza_type == "big boys":
     number_of_slices=8
     price_per_box=3000

elif pizza_type == "odogwu":
     number_of_slices=12
     price_per_box=4200

number_of_boxes= math.ceil(guest_number/number_of_slices)
remainder=(number_of_boxes*number_of_slices)-guest_number
price= number_of_boxes*price_per_box


print(f"{pizza_type} size contain {number_of_slices} slice per box, {number_of_boxes}  boxes should be sufficient for {guest_number} people as it would contain {number_of_boxes*number_of_slices} slices in all  ")


print(f"After Serving {guest_number} slices, you should have {remainder} slices left")
print(f"{price} = {price_per_box} per box for {number_of_boxes} boxes ")













