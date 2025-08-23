# 🎯 Dự án Theo dõi Đối tượng với YOLOv8 + DeepSORT  

Hệ thống theo dõi đối tượng trong video sử dụng **YOLOv8** để phát hiện và **DeepSORT** để theo dõi. Toàn bộ logic được đóng gói thành **Web API** với **FastAPI**.  

---

## 🚀 Hướng dẫn Bắt đầu Nhanh  

### 1️⃣ Cài đặt (Setup)  

#### a. Tạo và kích hoạt môi trường ảo  

```bash
# 1. Tạo môi trường ảo
python -m venv venv

# 2. Kích hoạt môi trường
# Trên Windows (có thể có hoặc không)
venv\Scripts\activate
```

#### b. Cài đặt thư viện cần thiết  

```bash
pip install -r requirements.txt
```

#### c. Tải model cần thiết  

- **DeepSORT:** Tải file `ckpt.t7` và đặt vào thư mục `Models/deepsort/`.  
- **YOLOv8:** Đảm bảo file `yolov8n.pt` (hoặc phiên bản khác) nằm trong thư mục `Models/`.  

---

### 2️⃣ Tối ưu hóa Model (Chạy 1 lần duy nhất)  

Chuyển đổi YOLOv8 sang định dạng **OpenVINO** để tăng tốc độ xử lý:  

```bash
python export_model.py
```

Sau khi chạy, kiểm tra lại `tracking_config.yaml` trỏ đúng tới model OpenVINO mới trong `Models/`.  

---

### 3️⃣ Chạy ứng dụng  

```bash
uvicorn run:app --reload
```

Ứng dụng sẽ chạy tại: 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## 📂 Cấu trúc Dự án  

```
.
├── Models/                     # Chứa các model đã tải và tối ưu hóa
│   ├── deepsort/
│   │   └── ckpt.t7
│   └── yolov8n_openvino_model/
│
├── src/                        # Mã nguồn chính
│   ├── api/                    # Logic API
│   │   ├── routers/
│   │   │   └── tracking_router.py
│   │   └── api.py
│   ├── configs/                # File cấu hình
│   │   └── tracking_config.yaml
│   ├── tracking/               # AI core (YOLOv8 + DeepSORT)
│   │   ├── object_tracking.py
│   │   ├── yolov8_model.py
│   │   └── deepsort_model.py
│   └── utils/                  # Hàm tiện ích
│       └── config_loader.py
│
├── tests/                      # Unit tests
├── Readme.md                   # Tài liệu hướng dẫn
├── requirements.txt            # Thư viện cần thiết
├── export_model.py             # Script tối ưu hóa YOLOv8 → OpenVINO
└── run.py                      # File khởi chạy server
```

---

## 📖 Mô tả Thành phần  

- **`run.py`** – File khởi chạy server API (FastAPI + Uvicorn).  
- **`export_model.py`** – Chuyển đổi YOLOv8 sang OpenVINO để tăng tốc.  
- **`requirements.txt`** – Danh sách dependency.  
- **`Models/`** – Lưu trữ các file model (YOLOv8, DeepSORT).  
- **`src/api/`** – Định nghĩa endpoint & logic request/response.  
  - `tracking_router.py` – Router cho chức năng tracking.  
- **`src/configs/tracking_config.yaml`** – File config trung tâm (tham số YOLO + DeepSORT).  
- **`src/tracking/`** – Bộ não AI:  
  - `object_tracking.py` – Điều phối YOLO + DeepSORT.  
  - `yolov8_model.py` – Quản lý YOLOv8.  
  - `deepsort_model.py` – Quản lý DeepSORT.  
- **`src/utils/`** – Tiện ích (ví dụ: `config_loader.py` để đọc YAML).  

---

## ✅ Yêu cầu hệ thống  

- Python ≥ 3.8  
- FastAPI + Uvicorn  
- Ultralytics YOLOv8  
- OpenVINO Runtime  
- Torch, TorchVision  

---

## 📌 Ghi chú  

- Sau khi tối ưu, nên luôn dùng model OpenVINO để đạt tốc độ tốt nhất.  
- Có thể mở rộng thêm tracker khác (ByteTrack, StrongSORT) bằng cách thêm class trong `src/tracking/`.  
