# -*- coding: utf-8 -*-
import base64, html, json, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import PROCESSES, EXTRA

HERE = os.path.dirname(__file__)
ROOT = os.path.dirname(HERE)

def md(s):
    s = html.escape(s)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)

KIND = {"manual": ("Làm việc", "ev"), "sign": ("Trình ký / duyệt", "po"),
        "sub": ("Công việc con", "app"), "merge": ("Gộp nhánh", "fd")}

def flow_svg(p):
    W, NW, NH, GAP = 640, 250, 58, 44
    rows = p["rows"]
    y = 20
    pos = {}
    for r in rows:
        k = len(r)
        for i, n in enumerate(r):
            cx = W/2 if k == 1 else (W/2 - 150 + i*300)
            pos[n["id"]] = (cx, y)
        y += NH + GAP
    H = y - GAP + 24
    out = [f'<svg class="arch" viewBox="0 0 {W+140} {H}" role="img" aria-label="Lưu đồ {html.escape(p["code"])}">']
    out.append('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="var(--muted)"/></marker>'
               '<marker id="ard" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="var(--danger)"/></marker></defs>')
    # edges
    for ri in range(len(rows)-1):
        for a in rows[ri]:
            for b in rows[ri+1]:
                ax, ay = pos[a["id"]]; bx, by = pos[b["id"]]
                out.append(f'<path d="M{ax} {ay+NH} C{ax} {ay+NH+GAP/2} {bx} {by-GAP/2} {bx} {by}" class="edge" marker-end="url(#ar)"/>')
    # reject loops
    for r in rows:
        for n in r:
            if n.get("reject"):
                ax, ay = pos[n["id"]]; bx, by = pos[n["reject"]]
                x1 = ax + NW/2; x2 = bx + NW/2
                xo = x1 + 56
                out.append(f'<path d="M{x1} {ay+NH/2} H{xo} V{by+NH/2} H{x2}" class="edge rej" marker-end="url(#ard)"/>')
                out.append(f'<text x="{xo+8}" y="{(ay+by+NH)/2}" class="elabel rejt">Từ chối</text>')
    # nodes
    for r in rows:
        for n in r:
            cx, ny = pos[n["id"]]
            x = cx - NW/2
            lab, cls = KIND[n["kind"]]
            t = n["t"]
            if len(t) > 34: t = t[:33].rstrip() + "…"
            out.append(f'<a href="#{p["id"]}-{n["id"]}" class="node k-{cls}" data-go="{p["id"]}-{n["id"]}">'
                       f'<rect x="{x}" y="{ny}" width="{NW}" height="{NH}" rx="12"/>'
                       f'<text x="{x+14}" y="{ny+23}" class="nt">{html.escape(n["n"])} · {html.escape(t)}</text>'
                       f'<text x="{x+14}" y="{ny+42}" class="ns">{html.escape(n["who"])} · {lab}</text>'
                       f'<title>{html.escape(n["t"])}</title></a>')
    out.append('</svg>')
    return "".join(out)

def pinfig(sh, cap):
    pins = "".join(f"<li><i class='pin'>{i+1}</i><span>{md(t)}</span></li>" for i, t in enumerate(sh["pins"]))
    return (f'<figure class="shot big"><img data-k="{sh["img"]}" alt=""><figcaption>{cap} · bấm để phóng to</figcaption></figure>'
            f'<ol class="pinlist">{pins}</ol>')

def step_cards(p):
    ex = EXTRA.get(p["id"], {})
    out = []
    if ex.get("form"):
        out.append(f'''<article class="step wide k-ev" id="{p["id"]}-form"><div class="sh"><span class="sn2">B0</span><div><h4>Tạo công việc mới</h4>
<div class="pills"><span class="chip ev">Làm việc</span><span class="chip">👤 Người khởi tạo</span></div></div></div>
<p class="do">Bấm <b>Công việc mới</b> ở góc phải trên của dịch vụ {html.escape(p["code"])}, điền theo ảnh rồi bấm <b>Tạo công việc</b>.</p>
{pinfig(ex["form"], "Form Công việc mới trên BPM")}
<p class="goto">Làm theo: <a class="golink" href="{p["url"]}" target="_blank" rel="noopener">Mở {html.escape(p["code"])} trên BPM ↗</a></p></article>''')
    for r in p["rows"]:
        for n in r:
            s = p["steps"][n["id"]]
            lab, cls = KIND[n["kind"]]
            how = "".join(f"<li>{md(h)}</li>" for h in s["how"])
            out.append(f'''<article class="step k-{cls}{' wide' if n['id'] in ex.get('shots', {}) else ''}" id="{p["id"]}-{n["id"]}">
<div class="sh"><span class="sn2">{html.escape(n["n"])}</span><div><h4>{html.escape(n["t"])}</h4>
<div class="pills"><span class="chip {cls}">{lab}</span><span class="chip">👤 {html.escape(n["who"])}</span></div></div></div>
<p class="do">{md(s["do"])}</p>
<h5>Cách làm</h5><ol>{how}</ol>
<p class="done"><b>Xong bước khi:</b> {md(s["done"])}</p>
{pinfig(ex["shots"][n["id"]], "Màn hình xử lý bước") if n["id"] in ex.get("shots", {}) else ""}
<p class="goto">Làm theo: <a class="golink" href="{p["url"]}" target="_blank" rel="noopener">Mở {html.escape(p["code"])} trên BPM ↗</a></p>
</article>''')
    return "\n".join(out)

def faq(p):
    out = []
    for q, a, step in p["faq"]:
        out.append(f'<details class="prob"><summary>{md(q)}</summary><p>{md(a)}</p>'
                   f'<p class="goto"><a href="#{p["id"]}-{step}" data-go="{p["id"]}-{step}">Xem hướng dẫn bước liên quan →</a></p></details>')
    return "\n".join(out)

def tab(p, idx):
    nsteps = sum(len(r) for r in p["rows"] if r[0]["kind"] != "merge")
    nsign = sum(1 for r in p["rows"] for n in r if n["kind"] == "sign")
    nsub = sum(1 for r in p["rows"] for n in r if n["kind"] == "sub")
    par = sum(1 for r in p["rows"] if len(r) > 1)
    fig2 = f'<figure class="shot"><img data-k="{p["img2"]}" alt=""><figcaption>Màn hình thật · bấm để phóng to</figcaption></figure>' if p.get("img2") else ""
    samples = "".join(f"<li>{html.escape(s)}</li>" for s in p["samples"])
    legend = '<div class="legend"><span><i class="sw ev"></i>Làm việc</span><span><i class="sw po"></i>Trình ký / duyệt</span><span><i class="sw app"></i>Công việc con</span><span><i class="sw fd"></i>Gộp nhánh</span><span><i class="sw rj"></i>Từ chối (nét đứt)</span></div>'
    return f'''<section class="tabpane" id="pane-{p["id"]}" data-tab="{p["id"]}" hidden>
<div class="hero"><div class="eyebrow">HƯỚNG DẪN SỬ DỤNG · BPM · {html.escape(p["group"]).upper()}</div>
<h1>{html.escape(p["code"])} · {html.escape(p["name"])}</h1>
<p class="lead">{md(p["lead"])}</p>
<div class="path"><a href="#{p["id"]}-flow">① Xem lưu đồ</a><a href="#{p["id"]}-steps">② Làm theo từng bước</a><a href="#{p["id"]}-faq">③ Gặp vấn đề?</a></div>
<div class="kpis"><div class="kpi"><b>{nsteps}</b><span>bước xử lý</span></div><div class="kpi"><b>{nsign}</b><span>bước ký / duyệt</span></div><div class="kpi"><b>{nsub}</b><span>bước công việc con</span></div><div class="kpi"><b>{par}</b><span>cặp nhánh song song</span></div></div>
<p class="hint">Dữ liệu đọc từ hệ thống BPM ngày 20/11/2026. <a class="golink" href="{p["url"]}" target="_blank" rel="noopener">Mở dịch vụ ↗</a></p></div>

<h2 id="{p["id"]}-flow"><span class="sn">1</span>Lưu đồ quy trình</h2>
<p class="lead2">Bấm vào từng bước để nhảy tới hướng dẫn. Đường nét đứt đỏ là nhánh Từ chối.</p>
{legend}
<div class="two"><div class="diag">{flow_svg(p)}</div>
<figure class="shot"><img data-k="{p["img"]}" alt="Lưu đồ {html.escape(p["code"])} trên BPM"><figcaption>Lưu đồ thật trên BPM (tab Quy trình) · bấm để phóng to</figcaption></figure></div>
{fig2}

<h2 id="{p["id"]}-steps"><span class="sn">2</span>Làm theo từng bước</h2>
<div class="steps">{step_cards(p)}</div>

<h2 id="{p["id"]}-faq"><span class="sn">3</span>Gặp vấn đề?</h2>
<div class="probs">{faq(p)}</div>

<h2 id="{p["id"]}-sample"><span class="sn">4</span>Dữ liệu mẫu để xem thử</h2>
<div class="note"><p>Các phiếu có sẵn trong dịch vụ (mở bằng bộ lọc trên BPM):</p><ul>{samples}</ul>
<p class="goto">Làm theo: <a class="golink" href="{p["url"]}" target="_blank" rel="noopener">Mở {html.escape(p["code"])} ↗</a></p></div>
</section>'''

def overview():
    TOT = sum(len(r) for p in PROCESSES for r in p['rows'] if r[0]['kind'] != 'merge')
    SG = sum(1 for p in PROCESSES for r in p['rows'] for n in r if n['kind'] == 'sign')
    cards = []
    for p in PROCESSES:
        cards.append(f'<a class="svc" href="#{p["id"]}" data-tabgo="{p["id"]}"><div class="k">{html.escape(p["group"])}</div><h4>{html.escape(p["code"])} · {html.escape(p["name"])}</h4><p>{md(p["lead"])}</p><span class="golink">Xem hướng dẫn →</span></a>')
    return f'''<section class="tabpane" id="pane-home" data-tab="home">
<div class="hero"><div class="eyebrow">HƯỚNG DẪN SỬ DỤNG · BASE BPM</div>
<h1>6 quy trình <span class="grad">BPM</span> của Kinh Đô</h1>
<p class="lead">Chọn quy trình trên thanh phía trên. Mỗi tab có **lưu đồ**, **hướng dẫn từng bước** và **tình huống thường gặp**.</p>
<div class="kpis"><div class="kpi"><b>6</b><span>quy trình</span></div><div class="kpi"><b>3</b><span>nhóm dịch vụ</span></div><div class="kpi"><b>{TOT}</b><span>bước xử lý</span></div><div class="kpi"><b>{SG}</b><span>bước ký / duyệt</span></div></div></div>
<h2><span class="sn">1</span>Chọn quy trình</h2><div class="grid3">{"".join(cards)}</div>
<h2><span class="sn">2</span>Cách đọc tài liệu</h2>
<div class="note"><p>① <b>Lưu đồ</b>: các bước theo thứ tự, màu theo loại bước. ② <b>Làm theo từng bước</b>: ai làm, bấm gì, khi nào xong. ③ <b>Gặp vấn đề?</b>: triệu chứng và cách xử lý. Mỗi mục có link mở đúng màn hình trên BPM.</p></div>
<div class="note po"><p><b>Cần xác nhận với Quản trị:</b> người phụ trách cụ thể từng bước, trường bắt buộc và SLA được cấu hình trong <b>Cài đặt dịch vụ</b>. Tài liệu ghi theo bộ phận lấy từ tên bước.</p></div>
</section>'''

def main():
    imgs = {}
    for f in os.listdir(os.path.join(HERE, "img")):
        k = os.path.splitext(f)[0]
        imgs[k] = "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(HERE, "img", f), "rb").read()).decode()
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    tabs = [("home", "Tổng quan")] + [(p["id"], f'{p["code"]} · {p["name"]}'.replace("Theo dõi hồ sơ thanh toán Tổ đội, Nhà thầu phụ", "Theo dõi hồ sơ TT")) for p in PROCESSES]
    tabbar = "".join(f'<button class="tabbtn" data-tab="{i}">{html.escape(t)}</button>' for i, t in tabs)
    panes = overview() + "\n".join(tab(p, i) for i, p in enumerate(PROCESSES))
    out = (tpl.replace("{{TABBAR}}", tabbar).replace("{{PANES}}", panes)
              .replace("{{IMGS}}", json.dumps(imgs)))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(out)
    print("OK", len(out)//1024, "KB")

if __name__ == "__main__":
    main()
