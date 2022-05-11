# Instance creator for CLIPS

This program takes an structured CSV file with instance information and formats its contents into CLIPS definstances format.

CSV files follow this format:
- Headers: The first element should be the class name. The rest should be attribute names in no particular order.
- Data should be separated in commas. For multislots, separe the different elements with semicolon (;). No spaces allowed.

IMPORTANT: This script assumes that relation names (that is, attributes with type INSTANCE) begin with lowercase, and primitive attributes begin with uppercase. This is important because otherwise it's quite cumbersome to deal with the values for relations formatted as strings or literals instead of instance names. Feel free to modify the relevant part to adapt the script to your particular formatting needs.

