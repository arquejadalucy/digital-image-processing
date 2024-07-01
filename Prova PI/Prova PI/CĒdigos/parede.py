import cv2
import numpy as np
# Testando com barra lateral e interaçoes e HSV
def nothing(x):
    pass

initial_parameters = {
    'Low H O': 0,
    'Low S O': 0,
    'Low V O': 0,
    'High H O': 179,
    'High S O': 255,
    'High V O': 255,
    'Low H B': 0,
    'Low S B': 0,
    'Low V B': 0,
    'High H B': 179,
    'High S B': 255,
    'High V B': 255,
    'Low H S': 0,
    'Low S S': 0,
    'Low V S': 0,
    'High H S': 179,
    'High S S': 255,
    'High V S': 255,
}
initial_iterations = {
    'Erode O': 1,
    'Dilate O': 1,
    'Erode B': 1,
    'Dilate B': 1,
    'Erode S': 1,
    'Dilate S': 1
}

# Calculate the height of the 'Segmentation Parameters' window based on the number of items in initial_parameters
num_parameters = len(initial_parameters)
num_iterations = len(initial_iterations)
window_height_parameters = num_parameters * 38  # Adjust the value as needed
window_height_iterations = num_iterations * 39  # Adjust the value as needed

# Create the 'Segmentation Parameters' window with adjusted size
cv2.namedWindow('Segmentation Parameters')
cv2.resizeWindow('Segmentation Parameters', 300, window_height_parameters)
cv2.namedWindow('Adjustment Window')
cv2.resizeWindow('Adjustment Window', 300, window_height_iterations)

# Create parameter bars for HSV values in the 'Segmentation Parameters' window
for key, value in initial_parameters.items():
    cv2.createTrackbar(key, 'Segmentation Parameters', value, 255, nothing)

# Create a separate window for initial_iterations parameter bars
for key, value in initial_iterations.items():
    cv2.createTrackbar(key, 'Adjustment Window', value, 255, nothing)

# Load the image and calculate proportions
width, height = 800, 600
image = cv2.imread('./img/parede.jpg')
proportion_width = width / image.shape[1]
proportion_height = height / image.shape[0]
proportion = min(proportion_width, proportion_height)
new_width = int(image.shape[1] * proportion)
new_height = int(image.shape[0] * proportion)
img = cv2.resize(image, (new_width, new_height))

kernel = np.ones((9, 9), np.uint8)

# Callback function to update iterations
def update_iterations(image, erode_o, dilate_o, erode_b, dilate_b, erode_s, dilate_s):

    # Capture the values from the sliders
    low_h_O = cv2.getTrackbarPos('Low H O', 'Segmentation Parameters')
    low_s_O = cv2.getTrackbarPos('Low S O', 'Segmentation Parameters')
    low_v_O = cv2.getTrackbarPos('Low V O', 'Segmentation Parameters')
    high_h_O = cv2.getTrackbarPos('High H O', 'Segmentation Parameters')
    high_s_O = cv2.getTrackbarPos('High S O', 'Segmentation Parameters')
    high_v_O = cv2.getTrackbarPos('High V O', 'Segmentation Parameters')

    low_h_B = cv2.getTrackbarPos('Low H B', 'Segmentation Parameters')
    low_s_B = cv2.getTrackbarPos('Low S B', 'Segmentation Parameters')
    low_v_B = cv2.getTrackbarPos('Low V B', 'Segmentation Parameters')
    high_h_B = cv2.getTrackbarPos('High H B', 'Segmentation Parameters')
    high_s_B = cv2.getTrackbarPos('High S B', 'Segmentation Parameters')
    high_v_B = cv2.getTrackbarPos('High V B', 'Segmentation Parameters')

    low_h_S = cv2.getTrackbarPos('Low H S', 'Segmentation Parameters')
    low_s_S = cv2.getTrackbarPos('Low S S', 'Segmentation Parameters')
    low_v_S = cv2.getTrackbarPos('Low V S', 'Segmentation Parameters')
    high_h_S = cv2.getTrackbarPos('High H S', 'Segmentation Parameters')
    high_s_S = cv2.getTrackbarPos('High S S', 'Segmentation Parameters')
    high_v_S = cv2.getTrackbarPos('High V S', 'Segmentation Parameters')

    mask_orange, _, _ = segment(image, low_h_O, low_s_O, low_v_O, high_h_O, high_s_O, high_v_O)

    _, mask_brick, _ = segment(image, low_h_B, low_s_B, low_v_B, high_h_B, high_s_B, high_v_B)

    _, _, mask_skin = segment(image, low_h_S, low_s_S, low_v_S, high_h_S, high_s_S, high_v_S)

    mask_orange_erode = cv2.erode(mask_orange, kernel, iterations=erode_o)
    mask_orange_dilate = cv2.dilate(mask_orange_erode, kernel, iterations=dilate_o)

    mask_brick_erode = cv2.erode(mask_skin, kernel, iterations=erode_b)
    mask_brick_dilate = cv2.dilate(mask_brick_erode, kernel, iterations=dilate_b)

    mask_skin_erode = cv2.erode(mask_brick, kernel, iterations=erode_s)
    mask_skin_dilate = cv2.dilate(mask_skin_erode, kernel, iterations=dilate_s)

    result_orange = cv2.bitwise_and(image, image, mask=mask_orange_dilate)
    result_brick = cv2.bitwise_and(image, image, mask=mask_brick_dilate)
    result_skin = cv2.bitwise_and(image, image, mask=mask_skin_dilate)

    orange_brick = cv2.bitwise_and(result_orange, result_skin)
    fusion = cv2.bitwise_or(orange_brick, result_brick)

    return fusion

def segment(image,low_h, low_s, low_v, high_h, high_s, high_v):


    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([low_h, low_s, low_v], dtype=np.uint8)
    upper_orange = np.array([high_h, high_s, high_v], dtype=np.uint8)

    lower_brick = np.array([low_h, low_s, low_v], dtype=np.uint8)
    upper_brick = np.array([high_h, high_s, high_v], dtype=np.uint8)

    lower_skin = np.array([low_h, low_s, low_v], dtype=np.uint8)
    upper_skin = np.array([high_h, high_s, high_v], dtype=np.uint8)

    mask_orange = cv2.inRange(hsv_image, lower_orange, upper_orange)
    mask_brick = cv2.inRange(hsv_image, lower_brick, upper_brick)
    mask_skin = cv2.inRange(hsv_image, lower_skin, upper_skin)

    return mask_orange, mask_brick, mask_skin

while True:
    erode_o = cv2.getTrackbarPos('Erode O', 'Adjustment Window')
    dilate_o = cv2.getTrackbarPos('Dilate O', 'Adjustment Window')
    erode_b = cv2.getTrackbarPos('Erode B', 'Adjustment Window')
    dilate_b = cv2.getTrackbarPos('Dilate B', 'Adjustment Window')
    erode_s = cv2.getTrackbarPos('Erode S', 'Adjustment Window')
    dilate_s = cv2.getTrackbarPos('Dilate S', 'Adjustment Window')

    # Apply segmentation
    iterations = update_iterations(img, erode_o, dilate_o, erode_b, dilate_b, erode_s, dilate_s)

    # Display the segmented image
    cv2.imshow('Segmented Image', iterations)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
