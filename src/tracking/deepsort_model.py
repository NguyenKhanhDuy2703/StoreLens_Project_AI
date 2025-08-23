# tạo phương thức của depsort model
from deep_sort_realtime.deepsort_tracker import DeepSort


class DeepSortModel:
    def __init__(self , config):
        # Lấy toàn bộ phần config của deepsort
        deepsort_config = config['deepsort']
        # Truyền trực tiếp các giá trị vào hàm khởi tạo
        # mà không cần lưu chúng vào self một cách riêng lẻ
        self.model = DeepSort(
            max_age=deepsort_config['max_age'],
            n_init=deepsort_config['n_init'],
            max_cosine_distance=deepsort_config['max_cosine_distance'],
            nn_budget=deepsort_config['nn_budget']
        )
    def tracker_predict(self , detections , frame):
        # tạo function dự đoán frame với deepsort model 
        # Tham số đầu vào là detections từ yolo model và frame hình ảnh
        # Tham số đầu ra là kết quả dự đoán
        tracks = self.model.update_tracks(detections, frame=frame) 
        return tracks
        