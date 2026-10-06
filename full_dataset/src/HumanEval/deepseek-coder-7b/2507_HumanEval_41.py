

def car_race_collision(n: int):
    # Initialize the number of collisions
    collisions = 0

    # Iterate over each car
    for i in range(n):
        # Calculate the position of the car moving left to right
        left_car_position = i

        # Calculate the position of the car moving right to left
        right_car_position = n - 1 - i

        # Check if the cars will collide
        if left_car_position == right_car_position:
            collisions += 1

    # Return the number of collisions
    return collisions
