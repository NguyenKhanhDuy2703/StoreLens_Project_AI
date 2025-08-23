from ultralytics import YOLO

class YOLOv8Model:
    def __init__(self , config):
        # lấy thông số từ config
        model_path = config['yolov8']['model_path']
        self.conf_threshold = config['yolov8']['confidence_threshold']
        self.model = YOLO(model_path)
        self.classes = config['yolov8']['classes']
        self.iou_threshold = config['yolov8']['iou_threshold']

    
    
    def predict_frame(self, frame):
        # tạo function dự đoán frame với yolo model 
        # Tham số đầu vào là frame hình ảnh
        # Tham số đầu ra là kết quả dự đoán
        # tạo model với các tham số từ config 
        results = self.model(frame, conf=self.conf_threshold , classes=self.classes, iou=self.iou_threshold) 
        return results