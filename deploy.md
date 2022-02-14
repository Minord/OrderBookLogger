
# Create the data base

```bash
sqlite order-book-binance.db
sqlite order-book-binance.db "CREATE TABLE order_book (time timestamp, json text);"
```

# Execute Program on background
``` bash
nohup python3 booklogger.py
```

# Stop Program
``` bash
htop  #find program id
kill id
```
