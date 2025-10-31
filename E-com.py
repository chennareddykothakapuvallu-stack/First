# Simple E-Commerce Website Program

# Step 1: Create a product list (like a catalog)
products = {
    1: {"name": "Mobile", "price": 10000},
    2: {"name": "Headphones", "price": 1500},
    3: {"name": "Smart Watch", "price": 2500},
    4: {"name": "Laptop", "price": 45000},
    5: {"name": "Charger", "price": 500}
}

cart = []

# Step 2: Display products
def show_products():
    print("\nAvailable Products:")
    for pid, info in products.items():
        print(f"{pid}. {info['name']} - ₹{info['price']}")

# Step 3: Add product to cart
def add_to_cart():
    pid = int(input("Enter the product ID to add to cart: "))
    if pid in products:
        cart.append(products[pid])
        print(f"{products[pid]['name']} added to cart!")
    else:
        print("Invalid Product ID!")

# Step 4: View cart and total bill
def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:")
        total = 0
        for item in cart:
            print(f"- {item['name']} ₹{item['price']}")
            total += item['price']
        print(f"\nTotal Amount: ₹{total}")

# Step 5: Main program loop
while True:
    print("\n--- Welcome to Mini E-Commerce ---")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_products()
    elif choice == '2':
        add_to_cart()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice, please try again.")
