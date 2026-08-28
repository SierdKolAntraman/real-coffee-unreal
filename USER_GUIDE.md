# Real Coffee Unreal — User Guide

## Starting the app

Open a terminal, go to the project folder, and run:

    python app.py

## Main menu options

1. View full menu — shows every product with price and stock.
2. View coffee — shows only coffee products.
3. View soft drinks — shows only soft drinks.
4. View desserts — shows only desserts.
5. Order product — shows the menu, then enter a product number
   to add it to your basket.
6. Review basket — shows everything in the basket with a total.
7. Checkout — shows the total and asks to confirm (y/n).
   Confirmed orders are saved and the basket is cleared.
8. Exit — closes the app.

## Tips for staff

- If you type letters instead of numbers, the app asks again
  instead of crashing.
- Order records are stored in `data/orders.json` — one record
  per confirmed order, with items, quantities, and total.
