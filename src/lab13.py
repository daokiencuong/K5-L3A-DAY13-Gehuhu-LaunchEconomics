"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd
from statistics import NormalDist

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is None:
        return 1 / p
    if k < 1:
        raise ValueError('k phải lớn hơn hoặc bằng 1')
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong khoảng [0, 1]')
    if k is None:
        return 1.0
    if k < 1:
        raise ValueError('k phải lớn hơn hoặc bằng 1')
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    ti_le = ti_le_thanh_cong(p, k)
    if ti_le == 0:
        raise ValueError('Không thể tính chi phí khi xác suất thành công bằng 0')
    return so_lan_chay_ky_vong(p, k) / ti_le


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay].copy()
        vuot_gioi_han = reqs['so_lan_chay'].astype(int) > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han,
                 ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = (runs['tokens_in'] / 1000 * gia_vao
                  + runs['tokens_out'] / 1000 * gia_ra)
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = (reqs['phut_xem_lai_simulated'].astype(float).sum()
               * luong_phut * he_so_xem_lai)
    lam_lai = (reqs['phut_lam_lai_simulated'].astype(float).sum()
               * luong_phut * he_so_lam_lai)
    tong = float(tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai)
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong else math.inf
    hoa_don_moi_yc = ((float(tien_token.sum()) + float(tien_tool.sum())) / len(reqs)
                      if len(reqs) else 0.0)

    return {
        'token': float(tien_token.sum()),
        'tool': float(tien_tool.sum()),
        'chay_lai': float((tien_token + tien_tool)[runs['attempt'] > 1].sum()),
        'xem_lai': float(xem_lai),
        'lam_lai': float(lam_lai),
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': cps,
        'hoa_don_moi_yc': hoa_don_moi_yc,
    }


def in_bang_a3(runs, reqs):
    """In A3 theo từng loại, đồng thời trả kết quả để điền A4."""
    ket_qua_theo_loai = {}
    print('\nA3 · Chi phí theo loại yêu cầu')
    print(f"{'Loại':12s} {'Yêu cầu':>9s} {'Thành công':>12s} {'Tỉ lệ':>8s} "
          f"{'Lần/yêu cầu':>13s} {'Chi phí thành công':>21s} {'/ 12.000đ':>11s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        nhom = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, nhom)
        n = len(nhom)
        ket_qua_theo_loai[loai] = kq
        ti_le = kq['thanh_cong'] / n if n else 0
        lan_chay = nhom['so_lan_chay'].astype(float).sum() / n if n else 0
        print(f"{loai:12s} {n:9d} {kq['thanh_cong']:12d} {ti_le:7.1%} "
              f"{lan_chay:13.2f} {kq['cps']:21,.0f} {kq['cps']/BASELINE:10.2f}x")
    return ket_qua_theo_loai


def in_bang_a4(runs, reqs):
    """Cộng chi phí cố định tháng cho phạm vi noi_dia + hang_nang."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq = mo_hinh(runs, pham_vi)
    so_thanh_cong_mau = kq['thanh_cong']
    cps_bien_doi = kq['cps']
    print('\nA4 · Chi phí cố định (noi_dia + hang_nang)')
    print(f"{'Khối lượng/tháng':24s} {'Thành công/tháng':>18s} "
          f"{'Cố định/việc':>15s} {'CPS + cố định':>16s} {'/ 12.000đ':>11s}")
    for nhan, khoi_luong in [('45.000 yêu cầu/tháng', 45000),
                             ('Một nửa khối lượng', 22500)]:
        # 45.000 là tổng volume thị trường; phần hoàn thành trong pilot scope
        # lấy theo số thành công trên toàn bộ mẫu (900/1.200).
        thanh_cong_thang = khoi_luong * so_thanh_cong_mau / len(reqs)
        co_dinh_moi_viec = 40_000_000 / thanh_cong_thang
        cps_tong = cps_bien_doi + co_dinh_moi_viec
        print(f"{nhan:24s} {thanh_cong_thang:18,.0f} "
              f"{co_dinh_moi_viec:15,.0f} {cps_tong:16,.0f} "
              f"{cps_tong/BASELINE:10.2f}x")


def in_bang_b(runs, reqs):
    """Tính độ nhạy B1–B4 từ cùng mô hình chi phí A2."""
    goc = mo_hinh(runs, reqs)
    cps_goc = goc['cps']
    kich_ban = [
        ('Giá token gấp đôi', dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa', dict(gia_vao=13, gia_ra=65)),
        ('Tỉ lệ xem lại gấp đôi', dict(he_so_xem_lai=2)),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', dict(he_so_lam_lai=2)),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', dict(luong_phut=2500)),
        ('Chỉ cho chạy tối đa 2 lần', dict(max_lan_chay=2)),
        ('Chỉ cho chạy 1 lần', dict(max_lan_chay=1)),
    ]

    print('\nB1 · Độ nhạy từng yếu tố (so với A2)')
    print(f"{'Kịch bản':30s} {'CPS (đ)':>12s} {'Thay đổi':>11s}")
    for ten, tham_so in kich_ban:
        kq = mo_hinh(runs, reqs, **tham_so)
        thay_doi = (kq['cps'] / cps_goc - 1) * 100
        print(f"{ten:30s} {kq['cps']:12,.0f} {thay_doi:+10.1f}%")

    cap_doi = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260,
                      he_so_xem_lai=2)
    cap_doi_pct = (cap_doi['cps'] / cps_goc - 1) * 100
    print(f"\nB2 · Token và xem lại cùng gấp đôi: "
          f"{cap_doi['cps']:,.0f} đ ({cap_doi_pct:+.1f}%)")
    print('Xếp hạng: 1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên')

    print('\nB3 · Chi phí cả hệ thống khi giới hạn số lần chạy')
    print(f"{'Giới hạn':>10s} {'Chi phí trợ lý':>18s} {'Không thành công':>18s} "
          f"{'Chi phí hệ thống':>18s} {'CPS':>12s}")
    for gioi_han in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        that_bai = len(reqs) - kq['thanh_cong']
        chi_phi_he_thong = kq['tong'] + BASELINE * that_bai
        print(f"{gioi_han:10d} {kq['tong']:18,.0f} {that_bai:18d} "
              f"{chi_phi_he_thong:18,.0f} {kq['cps']:12,.0f}")

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    ids_pham_vi = set(pham_vi['request_id'])
    runs_pham_vi = runs[runs['request_id'].isin(ids_pham_vi)]
    so_can_xem = runs_pham_vi.loc[
        runs_pham_vi['status'] == 'ok', 'request_id'
    ].nunique()
    so_ca_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    tien_token_tool = float(
        (runs_pham_vi['tokens_in'] / 1000 * GIA_VAO
         + runs_pham_vi['tokens_out'] / 1000 * GIA_RA
         + runs_pham_vi['tool_calls'] * GIA_TOOL).sum()
    )
    tong_xem_100 = tien_token_tool + so_can_xem * 5 * LUONG_PHUT \
        + so_ca_lam_lai * 9 * LUONG_PHUT
    cps_xem_100 = tong_xem_100 / int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    # Hướng dẫn B4 yêu cầu kiểm tra độ nhạy bằng mức trung bình 15,3 phút
    # trên toàn bộ ca làm lại, áp vào 48 ca làm lại trong phạm vi pilot.
    phut_lam_lai_tb = reqs.loc[
        reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'
    ].astype(float).mean()
    tong_xem_100_thuc_te = tien_token_tool + so_can_xem * 5 * LUONG_PHUT \
        + so_ca_lam_lai * phut_lam_lai_tb * LUONG_PHUT
    cps_xem_100_thuc_te = tong_xem_100_thuc_te / int(
        (pham_vi['ket_qua'] == 'thanh_cong').sum()
    )
    print('\nB4 · Xem lại 100% (noi_dia + hang_nang)')
    print(f"Yêu cầu có ít nhất một lần chạy ok: {so_can_xem}; "
          f"làm lại: {so_ca_lam_lai}; token + tool: {tien_token_tool:,.0f} đ")
    print(f"Giả định làm lại 9 phút: {cps_xem_100:,.0f} đ/việc "
          f"({cps_xem_100/BASELINE:.2f}x); theo thời gian simulated "
          f"{phut_lam_lai_tb:.1f} phút/ca: {cps_xem_100_thuc_te:,.0f} đ "
          f"({cps_xem_100_thuc_te/BASELINE:.2f}x)")


def co_mau_hai_ty_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhánh cho kiểm định hai tỷ lệ độc lập."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    tu_so = (za * math.sqrt(2 * p_bar * (1 - p_bar))
             + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(tu_so / (p2 - p1) ** 2)


def in_bang_d(reqs):
    """Tính D1 và in các câu trả lời thiết kế D2 để ghi vào pilot_plan.yaml."""
    p1, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    n_5_diem = co_mau_hai_ty_le(p1, 0.75, alpha, power)
    n_6_diem = co_mau_hai_ty_le(p1, 0.76, alpha, power)

    de_staff_75 = 1 + (75 - 1) * icc
    n_staff_75 = math.ceil(n_5_diem * de_staff_75)
    staff_each_needed = math.ceil(n_staff_75 / 75)
    max_neff_20_staff = 20 / icc
    max_neff_6_depot = 6 / icc

    n_staff_each = 20
    m = 1
    while n_staff_each * m / (1 + (m - 1) * icc) < n_6_diem:
        m += 1
    de_m = 1 + (m - 1) * icc
    n_eff = n_staff_each * m / de_m

    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize
    power_at_5 = NormalIndPower().power(
        effect_size=proportion_effectsize(0.70, 0.75),
        nobs1=n_6_diem, alpha=alpha, ratio=1, alternative='two-sided'
    )

    print('\nD1 · Cỡ mẫu và hệ số thiết kế')
    print(f"Chia theo yêu cầu: {n_5_diem:,} yêu cầu/nhóm cho MDE 5 điểm.")
    print(f"Theo nhân viên, m=75: DE={de_staff_75:.2f}; "
          f"{n_staff_75:,} yêu cầu/nhóm, cần {staff_each_needed} nhân viên/nhóm "
          f"({staff_each_needed * 2} tổng), không đủ 40.")
    print(f"20 nhân viên/nhóm: tối đa c/ICC={max_neff_20_staff:,.0f} mẫu hiệu dụng, "
          f"thấp hơn {n_5_diem:,}.")
    print(f"6 depot/nhóm: tối đa c/ICC={max_neff_6_depot:,.0f} mẫu hiệu dụng.")
    print(f"MDE 6 điểm: {n_6_diem} mẫu hiệu dụng/nhóm; 20 nhân viên/nhóm cần "
          f"m={m} yêu cầu/nhân viên, DE={de_m:.2f}, n_eff={n_eff:.1f}.")
    print(f"Nếu hiệu ứng thật chỉ là 5 điểm, power tại n_eff={n_6_diem} "
          f"còn {power_at_5:.2f}.")

    reopen_all = reqs['mo_lai_trong_7_ngay'].astype(int).mean()
    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    reopen_scope = scope['mo_lai_trong_7_ngay'].astype(int).mean()
    print(f"Mở lại trong 7 ngày hiện tại: {reopen_all:.2%} toàn mẫu "
          f"({int(reqs['mo_lai_trong_7_ngay'].astype(int).sum())}/{len(reqs)}); "
          f"{reopen_scope:.2%} trong phạm vi pilot.")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    in_bang_a3(runs, reqs)
    in_bang_a4(runs, reqs)
    in_bang_b(runs, reqs)
    in_bang_d(reqs)
