# -*- coding: utf-8 -*-
"""Nội dung HDSD 6 quy trình trên BPM (đọc từ hệ thống bpm.base.vn ngày 20/11/2026)."""

BASE = "https://bpm.base.vn/service/"

# kind: manual (làm việc) | sign (trình ký/phê duyệt) | sub (công việc con) | merge
# rows: danh sách hàng; mỗi hàng là 1 hoặc 2 bước chạy song song

PROCESSES = [
 dict(
  id="qt01", code="QT-01", name="Yêu cầu cấp vật tư", group="Kế hoạch - Vật tư",
  url=BASE+"aFAxNX5y-VvPzKbiZWx-AUwZHuNFJdJ", img="qt01-flow",
  lead="Ban chỉ huy lập **Yêu cầu cấp vật tư**, Ban Giám đốc **ký duyệt**, rồi Phòng Kế hoạch và NV Mua hàng xử lý và **chia đợt mua hàng**.",
  rows=[
   [dict(id="s1", n="1", t="Yêu cầu cấp vật tư", who="Ban chỉ huy", kind="manual")],
   [dict(id="s2", n="2", t="Phê duyệt yêu cầu", who="Phạm Thị Hồng Minh (Trợ lý CT HĐQT)", kind="sign", reject="s1")],
   [dict(id="s3", n="3", t="Tiếp nhận, kiểm tra và xử lý YCCVT", who="Phòng Kế hoạch", kind="manual")],
   [dict(id="s4", n="4", t="Nhân viên Mua hàng tiếp nhận", who="NV Mua hàng", kind="manual")],
   [dict(id="s5", n="5", t="Phân chia mua hàng", who="NV Mua hàng", kind="sub")],
  ],
  steps={
   "s1": dict(do="Lập yêu cầu cấp vật tư cho dự án, tạo yêu cầu ký và gửi lên Ban Giám đốc.",
     how=["Bấm **Công việc mới** góc phải trên (xem ảnh form bên dưới), điền và bấm **Tạo công việc**.", "Mở thẻ vừa tạo, bấm **Trình ký: Phê duyệt yêu cầu (Ban Giám đốc)** để tạo yêu cầu ký.", "Bấm **Submit** để chuyển sang bước 2."],
     done="Thẻ chuyển sang cột **2. Phê duyệt yêu cầu**."),
   "s2": dict(do="Bước chạy tự động: hệ thống chờ Ban Giám đốc ký. Thẻ hiện tiến độ ký, ví dụ **Đã ký 0/1**. Người ký là người được giao ở bước này.",
     how=["Người làm phiếu không cần thao tác, chỉ theo dõi khung xanh **Đang chờ ... đã ký x/y**.", "Người ký mở tài liệu và ký (hoặc từ chối) theo yêu cầu ký đã gửi.", "Đủ chữ ký thì phiếu tự sang bước 3 và tệp PDF đã ký được ghi vào phiếu."],
     done="Số ký đạt đủ (ví dụ 1/1) và phiếu sang bước 3. Từ chối: phiếu kết thúc với nhãn **Bị từ chối**."),
   "s3": dict(do="Phòng Kế hoạch tiếp nhận, kiểm tra và xử lý yêu cầu cấp vật tư.",
     how=["Mở thẻ ở cột 3, kiểm tra thông tin yêu cầu.", "Bổ sung hoặc chỉnh trường cần thiết.", "Bấm **Submit** để chuyển NV Mua hàng."],
     done="Thẻ sang cột **4. Nhân viên Mua hàng tiếp nhận**."),
   "s4": dict(do="Nhân viên Mua hàng nhận yêu cầu và chuẩn bị phân chia các đợt mua hàng.",
     how=["Mở thẻ ở cột 4, xác nhận đã nhận.", "Bấm **Submit** để sang bước phân chia mua hàng."],
     done="Thẻ sang cột **Phân chia mua hàng**."),
   "s5": dict(do="Tách yêu cầu thành các **công việc con** (**Đợt Mua hàng**) và theo dõi tiến độ, ví dụ **Đã xong 1/2**.",
     how=["Trên thẻ, bấm **Đợt Mua hàng** để tạo công việc con cho từng đợt.", "Khi danh sách đợt đã đủ, bấm **Chốt danh sách** (góc phải trên màn hình chi tiết).", "Theo dõi số công việc con đã xong ở khung xanh."],
     done="Tất cả công việc con hoàn thành thì phiếu sang **End**. Nếu có công việc con bị huỷ, lưu đồ đi nhánh **Có công việc con bị huỷ**."),
  },
  faq=[
   ("Thẻ báo đỏ **Trễ x ngày**", "Bước đã quá thời hạn. Mở thẻ, xử lý và bấm Submit, hoặc đổi thời hạn của bước nếu được cấp quyền.", "s1"),
   ("Phiếu hiện **Bị từ chối (không có nhánh đi tiếp)**", "Người ký đã chọn Từ chối ở bước 2. Tạo phiếu mới sau khi chỉnh nội dung.", "s2"),
   ("Không thấy nút chuyển bước trên thẻ", "Chỉ người được giao ở bước hiện tại mới thấy nút. Kiểm tra tên người phụ trách trên thẻ hoặc nhờ Quản trị gán lại.", "s3"),
   ("Phiếu chưa sang End dù đã mua xong", "Còn công việc con chưa hoàn thành hoặc đã bị huỷ. Mở thẻ Phân chia mua hàng và kiểm tra bộ đếm công việc con.", "s5"),
  ],
  samples=["Đề xuất vật tư lần 2", "Đề xuất trình yêu cầu vật tư", "Yêu cầu cấp vật tư đợt 3 – thép D16 và xi măng PCB40 – Dự án Khu nhà ở Phú Mỹ"],
 ),
 dict(
  id="qt02", code="QT-02", name="Mua hàng", group="Kế hoạch - Vật tư",
  url=BASE+"aFAxNe5o-cbQYFnNu7c-V67Nos4YKvC", img="qt02-flow",
  lead="Từ yêu cầu mua hàng đến **báo giá tối thiểu 3 NCC**, **phê duyệt nhà cung cấp**, chuyển thanh toán, nhập hàng, kiểm tra chứng chỉ và **nhập kho dự án**.",
  rows=[
   [dict(id="s1", n="1", t="Yêu cầu mua hàng", who="Theo gán trong dịch vụ", kind="manual")],
   [dict(id="s2", n="2", t="Đề nghị báo giá tối thiểu 3 NCC", who="Phòng Kế hoạch", kind="manual")],
   [dict(id="s3", n="3", t="Phê duyệt NCC", who="Ban Lãnh đạo", kind="sign", reject="s2")],
   [dict(id="s4", n="4", t="Chuyển bộ phận Thanh toán", who="Phòng Kế hoạch", kind="sub")],
   [dict(id="s5", n="5", t="Nhập hàng hoặc kiểm hàng", who="PKH, Ban chỉ huy", kind="manual")],
   [dict(id="s6", n="6", t="Kiểm tra hàng hóa, chứng chỉ hàng hóa", who="Ban chỉ huy, PKH", kind="manual")],
   [dict(id="s7", n="7", t="Nhập kho dự án", who="Thủ kho", kind="manual")],
  ],
  steps={
   "s1": dict(do="Tạo yêu cầu mua hàng (thường từ yêu cầu cấp vật tư đã duyệt).",
     how=["Bấm **Công việc mới**, chọn QT-02.", "Nhập tiêu đề và thông tin vật tư cần mua.", "Bấm **Submit** để chuyển Phòng Kế hoạch."],
     done="Thẻ sang cột **2. Đề nghị báo giá**."),
   "s2": dict(do="Phòng Kế hoạch đề nghị báo giá **tối thiểu 3 nhà cung cấp**.",
     how=["Mở thẻ, ghi nhận báo giá của từng NCC.", "Đính kèm báo giá, bấm **Submit** sang bước phê duyệt."],
     done="Thẻ sang **Phê duyệt NCC**."),
   "s3": dict(do="Ban Lãnh đạo chọn và phê duyệt nhà cung cấp.",
     how=["Mở thẻ, so sánh báo giá.", "Chọn **Approve** để đi tiếp hoặc **Reject** để trả lại."],
     done="Approve: sang **Chuyển bộ phận Thanh toán**. Reject: quay lại bước báo giá."),
   "s4": dict(do="Tạo công việc con chuyển hồ sơ cho bộ phận Thanh toán và theo dõi kết quả.",
     how=["Trên thẻ, tạo công việc con cho bộ phận Thanh toán.", "Chờ công việc con hoàn thành."],
     done="Tất cả công việc con hoàn thành thì sang bước nhập hàng. Có công việc con bị huỷ thì đi nhánh riêng trên lưu đồ."),
   "s5": dict(do="Nhận hàng về hoặc kiểm hàng tại nơi cung cấp.",
     how=["Mở thẻ, ghi nhận số lượng nhận.", "Bấm **Submit**."],
     done="Thẻ sang bước kiểm tra hàng hóa."),
   "s6": dict(do="Kiểm tra chất lượng hàng và chứng chỉ hàng hóa.",
     how=["Đối chiếu hàng với chứng chỉ, đính kèm kết quả kiểm tra.", "Bấm **Submit**."],
     done="Thẻ sang bước nhập kho."),
   "s7": dict(do="Thủ kho nhập kho dự án.",
     how=["Mở thẻ, xác nhận số lượng nhập kho.", "Bấm **Submit** để kết thúc."],
     done="Thẻ sang **End**, trạng thái **Đã hoàn thành**."),
  },
  faq=[
   ("Muốn đổi nhà cung cấp sau khi Reject", "Phiếu quay lại bước báo giá. Cập nhật báo giá rồi Submit lần nữa.", "s3"),
   ("Công việc con thanh toán bị huỷ", "Phiếu đi nhánh riêng thay vì sang nhập hàng. Liên hệ Quản trị để xử lý hoặc tạo lại công việc con.", "s4"),
   ("Không thấy thẻ ở bước của tôi", "Kiểm tra bộ lọc **Tất cả những gì có thể xem** hoặc dùng **Việc của tôi** ở menu trái.", "s5"),
  ],
  samples=["Đề xuất mua hàng", "Lần 1, Lần 2, Lần 3 (các phiếu đã huỷ trong dịch vụ)"],
 ),
 dict(
  id="qt03", code="QT-03", name="Theo dõi hồ sơ thanh toán Tổ đội, Nhà thầu phụ", group="Kế hoạch - Vật tư",
  url=BASE+"aFCwV8lB-Dm9asogs68-QxrvM9CrjZ2", img="qt03-flow",
  lead="Theo dõi **hồ sơ thanh toán** của Tổ đội và Nhà thầu phụ: gửi hồ sơ, lập và **ký biên bản giao nhận**, Phòng Kế hoạch nhận rồi **tạo Tờ trình thanh toán**.",
  rows=[
   [dict(id="s1", n="1", t="Gửi hồ sơ thanh toán", who="Tổ đội, Nhà thầu phụ", kind="manual")],
   [dict(id="s2", n="2", t="Tạo biên bản giao nhận", who="Người nhận hồ sơ", kind="manual")],
   [dict(id="s3", n="3", t="Ký biên bản giao nhận", who="Người ký", kind="sign", reject="s2")],
   [dict(id="s4", n="4", t="Phòng Kế hoạch nhận", who="Phòng Kế hoạch", kind="manual")],
   [dict(id="s5", n="5", t="Tạo Tờ trình thanh toán", who="Phòng Kế hoạch", kind="sub")],
  ],
  steps={
   "s1": dict(do="Gửi hồ sơ đề nghị thanh toán của Tổ đội hoặc Nhà thầu phụ.",
     how=["Bấm **Công việc mới**, chọn QT-03.", "Nhập tiêu đề, đính kèm hồ sơ.", "Bấm **Submit**."], done="Thẻ sang bước tạo biên bản giao nhận."),
   "s2": dict(do="Lập biên bản giao nhận cho hồ sơ vừa nhận.",
     how=["Mở thẻ, nhập thông tin biên bản.", "Bấm **Submit** để trình ký."], done="Thẻ sang bước ký."),
   "s3": dict(do="Người có thẩm quyền ký biên bản giao nhận.",
     how=["Mở thẻ, kiểm tra biên bản.", "Chọn **Đã ký** hoặc **Từ chối**."], done="Đã ký: sang Phòng Kế hoạch. Từ chối: trả về bước lập biên bản."),
   "s4": dict(do="Phòng Kế hoạch xác nhận đã nhận hồ sơ.",
     how=["Mở thẻ, đối chiếu hồ sơ.", "Bấm **Submit**."], done="Thẻ sang bước tạo Tờ trình thanh toán."),
   "s5": dict(do="Tạo công việc con **Tờ trình thanh toán** và theo dõi đến khi xong.",
     how=["Tạo công việc con từ thẻ.", "Theo dõi bộ đếm công việc con."], done="Tất cả công việc con hoàn thành thì sang **End**."),
  },
  faq=[
   ("Biên bản bị Từ chối", "Thẻ quay lại bước lập biên bản. Sửa nội dung rồi Submit lại.", "s3"),
   ("Dịch vụ chưa có công việc nào", "Dịch vụ mới cấu hình. Bấm **Công việc mới** để tạo phiếu đầu tiên.", "s1"),
  ],
  samples=["Chưa có công việc thật. Xem phần Dữ liệu mẫu bên dưới."],
 ),
 dict(
  id="qt05", code="QT-05", name="Quy trình Thanh, Quyết toán", group="Phòng QS",
  url=BASE+"aFBcYBmh-EcBHa0bFSj-NYT3MkRUCOE", img="qt05-flow",
  lead="Thanh, quyết toán công trình: sau **yêu cầu thanh toán**, hai nhánh **chạy song song** rồi gộp, lập hồ sơ chất lượng và giá trị thanh toán, cuối cùng **hai lần ký xác nhận**.",
  rows=[
   [dict(id="s1", n="1", t="Yêu cầu thanh toán", who="Bước bắt đầu", kind="manual")],
   [dict(id="s2", n="2a", t="Nghiệm thu thiết bị", who="Theo gán trong dịch vụ", kind="manual"),
    dict(id="s3", n="2b", t="Nhận khối lượng thi công chỉ huy công trường", who="Chỉ huy công trường", kind="manual")],
   [dict(id="m1", n="⊕", t="Gộp nhánh (Merge Branches)", who="Tự động", kind="merge")],
   [dict(id="s4", n="3a", t="Lập hồ sơ Quản lý chất lượng", who="Theo gán trong dịch vụ", kind="manual"),
    dict(id="s5", n="3b", t="Lập hồ sơ Giá trị thanh toán", who="Theo gán trong dịch vụ", kind="manual")],
   [dict(id="m2", n="⊕", t="Gộp nhánh (Merge Branches)", who="Tự động", kind="merge")],
   [dict(id="s6", n="4", t="Ký xác nhận đơn vị tư vấn giám sát", who="Tư vấn giám sát", kind="manual")],
   [dict(id="s7", n="5", t="Ký xác nhận Chủ đầu tư", who="Chủ đầu tư", kind="manual")],
  ],
  steps={
   "s1": dict(do="Tạo yêu cầu thanh toán, hệ thống tách thành hai nhánh làm song song.",
     how=["Bấm **Công việc mới**, chọn QT-05.", "Nhập thông tin đợt thanh toán, bấm **Submit**."], done="Hai thẻ xuất hiện đồng thời ở Nghiệm thu thiết bị và Nhận khối lượng."),
   "s2": dict(do="Nghiệm thu thiết bị (nhánh 2a).", how=["Mở thẻ, nhập kết quả nghiệm thu.", "Bấm **Submit**."], done="Chờ nhánh 2b xong thì hai nhánh tự gộp."),
   "s3": dict(do="Xác nhận khối lượng thi công (nhánh 2b).", how=["Mở thẻ, nhập khối lượng.", "Bấm **Submit**."], done="Cả 2a và 2b xong thì gộp nhánh."),
   "m1": dict(do="Hệ thống tự gộp hai nhánh, không cần thao tác.", how=["Không có thao tác. Nếu thẻ chưa đi tiếp, kiểm tra nhánh còn lại."], done="Mở hai thẻ song song ở bước 3."),
   "s4": dict(do="Lập hồ sơ quản lý chất lượng (nhánh 3a).", how=["Mở thẻ, đính kèm hồ sơ.", "Bấm **Submit**."], done="Chờ nhánh 3b."),
   "s5": dict(do="Lập hồ sơ giá trị thanh toán (nhánh 3b).", how=["Mở thẻ, đính kèm hồ sơ.", "Bấm **Submit**."], done="Cả hai nhánh xong thì gộp."),
   "m2": dict(do="Hệ thống tự gộp nhánh lần hai.", how=["Không có thao tác."], done="Thẻ sang bước ký xác nhận đơn vị tư vấn giám sát."),
   "s6": dict(do="Đơn vị tư vấn giám sát ký xác nhận.", how=["Mở thẻ, kiểm tra hồ sơ.", "Bấm **Submit**."], done="Thẻ sang bước ký của Chủ đầu tư."),
   "s7": dict(do="Chủ đầu tư ký xác nhận cuối cùng.", how=["Mở thẻ, kiểm tra hồ sơ.", "Bấm **Submit**."], done="Thẻ sang **End**, trạng thái **Đã hoàn thành**."),
  },
  faq=[
   ("Chỉ thấy một thẻ ở bước song song", "Nhánh còn lại có người phụ trách khác. Đợi cả hai nhánh xong, hệ thống mới gộp.", "m1"),
   ("Thẻ đứng ở Merge Branches", "Một trong hai nhánh chưa Submit. Mở thẻ nhánh còn lại để xử lý.", "m2"),
  ],
  samples=["Thanh toán đợt 1 (đã hoàn thành 03/11/2026)"],
 ),
 dict(
  id="qt06", code="QT06", name="Quy trình duyệt chủ trương thanh toán", group="Phòng TCTH",
  url=BASE+"aFBsYFMY-YM7zY1KKeT-roaPEYibQVm", img="qt06-flow", img2="qt06-pipeline",
  lead="Các phòng/ban gửi **tờ trình thanh toán**, bộ phận **Kiểm soát & Phê duyệt** ký duyệt, Phòng TCTH **lưu trữ và tổng hợp**.",
  rows=[
   [dict(id="s1", n="1", t="Các phòng/ban gửi tờ trình: T/Ư, TT, BLTT cho nhà cung cấp", who="Các phòng/ban chức năng", kind="manual")],
   [dict(id="s2", n="2", t="Kiểm soát & Phê duyệt", who="Người kiểm soát, phê duyệt", kind="sign", reject="s1")],
   [dict(id="s3", n="3", t="Phòng TCTH lưu trữ và tổng hợp", who="Phòng TCTH", kind="manual")],
  ],
  steps={
   "s1": dict(do="Phòng/ban gửi tờ trình tạm ứng (T/Ư), thanh toán (TT) hoặc bảo lãnh thanh toán (BLTT) cho nhà cung cấp. Bước này có thời hạn **1 ngày**.",
     how=["Bấm **Công việc mới**, điền form (xem ảnh bên dưới) rồi **Tạo công việc**.", "Mở thẻ, bấm **Trình ký: Ký Tờ trình TT, TƯ** để tạo yêu cầu ký.", "Bấm **Submit** để gửi sang Kiểm soát & Phê duyệt."], done="Thẻ sang cột **Kiểm soát & Phê duyệt**."),
   "s2": dict(do="Bước chạy tự động: hệ thống chờ chữ ký của tờ trình. Thẻ hiện **Đã ký 0/1**.",
     how=["Nếu còn bản nháp yêu cầu ký, bấm **Tiếp tục bản nháp**; tạo đủ yêu cầu ký rồi bấm **Chốt danh sách**.", "Người ký ký hoặc từ chối trên yêu cầu ký.", "Hệ thống xét kết quả và chuyển bước."], done="Đủ chữ ký thì sang Phòng TCTH. Từ chối thì trả về phòng/ban gửi."),
   "s3": dict(do="Phòng TCTH lưu trữ hồ sơ và tổng hợp.",
     how=["Mở thẻ, lưu trữ hồ sơ.", "Bấm **Submit** để kết thúc."], done="Thẻ sang **End**, trạng thái **Đã hoàn thành**."),
  },
  faq=[
   ("Thẻ ở Kiểm soát & Phê duyệt hiện **Đã ký 0/1**", "Chưa đủ chữ ký. Người ký mở thẻ và chọn Đã ký.", "s2"),
   ("Tờ trình bị Từ chối", "Thẻ về bước 1 để phòng/ban chỉnh sửa. Một số phiếu cũ hiển thị **Đã huỷ**.", "s1"),
  ],
  samples=["Đề nghị thanh toán lần 1, 2, 3", "Đề xuất thanh toán dự án Base lần 1, 2"],
 ),
 dict(
  id="qt07", code="QT07", name="Quy trình thực hiện thanh toán", group="Phòng TCTH",
  url=BASE+"aFCBKaiE-lKABDlktz3-XqhAMKRZfKa", img="qt07-flow", img2="qt07-form",
  lead="Phòng TCTH **tổng hợp đợt thanh toán** từ các đề nghị, rồi **trình ký thanh toán**.",
  rows=[
   [dict(id="s1", n="1", t="Tổng hợp đợt thanh toán", who="Phòng TCTH", kind="manual")],
   [dict(id="s2", n="2", t="Trình ký Thanh toán", who="Người ký thanh toán", kind="sign")],
  ],
  steps={
   "s1": dict(do="Tạo công việc và tổng hợp đợt thanh toán. Form có các trường: **Tiêu đề, Người theo dõi, Dự án, Hợp đồng, File Đề nghị thanh toán**.",
     how=["Bấm **Công việc mới**, chọn QT07.", "Nhập **Tiêu đề**; chọn **Dự án** (Chọn bản ghi) và **Hợp đồng**.", "Đính kèm **File Đề nghị thanh toán**, thêm **Người theo dõi** nếu cần.", "Bấm **Tạo công việc**, rồi **Submit**."], done="Thẻ sang **Trình ký Thanh toán**."),
   "s2": dict(do="Người có thẩm quyền ký thanh toán.",
     how=["Mở thẻ, kiểm tra đề nghị thanh toán.", "Chọn **Đã ký** để hoàn thành hoặc **Từ chối**."], done="Đã ký: phiếu sang **End**. Từ chối: phiếu kết thúc theo nhánh từ chối."),
  },
  faq=[
   ("Không chọn được Dự án hoặc Hợp đồng", "Trường Dự án chọn từ bản ghi có sẵn. Nếu danh sách trống, nhờ Quản trị bổ sung bản ghi.", "s1"),
   ("Không bấm được Tạo công việc", "Điền Tiêu đề trước. Có thể bấm **Lưu nháp** để giữ lại và quay lại sau.", "s1"),
  ],
  samples=["Chưa có công việc thật. Xem phần Dữ liệu mẫu bên dưới."],
 ),
]


# ---- Ảnh thao tác (đã ghim số) ----
EXTRA = {
 "qt01": dict(
  form=dict(img="qt01-form", pins=["Nhập **Tiêu đề** (tên đợt, vật tư, dự án).", "Chọn **Dự án** trong danh sách.", "Đính kèm **Phiếu yêu cầu cấp vật tư (BM-01.1)**; có phát sinh thì đính thêm BM-01.2.", "Nhập **Bảng Vật tư yêu cầu** (Tên, Ghi chú, File đính kèm), bấm **Thêm dòng**.", "Bấm **Tạo công việc** (hoặc **Lưu nháp** để làm tiếp sau)."]),
  shots=dict(
   s1=dict(img="qt01-s1", pins=["Bấm **Trình ký: Phê duyệt yêu cầu (Ban Giám đốc)** để tạo yêu cầu ký. Nếu còn bản nháp, bấm **Tiếp tục bản nháp** ở khung CẦN BẠN TRÌNH KÝ.", "Bấm **Submit** để chuyển bước.", "Thanh bước cho biết đang ở bước nào và bước kế tiếp.", "Dữ liệu và tệp của phiếu (Hợp đồng, BM-01.1, Bảng vật tư): bấm biểu tượng bút để sửa.", "Thanh Thời gian báo **Quá hạn** nếu trễ; bấm bút để đổi hạn."]),
   s2=dict(img="qt01-s2", pins=["Khung xanh báo **Đang chờ Phê duyệt yêu cầu (Ban Giám đốc) · đã ký 0/1**. Bước này tự chạy, không cần bấm gì.", "Người ký được giao: **Phạm Thị Hồng Minh** (Trợ lý CT HĐQT).", "Sau khi ký, tệp PDF đã ký hiện ở mục **Do kết quả ký ghi**.", "Thanh bước đang dừng ở bước 3 Phê duyệt yêu cầu."]),
   s5=dict(img="qt01-s5", pins=["Bấm **Chốt danh sách** khi đã tạo đủ **Đợt Mua hàng**.", "Khung xanh báo tiến độ, ví dụ **Đang chờ Đợt Mua hàng · đã xong 1/2**.", "Bảng Vật tư yêu cầu chuyển từ phiếu gốc (2 hàng).", "Người phụ trách bước: **Trần Đình Thái** (NV)."]),
  )),
 "qt02": dict(
  form=dict(img="qt02-form", pins=["Nhập **Tiêu đề**.", "Chọn **Dự án**.", "Đính kèm **Phiếu yêu cầu mua hàng**.", "Bấm **Tạo công việc**."]),
  shots=dict(
   s2=dict(img="qt02-s2", pins=["Nếu bạn không phải người được giao, màn hình ghi **Hiện bạn không phải làm gì ở bước này**, kèm tên người đang xử lý.", "Thanh bước: đang ở bước 2, kế tiếp là **Phê duyệt NCC**, rồi rẽ nhánh 1 trong 2.", "Các trường cập nhật tại bước này: Dự án, Hợp đồng, Hợp đồng mua bán, **Báo giá của nhà cung cấp**.", "Người được giao bước: **Trần Đình Thái** (NV)."]),
  )),
 "qt03": dict(
  form=dict(img="qt03-form", pins=["Nhập **Tiêu đề**.", "Chọn **Dự án**.", "Đính kèm **Bộ hồ sơ** thanh toán.", "Bấm **Chọn tệp** để thêm **Biên bản giao nhận**.", "Bấm **Tạo công việc**."]),
  shots={}),
 "qt05": dict(
  form=dict(img="qt05-form", pins=["Nhập **Tiêu đề**.", "Nhập số **Hợp đồng**.", "Đính kèm **Yêu cầu thanh toán**.", "Bấm **Tạo công việc**."]),
  shots={}),
 "qt06": dict(
  form=dict(img="qt06-form", pins=["Nhập **Tiêu đề** (ví dụ: Đề nghị thanh toán lần 1).", "Chọn **Dự án**.", "Chọn **Nhà cung cấp**.", "Đính kèm **Tờ trình Đề nghị TT, TƯ** và **Giấy tờ kèm theo** (hoá đơn, hợp đồng...).", "Bấm **Tạo công việc**. Các trường còn lại (Nội dung thanh toán, Tài khoản, Giá trị hợp đồng, Giá trị thực hiện...) có thể điền sau."]),
  shots=dict(
   s1=dict(img="qt06-s1", pins=["Bấm **Trình ký: Ký Tờ trình TT, TƯ** để tạo yêu cầu ký.", "Bấm **Submit** để chuyển sang bước Kiểm soát & Phê duyệt.", "Thanh bước: đang ở bước 2, kế tiếp là Kiểm soát & Phê duyệt.", "Các trường dữ liệu: Dự án, Nhà cung cấp, Giấy tờ kèm theo... bấm bút để sửa.", "Người được giao xử lý bước này."]),
   s2=dict(img="qt06-s2", pins=["Nếu còn bản nháp, bấm **Tiếp tục bản nháp** ở khung CẦN BẠN TRÌNH KÝ.", "Khung xanh: **Đang chờ Ký Tờ trình TT, TƯ · đã ký 0/1**. Bước chạy tự động.", "Bấm **Chốt danh sách** khi đã tạo đủ yêu cầu ký để hệ thống xét kết quả.", "Thanh bước đang ở bước 3 Kiểm soát & Phê duyệt."]),
  )),
 "qt07": dict(
  form=dict(img="qt07-form", pins=["Nhập **Tiêu đề**.", "Bấm **Chọn bản ghi** ở mục **Dự án**.", "Nhập **Hợp đồng**.", "Đính kèm **File Đề nghị thanh toán**.", "Bấm **Tạo công việc**."]),
  shots={}),
}
