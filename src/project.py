# -*- coding: utf-8 -*-
"""Tab HDSD app Base Project (dự án Hợp đồng Mẫu), đọc từ project.base.vn ngày 20/11/2026."""
import html
URL = "https://project.base.vn/service/aFBcKoH7-jMrHFtqV4a-LUTQ8isznxo"

def sh(img, *pins): return dict(img=img, pins=list(pins))

SECTIONS = [
 ("pj-list", "Mở dự án từ danh sách", "Mọi người", "Vào app **Dự án** ở thanh trái để thấy các dự án bạn tham gia.",
  ["Xem 3 cách hiển thị: **Danh sách**, **Bảng biểu**, **Bảng** (góc phải trên).", "Lọc nhanh bằng thẻ **Tất cả / Có rủi ro / Đến hạn trong 30 ngày**.", "Bấm tên dự án (ví dụ **Hợp đồng Mẫu**, mã HNAD1) để vào dự án.", "Bấm **Dự án mới** để tạo dự án. Chọn nghiệp vụ **Dự án công ty** rồi điền thông tin (chỉ người được cấp quyền)."],
  [sh("pj-list", "Bấm **Dự án mới** để tạo dự án.", "Chuyển giữa **Danh sách / Bảng biểu / Bảng**.", "Thẻ lọc: Tất cả, Có rủi ro, Đến hạn trong 30 ngày, Phí trọn gói.", "Hàng dự án: tiến độ công việc (**6/14**), trạng thái, hạn chốt.")]),
 ("pj-over", "Tổng quan dự án", "Quản lý dự án, thành viên", "Trang đầu tiên khi mở dự án. Xem tiến độ, lịch trình, nhân sự và hoạt động gần đây.",
  ["Xem **Tiến độ** (ví dụ 43%, 6/14 công việc, 1 quá hạn) và **Lịch trình** (còn bao nhiêu ngày đến hạn).", "Bấm **Cập nhật tiến độ** (cột phải) để gửi báo cáo trạng thái: Đúng tiến độ, Có rủi ro, Lệch tiến độ.", "Xem mục **Bảng**: Tasks và Issues với số công việc hoàn thành, đang hoạt động.", "Xem **Vai trò** (người sở hữu, thành viên) và **Hoạt động gần đây** ở cột phải."],
  [sh("pj-over", "Tiến độ: % hoàn thành, số việc đang chạy, số việc quá hạn.", "Lịch trình: số ngày đến hạn và % thời gian đã dùng.", "Bấm **Cập nhật tiến độ** để báo trạng thái dự án.", "Danh sách **Bảng** của dự án: bấm vào Tasks để mở công việc.", "**Vai trò**: người sở hữu và thành viên của dự án.")]),
 ("pj-road", "Lộ trình (gói công việc)", "Quản lý dự án", "Xem dự án theo **giai đoạn và gói công việc** trên biểu đồ thời gian.",
  ["Bấm **Lộ trình** ở thanh trái.", "Đọc mỗi dòng: tên gói, số công việc, % hoàn thành và thanh thời gian.", "Đổi thang thời gian bằng nút **Tháng** hoặc **Hôm nay** để quay về ngày hiện tại.", "Bấm **Tạo mới** để thêm gói công việc hoặc cột mốc."],
  [sh("pj-road", "**Tạo mới**: thêm gói công việc hoặc cột mốc.", "Chọn thang thời gian (Tháng...) và nút **Hôm nay**.", "Gói công việc: ví dụ *1. Hồ sơ pháp lý* hoàn thành 100%.", "Đường đỏ là ngày hôm nay (20 thg 11).")]),
 ("pj-table", "Công việc (Tasks): xem dạng Bảng biểu", "Mọi người", "Danh sách công việc của dự án, gom theo nhóm (ví dụ Phòng QS, Phòng KHĐT).",
  ["Bấm **Tasks** ở thanh trái.", "Dùng các tab phía trên để đổi cách xem: **Bảng biểu, Danh sách, Bảng, Dòng thời gian, Lịch**.", "Bấm **Lọc** hoặc ô tìm kiếm để tìm công việc.", "Bấm tên công việc để mở chi tiết; bấm **Thêm công việc** để tạo mới."],
  [sh("pj-table", "Tab chế độ xem: Bảng biểu, Danh sách, Bảng, Dòng thời gian, Lịch.", "**Thêm công việc** (nút xanh) để tạo công việc mới.", "Tiêu đề nhóm, ví dụ **Phòng QS**, kèm tiến độ **3/4 hoàn thành**.", "Cột **Trạng thái**: Hoàn thành, Bản nháp...", "**Lọc** và ô tìm kiếm.")]),
 ("pj-tlist", "Các cách xem khác của Tasks", "Mọi người", "Cùng một dữ liệu, chọn cách xem hợp với việc bạn đang làm.",
  ["**Danh sách**: nhiều cột (người phụ trách, hạn chốt, dòng thời gian).", "**Bảng**: thẻ kéo thả theo nhóm hoặc bước.", "**Dòng thời gian**: biểu đồ Gantt, thanh đỏ gạch là công việc quá hạn.", "**Lịch**: xem theo tháng hoặc tuần; việc chưa có ngày nằm ở **Không có ngày**."],
  [sh("pj-tlist", "**Danh sách**: có cột hạn chốt và dòng thời gian.", "Cột **Người phụ trách** và **Trạng thái**.", "Tuỳ chỉnh **chế độ xem** và **Sắp xếp**.", "Công việc quá hạn hiện chữ đỏ, ví dụ *6 ngày trễ*."),
   sh("pj-kan", "Chuyển sang dạng **Bảng** (kéo thả).", "Gom nhóm theo **Bước** hoặc nhóm khác.", "Nhóm công việc, ví dụ **Phòng QS**.", "Thẻ công việc: mã, hạn, người phụ trách."),
   sh("pj-tline", "Chuyển sang **Dòng thời gian**.", "Chọn thang **Tuần, Tháng, Quý, Năm**.", "Đường đỏ là **Hôm nay**.", "Thanh đỏ gạch chéo: công việc **quá hạn**."),
   sh("pj-cal", "Chuyển sang **Lịch**.", "Đổi **Tháng / Tuần**.", "Bấm mũi tên để đổi tháng.", "**Không có ngày**: công việc chưa đặt hạn.")]),
 ("pj-tform", "Thêm công việc", "Thành viên dự án", "Tạo công việc mới trong dự án.",
  ["Bấm **Thêm công việc** (góc phải trên Tasks).", "Nhập **Tên** (bắt buộc). Chọn **Mức ưu tiên** và **Nhóm** (ví dụ Phòng QS).", "Chọn **Người phụ trách**, **Người theo dõi**, **Ngày bắt đầu** và **Hạn chốt**.", "Thêm **Mô tả** nếu cần, rồi bấm **Thêm công việc**. Muốn thêm nhanh: bấm **+ Thêm công việc** ngay trong nhóm, gõ tên rồi **Lưu**."],
  [sh("pj-tform", "Nhập **Tên** công việc (bắt buộc).", "Chọn **Mức ưu tiên**.", "Chọn **Nhóm** công việc.", "Chọn **Người phụ trách** theo tên hoặc email.", "Đặt **Ngày bắt đầu** và **Hạn chốt**.", "Bấm **Thêm công việc** để lưu.")]),
 ("pj-task", "Mở và cập nhật một công việc", "Người phụ trách", "Bấm vào tên công việc để mở khung chi tiết bên phải.",
  ["Bấm tên công việc, ví dụ **Hồ sơ thanh toán** (mã HNAD1-TASK-3).", "Bấm **Giao cho** và **Đặt hạn** để giao người và hạn.", "Thêm **Công việc con**, **Tệp** hoặc **Phụ thuộc** bằng các nút dưới mô tả.", "Viết **Bình luận**; xem **Thời gian & chi phí** và **Nhật ký hoạt động** ở các tab bên dưới.", "Đổi **Trạng thái** (Bản nháp, Hoạt động, Hoàn thành) ở cột phải."],
  [sh("pj-task", "**Giao cho** người phụ trách.", "**Đặt hạn** cho công việc.", "**Công việc con, Tệp, Phụ thuộc**.", "Tab **Bình luận / Thời gian & chi phí / Nhật ký hoạt động**.", "Đổi **Trạng thái** công việc.", "**Gói công việc** mà việc này thuộc về.")]),
 ("pj-work", "Khối lượng công việc", "Quản lý dự án", "Lập kế hoạch và ghi nhận công sức theo người. Dự án mẫu chưa có dữ liệu.",
  ["Bấm **Khối lượng công việc**.", "Bấm **Kế hoạch và ghi nhận** hoặc **Tạo khối lượng công việc** để thêm bản ghi.", "Lọc theo **Bảng**, **Trạng thái**, **Người sở hữu** ở cột trái."],
  [sh("pj-work", "**Kế hoạch và ghi nhận** công sức.", "**Tạo khối lượng công việc**.", "Bộ lọc **Bảng**.", "Bộ lọc **Trạng thái**.")]),
 ("pj-recur", "Công việc lặp lại", "Quản lý dự án", "Tự tạo công việc theo chu kỳ. Dự án mẫu có **Báo cáo ngày**, tạo hàng ngày vào bảng Tasks, giao cho Base Support.",
  ["Bấm **Lặp lại** ở thanh trái.", "Mỗi dòng cho biết chu kỳ, bảng, người nhận và **kỳ kế tiếp**.", "Bấm **Công việc lặp lại mới** để tạo lịch mới, hoặc **Nhập** để nhập hàng loạt.", "Dùng biểu tượng tạm dừng, sửa, nhân bản, xoá ở cuối dòng."],
  [sh("pj-recur", "**Công việc lặp lại mới**.", "Dòng lịch: Hàng ngày, Tasks, Base Support, kỳ kế tiếp 21/11/2026.", "**Nhập** nhiều lịch một lần.", "Nút chạy ngay, tạm dừng, sửa, nhân bản, xoá.")]),
 ("pj-auto", "Tự động hoá trong dự án", "Quản trị dự án", "Quy tắc chạy ngay khi sửa công việc, ví dụ gán người duyệt khi công việc chuyển sang bước duyệt. Dự án mẫu chưa có quy tắc nào.",
  ["Bấm **Tự động hoá**, rồi **Tạo tự động hoá**.", "Chọn điều kiện kích hoạt và hành động, lưu lại.", "Cần gọi hệ thống bên ngoài thì dùng app **Automation**."],
  [sh("pj-auto", "**Tạo tự động hoá** mới.", "Bấm **Tạo tự động hoá đầu tiên** khi danh sách trống.")]),
 ("pj-log", "Nhật ký hoạt động", "Mọi người", "Xem ai đã tạo, sửa, đánh dấu hoàn thành công việc nào.",
  ["Bấm **Nhật ký hoạt động**, khung mở bên phải.", "Bấm **Xem chi tiết** ở dòng sửa đổi để biết giá trị trước và sau.", "Bấm **X** để đóng."],
  [sh("pj-log", "Danh sách sự kiện mới nhất ở đầu.", "**Xem chi tiết** thay đổi.")]),
 ("pj-set", "Cài đặt dự án", "Người sở hữu dự án", "Quản lý nhân sự, đơn vị đo, tiền tệ và quy tắc của dự án.",
  ["Bấm **Cài đặt**.", "Mục **Nhân sự**: **Người sở hữu** quản lý dự án; **Thành viên** xem và làm việc trong dự án. Gõ tên hoặc email để thêm, bấm **Lưu**.", "Mục **Đơn vị đo và tiền tệ**: chọn đơn vị khối lượng (Ngày), tiền tệ (VND) và số giờ mỗi ngày (8).", "Kéo xuống để xem các mục còn lại."],
  [sh("pj-set", "**Người sở hữu** dự án (Base Support, Nguyễn Thế Dũng).", "**Thành viên** dự án; thêm từ nhóm hoặc đơn vị đội nhóm.", "**Đơn vị khối lượng công việc**.", "**Tiền tệ** của dự án.")]),
]

FAQ = [
 ("Tôi không thấy dự án **Hợp đồng Mẫu**", "Bạn chưa là người sở hữu hay thành viên. Nhờ người sở hữu thêm tên bạn ở **Cài đặt → Nhân sự**.", "pj-set"),
 ("Công việc đang **quá hạn** màu đỏ", "Hạn chốt đã qua mà chưa **Hoàn thành**. Mở công việc, xử lý rồi đổi Trạng thái, hoặc đặt hạn mới.", "pj-task"),
 ("Muốn công việc xuất hiện **mỗi ngày**", "Dùng **Lặp lại**: tạo lịch hàng ngày. Dự án mẫu đã có lịch Báo cáo ngày.", "pj-recur"),
 ("Không bấm được **Thêm công việc**", "Cần là thành viên hoặc người sở hữu dự án. Kiểm tra ở Cài đặt → Nhân sự.", "pj-tform"),
]

def md(s):
    import re
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", re.sub(r"\*(.+?)\*", r"<i>\1</i>", html.escape(s)))

def fig(s):
    pins = "".join(f"<li><i class='pin'>{i+1}</i><span>{md(t)}</span></li>" for i, t in enumerate(s["pins"]))
    return (f'<figure class="shot big"><img data-k="{s["img"]}" alt=""><figcaption>Màn hình thật trên Base Project · bấm để phóng to</figcaption></figure><ol class="pinlist">{pins}</ol>')

def pane():
    cards = []
    for n, (key, title, who, do, how, shots) in enumerate(SECTIONS, 1):
        cards.append(f'''<article class="step wide k-ev" id="project-{key}"><div class="sh"><span class="sn2">{n}</span><div><h4>{html.escape(title)}</h4>
<div class="pills"><span class="chip ev">Project</span><span class="chip">👤 {html.escape(who)}</span></div></div></div>
<p class="do">{md(do)}</p><h5>Cách làm</h5><ol>{"".join(f"<li>{md(h)}</li>" for h in how)}</ol>
{"".join(fig(s) for s in shots)}
<p class="goto">Làm theo: <a class="golink" href="{URL}" target="_blank" rel="noopener">Mở Base Project ↗</a></p></article>''')
    faq = "".join(f'<details class="prob"><summary>{md(q)}</summary><p>{md(a)}</p><p class="goto"><a href="#project-{s}" data-go="project-{s}">Xem hướng dẫn liên quan →</a></p></details>' for q, a, s in FAQ)
    return f'''<section class="tabpane" id="pane-project" data-tab="project" hidden>
<div class="hero"><div class="eyebrow">HƯỚNG DẪN SỬ DỤNG · BASE PROJECT · DỰ ÁN CÔNG TY</div>
<h1>Project · Hợp đồng Mẫu</h1>
<p class="lead">Quản lý dự án **Hợp đồng Mẫu** (mã HNAD1): **công việc** theo nhóm, **lộ trình**, **tiến độ**, lịch lặp và **cài đặt** dự án.</p>
<div class="path"><a href="#project-pj-list">① Vào dự án</a><a href="#project-steps">② Làm theo từng mục</a><a href="#project-faq">③ Gặp vấn đề?</a></div>
<div class="kpis"><div class="kpi"><b>14</b><span>công việc</span></div><div class="kpi"><b>5</b><span>cách xem Tasks</span></div><div class="kpi"><b>9</b><span>thành viên</span></div><div class="kpi"><b>{len(SECTIONS)}</b><span>mục hướng dẫn</span></div></div>
<p class="hint">Dữ liệu đọc từ project.base.vn ngày 20/11/2026. <a class="golink" href="{URL}" target="_blank" rel="noopener">Mở dịch vụ Dự án công ty ↗</a></p></div>
<h2 id="project-steps"><span class="sn">1</span>Làm theo từng mục</h2>
<div class="steps">{"".join(cards)}</div>
<h2 id="project-faq"><span class="sn">2</span>Gặp vấn đề?</h2>
<div class="probs">{faq}</div>
<h2><span class="sn">3</span>Dữ liệu mẫu để xem thử</h2>
<div class="note"><ul><li>Dự án <b>Hợp đồng Mẫu</b> (HNAD1): 14 công việc, 5 gói công việc, nhóm Phòng QS và Phòng KHĐT.</li><li>Lịch lặp <b>Báo cáo ngày</b> tạo công việc hàng ngày.</li><li>Khối lượng công việc, tự động hoá: chưa có dữ liệu (đang để trống).</li></ul>
<p class="goto">Làm theo: <a class="golink" href="{URL}" target="_blank" rel="noopener">Mở Base Project ↗</a></p></div>
</section>'''

CARD = ('<a class="svc" href="#project" data-tabgo="project"><div class="k">Base Project</div><h4>Project · Hợp đồng Mẫu</h4>'
        '<p>Quản lý **công việc**, **lộ trình**, tiến độ và lịch lặp của dự án.</p><span class="golink">Xem hướng dẫn →</span></a>')
