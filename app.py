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

        elif choice == "2":
            coffee = filter_by_category(products, "Coffee")
            display_menu(coffee, "Coffee Menu")

        elif choice == "3":
            soft_drinks =  filter_by_category(products, "Soft Drink")
            display_menu(soft_drinks, "Soft Drink Menu")

        elif choice == "4":
            desserts = filter_by_category(products, "Dessert")
            display_menu(desserts, "Desserts Menu")

        elif choice == "5":
            print("\nThank you for visiting Real Coffee Unreal. Goodbye!")
            break

        else:
            print("\nInvalid option. Please choose a number from 1 to 5.")
        




if __name__ == "__main__":
    main()

    
