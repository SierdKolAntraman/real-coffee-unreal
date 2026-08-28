# Real Coffee Unreal

A terminal-based coffee shop application written in Python.
Customers can browse the menu, view product details, build a basket,
review it, and place orders. Confirmed orders are saved to a JSON file.

## Features

- View the full menu or filter by category (Coffee, Soft Drink, Dessert)
- View detailed product descriptions
- Add products to a basket by product number
- Review the basket with quantities and a running total
- Checkout with a confirmation step
- Confirmed orders are saved to `data/orders.json`
- Invalid input (wrong numbers, letters) is handled without crashing

## Requirements

- Python 3 (no external packages needed — only the standard library)

## How to run

1. Clone the repository:

   git clone https://github.com/SierdKolAntraman/real-coffee-unreal.git

2. Enter the project folder:

   cd real-coffee-unreal

3. Run the app:

   python app.py

## Project structure

- `app.py` — the main application
- `data/products.json` — the product catalogue
- `data/orders.json` — saved confirmed orders
- `USER_GUIDE.md` — guide for staff using the app

## Future improvements

- Employee login and promotional discounts
- Stock levels that decrease after each order
- Delivery orders and a customer loyalty program
