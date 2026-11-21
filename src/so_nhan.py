"""So hai bộ nhãn độc lập của Nhiệm vụ C.
Chạy trong src/ sau khi đã merge cả hai branch nhãn:  python so_nhan.py
Đọc ../report/team/nhan_nguoi_1.md và ../report/team/nhan_nguoi_2.md (bảng | Ca | Nhãn |).
"""
import re
import sys

MA = {'ND': 'Do người dùng', 'HT': 'Hệ thống', 'NC': 'Ngữ cảnh',
      'GH': 'Giới hạn hệ thống', 'NG': 'Ngầm'}


def doc_nhan(duong_dan):
    nhan = {}
    with open(duong_dan, encoding='utf-8') as f:
        for dong in f:
            m = re.match(r'^\|\s*(\d+)\s*\|\s*([A-Za-z]*)\s*\|', dong)
            if m:
                nhan[int(m.group(1))] = m.group(2).upper()
    return nhan


n1 = doc_nhan('../report/team/nhan_nguoi_1.md')
n2 = doc_nhan('../report/team/nhan_nguoi_2.md')

loi = [f'người {i}, ca {ca}: "{ma}"' for i, n in ((1, n1), (2, n2))
       for ca, ma in sorted(n.items()) if ma not in MA]
thieu = [f'người {i}, ca {ca}' for i, n in ((1, n1), (2, n2))
         for ca in range(1, 21) if ca not in n]
if loi or thieu:
    print('Chưa so được, còn ô trống hoặc mã sai:', '; '.join(thieu + loi))
    sys.exit(1)

trung = 0
print(f'{"Ca":>3}  {"Người 1":18s} {"Người 2":18s} Trùng?')
for ca in range(1, 21):
    ok = n1[ca] == n2[ca]
    trung += ok
    print(f'{ca:>3}  {MA[n1[ca]]:18s} {MA[n2[ca]]:18s} {"có" if ok else "KHÔNG"}')
print(f'\nTỉ lệ đồng thuận: {trung} / 20 = {trung / 20:.0%}'
      + ('' if trung >= 16 else '  → dưới 80%: viết lại định nghĩa trước khi đi tiếp'))
