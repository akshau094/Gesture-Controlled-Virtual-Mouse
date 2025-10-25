# Top-level module imports and env setup
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 2=hide INFO, 3=hide INFO+WARN
# Optional: disable oneDNN custom ops (can reduce performance). Remove if not needed.
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import cv2
import numpy as np
import time
import math
from collections import deque

import mediapipe as mp
import pyautogui

# Disable PyAutoGUI pause for faster actions
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

class VirtualMouseController:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("Could not access webcam. Ensure it's connected and not used by another app.")

        # Screen size
        self.screen_w, self.screen_h = pyautogui.size()

        # MediaPipe Hands
        self.hands = mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.5
        )

        # Movement smoothing (dynamic)
        self.prev_mouse_x = None
        self.prev_mouse_y = None
        self.base_smooth_factor = 4.0   # higher = smoother (slower)
        self.max_smooth_factor = 6.5    # small movements get extra smoothing
        self.deadzone_px = 2            # ignore tiny jitter

        # Movement area reduction (pixels margin in camera frame)
        self.frame_reduction = 100

        # Click/drag debounce
        self.left_click_active = False
        self.right_click_active = False
        self.drag_active = False
        self.pinch_start_time = None
        self.drag_hold_seconds = 0.45  # hold pinch to start drag

        # Double-click support (two quick pinches)
        self.double_click_window = 0.35   # seconds between pinches
        self.last_click_time = None       # tracks last release-to-click time

        # Scroll
        self.scroll_mode = False
        self.scroll_last_y = None
        self.scroll_sensitivity = 1.4

        # History for stability (increase window)
        self.point_history = deque(maxlen=7)

        # Tip landmarks
        self.tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

    def fingers_up(self, lm_list):
        # Returns [thumb, index, middle, ring, pinky] booleans
        fingers = [False]*5
        if not lm_list:
            return fingers

        # Thumb: compare x coordinates (after horizontal flip, thumb open -> tip.x > ip.x for right hand)
        # This is a heuristic; we keep thumb mostly for pinch detection.
        thumb_tip = lm_list[4]
        thumb_ip = lm_list[3]
        fingers[0] = thumb_tip[0] > thumb_ip[0]

        # Other fingers: tip.y < pip.y means finger is up (y grows downwards)
        for i, tip_id in enumerate([8, 12, 16, 20], start=1):
            tip_y = lm_list[tip_id][1]
            pip_y = lm_list[tip_id - 2][1]
            fingers[i] = tip_y < pip_y

        return fingers

    def distance(self, p1, p2):
        return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

    def map_to_screen(self, x, y, img_w, img_h):
        # Limit movement to a reduced frame for better control
        x_min = self.frame_reduction
        x_max = img_w - self.frame_reduction
        y_min = self.frame_reduction
        y_max = img_h - self.frame_reduction

        x = int(np.clip(x, x_min, x_max))
        y = int(np.clip(y, y_min, y_max))

        # Interpolate to screen coordinates
        screen_x = np.interp(x, (x_min, x_max), (0, self.screen_w))
        screen_y = np.interp(y, (y_min, y_max), (0, self.screen_h))
        return int(screen_x), int(screen_y)

    def smooth_move(self, target_x, target_y):
        if self.prev_mouse_x is None or self.prev_mouse_y is None:
            self.prev_mouse_x, self.prev_mouse_y = target_x, target_y

        dx = target_x - self.prev_mouse_x
        dy = target_y - self.prev_mouse_y
        delta = math.hypot(dx, dy)

        # Dynamic smoothing: smaller movement → more smoothing, larger movement → less smoothing
        # Scale factor in [base_smooth_factor, max_smooth_factor] based on delta magnitude
        scale = 1.0 - min(delta / 150.0, 1.0)
        smooth_factor = self.base_smooth_factor + (self.max_smooth_factor - self.base_smooth_factor) * scale

        # Deadzone to suppress jitter
        if delta < self.deadzone_px:
            return

        new_x = self.prev_mouse_x + dx / smooth_factor
        new_y = self.prev_mouse_y + dy / smooth_factor

        self.prev_mouse_x, self.prev_mouse_y = new_x, new_y
        pyautogui.moveTo(int(new_x), int(new_y))

    def dynamic_threshold(self, lm_list, tip_id, pip_id, multiplier=1.8):
        # Use finger segment length as scale reference
        tip = lm_list[tip_id]
        pip = lm_list[pip_id]
        base = self.distance(tip, pip)
        return max(25.0, base * multiplier)

    def draw_ui(self, img, img_w, img_h):
        # Movement boundary rectangle
        cv2.rectangle(
            img,
            (self.frame_reduction, self.frame_reduction),
            (img_w - self.frame_reduction, img_h - self.frame_reduction),
            (255, 0, 255),
            2
        )
        # HUD
        hud = f"Scroll: {'ON' if self.scroll_mode else 'OFF'}  Drag: {'ON' if self.drag_active else 'OFF'}"
        cv2.putText(img, hud, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 200, 50), 2)

    def run(self):
        while True:
            ok, img = self.cap.read()
            if not ok:
                break

            # Flip horizontally for selfie-view
            img = cv2.flip(img, 1)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_h, img_w = img.shape[:2]

            results = self.hands.process(img_rgb)

            lm_list = []
            if results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]
                for id, lm in enumerate(hand.landmark):
                    cx, cy = int(lm.x * img_w), int(lm.y * img_h)
                    lm_list.append((cx, cy))

                # Optional: draw landmarks
                mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

            if lm_list:
                fingers = self.fingers_up(lm_list)
                index_tip = lm_list[8]
                middle_tip = lm_list[12]
                thumb_tip = lm_list[4]

                # Keep small history of index for steadier movement
                self.point_history.append(index_tip)
                avg_x = int(np.mean([p[0] for p in self.point_history]))
                avg_y = int(np.mean([p[1] for p in self.point_history]))

                # Gestures thresholds (dynamic with finger size)
                left_click_thresh = self.dynamic_threshold(lm_list, tip_id=8, pip_id=6, multiplier=1.6)
                right_click_thresh = self.dynamic_threshold(lm_list, tip_id=12, pip_id=10, multiplier=1.6)

                # Scroll mode: index + middle up
                if fingers[1] and fingers[2]:
                    self.scroll_mode = True
                else:
                    # Turn off when not both fingers up
                    if self.scroll_mode:
                        self.scroll_mode = False
                        self.scroll_last_y = None

                if self.scroll_mode:
                    # Use vertical delta to scroll
                    if self.scroll_last_y is not None:
                        dy = avg_y - self.scroll_last_y
                        # Negative dy -> scroll up (positive value in pyautogui.scroll)
                        scroll_amount = int(-dy * self.scroll_sensitivity)
                        if scroll_amount != 0:
                            pyautogui.scroll(scroll_amount)
                    self.scroll_last_y = avg_y
                    # In scroll mode, skip cursor movement
                else:
                    # Move cursor when only index is up (others down)
                    if fingers[1] and not fingers[2] and not fingers[3] and not fingers[4]:
                        screen_x, screen_y = self.map_to_screen(avg_x, avg_y, img_w, img_h)
                        self.smooth_move(screen_x, screen_y)

                # Left click & drag: thumb–index pinch
                pinch_dist = self.distance(thumb_tip, index_tip)
                left_click_thresh = self.dynamic_threshold(lm_list, tip_id=8, pip_id=6, multiplier=1.6)

                if pinch_dist < left_click_thresh and not self.scroll_mode:
                    # Pinch down
                    if not self.left_click_active:
                        # Potential drag start if held longer than drag_hold_seconds
                        self.pinch_start_time = time.time()
                    else:
                        # Already active; check drag hold
                        if self.pinch_start_time and not self.drag_active:
                            held = time.time() - self.pinch_start_time
                            if held >= self.drag_hold_seconds:
                                pyautogui.mouseDown()
                                self.drag_active = True
                    self.left_click_active = True
                else:
                    # Pinch up (release): decide click vs double-click vs drag release
                    if self.left_click_active:
                        now = time.time()
                        if self.drag_active:
                            pyautogui.mouseUp()
                            self.drag_active = False
                            self.last_click_time = None  # do not count drags toward double-clicks
                        else:
                            # Double-click detection: two quick pinches within window
                            if self.last_click_time and (now - self.last_click_time) <= self.double_click_window:
                                pyautogui.doubleClick()
                                self.last_click_time = None
                            else:
                                pyautogui.click()
                                self.last_click_time = now
                    self.left_click_active = False
                    self.pinch_start_time = None

                # Right click: thumb–middle pinch (unchanged)
                pinch_right = self.distance(thumb_tip, middle_tip)
                right_click_thresh = self.dynamic_threshold(lm_list, tip_id=12, pip_id=10, multiplier=1.6)
                if pinch_right < right_click_thresh and not self.right_click_active and not self.scroll_mode:
                    pyautogui.rightClick()
                    self.right_click_active = True
                elif pinch_right >= right_click_thresh:
                    self.right_click_active = False

            # UI
            self.draw_ui(img, img_w, img_h)

            cv2.putText(img, "Press 'Q' to quit", (10, img_h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)
            cv2.imshow("Gesture Controlled Virtual Mouse", img)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        vm = VirtualMouseController()
        vm.run()
    except Exception as e:
        print("Error:", e)