import time
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

current_timestamp = int(time.time())
# 设置随机种子以保证结果可重复
np.random.seed(current_timestamp)

# 定义数据大小
n = 10000

# 生成数据
data = {
    'ID': np.arange(n),
    'FloatValue': np.random.randn(n),
    'StringValue': [''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), 10)) for _ in range(n)],
    'DateTimeValue': [datetime.now() - timedelta(days=np.random.randint(0, 365)) for _ in range(n)]
}

# 创建DataFrame
df = pd.DataFrame(data)
print(df)
# 输出为Parquet文件
output_file = 'random_data.parquet'
df.to_parquet(output_file, engine='pyarrow', compression=None)

print(f"Data has been written to {output_file}")
