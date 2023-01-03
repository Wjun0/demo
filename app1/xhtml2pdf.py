
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template

from app1.reportlib_test import gen_pdf_template


def font_patch():
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics
    from xhtml2pdf.default import DEFAULT_FONT
    pdfmetrics.registerFont(TTFont('yh', '{}/msyh.ttf'.format(
        settings.STATICFILES_DIRS[0])))
    DEFAULT_FONT['helvetica'] = 'yh'

def render_pdf_view(request):
    template_path = 'render_pdf.html'

    str = """
    <h2><strong>1.1.       </strong>2370可水平越权删除我的购物车漏洞</h2><h3><a name="_Toc95751516"></ a><strong>1.1.1.    </strong>漏洞描述</h3>↵<table>↵<tbody>↵<tr>↵<td width="113">↵<p>漏洞描述</p >↵</td>↵<td width="440">↵<p>可水平越权删除我的购物车</p >↵</td>↵</tr>↵<tr>↵<td width="113">↵<p>可利用场景</p >↵</td>↵<td width="440">↵<p> </p >↵</td>↵</tr>↵<tr>↵<td width="113">↵<p>风险等级</p >↵</td><td width="440"><p>低</p ></td></tr></tbody></table><p> </p ><h3><a name="_Toc95751517"></ a><strong>1.1.2.    </strong>漏洞验证和POC</h3><p>接口：</p ><p>< a href=" ">https://rmb-stg.pingan.com.cn/member/stp/guest/iep-website/wechat/callFunc</ a></p >↵<p>过程描述：</p ><p>       A用户登录小程序，进入我的购物车，选择某一购物车列表，进行删除，抓包。替换token为B用户，可删除成功。重新登录A，进入购物车，发现购物车已删除</p ><p>< img src="http://sop.uat.qa.pab.com.cn/vrm/files/editor_img/Fe33d3560b39a4ca3b3cd9f87ce16c5ca.png" /></p ><h3><a name="_Toc95751518"></ a><strong>1.1.3.    </strong>修复建议</h3><p>鉴权、后端判断资源归属</p >
    """.replace("↵",'')
    context = {'myvar': str}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    font_patch()
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    gen_pdf_template("xx")
    return response