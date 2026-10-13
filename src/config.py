from pathlib import Path

# Пути к папкам
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SRC_DIR = BASE_DIR / "src"

# Значения для поиска скрытых пропусков
MISSING_MARKERS = ['', ' ', 'N/A', 'n/a', 'NA', 'null', 'NULL', 'None', 'nan']

# Дни недели
DAYS = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

