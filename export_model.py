from ultralytics import YOLO

# Tải model .pt gốc
print("Đang tải model yolov8n.pt...")
model = YOLO('models/yolov8n.pt')

# Xuất ra định dạng OpenVINO
print("Đang tối ưu hóa sang OpenVINO...")
# Lệnh này sẽ tạo ra thư mục 'yolov8n_openvino_model'
model.export(format='openvino') 

print("Hoàn thành! Model đã được lưu tại thư mục 'models/yolov8n_openvino_model'.")