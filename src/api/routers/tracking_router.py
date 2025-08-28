from fastapi import APIRouter, UploadFile, File , HTTPException
from ...tracking.object_tracking import ObjectTracking
from ...tests.drawScapter import draw_scatter
# 1. Khởi tạo một đối tượng APIRouter
#    - prefix: Thêm tiền tố /tracking vào tất cả các URL của router này.
#    - tags: Nhóm các endpoint này dưới một thẻ tên là "Object Tracking" trong tài liệu API.
tracking_router  = APIRouter(
    prefix="/api/v1",
    tags=["Object Tracking"]
)

# Khởi tạo tracker một lần để tái sử dụng
object_tracker = ObjectTracking()


@tracking_router.get("/tracking_video")
async def track_video( ):
 
    try:
        result = object_tracker.run_stream()
        draw_scatter(result)
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