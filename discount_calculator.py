# Define the function to calculate the discounted price
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.

    Parameters:
    - price (float): The original price of the item
    - discount_percent (float): The discount percentage to apply

    Returns:
    - float: The final price after applying the discount, or the original price if discount is less than 20%
    """
    
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the amount to discount
        discount_amount = price * (discount_percent / 100)
        # Subtract discount from original price to get final price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
try:
    # Get original price from the user and convert it to a float
    original_price = float(input("Enter the original price of the item: "))
    # Get discount percentage from the user and convert it to a float
    discount_percentage = float(input("Enter the discount percentage: "))

    # Call the function to calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Display the result to the user
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print(f"Discount applied! The final price is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
