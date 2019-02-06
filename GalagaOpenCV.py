import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import base64
import cv2
import numpy as np
import pyautogui

BINARY_THRESHOLD = 254
CONNECTIVITY = 4

player_params = cv2.SimpleBlobDetector_Params()
player_params.filterByArea = True
player_params.minArea = 411
player_params.maxArea =420
player_params.filterByCircularity = False
player_params.filterByConvexity = False
player_params.filterByInertia = False
player_detector = cv2.SimpleBlobDetector_create(player_params)
enemy_params = cv2.SimpleBlobDetector_Params()
enemy_params.filterByArea = True
enemy_params.minArea = 101
enemy_params.maxArea =400
enemy_params.filterByCircularity = False
enemy_params.filterByConvexity = False
enemy_params.filterByInertia = False
enemy_detector = cv2.SimpleBlobDetector_create(enemy_params)
missile_params = cv2.SimpleBlobDetector_Params()
missile_params.filterByArea = True
missile_params.minArea = 30
missile_params.maxArea =100
missile_params.filterByCircularity = False
missile_params.filterByConvexity = False
missile_params.filterByInertia = False
missile_detector = cv2.SimpleBlobDetector_create(missile_params)
player_axis_y = 0


driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.tripletsandus.com/80s/80s_games/html5_galaga.htm")
clickToPlay = driver.find_element_by_css_selector("select")
actions = ActionChains(driver)
actions.click(clickToPlay).perform()
time.sleep(1)
a = driver.find_element_by_class_name("nes-screen")
actions = ActionChains(driver)
actions.click(a).perform()
actions.perform()
time.sleep(1)
actions.send_keys(Keys.RETURN, Keys.RETURN)
actions.perform()
time.sleep(1)
actions.send_keys(Keys.RETURN, Keys.RETURN)
actions.perform()

def get_driver_image(driver):
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", a)
    cap = base64.b64decode(canvas_base64)
    global image
    global gray_image
    image = cv2.imdecode(np.frombuffer(cap, np.uint8), 1)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def prepare_image(image, gray_image):
    global crop_img
    global threshold
    crop_img = gray_image[0:240, 0:205]
    binary_image = cv2.Laplacian(crop_img, cv2.CV_8UC1)
    dilated_image = cv2.dilate(binary_image, np.ones((6, 6)))
    _, thresh = cv2.threshold(dilated_image, BINARY_THRESHOLD, 255, cv2.THRESH_BINARY)
    components = cv2.connectedComponentsWithStats(thresh, CONNECTIVITY, cv2.CV_32S)
    centers = components[3]
    retval, threshold = cv2.threshold(thresh, 200, 255, cv2.THRESH_BINARY_INV)

def draw_keypoints(image, *args):
    for keypoint in args:
        if keypoint == keypoints_player:
            point_color = [0, 255, 0]
        elif keypoint == keypoints_enemy:
            point_color = [0, 0, 255]
        else:
            point_color = [255, 255, 255]
        image = cv2.drawKeypoints(
            image, keypoint, np.array([]), (point_color),
            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
        )
    return image

def lowest_enemy_location():
    #global lowest_enemy_y_axis
    lowest_enemy_y_axis = 0
    lowest_enemy_x_axis = 0
    #lowest_enemy_x = 0
    j = 0
    while j<len(keypoints_enemy):
        enemy_axis_y = keypoints_enemy[j].pt[0]
        enemy_axis_x = keypoints_enemy[j].pt[1]
        #if enemy_axis_x is not None:
        if enemy_axis_x > lowest_enemy_x:
            lowest_enemy_x_axis = enemy_axis_x
            lowest_enemy_y_axis = enemy_axis_y
        j += 1
    return lowest_enemy_y_axis, lowest_enemy_x_axis

def evasion_manever_alpha(lowest_enemy_y_axis):
    if player_axis_y > lowest_enemy_y_axis:
        pyautogui.keyDown('right')
        pyautogui.keyDown('x')
    if player_axis_y < lowest_enemy_y_axis:
        pyautogui.keyDown('left')
        pyautogui.keyDown('x')

def follow_and_destroy(lowest_enemy_y_axis, lowest_enemy_x_axis):
    i = 0
    while i<len(keypoints_player):
        player_axis_y = keypoints_player[i].pt[0]
        player_axis_x = keypoints_player[i].pt[1]
        print(player_axis_y)
        i += 1
        if lowest_enemy_x_axis > 130:
            evasion_manever_alpha(lowest_enemy_y_axis)
        if player_axis_y > lowest_enemy_y_axis:
            pyautogui.keyDown('left')
            pyautogui.keyDown('x')
        else:
            pyautogui.keyUp('left')
            pyautogui.keyUp('x')
        if player_axis_y < lowest_enemy_y_axis:
            pyautogui.keyDown('right')
            pyautogui.keyDown('x')
        else:
            pyautogui.keyUp('right')
            pyautogui.keyUp('x')

def game_loop():
    while True:
        get_driver_image(driver)
        prepare_image(image, gray_image)
        keypoints_player = player_detector.detect(threshold)
        keypoints_enemy = enemy_detector.detect(threshold)
        keypoints_missile = missile_detector.detect(threshold)
        im_with_keypoints = draw_keypoints(
            image, keypoints_player,
            keypoints_enemy,
            keypoints_missile
        )
        lowest_enemy_y_axis, lowest_enemy_x_axis = lowest_enemy_location()
        follow_and_destroy(lowest_enemy_y_axis, lowest_enemy_x_axis)
        cv2.imshow("Galaga", im_with_keypoints)
        if cv2.waitKey(1) == ord('q'):
            break

game_loop()

cap.release()
cv2.destroplayer_axis_xllWindows()
