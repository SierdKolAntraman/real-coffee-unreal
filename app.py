import json #products.json file will be imported for the menu visual

def load_products():
    with open("data/products.json", "r", encoding="utf-8") as file:
        return json.load(file)

def display_menu(products):
    print("\n--- Real Coffee Unreal Menu  ---")

    for product in products:
        print(
            f"{product['id']}. {product['name']} - "
            f"€{product['price']:.2f} "
            f"(Stock: {product['stock']})"
        ) 

def main():
    products = load_products()
    display_menu(products)


if __name__ == "__main__":
    main()

    
