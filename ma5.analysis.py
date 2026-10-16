import akshare as ak
import pandas as pd

print("正在获取数据，请稍等...")
# 1. 获取平安银行近期数据
stock_data = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20240101", end_date="20241014")

# 2. 计算5日均线（MA5）
# 公式：收盘价 -> 滚动5行 -> 求平均
stock_data['MA5'] = stock_data['收盘'].rolling(window=5).mean()

# 3. 打印查看带有MA5的数据
print("数据计算成功！")
print(stock_data[['日期', '收盘', 'MA5']].head(10)) # 只显示日期、收盘、MA5这三列，方便看