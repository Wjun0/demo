
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Spacer, Table, SimpleDocTemplate



pdfmetrics.registerFont(TTFont('msyh', 'msyh.ttc'))
pdfmetrics.registerFont(TTFont('msyhbd', 'msyhbd.ttc'))

basic_style = [('FONTNAME', (0, 0), (-1, -1), 'msyh'),  # 字体
               ('FONTSIZE', (0, 0), (-1, 0), 10),  # 第一行的字体大小
               ('FONTSIZE', (0, 1), (-1, -1), 7),  # 第二行到最后一行的字体大小
               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 所有表格左右中间对齐
               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
               ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(0x8DB4E2)),  # 设置第一行背景颜色
               # ('TEXTCOLOR', (0, -1), (0, -1), colors.green),  # 设置表格内文字颜色
               ('GRID', (0, 0), (-1, -1), 0.1, colors.black),  # 设置表格框线为灰色，线宽为0.1
               ]


def append_data_list(story, content_style, table_style, data_list, label, title, note, col_widths):
    if data_list:
        story.append(Paragraph(f"&nbsp&nbsp&nbsp&nbsp {title}", content_style))
        story.append(Spacer(1, 5 * mm))
        data_list = label + data_list
        data_list = [[Paragraph(cell, table_style) for cell in row] for row in data_list]
        sr_table = Table(data=data_list, colWidths=col_widths, style=basic_style, repeatRows=1)
        story.append(sr_table)
    else:
        story.append(Paragraph(f"&nbsp&nbsp&nbsp&nbsp {title}：{note}", content_style))


def gen_pdf_template(html_data):
    str = """
    <h2><strong>1.1.</strong>2370可水平越权删除我的购物车漏洞 </h2>
    """
    story = []
    title_style = ParagraphStyle(name="Title", fontName="msyhbd",fontSize=11, alignment=TA_CENTER)
    body_style = ParagraphStyle(name="body", fontName="msyh",fontSize=8, alignment=TA_CENTER)
    story.append(Paragraph("安全检测报告", title_style))
    story.append(Paragraph(str, body_style))

    doc = SimpleDocTemplate("test.pdf")
    doc.build(story)
