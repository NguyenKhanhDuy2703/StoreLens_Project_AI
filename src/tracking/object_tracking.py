from ..utils.config_loader import load_config
import cv2
from .yolov8_model import YOLOv8Model
from .deepsort_model import DeepSortModel

class ObjectTracking:
    def __init__(self, config_path='src/configs/tracking_config.yaml'):
        config = load_config(config_path)
        self.yolo_model = YOLOv8Model(config)
        self.deepsort_model = DeepSortModel(config)
        # Không cần return ở đây

    def Transform_YOLO_to_DeepSort(self, results):
        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                w = x2 - x1
                h = y2 - y1
                detections.append(([x1, y1, w, h], conf, cls))
        return detections

    def track_video(self, video_file):
        data_tracking = {}
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            raise FileNotFoundError(f"Could not open video file: {video_file}")
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            results = self.yolo_model.predict_frame(frame)
            detections = self.Transform_YOLO_to_DeepSort(results)
            tracks = self.deepsort_model.tracker_predict(detections, frame)

            if tracks:
                for track in tracks:
                    if not track.is_confirmed():
                        continue
                    track_id = track.track_id
                    bbox = track.to_tlbr() 
                    cls = track.get_det_class() # Lấy lớp của đối tượng
                    
                    x1, y1, x2, y2 = map(int, bbox)
                    if track_id not in data_tracking:
                        data_tracking[track_id] = {
                            'class': cls,
                            'positions': []
                        }
                    x_foot = int((x1 + x2) / 2)
                    y_foot = y2
                    data_tracking[track_id]['positions'].append((x_foot, y_foot))
                    
                    # Vẽ hcn và id lên frame
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f'ID: {track_id}', (x1, y1 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.imshow('Tracking', frame) # Hiển thị 'frame'
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        cap.release()
        cv2.destroyAllWindows()
        return data_tracking