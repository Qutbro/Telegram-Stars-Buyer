# ⭐ Telegram Stars Buyer (TON / Fragment API)

**Telegram Stars Buyer** — это Python-инструмент для автоматической покупки и отправки **Telegram Stars** через **Fragment API** с оплатой через сеть **TON**.

Проект выполняет полный цикл покупки:

1. Поиск получателя Stars через Fragment  
2. Создание запроса покупки  
3. Получение транзакции TON  
4. Отправка TON через кошелёк  

---

# 🚀 Возможности

- 🔍 Поиск пользователя Telegram через Fragment API  
- ⭐ Покупка Telegram Stars  
- 💰 Автоматическая отправка TON транзакции  
- 🔗 Интеграция с Fragment  
- 🪙 Работа с TON blockchain  
- ⚡ Асинхронная работа через `asyncio`  
- 🧠 Автоматическое извлечение payload для транзакции  

---

# 🛠 Используемые технологии

- Python 3.10+
- httpx
- asyncio
- tonutils
- Fragment API
- TON blockchain

---

# 📁 Структура проекта

```
.
├── main.py
├── client.py
├── config.py
├── buystarstg
│   └── transaction.py
└── README.md
```

---

# ⚙️ Установка

## 1. Клонировать репозиторий

```bash
git clone https://github.com/qutbro/telegram-stars-buyer.git
cd telegram-stars-buyer
```

---

## 2. Установить зависимости

```bash
pip install httpx tonutils
```

---

# 🔐 Настройка

Перед запуском необходимо заполнить `config.py`.

---

## TON API

```python
API_TON = "YOUR_TONAPI_KEY"
```

Получить можно на:

```
https://tonapi.io
```

---

## MNEMONIC кошелька

```python
MNEMONIC = [
    "word1",
    "word2",
    "word3",
    ...
]
```

⚠ Никогда не публикуйте mnemonic в открытом репозитории.

---

## Fragment cookies

```python
DATA = {
    'stel_ssid': '',
    'stel_dt': '',
    'stel_ton_token': '',
    'stel_token': '',
}
```

---

## Fragment параметры

```python
FRAGMENT_HASH = ""
FRAGMENT_PUBLICKEY = ""
FRAGMENT_WALLETS = ""
FRAGMENT_ADDRES = ""
```

---

# ▶ Использование

Откройте `main.py` и укажите:

```python
USERNAME = "@username"
QUANTITY = 50
```

где:

- `USERNAME` — Telegram пользователь  
- `QUANTITY` — количество Stars  

---

## Запуск

```bash
python main.py
```

---

# 🔄 Как работает покупка

1️⃣ Fragment API ищет пользователя

```
searchStarsRecipient
```

2️⃣ Fragment создаёт запрос покупки

```
initBuyStarsRequest
```

3️⃣ Fragment возвращает данные TON транзакции

```
getBuyStarsLink
```

4️⃣ Скрипт отправляет TON через кошелёк

```
wallet.transfer()
```

---

# 💰 Пример логов

```
Кошелек успешно загружен
Сумма для отправки: 0.2200 TON
Decoded payload text: 50 Telegram Stars purchase
Транзакция отправлена
```

---

# ⚠ Безопасность

Никогда не публикуйте:

- mnemonic кошелька
- cookies Fragment
- TON API ключ

Рекомендуется использовать `.env`.

---

# 📄 Возможные улучшения

- поддержка нескольких кошельков
- CLI интерфейс
- GUI интерфейс
- покупка Stars для списка пользователей
- автоматический расчёт цены
- прокси поддержка
- Docker


---

# 👨‍💻 Назначение проекта

Проект предназначен для автоматизации покупки **Telegram Stars** через **Fragment** с оплатой в **TON**.
