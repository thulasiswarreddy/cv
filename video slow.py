
import cv2

video_path = "/Users/eswar/Desktop/video.mp4"

def play_video(delay, title):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video not found! Check the file path.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow(title, frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

play_video(100, "Slow Motion")
play_video(1, "Fast Motion")
cv2.destroyAllWindows()
