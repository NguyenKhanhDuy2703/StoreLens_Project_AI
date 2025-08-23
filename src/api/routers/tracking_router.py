from fastapi import APIRouter, UploadFile, File , HTTPException
from ...tracking.object_tracking import ObjectTracking
import os
import tempfile
import shutil

# 1. Khởi tạo một đối tượng APIRouter
#    - prefix: Thêm tiền tố /tracking vào tất cả các URL của router này.
#    - tags: Nhóm các endpoint này dưới một thẻ tên là "Object Tracking" trong tài liệu API.
tracking_router  = APIRouter(
    prefix="/api/v1",
    tags=["Object Tracking"]
)

# Khởi tạo tracker một lần để tái sử dụng
object_tracker = ObjectTracking()

DEFAULT_VIDEO_PATH = r"D:\NCKH\AI2\src\data\videos\video_2.mp4"
DEFAULT_IMAGE_PATH = r"D:\NCKH\AI2\src\data\images\image_1.jpg"
# 2. Định nghĩa endpoint trên đối tượng `router` thay vì `app`

@tracking_router.post("/tracking_video")
async def track_video( video_file: UploadFile = File(...)):
 
    try:
        result = object_tracker.track_video(DEFAULT_VIDEO_PATH)
        return result
    except FileNotFoundError as e:
        # 404 Not Found
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        # 400 Bad Request
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # 500 Internal Server Error
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@tracking_router.get("/health")
def check_health():
    return {"status": "Tracking router is healthy"}