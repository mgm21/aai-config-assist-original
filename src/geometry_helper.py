import numpy as np


# TODO: write doc strings for the methods
# TODO: add examples to all the methods (can just use the examples that you've written out below)
# TODO: check all functions with tests

def calculate_vertices_of_rotated_rectangle(center, width, height, angle_deg):
    """Calculates the 4 vertex coordinates of a rectangle in the x-y plane rotated about its centroid.

    Args:
        center (np.ndarray): The x and y coordinates of the rectangle's centroid.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        angle_deg (float): The clockwise angle of rotation of the rectangle, given in degrees.

    Returns:
        np.ndarray: Array (4x2) containing the 4 x and y coordinate pairs of the rotated rectangle's vertices.
    """
    vertices = calculate_vertices_of_axis_aligned_rectangle(center, width, height)
    rotated_vertices = calculate_clockwise_rotated_2d_point(vertices, angle_deg, center)
    return rotated_vertices


def calculate_vertices_of_axis_aligned_rectangle(center, width, height):
    """Calculates the 4 vertex coordinates of a rectangle whose sides are aligned with the x and y axes.

    Args:
        center (np.ndarray): The x and y coordinates of the rectangle's centroid.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
      np.ndarray: Array (4x2) containing the 4 x and y coordinate pairs of the rectangle vertices.
    """
    half_width = 0.5 * width
    half_height = 0.5 * height

    a = center + np.array([-half_width, half_height])
    b = center + np.array([half_width, half_height])
    c = center + np.array([half_width, -half_height])
    d = center + np.array([-half_width, -half_height])

    vertices = np.array([a, b, c, d])
    return vertices


def calculate_clockwise_rotated_2d_point(points, angle_deg, center_of_rotation=np.array([0, 0])):
    """Calculates the new coordinates of 2d points rotated by a given angle about a center of rotation.

    Args:
        points (np.ndarray): The x and y coordinates of all the points to be rotated, stacked vertically.
            If N points are provided, the array will be of dimension (N, 2).
        angle_deg (float): The clockwise angle of rotation of the points, given in degrees.
        center_of_rotation (np.ndarray): The x and y coordinates of the center of rotation.

    Returns:
        np.ndarray: The x and y coordinates of all the rotated points.
    """
    # Translate the points by center_of_rotation
    points -= center_of_rotation

    # Perform the rotation
    angle = np.deg2rad(angle_deg)
    # Note: this is for clockwise 2d rotation, not for the more common anticlockwise counterpart
    rotation_mat = np.array([
        [np.cos(angle), np.sin(angle)],
        [-np.sin(angle), np.cos(angle)]
    ])
    rotated_points = np.matmul(rotation_mat, points.T).T

    # Reverse the translation by center_of_rotation
    rotated_points += center_of_rotation
    return rotated_points


def determine_overlap_between_aligned_segments(segment1, segment2):
    """Determines the overlap value between segments 1 and 2.

    Each segment is defined by a min and max value corresponding to their start and stop points on the same line.

    Args:
        segment1 (np.ndarray): The min and max values of segment 1 along a common line, in an array of dimension (1, 2)
        segment2 (np.ndarray): The min and max values of segment 2 along a common line, in an array of dimension (1, 2)

    Returns:
        float: The overlap distance between the two inputted segments.
    """
    start1, stop1 = min(segment1), max(segment1)
    start2, stop2 = min(segment2), max(segment2)
    overlap = max(0, min(stop2, stop1) - max(start2, start1))
    return overlap


def get_min_max_projections(points, axis):
    """Computes the minimum and maximum projection values of the inputted points onto an axis.

    This is equivalent to the boundaries of the total projection distance covered by a polygon when all of its
    vertices (defined in points), are projected onto a vector (defined as axis).

    Args:
        points (np.ndarray): The x and y coordinates of all the points to be rotated, stacked vertically.
            If N points are provided, the array will be of dimension (N, 2).
        axis (np.ndarray): A normalised axis defined by an x and y coordinate given in an array of dimension (1, 2).

    Returns:
        tuple(float, float): The minimum and maximum values of the projections of all inputted points onto the axis.
    """
    projections = get_projected_distance_of_2d_points_onto_axis(points, axis)
    min_distance = min(projections)
    max_distance = max(projections)
    return min_distance, max_distance


def get_projected_distance_of_2d_points_onto_axis(points, axis):
    """Compute the projected distance (the dot product) of a set of points onto an axis.

    Args:
        points (np.ndarray): The x and y coordinates of all the points to be rotated, stacked vertically.
            If N points are provided, the array will be of dimension (N, 2).
        axis (np.ndarray): A normalised axis defined by an x and y coordinate given in an array of dimension (1, 2).

    Returns:
        np.ndarray: The distances obtained from projecting the inputted points onto the inputted axis. The resulting
            array has the same dimension as the inputted points array.
    """
    # TODO: decide whether to normalise here or not
    # axis = normalise_vector(axis)
    projected_points = np.dot(points, axis)
    return projected_points


def normalise_vector(vec):
    """Normalises a vector.

    Args:
        vec (np.ndarray): An array of component values, as many values as the dimensionality of the vector space.

    Returns:
        np.ndarray: A normalised vector whose component values sum to 1.
    """
    normalised_vec = vec / np.linalg.norm(vec)
    return normalised_vec


if __name__ == "__main__":
    # Calculating the rotated vertices of a rectangle from center, width, height, and rotation in degrees
    centroid2 = np.array([0, 0])
    height2 = 2
    width2 = 2
    rotation2 = 45
    vertices2 = calculate_vertices_of_rotated_rectangle(center=centroid2, width=width2,
                                                        height=height2, angle_deg=rotation2)
    print(np.shape(vertices2))
    print(vertices2)

    # Calculating the vertices of an axis-aligned rectangle from center, width, and height
    centroid1 = np.array([0, 0])
    height1 = 2
    width1 = 2
    vertices1 = calculate_vertices_of_axis_aligned_rectangle(center=centroid1, width=width1, height=height1)
    print(np.shape(vertices1))
    print(vertices1)

    # Rotating a points in a 2d plane
    original_point = np.array([[-1, 1], [1, 1], [1, -1], [-1, -1]])
    angle_degrees = 45
    new_points = calculate_clockwise_rotated_2d_point(points=original_point, angle_deg=angle_degrees)
    print(np.shape(new_points))
    print(new_points)

    # Normalise an axis vector
    axis = np.array([1, -1])
    normalised_axis = normalise_vector(axis)
    print(normalised_axis[0])
    print((normalised_axis / np.linalg.norm(normalised_axis))[0])

    # TODO: strangely, approximation of the float makes this check false, though the formula in the function is correct
    print(normalised_axis == normalised_axis / np.linalg.norm(normalised_axis))

    # Project a points onto an axis
    points = np.array([[4, 1], [4, 1], [5, 1], [6, 2], [-1, 5]])
    new_axis = np.array([1, -1])
    normalised_new_axis = normalise_vector(new_axis)
    new_points = get_projected_distance_of_2d_points_onto_axis(points, normalised_new_axis)
    print(new_points)

    # Get min and max values of projected points onto an axis
    points = np.array([[4, 1], [4, 1], [5, 1], [6, 2], [-1, 5]])
    new_axis = np.array([1, -1])
    normalised_new_axis = normalise_vector(new_axis)
    min_val, max_val = get_min_max_projections(points, normalised_new_axis)
    print(min_val, max_val)

    # Determine the overlap between two segments
    segment1 = np.array([-1, 2])
    segment2 = np.array([-3, 1])
    overlap = determine_overlap_between_aligned_segments(segment1, segment2)
    print(overlap)

    print("Exit ok")
