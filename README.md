# MC Digger Tool 🎮⛏️

Một script Python tự động đào khu vực trong Minecraft Java Edition. Hỗ trợ cả **Single Player** và **Server**.

## 🌟 Tính năng

✅ Đào khu vực tự động với kích thước tuỳ chỉnh
✅ Điều chỉnh độ sâu linh hoạt
✅ Tự động thay đổi công cụ phù hợp (pickaxe, axe, shovel)
✅ Hỗ trợ Single Player & Server
✅ Logging chi tiết
✅ Giao diện dễ sử dụng
✅ Cấu hình tuỳ chỉnh

## 📋 Yêu cầu

- Python 3.8+
- Minecraft Java Edition
- Các thư viện Python (xem `requirements.txt`)

## 🚀 Cài đặt

### 1. Clone repository
```bash
git clone https://github.com/duyanhggg/mc-digger-tool.git
cd mc-digger-tool
```

### 2. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 3. Cấu hình
Chỉnh sửa file `config.py`:

```python
# Minecraft Server Configuration
SERVER_HOST = "localhost"  # IP hoặc domain
SERVER_PORT = 25565        # Port (mặc định 25565)
USERNAME = "YourUsername"  # Tên người chơi
OFFLINE_MODE = True        # True cho Single Player/offline server

# Digger Configuration
DIG_WIDTH = 10             # Rộng (X axis)
DIG_LENGTH = 10            # Dài (Z axis)
DIG_DEPTH = 5              # Sâu (Y axis)
DIG_INTERVAL = 5           # Cách bao nhiêu block thì đào tiếp
```

## 💻 Sử dụng

### Chạy script
```bash
python main.py
```

### Interactive Mode
Script sẽ hỏi bạn:
```
Width (X axis) [default: 10]: 15
Length (Z axis) [default: 10]: 20
Depth (Y axis) [default: 5]: 8
Dig interval (blocks) [default: 5]: 3

Start mining? (y/n): y
```

## 📝 Cấu trúc File

```
mc-digger-tool/
├── main.py              # Script chính
├── config.py            # File cấu hình
├── requirements.txt     # Dependencies
├── README.md           # Hướng dẫn này
└── .gitignore          # Git ignore
```

## ⚙️ Cấu hình Chi Tiết

### config.py

| Tham số | Mô tả | Mặc định |
|---------|-------|---------|
| `SERVER_HOST` | Địa chỉ server | `localhost` |
| `SERVER_PORT` | Port kết nối | `25565` |
| `USERNAME` | Tên người chơi | `YourUsername` |
| `OFFLINE_MODE` | Chế độ offline | `True` |
| `DIG_WIDTH` | Chiều rộng khu vực | `10` |
| `DIG_LENGTH` | Chiều dài khu vực | `10` |
| `DIG_DEPTH` | Độ sâu đào | `5` |
| `DIG_INTERVAL` | Khoảng cách giữa các lần đào | `5` |
| `DEBUG_MODE` | Chế độ debug | `True` |

### TOOLS Mapping

Tự động chọn công cụ phù hợp cho từng loại khối:

```python
TOOLS = {
    "stone": "wooden_pickaxe",
    "cobblestone": "wooden_pickaxe",
    "dirt": "wooden_shovel",
    "grass": "wooden_shovel",
    "sand": "wooden_shovel",
    "gravel": "wooden_shovel",
    "wood": "wooden_axe",
    "oak_log": "wooden_axe",
}
```

## 📊 Logging

Log được lưu vào `digger.log`:
```
2026-01-02 10:30:45,123 - INFO - MC Digger Tool initialized
2026-01-02 10:30:45,456 - INFO - Configuration: 10x10x5
```

## 🎯 Các Mode Hoạt Động

### Mode 1: Single Player
- Set `OFFLINE_MODE = True`
- Set `SERVER_HOST = "localhost"`
- Chạy Minecraft Single Player
- Chạy script

### Mode 2: Server
- Set `OFFLINE_MODE = False`
- Set `SERVER_HOST = "your.server.ip"`
- Set `SERVER_PORT = 25565` (hoặc cổng đúng)
- Set `USERNAME = "YourUsername"`
- Chạy script

## ⚠️ Lưu Ý Quan Trọng

⚠️ **Cảnh báo**: 
- Hãy sử dụng công cụ này có trách nhiệm
- Không sử dụng trên server công cộng mà không có quyền
- Luôn backup thế giới trước khi chạy script
- Có thể gây lag nếu đào quá nhiều cùng một lúc

## 🐛 Troubleshooting

### Lỗi: "Connection refused"
```
→ Kiểm tra SERVER_HOST và SERVER_PORT
→ Kiểm tra server có running không
```

### Lỗi: "Invalid username"
```
→ Kiểm tra USERNAME trong config.py
→ Kiểm tra OFFLINE_MODE setting
```

### Script không đào gì
```
→ Kiểm tra DIG_WIDTH, DIG_LENGTH, DIG_DEPTH
→ Kiểm tra DIG_INTERVAL (nên ≤ WIDTH, LENGTH)
```

## 🤝 Đóng Góp

Issues và PRs được chào đón! 

## 📄 License

MIT License - Thoải mái sử dụng

## 👨‍💻 Tác Giả

**duyanhggg** - Creator

## 📞 Support

Nếu có vấn đề, tạo Issue trên GitHub repo này.

---

**Happy Mining!** ⛏️✨