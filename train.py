from ultralytics import YOLO

# Load a pretrained YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Train
model.train(
    data=r"D:\Projects\Fall_detection\fall_dataset\venv\data.yaml",
    epochs=20,
    imgsz=640,
    batch=8,
    device='cpu'  # GPU if available; use "cpu" if not
)
