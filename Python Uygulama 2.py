import math

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların tanımlanması
points = [(1, 2), (4, 6), (5, 1), (2, 8), (7, 3)]

# Mesafelerin saklanacağı liste
distances = []

# Mesafelerin hesaplanması
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

print("Points:", points)
print("Distances:", distances)
print("Minimum Distance:", min_distance)