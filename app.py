import json #products.json file will be imported for the menu visual

def load_products():
    with open("data/products.json", "r", encoding="utf-8") as file:
        return json.load(file)

def display_menu(products, title):
    title == "Real Coffee Unreal"
    print(f"\n---{title} ---")

    for product in products:
        print(
            f"{product['id']}. {product['name']} - "
            f"€{product['price']:.2f} "
            f"(Stock: {product['stock']})"
        ) 

def display_product_details(product):
    print(f"\n--- Product Details ---")
    print(f"Name: {product['name']}")
    print(f"Category: {product['category']}")
    print(f"Price: {product['price']:.2f}")
    print(f"Description: {product['description']}")

    

def filter_by_category(products, category):

    filtered_products = []
    
    for product in products:
        if product["category"] == category:
            filtered_products.append(product)
    return product

def show_main_menu():
    print("\n=== Real Coffee Unreal ===")
    print("1. View full menu")
    print("2. View coffee")
    print("3. View soft drinks")
    print("4. View desserts")
    print("5. Exit")


def main():

    products = load_products()

    while True:
        show_main_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            display_menu(products, "Full Menu")
            detail_choice = input("Enter product number for details, or press Enter to return: ")

            if detail_choice.isdigit():
                product_id = int(detail_choice)

                for product in products:
                    if product["id"] == product_id:
                        display_product_details(product)
                        break

        elif choice == "2":
            coffee = [product for product in products if product["category"] == "Coffee"]
           # print(coffee)
            display_menu(coffee, "Coffee Menu")

        elif choice == "3":
            soft_drink = [product for product in products if product["category"] == "Soft Drink"]
            display_menu(soft_drink, "Soft Drink Menu")

        elif choice == "4":
            dessert = [product for product in products if product["category"] == "Dessert"]
            display_menu(dessert, "Desserts Menu")

        elif choice == "5":
            print("\nThank you for visiting Real Coffee Unreal. Goodbye!")
            break

        else:
            print("\nInvalid option. Please choose a number from 1 to 5.")
        




if __name__ == "__main__":
    main()

    
