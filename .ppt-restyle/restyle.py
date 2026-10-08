"""Restyle 电控组第二讲~第五讲 content pages into 第一讲's single-column style.

Source grammar (2-5讲 content pages):
  * title textbox at (1.54,0.46); section badge (0.46,0.22); footer (9.80,0.76)
  * ITEM blocks: left column (0.87|1.26, y) w 5.58|5.97, heading + description
  * CARD (7.08,1.56) 5.25x3.19 + CARD_CODE (7.25,1.67) 4.92x2.94
  * drawn tables: header text row at y~1.65 + row textboxes at y 2.18/2.79/3.40/4.01
  * homework: badge (0.87,y) 0.78x0.56 + text (1.72,y) 10.44x0.89
  * bottom bar: shape at (0.87, y>=5.0) w 11.36 (with or without its own text)

Target style (第一讲 content pages 18-28):
  title (1.56,0.44) 7.66x0.60, 24pt bold #084A91
  single column x=0.99 w=11.35, from y=1.55 to y=6.90
  section head bold #084A91 / body #17212B / note #505A65 / code mono #17212B
  native table 11.35 wide, header fill #084A91 white bold, thin black rules
"""
import sys, math, os, re
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml

A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
CN = 'Noto Sans SC'
MONO = 'Consolas'
TITLE_C, HEAD_C, BODY_C, NOTE_C, CODE_C, RULE_C = \
    '084A91', '084A91', '17212B', '505A65', '17212B', '000000'
TITLE_POS = (1.56, 0.44, 7.66, 0.60)
FOOTER_TEXT = '哈理工 A.I.R. 创新实验室'
FOOTER_POS = (9.83, 0.77, 2.52, 0.33)
FOOTER_SIZE = 12.75
X, W = 0.99, 11.35
TITLE_DROP, BOTTOM = 1.55, 6.90

CHROME_POS = {(0.0, 0.0), (0.4, -0.04), (0.55, -0.26), (0.61, 0.94),
              (11.54, 5.71), (12.36, 3.35), (12.84, 0.86), (9.36, 0.6),
              (12.37, 0.6), (9.8, 0.76), (9.83, 0.77), (0.46, 0.22),
              (1.54, 0.46), (1.55, 0.47)}
TITLE_POS_KEYS = {(1.54, 0.46), (1.55, 0.47)}
FOOTER_KEYS = {(9.8, 0.76), (9.83, 0.77)}
BADGE_KEYS = {(0.46, 0.22)}

LADDER = [
    (21.0, 21.0, 17.25, 20.25, 19.5),
    (19.5, 19.5, 16.5, 18.0, 18.0),
    (18.0, 18.5, 15.5, 16.5, 17.0),
    (17.0, 17.5, 15.0, 15.5, 16.0),
    (16.0, 16.5, 14.0, 15.0, 15.0),
    (15.0, 15.5, 13.0, 14.0, 14.0),
    (14.0, 14.5, 12.0, 13.0, 13.0),
]
LINE, CODE_LINE, INSET = 1.35, 1.30, 0.10


# ------------------------------------------------------------------ text metrics
def is_wide(ch):
    o = ord(ch)
    return (0x1100 <= o <= 0x115F or 0x2E80 <= o <= 0xA4CF or 0xAC00 <= o <= 0xD7A3
            or 0xF900 <= o <= 0xFAFF or 0xFE30 <= o <= 0xFE4F
            or 0xFF00 <= o <= 0xFF60 or 0xFFE0 <= o <= 0xFFE6 or o == 0x200B)


def ems(s, mono=False):
    cjk, latin = (1.0, 0.55) if mono else (1.0, 0.5)
    return sum(cjk if is_wide(c) else latin for c in s)


def n_lines(s, width_in, pt, mono=False):
    if not s:
        return 1
    per = max((width_in - INSET) * 72.0 / pt, 1.0)
    return sum(max(1, math.ceil(ems(hard, mono) * 1.04 / per)) for hard in s.split('\n'))


def txt_h(s, width_in, pt, mono=False, line=LINE):
    return n_lines(s, width_in, pt, mono) * pt * line / 72.0


# ------------------------------------------------------------------ pptx helpers
def geom(sh):
    return (round(Emu(sh.left).inches, 2), round(Emu(sh.top).inches, 2),
            round(Emu(sh.width).inches, 2), round(Emu(sh.height).inches, 2))


def paras_of(sh):
    if not sh.has_text_frame:
        return []
    return [''.join(r.text for r in p.runs).strip()
            for p in sh.text_frame.paragraphs if ''.join(r.text for r in p.runs).strip()]


def text_of(sh):
    return '\n'.join(paras_of(sh))


def is_mono(sh):
    if not sh.has_text_frame:
        return False
    return any(r.font.name in ('Consolas', 'DejaVu Sans Mono', 'Courier New')
               for p in sh.text_frame.paragraphs for r in p.runs)


def is_footer_text(sh):
    t = text_of(sh).replace('\u200b', '').replace(' ', '').strip()
    return t == '哈理工A.I.R.创新实验室'

def keep(sh):
    if sh.left is None:
        return False
    if geom(sh)[:2] in CHROME_POS:
        return True
    return is_footer_text(sh)


def set_font(run, size, bold, color, name):
    f = run.font
    f.size = Pt(size)
    f.bold = bold
    f.color.rgb = RGBColor.from_string(color)
    f.name = name
    rPr = run._r.get_or_add_rPr()
    for tag in ('ea', 'cs'):
        for el in rPr.findall(qn('a:' + tag)):
            rPr.remove(el)
        rPr.append(parse_xml('<a:%s xmlns:a="%s" typeface="%s"/>' % (tag, A, name)))


def style_para(p, size, line):
    p.line_spacing = Pt(size * line)
    p.space_before = Pt(0)
    p.space_after = Pt(0)


def add_text_block(slide, kind, payload, y, h, sizes):
    body, head, code, tbl, emph = sizes
    box = slide.shapes.add_textbox(Inches(X), Inches(y), Inches(W), Inches(max(h, 0.25)))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = MSO_ANCHOR.TOP
    if kind == 'code':
        pt, bold, color, name, line, mono = code, False, CODE_C, MONO, CODE_LINE, True
    else:
        pt, bold, color, name, mono = {
            'head': (head, True, HEAD_C, CN, False),
            'body': (body, False, BODY_C, CN, False),
            'note': (max(body - 2.25, 11.0), False, NOTE_C, CN, False),
            'emph': (emph, True, HEAD_C, CN, False),
        }[kind]
        line = LINE
    for i, ln in enumerate(payload.split('\n')):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        style_para(p, pt, line)
        r = p.add_run()
        r.text = ln if ln else ' '
        set_font(r, pt, bold, color, name)
    return box


def block_h(kind, payload, sizes):
    body, head, code, tbl, emph = sizes
    if kind == 'code':
        return sum(max(1, n_lines(ln, W, code, True)) for ln in payload.split('\n')) * code * CODE_LINE / 72.0
    pt = {'head': head, 'body': body, 'note': max(body - 2.25, 11.0), 'emph': emph}[kind]
    return sum(txt_h(ln, W, pt) for ln in payload.split('\n'))


def table_rows_h(rows, widths, pt):
    hs = []
    for row in rows:
        mx = 1
        for j, cell in enumerate(row):
            mx = max(mx, n_lines(cell, widths[j], pt))
        hs.append(max(mx * pt * LINE / 72.0 + 0.14, 0.34))
    return hs


def add_table(slide, rows, widths, y, pt):
    nrow, ncol = len(rows), len(rows[0])
    widths = [w * W / sum(widths) for w in widths]
    hs = table_rows_h(rows, widths, pt)
    gf = slide.shapes.add_table(nrow, ncol, Inches(X), Inches(y), Inches(W), Inches(sum(hs)))
    table = gf.table
    tbl = gf._element.graphic.graphicData.find(qn('a:tbl'))
    old = tbl.find(qn('a:tblPr'))
    if old is not None:
        tbl.remove(old)
    tbl.insert(0, parse_xml('<a:tblPr xmlns:a="%s" firstRow="1" bandRow="0"/>' % A))
    for j, w in enumerate(widths):
        table.columns[j].width = Inches(w)
    for i, h in enumerate(hs):
        table.rows[i].height = Inches(h)
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            c = table.cell(i, j)
            c.margin_left = c.margin_right = Inches(0.08)
            c.margin_top = c.margin_bottom = Inches(0.02)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            hdr = (i == 0)
            tcPr = c._tc.get_or_add_tcPr()
            for tag in ('lnL', 'lnR', 'lnT', 'lnB', 'lnTlToBr', 'lnBlToTr',
                        'solidFill', 'noFill', 'gradFill', 'blipFill', 'pattFill', 'grpFill'):
                for el in tcPr.findall(qn('a:' + tag)):
                    tcPr.remove(el)
            for tag in ('lnL', 'lnR', 'lnT', 'lnB'):
                tcPr.append(parse_xml(
                    '<a:%s xmlns:a="%s" w="9525" cap="flat" cmpd="sng" algn="ctr">'
                    '<a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
                    '<a:prstDash val="solid"/></a:%s>' % (tag, A, RULE_C, tag)))
            tcPr.append(parse_xml('<a:solidFill xmlns:a="%s"><a:srgbClr val="%s"/></a:solidFill>'
                                  % (A, HEAD_C if hdr else 'FFFFFF')))
            tf = c.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            style_para(p, pt, LINE)
            r = p.add_run()
            r.text = cell if cell else ' '
            set_font(r, pt, hdr, 'FFFFFF' if hdr else BODY_C, CN)
    return sum(hs)


# ------------------------------------------------------------------ extraction
NUM_MAP = {'①': '1.', '②': '2.', '③': '3.', '④': '4.', '⑤': '5.', '⑥': '6.',
           '❶': '1.', '❷': '2.', '❸': '3.'}
BADGE_RE = re.compile(r'^\d{1,2}\s*[.、]?$')


def strip_marker(s):
    s = s.strip()
    if s[:1] in NUM_MAP:
        return NUM_MAP[s[0]] + ' ' + s[1:].strip()
    return s


STRIP_RE = re.compile(r'[\s\u200b\u3000]')
MARK_CHARS = '①②③④⑤⑥⑦⑧⑨⑩'


def norm_key(s):
    s = s.replace('\u200b', '')
    for m in MARK_CHARS:
        s = s.replace(m, '')
    s = STRIP_RE.sub('', s)
    return re.sub(r'^[0-9]{1,2}[.、)）]?', '', s)


def clean_num(s):
    s = s.strip().rstrip('.．、)）')
    return str(int(s)) if s.isdigit() else s


def extract(slide):
    kept, content, pics = [], [], []
    for sh in slide.shapes:
        if sh.left is None:
            continue
        if keep(sh):
            kept.append(sh)
        else:
            content.append(sh)
            if sh.shape_type == 13:
                pics.append(sh)

    title = footer = badge = None
    for sh in kept:
        k = geom(sh)[:2]
        if k in TITLE_POS_KEYS:
            title = sh
        elif k in FOOTER_KEYS or is_footer_text(sh):
            footer = sh
        elif k in BADGE_KEYS:
            badge = sh

    # pictures that own the page (e.g. 关于时间安排 schedule image) -> leave page alone
    if any(Emu(p.width).inches > 6.0 and Emu(p.height).inches > 3.0 for p in pics):
        return title, footer, badge, None, ['picture-page']

    bars, hwbadge, hwtext, items, codes, smallnum, tbls, texts = \
        [], [], [], [], [], [], [], []
    for sh in content:
        L, T, Wd, H = geom(sh)
        if sh.has_table:
            tbls.append(sh)
            continue
        if sh.shape_type == 13:
            continue
        t = text_of(sh)
        if T >= 4.95 and Wd >= 11.0 and abs(L - 0.87) < 0.08:
            bars.append(sh)
            continue
        if Wd < 0.5 and BADGE_RE.match(t):
            smallnum.append(sh)
            continue
        if abs(Wd - 0.78) < 0.10 and H > 0.4 and t:
            hwbadge.append(sh)
            continue
        if Wd < 0.35:
            continue
        if 6.9 < L < 7.6 and Wd > 3.5 and t:
            codes.append(sh)
            continue
        if 0.75 < L < 1.45 and 4.5 < Wd < 7.0 and T < 5.0 and t:
            items.append(sh)
            continue
        if is_mono(sh) and t:
            codes.append(sh)
            continue
        if t:
            texts.append(sh)

    bar_text = ''
    for sh in bars:
        t = text_of(sh)
        if len(t) > len(bar_text):
            bar_text = t

    blocks = []
    smallnum.sort(key=lambda s: geom(s)[1])

    if items:
        items.sort(key=lambda s: geom(s)[1])
        used_codes = set()
        for it in items:
            iy = geom(it)[1]
            near = [b for b in smallnum if abs(geom(b)[1] - iy) < 0.30]
            num = clean_num(text_of(near[0])) if near else ''
            ps = paras_of(it)
            if not ps:
                continue
            head = strip_marker(ps[0])
            if num and not re.match(r'^\d+[.、]', head):
                head = '%s. %s' % (num, head)
            blocks.append(('head', head))
            for p in ps[1:]:
                blocks.append(('body', p))
            if len(codes) > 1:
                for c in codes:
                    if abs(geom(c)[1] - iy) < 0.35 and id(c) not in used_codes:
                        blocks.append(('code', text_of(c)))
                        used_codes.add(id(c))
        for c in codes:
            if id(c) not in used_codes:
                blocks.append(('code', text_of(c)))
        for sh in texts:
            blocks.append(('code' if is_mono(sh) else 'body', text_of(sh)))

    elif hwbadge:
        hwbadge.sort(key=lambda s: geom(s)[1])
        hwtext = sorted([s for s in texts if geom(s)[2] > 8.0], key=lambda s: geom(s)[1])
        for i, nsh in enumerate(hwbadge):
            num = clean_num(text_of(nsh)) or str(i + 1)
            body = hwtext[i] if i < len(hwtext) else None
            ps = paras_of(body) if body is not None else []
            if len(ps) >= 2:
                # task name + explanation -> 第一讲 style: bold head then body
                blocks.append(('head', '%s. %s' % (num, ps[0])))
                for p in ps[1:]:
                    blocks.append(('body', p))
            elif ps:
                # a single line is the requirement itself -> plain numbered line
                blocks.append(('body', '%s. %s' % (num, ps[0])))
            else:
                blocks.append(('body', '%s.' % num))
        for sh in hwtext[len(hwbadge):]:
            blocks.append(('body', text_of(sh)))
        for c in codes:
            blocks.append(('code', text_of(c)))
        for sh in texts:
            if sh not in hwtext:
                blocks.append(('body', text_of(sh)))

    elif tbls:
        for sh in tbls:
            rows = [[c.text.replace('\u200b', '').strip() for c in r.cells] for r in sh.table.rows]
            wds = [Emu(c.width).inches for c in sh.table.columns]
            blocks.append(('table', (rows, wds)))
        for sh in texts:
            blocks.append(('code' if is_mono(sh) else 'body', text_of(sh)))

    else:
        rows_by_y = {}
        for sh in texts:
            L, T, Wd, H = geom(sh)
            if 1.5 <= T <= 4.9 and Wd < 11.0:
                rows_by_y.setdefault(round(T, 1), []).append(sh)
        if len(rows_by_y) >= 2:
            ys = sorted(rows_by_y)
            rows, widths = [], None
            for y in ys:
                cells = sorted(rows_by_y[y], key=lambda s: geom(s)[0])
                rows.append([text_of(c) for c in cells])
                if widths is None and len(cells) > 1:
                    widths = [geom(c)[2] + 0.30 for c in cells]
            ncol = max(len(r) for r in rows)
            rows = [r + [''] * (ncol - len(r)) for r in rows]
            if widths is None or len(widths) != ncol:
                widths = [1.0] * ncol
            blocks.append(('table', (rows, widths)))
            used = {id(s) for y in ys for s in rows_by_y[y]}
            for sh in texts:
                if id(sh) not in used:
                    blocks.append(('code' if is_mono(sh) else 'body', text_of(sh)))
        else:
            for sh in texts:
                blocks.append(('code' if is_mono(sh) else 'body', text_of(sh)))

    # ---- safety net: a page must never silently lose text
    handled = []
    for kind, payload in blocks:
        if kind == 'table':
            for r in payload[0]:
                for c in r:
                    handled.append(norm_key(c))
        else:
            for ln in payload.split('\n'):
                handled.append(norm_key(ln))
    joined = ' '.join(handled)
    for sh in content:
        if sh.shape_type == 13 or sh.has_table:
            continue
        L, T, Wd, H = geom(sh)
        if Wd >= 11.0 and T >= 4.95 and abs(L - 0.87) < 0.08:
            continue                       # bottom bar fill, already captured
        if abs(Wd - 0.78) < 0.10 and H > 0.4:
            continue                       # homework number badge
        if Wd < 0.5:
            continue                       # thin accent bar
        for p in paras_of(sh):
            k = norm_key(p)
            if len(k) >= 2 and k not in joined:
                blocks.append(('code' if is_mono(sh) else 'body', p))
                joined += ' ' + k

    blocks = [b for b in blocks if b[0] == 'table' or b[1]]
    if bar_text:
        blocks.append(('emph', bar_text))
    return title, footer, badge, blocks, []


def fit(blocks):
    for sizes in LADDER:
        body, head, code, tbl, emph = sizes
        y, ok = TITLE_DROP, True
        for kind, payload in blocks:
            if kind == 'table':
                rows, wds = payload
                h = sum(table_rows_h(rows, [w * W / sum(wds) for w in wds], tbl))
            else:
                h = block_h(kind, payload, sizes)
            if y + h > BOTTOM + 0.03:
                ok = False
                break
            gap = 0.09 if kind == 'head' else (0.16 if kind in ('code', 'table') else 0.11)
            y += h + gap
        if ok:
            return sizes
    return LADDER[-1]


def restyle_chrome(title, footer, badge):
    if title is not None:
        L, T, Wd, H = TITLE_POS
        title.left, title.top, title.width, title.height = \
            Inches(L), Inches(T), Inches(Wd), Inches(H)
        tf = title.text_frame
        tf.word_wrap = True
        txt = text_of(title)
        tf.clear()
        p = tf.paragraphs[0]
        style_para(p, 24, LINE)
        r = p.add_run()
        r.text = txt
        set_font(r, 24, True, TITLE_C, CN)
    if footer is not None:
        L, T, Wd, H = FOOTER_POS
        footer.left, footer.top, footer.width, footer.height = \
            Inches(L), Inches(T), Inches(Wd), Inches(H)
        tf = footer.text_frame
        tf.word_wrap = False
        tf.clear()
        p = tf.paragraphs[0]
        style_para(p, FOOTER_SIZE, LINE)
        r = p.add_run()
        r.text = FOOTER_TEXT
        set_font(r, FOOTER_SIZE, False, '000000', CN)


def rebuild(path, out):
    prs = Presentation(path)
    log = []
    for idx, slide in enumerate(prs.slides, 1):
        title, footer, badge, blocks, notes = extract(slide)
        if title is None:
            continue
        if blocks is None:
            restyle_chrome(title, footer, badge)
            log.append((idx, 'picture page kept', []))
            continue
        if not blocks:
            restyle_chrome(title, footer, badge)
            log.append((idx, 'no content detected', []))
            continue
        # drop old content while chrome still sits at its template position
        # (python-pptx yields fresh proxies, so compare XML elements, not objects)
        for sh in list(slide.shapes):
            if sh.left is None:
                continue
            if keep(sh):
                continue
            sh._element.getparent().remove(sh._element)
        restyle_chrome(title, footer, badge)

        sizes = fit(blocks)
        body, head, code, tbl, emph = sizes
        emph_idx = {i for i, b in enumerate(blocks) if b[0] == 'emph'}
        y, placed, warn = TITLE_DROP, [], []
        for i, (kind, payload) in enumerate(blocks):
            if kind == 'table':
                rows, wds = payload
                w2 = [w * W / sum(wds) for w in wds]
                h = sum(table_rows_h(rows, w2, tbl))
            else:
                h = block_h(kind, payload, sizes)
            gap = 0.09 if kind == 'head' else (0.16 if kind in ('code', 'table') else 0.11)
            if i in emph_idx and BOTTOM - h - y > 0.2:
                y = BOTTOM - h
            if y + h > BOTTOM + 0.03:
                warn.append('%s@%.2f overflow to %.2f' % (kind, y, y + h))
            if kind == 'table':
                add_table(slide, rows, wds, y, tbl)
            else:
                add_text_block(slide, kind, payload, y, h, sizes)
            placed.append((kind, round(y, 2), round(h, 2)))
            y += h + gap
        log.append((idx, sizes, placed, warn))
    prs.save(out)
    return log


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    os.makedirs('.ppt-restyle/out', exist_ok=True)
    for src in sys.argv[1:]:
        dst = os.path.join('.ppt-restyle/out', os.path.basename(src))
        log = rebuild(src, dst)
        print('===== %s' % src)
        for entry in log:
            if len(entry) == 3:
                print('  p%-3d %s' % (entry[0], entry[1]))
                continue
            idx, sizes, placed, warn = entry
            print('  p%-3d body=%.1f head=%.1f code=%.1f tbl=%.1f | %d blocks%s'
                  % (idx, sizes[0], sizes[1], sizes[2], sizes[3], len(placed),
                     ('  WARN: ' + '; '.join(warn)) if warn else ''))
