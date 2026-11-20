# -- coding: utf-8 --
"""Nội dung HDSD 6 quy trình trên BPM (đọc từ hệ thống bpm.base.vn ngày 20/11/2026)."""

BASE = "https://bpm.base.vn/service/"

# kind: manual (làm việc) | sign (trình ký/phê duyệt) | sub (công việc con) | merge
# rows: danh sách hàng; mỗi hàng là 1 hoặc 2 bước chạy song song

PROCESSES = [
 dict(
  id="qt01", code="QT-01", name="Yêu cầu cấp vật tư", group="Kế hoạch - Vật tư",
  url=BASE+"aFAxNX5y-VvPzKbiZWx-AUwZHuNFJdJ", img="qt01-flow",
  lead="Ban chỉ huy lập **Yêu cầu cấp vật tư**, **người duyệt có thẩm quyền** ký duyệt, rồi Phòng Kế hoạch và NV Mua hàng xử lý và **chia đợt mua hàng**.",
  rows=[
   [dict(id="s1", n="1", t="Yêu cầu cấp vật tư", who="Ban chỉ huy", kind="manual")],
   [dict(id="s2", n="2", t="Phê duyệt yêu cầu", who="Người duyệt có thẩm quyền", kind="sign", reject="s1")],
   [dict(id="s3", n="3", t="Tiếp nhận, kiểm tra và xử lý YCCVT", who="Phòng Kế hoạch", kind="manual")],
   [dict(id="s4", n="4", t="Nhân viên Mua hàng tiếp nhận", who="NV Mua hàng", kind="manual")],
   [dict(id="s5", n="5", t="Phân chia mua hàng", who="NV Mua hàng", kind="sub")],
  ],
  steps={
   "s1": dict(do="Lập yêu cầu cấp vật tư cho dự án, tạo yêu cầu ký và gửi người duyệt có thẩm quyền.",
     how=["Bấm **Công việc mới** góc phải trên (xem ảnh form bên dưới), điền và bấm **Tạo công việc**.", "Mở thẻ vừa tạo, bấm **Trình ký: Phê duyệt yêu cầu (Ban Giám đốc)** để tạo yêu cầu ký.", "Bấm **Submit** để chuyển sang bước 2."],
     done="Thẻ chuyển sang cột **2. Phê duyệt yêu cầu**."),
   "s2": dict(do="Bước chạy tự động: hệ thống chờ người duyệt có thẩm quyền ký. Thẻ hiện tiến độ ký, ví dụ **Đã ký 0/1**. Người ký là người được giao ở bước này.",
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
   [dict(id="s3", n="3", t="Phê duyệt NCC", who="Người duyệt có thẩm quyền", kind="sign", reject="s2")],
   [dict(id="s4", n="4", t="Chuyển bộ phận Thanh toán", who="Phòng Kế hoạch", kind="sub")],
   [dict(id="s5", n="5", t="Nhập hàng hoặc kiểm hàng", who="PKH, Ban chỉ huy", kind="manual")],
   [dict(id="s6", n="6", t="Kiểm tra hàng hóa, chứng chỉ hàng hóa", who="Ban chỉ huy, PKH", kind="manual")],
   [dict(id="s7", n="7", t="Nhập kho dự án", who="Thủ kho", kind="manual")],
  ],
  steps={
   "s1": dict(do="Tạo yêu cầu mua hàng (thường từ yêu cầu cấp vật tư đã duyệt).",
     how=["Bấm **Công việc mới**, chọn QT-02.", "Nhập tiêu đề và thông tin vật tư cần mua.", "Bấm **Submit** để chuyển Phòng Kế hoạch."],
     done="Thẻ sang cột **2. Đề nghị báo giá**."),
   "s2": dict(do="Phòng Kế hoạch đề nghị báo giá **tối thiểu 3 nhà cung cấp** và cập nhật các trường: Dự án, Hợp đồng, Hợp đồng mua bán, **Báo giá của nhà cung cấp**.",
     how=["Mở thẻ ở cột 2, bấm biểu tượng bút để điền **Báo giá của nhà cung cấp** (đính kèm tệp).", "Bấm **Submit**, xác nhận trong hộp thoại Submit."],
     done="Thẻ sang **Phê duyệt NCC**."),
   "s3": dict(do="Người phê duyệt (cột phải ghi tên, theo **Tuần tự**) xem báo giá và duyệt nhà cung cấp.",
     how=["Mở thẻ, so sánh báo giá.", "Bấm **Approve** (nút xanh) để đi tiếp hoặc **Reject** (nút đỏ) để trả lại.", "Trong hộp thoại Approve, điền Hợp đồng, Hợp đồng mua bán, Chứng chỉ - tài liệu hàng hóa (nếu có), bấm **Approve**."],
     done="Approve: sang **Chuyển bộ phận Thanh toán**. Reject: quay lại bước báo giá."),
   "s4": dict(do="Bước chạy tự động. Tạo công việc con **Tờ trình TT, TƯ** để chuyển hồ sơ cho bộ phận Thanh toán.",
     how=["Bấm **Tạo công việc con: Tờ trình TT, TƯ** (góc phải trên).", "Tạo đủ thì bấm **Chốt danh sách**.", "Chờ các công việc con hoàn thành."],
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
   [dict(id="s3", n="3", t="Ký biên bản giao nhận", who="Người duyệt có thẩm quyền", kind="sign", reject="s2")],
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
   "s1": dict(do="Tạo yêu cầu thanh toán. Bước có thời hạn **1 ngày**. Sau Submit, hệ thống tách thành hai nhánh làm song song.",
     how=["Bấm **Công việc mới**, nhập Tiêu đề, Hợp đồng, đính kèm Yêu cầu thanh toán.", "Mở thẻ, bấm **Submit** rồi xác nhận."], done="Hai thẻ xuất hiện đồng thời ở Nghiệm thu thiết bị và Nhận khối lượng."),
   "s2": dict(do="Nghiệm thu thiết bị (nhánh 2a). Trường cập nhật: **File nghiệm thu thiết bị**.", how=["Mở thẻ, đính kèm **File nghiệm thu thiết bị**.", "Bấm **Submit**, xác nhận."], done="Chờ nhánh 2b xong thì hai nhánh tự gộp."),
   "s3": dict(do="Xác nhận khối lượng thi công của chỉ huy công trường (nhánh 2b). Bước này không có trường nhập.", how=["Chọn bước **Nhận khối lượng Thi công chỉ huy công trường** ở khung Các bước thực hiện.", "Bấm **Submit**; hộp thoại ghi Bước này không cần nhập thông tin."], done="Cả 2a và 2b xong thì gộp nhánh."),
   "m1": dict(do="Hệ thống tự gộp hai nhánh. Màn hình hiện **Các nhánh: 1 trên 2 nhánh đã đến, đang chờ thêm 1**.", how=["Không có thao tác. Nếu thẻ chưa đi tiếp, xử lý nhánh còn lại."], done="Mở hai thẻ song song ở bước 3."),
   "s4": dict(do="Lập hồ sơ quản lý chất lượng (nhánh 3a). Trường: **Hồ sơ quản lý chất lượng**.", how=["Mở thẻ, đính kèm hồ sơ.", "Bấm **Submit**."], done="Chờ nhánh 3b."),
   "s5": dict(do="Lập hồ sơ giá trị thanh toán (nhánh 3b). Trường: **Lập Hồ sơ Giá trị thanh toán**.", how=["Mở thẻ, đính kèm hồ sơ.", "Bấm **Submit**."], done="Cả hai nhánh xong thì gộp."),
   "m2": dict(do="Hệ thống tự gộp nhánh lần hai.", how=["Không có thao tác."], done="Thẻ sang bước ký xác nhận đơn vị tư vấn giám sát."),
   "s6": dict(do="Đơn vị tư vấn giám sát xác nhận. Trường: **Xác nhận đơn vị tư vấn giám sát**. Bước thủ công, có thời hạn **1 ngày**.", how=["Mở thẻ, đính kèm bản xác nhận.", "Bấm **Submit**."], done="Thẻ sang bước ký của Chủ đầu tư."),
   "s7": dict(do="Chủ đầu tư xác nhận cuối cùng. Trường: **Xác nhận Chủ đầu tư**.", how=["Mở thẻ, đính kèm bản xác nhận.", "Bấm **Submit**."], done="Thẻ sang **End**, trạng thái **Đã hoàn thành**."),
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
   [dict(id="s2", n="2", t="Kiểm soát & Phê duyệt", who="Người duyệt có thẩm quyền", kind="sign", reject="s1")],
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
   [dict(id="s2", n="2", t="Trình ký Thanh toán", who="Người duyệt có thẩm quyền", kind="sign")],
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


# ---- Ảnh thao tác (đã ghim số, chụp trên job mẫu TEST) ----
def sh(img, *pins): return dict(img=img, pins=list(pins))
SUB = "Bấm **Submit**, xác nhận trong hộp thoại Submit."
EXTRA = {
 "qt01": dict(
  form=sh("qt01-form", "Nhập **Tiêu đề** (tên đợt, vật tư, dự án).", "Chọn **Dự án** trong danh sách.", "Đính kèm **Phiếu yêu cầu cấp vật tư (BM-01.1)**; có phát sinh thì đính thêm BM-01.2.", "Nhập **Bảng Vật tư yêu cầu** (Tên, Ghi chú, File đính kèm), bấm **Thêm dòng**.", "Bấm **Tạo công việc** (hoặc **Lưu nháp** để làm tiếp sau)."),
  shots=dict(
   s1=[sh("qt01-s1", "Bấm **Trình ký: Phê duyệt yêu cầu (Ban Giám đốc)** để tạo yêu cầu ký. Nếu còn bản nháp, bấm **Tiếp tục bản nháp** ở khung CẦN BẠN TRÌNH KÝ.", "Bấm **Submit** để chuyển bước.", "Thanh bước cho biết đang ở bước nào và bước kế tiếp.", "Dữ liệu và tệp của phiếu (Hợp đồng, BM-01.1, Bảng vật tư): bấm biểu tượng bút để sửa.", "Thanh Thời gian báo **Quá hạn** nếu trễ; bấm bút để đổi hạn.")],
   s2=[sh("qt01-s2", "Khung xanh báo **Đang chờ Phê duyệt yêu cầu · đã ký 0/1**. Bước này tự chạy, không cần bấm gì.", "Người ký là **Người duyệt có thẩm quyền** được giao ở bước này.", "Sau khi ký, tệp PDF đã ký hiện ở mục **Do kết quả ký ghi**.", "Thanh bước đang dừng ở bước 3 Phê duyệt yêu cầu.")],
   s5=[sh("qt01-s5", "Bấm **Chốt danh sách** khi đã tạo đủ **Đợt Mua hàng**.", "Khung xanh báo tiến độ, ví dụ **Đang chờ Đợt Mua hàng · đã xong 1/2**.", "Bảng Vật tư yêu cầu chuyển từ phiếu gốc (2 hàng).", "Người phụ trách bước: **Trần Đình Thái** (NV).")],
  )),
 "qt02": dict(
  form=sh("qt02-form", "Nhập **Tiêu đề**.", "Chọn **Dự án**.", "Đính kèm **Phiếu yêu cầu mua hàng**.", "Bấm **Tạo công việc**."),
  shots=dict(
   s2=[sh("qt02-s2", "Bấm **Submit** để chuyển sang Phê duyệt NCC.", "Thanh bước: đang ở bước 2, kế tiếp là **Phê duyệt NCC**, rồi rẽ nhánh 1 trong 2.", "Trường cập nhật tại bước này: Dự án, Hợp đồng, Hợp đồng mua bán, **Báo giá của nhà cung cấp**.", "Người được giao bước (ở job mẫu là **Base Support**).")],
   s3=[sh("qt02-s3", "Bấm **Approve** để duyệt nhà cung cấp.", "Bấm **Reject** để từ chối, trả phiếu lại.", "Cột phải ghi **Người phê duyệt** và kiểu duyệt **Tuần tự**.", "Thanh bước: đang ở bước 3 Phê duyệt NCC."), sh("qt02-s3dlg", "Điền **Hợp đồng** (nếu có).", "Đính kèm **Hợp đồng mua bán**.", "Đính kèm **Chứng chỉ, tài liệu hàng hóa**.", "Bấm **Approve** để hoàn tất duyệt.")],
   s4=[sh("qt02-s4", "Bấm **Tạo công việc con: Tờ trình TT, TƯ**.", "Bấm **Chốt danh sách** khi đã tạo đủ công việc con.", "Dòng thông báo: bước này chạy tự động, chưa có gì để thao tác.", "Dữ liệu của phiếu hiển thị chỉ đọc."), sh("qt02-s4b", "Sau khi tạo, mở tab **Liên kết** để xem công việc con.", "Công việc con hiện theo nhóm **Tờ trình TT, TƯ**.", "Trạng thái: **Đang xử lý** đến khi công việc con xong.", "Bấm lại nút Tạo công việc con nếu cần tạo thêm."), sh("qt02-s4dlg", "Mục **Tờ trình TT, TƯ** là danh sách sẽ chốt.", "Ghi chú (tuỳ chọn), lưu trong lịch sử công việc.", "Bấm **Chốt danh sách**: sau đó không nhận thêm công việc con."), sh("qt02-s4c", "Dòng đầu: **Chốt thủ công** kèm thời điểm, bước đang gom kết quả.", "Người xử lý công việc con (job mẫu: **Base Support**).", "Hạn còn lại của công việc con.", "Khi công việc con **Hoàn thành**, phiếu mua hàng tự đi tiếp bước 5.")],
  )),
 "qt03": dict(
  form=sh("qt03-form", "Nhập **Tiêu đề**.", "Chọn **Dự án**.", "Đính kèm **Bộ hồ sơ** thanh toán.", "Bấm **Chọn tệp** để thêm **Biên bản giao nhận**.", "Bấm **Tạo công việc**."),
  shots=dict(
   s1=[sh("qt03-s1", "Bấm **Submit** để gửi hồ sơ.", "Thanh bước: đang ở bước 2 Gửi hồ sơ thanh toán.", "Điền **Bộ hồ sơ** và **Biên bản giao nhận** bằng biểu tượng bút nếu chưa có.", "Người được giao: ở job mẫu là **Base Support**.")],
   s2=[sh("qt03-s2", "Bấm **Submit** để chuyển sang bước ký.", "Thanh bước: đang ở bước 3 Tạo biên bản giao nhận.", "Dữ liệu phiếu: Dự án, Bộ hồ sơ, Biên bản giao nhận.", "Người được giao bước.")],
   s3=[sh("qt03-s3", "Bấm **Trình ký: Biên bản giao nhận** để tạo yêu cầu ký.", "Bấm **Chốt danh sách** khi đã tạo đủ yêu cầu ký.", "Dòng thông báo: bước chạy tự động, chờ chữ ký.", "Mục **Do kết quả ký ghi**: biên bản đã ký sẽ hiện ở đây."), sh("qt03-signdlg", "**Tên yêu cầu ký** (tự điền theo tên tài liệu và công việc).", "Tick **Tài liệu cần ký**: Bộ hồ sơ hoặc Biên bản giao nhận.", "Tick **Gửi ngay khi văn bản đã đủ vị trí ký** nếu muốn gửi luôn.", "Bấm **Gửi ký**. Tài liệu phải là PDF hoặc Office đã đính kèm.")],
  )),
 "qt05": dict(
  form=sh("qt05-form", "Nhập **Tiêu đề**.", "Nhập số **Hợp đồng**.", "Đính kèm **Yêu cầu thanh toán**.", "Bấm **Tạo công việc**."),
  shots=dict(
   s1=[sh("qt05-s1", "Bấm **Submit** để tách hai nhánh song song.", "Thanh bước: đang ở bước 2 Yêu cầu thanh toán.", "Thanh Thời gian: bước có hạn **1 ngày** (ghi Còn 1 ngày).", "Dữ liệu phiếu: Hợp đồng, Yêu cầu thanh toán.")],
   s2=[sh("qt05-par", "Bấm **Submit** để hoàn thành nhánh A.", "Thanh bước báo **Nhánh A trong 2 · 1 đang xử lý**.", "Khung Các bước thực hiện liệt kê 2 nhánh, nhãn **Đến lượt bạn** là nhánh bạn phải làm.", "Điền **File nghiệm thu thiết bị**.")],
   m1=[sh("qt05-merge", "Khung **Các nhánh** cho biết tiến độ gộp.", "Thanh tiến độ: **1 trên 2 nhánh đã đến, đang chờ thêm 1**.", "Chip **Merge Branches** là bước gộp, chạy tự động.", "Dòng thông báo: bước chạy tự động.")],
   s4=[sh("qt05-pair2", "Bấm **Submit** khi xong hồ sơ của nhánh này.", "Hai chip đều ghi **Đến lượt bạn**: chọn nhánh cần làm.", "Điền **Lập Hồ sơ Giá trị thanh toán** (nhánh 3b) hoặc **Hồ sơ quản lý chất lượng** (nhánh 3a).", "Thời hạn còn lại của bước.")],
   s6=[sh("qt05-sign1", "Bấm **Submit** sau khi có xác nhận của tư vấn giám sát.", "Đính kèm **Xác nhận đơn vị tư vấn giám sát**.", "Thanh bước: bước 5 hiện tại, kế tiếp là Ký xác nhận Chủ đầu tư.")],
   s7=[sh("qt05-sign2", "Bấm **Submit** để hoàn tất.", "Đính kèm **Xác nhận Chủ đầu tư**.", "Thanh bước: bước 6, kế tiếp là End."), sh("qt05-end", "Tiêu đề ghi **Đã hoàn thành** kèm thời điểm.", "Thanh bước đi hết đến **End**.", "Thanh Thời gian: **Hoàn thành sau 1 phút** (job mẫu).")],
  )),
 "qt06": dict(
  form=sh("qt06-form", "Nhập **Tiêu đề** (ví dụ: Đề nghị thanh toán lần 1).", "Chọn **Dự án**.", "Chọn **Nhà cung cấp**.", "Đính kèm **Tờ trình Đề nghị TT, TƯ** và **Giấy tờ kèm theo** (hoá đơn, hợp đồng...).", "Bấm **Tạo công việc**. Các trường còn lại (Nội dung thanh toán, Tài khoản, Giá trị hợp đồng, Giá trị thực hiện...) có thể điền sau."),
  shots=dict(
   s1=[sh("qt06-s1", "Bấm **Trình ký: Ký Tờ trình TT, TƯ** để tạo yêu cầu ký.", "Bấm **Submit** để chuyển sang bước Kiểm soát & Phê duyệt.", "Thanh bước: đang ở bước 2, kế tiếp là Kiểm soát & Phê duyệt.", "Các trường dữ liệu: Dự án, Nhà cung cấp, Giấy tờ kèm theo... bấm bút để sửa.", "Người được giao xử lý bước này.")],
   s2=[sh("qt06-s2", "Nếu còn bản nháp, bấm **Tiếp tục bản nháp** ở khung CẦN BẠN TRÌNH KÝ.", "Khung xanh: **Đang chờ Ký Tờ trình TT, TƯ · đã ký 0/1**. Bước chạy tự động.", "Bấm **Chốt danh sách** khi đã tạo đủ yêu cầu ký để hệ thống xét kết quả.", "Thanh bước đang ở bước 3 Kiểm soát & Phê duyệt.")],
  )),
 "qt07": dict(
  form=sh("qt07-form", "Nhập **Tiêu đề**.", "Bấm **Chọn bản ghi** ở mục **Dự án**, chọn dự án rồi **Xác nhận**.", "Nhập **Hợp đồng**.", "Đính kèm **File Đề nghị thanh toán**.", "Bấm **Tạo công việc**."),
  shots=dict(
   s1=[sh("qt07-s1", "Bấm **Trình ký: Trình ký thanh toán** để tạo yêu cầu ký (cần tệp đính kèm).", "Bấm **Submit** để chuyển sang bước ký.", "Thanh bước: đang ở bước 2 Tổng hợp đợt thanh toán.", "Trường: Dự án (bản ghi liên kết), Hợp đồng, File Đề nghị thanh toán.")],
   s2=[sh("qt07-s2", "Bấm **Trình ký: Trình ký thanh toán** để gửi yêu cầu ký.", "Bấm **Chốt danh sách** khi đã tạo đủ yêu cầu ký.", "Dòng thông báo: bước chạy tự động, chờ chữ ký.", "Mục **Do kết quả ký ghi**: **File Đề nghị thanh toán** đã ký sẽ hiện ở đây.")],
  )),
}
