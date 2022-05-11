# Instance creator for CLIPS

This program takes an structured CSV file with instance information and formats its contents into CLIPS definstances format.

CSV files follow this format:
- Headers: The first element should be the class name. The rest should be attribute names in no particular order.
- Data should be separated in commas. For multislots, separe the different elements with semicolon (;). No spaces allowed.

Example:

Lodging,Lodging_type,located-at,Cost_person_night,Quality,Room_sizes
Eco_hotel_Rome_Australian_Shepherd,eco_hotel,Rome,114.96,4,1;2;3
Apartment_Rome_Sheep,apartment,Rome,89.98,4,1;2;3
Eco_hotel_Rome_Horn_Shark,eco_hotel,Rome,27.41,1,1;2;3
Resort_Rome_Red-handed_Tamarin,resort,Rome,119.02,4,1;2;3

IMPORTANT: This script assumes that relation names (that is, attributes with type INSTANCE) begin with lowercase, and primitive attributes begin with uppercase. This is important because otherwise it's quite cumbersome to deal with the values for relations formatted as strings or literals instead of instance names. Feel free to modify the relevant part to adapt the script to your particular formatting needs.

