cover_price = 24.95
bookstore_price = cover_price * .6
book_count = float(input('Number of copies purchased: '))
book_total = bookstore_price * book_count
shipping_cost = 3 + (.75 * (book_count - 1))
total_cost = book_total + shipping_cost
print(total_cost)


