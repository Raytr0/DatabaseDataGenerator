import csv

with open('rings.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["ringId", "name", "size"]
    rings = ["Solitaire", "Halo", "Pave", "Cluster", "Three-Stone", "Infinity", "Eternity Band", "Channel Set",
             "Bezel Set", "Tension", "Vintage", "Cocktail", "Signet", "Stackable", "Split Shank", "Pear-Shaped",
             "Heart-Shaped", "Nature-Inspired", "Celtic", "Minimalist"]
    sizes = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5]
    writer.writerow(field)
    for i in range(len(rings)):
        for j in range(len(sizes)):
            writer.writerow(["", rings[i], sizes[j]])
