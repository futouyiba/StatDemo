import pandas as pd
from update_excel import update_excel_with_dataframe

# 示例：假设我们有一个Excel文件和一个更新的DataFrame

# 1. 加载更新的DataFrame（示例数据）
# 这里假设您已经有了DataFrame，例如从某个数据处理过程中得到
df = pd.DataFrame({
    '产品': ['产品A', '产品B', '产品C'],
    '销量': [120, 150, 90],
    '价格': [25.5, 30.0, 15.75]
})

# 2. 定义Excel与DataFrame的列映射关系
# 例如：DataFrame的'产品'列对应Excel的第2列(B列)，'销量'对应第4列(D列)，'价格'对应第5列(E列)
column_mapping = {
    '产品': 2,  # B列
    '销量': 4,  # D列
    '价格': 5   # E列
}

# 3. 更新Excel文件
excel_path = "E:/DocsHDD/FGame/中鱼/StatDemo/example_report.xlsx"
sheet_name = "数据"

update_excel_with_dataframe(
    excel_path=excel_path,
    sheet_name=sheet_name,
    df=df,
    start_row=5,  # 数据从第5行开始（前4行是表头和说明）
    start_col=1,  # 数据从第1列开始（A列）
    column_mapping=column_mapping
)

print("示例完成！")
