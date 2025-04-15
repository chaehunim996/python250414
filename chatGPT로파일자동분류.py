import os
import shutil

# 다운로드 폴더 경로
downloads_path = r"C:\Users\student\Downloads"

# 이동할 폴더 설정
file_destinations = {
    "images": ['.jpg', '.jpeg'],
    "data": ['.csv', '.xlsx'],
    "docs": ['.txt', '.doc', '.pdf'],
    "archive": ['.zip']
}

# 이동 실행
def organize_downloads(download_path, destinations):
    for folder, extensions in destinations.items():
        # 대상 폴더 경로 생성
        dest_path = os.path.join(download_path, folder)
        # 폴더가 없으면 만든다
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        # 다운로드 폴더 내 모든 파일 검색
        for file_name in os.listdir(download_path):
            file_path = os.path.join(download_path, file_name)

            # 파일인지 확인 (디렉토리 무시)
            if os.path.isfile(file_path):
                # 파일 확장자 가져오기
                _, ext = os.path.splitext(file_name)
                if ext.lower() in extensions:
                    # 이동할 경로 지정
                    new_path = os.path.join(dest_path, file_name)
                    print(f"Moving: {file_name} → {folder}")
                    shutil.move(file_path, new_path)

# 실행
if __name__ == "__main__":
    organize_downloads(downloads_path, file_destinations)
