import cv2
import numpy as np

#pip install opencv-python
def draw_grid(frame, grid_size):
    
    w=638
    h=478
    x1=int(640//2)
    y1=int(480//2)
    for xxx in range(0,641,128):
        cv2.line(frame, (x1, y1), (xxx, 480), (255, 255, 255), 1)
        cv2.line(frame, (x1, y1), (xxx, 0), (255, 255, 255), 1)
        if xxx < 481:
            cv2.line(frame, (x1, y1), (0,xxx), (255, 255, 255), 1)
            cv2.line(frame, (x1, y1), (639,xxx), (255, 255, 255), 1)
    for xxx in range(18):
        cv2.line(frame, (x1-w//2, y1-h//2), (x1+w//2, y1-h//2), (255, 255, 255), 1)
        cv2.line(frame, (x1-w//2, y1-h//2), (x1-w//2, y1+h//2), (255, 255, 255), 1)
        cv2.line(frame, (x1-w//2, y1+h//2), (x1+w//2,y1+h//2), (255, 255, 255), 1)
        cv2.line(frame, (x1+w//2, y1-h//2), (x1+w//2, y1+h//2), (255, 255, 255), 1)
        w=int(w*100//120)
        h=int(h*100//120)

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    grid_size = 16

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Espelhar a imagem
        frame = cv2.flip(frame, 1)

        # Desenhar a grade
        draw_grid(frame, grid_size)

        # Mostrar a imagem
        cv2.imshow('Augmented Reality Grid', frame)

        # Sair ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

