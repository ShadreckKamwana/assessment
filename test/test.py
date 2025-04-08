from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Replace with yolov12n.pt when available
model.export(format="tflite")
