

import os
import socket
env = os.environ
print(env)
os.environ['ENV'] = "uat"


if __name__ == '__main__':
    s = """
    <h2><strong>1.1.       </strong>2370可水平越权删除我的购物车漏洞</h2>↵<h3><a name="_Toc95751516"></ a><strong>1.1.1.    </strong>漏洞描述</h3>↵<table>↵<tbody>↵<tr>↵<td width="113">↵<p>漏洞描述</p >↵</td>↵<td width="440">↵<p>可水平越权删除我的购物车</p >↵</td>↵</tr>↵<tr>↵<td width="113">↵<p>可利用场景</p >↵</td>↵<td width="440">↵<p> </p >↵</td>↵</tr>↵<tr>↵<td width="113">↵<p>风险等级</p >↵</td>↵<td width="440">↵<p>低</p >↵</td>↵</tr>↵</tbody>↵</table>↵<p> </p >↵<h3><a name="_Toc95751517"></ a><strong>1.1.2.    </strong>漏洞验证和POC</h3>↵<p>接口：</p >↵<p>< a href=" ">https://rmb-stg.pingan.com.cn/member/stp/guest/iep-website/wechat/callFunc</ a></p >↵<p>过程描述：</p >↵<p>       A用户登录小程序，进入我的购物车，选择某一购物车列表，进行删除，抓包。替换token为B用户，可删除成功。重新登录A，进入购物车，发现购物车已删除</p >↵<p>< img src="http://sop.uat.qa.pab.com.cn/vrm/files/editor_img/Fe33d3560b39a4ca3b3cd9f87ce16c5ca.png" /></p >↵<h3><a name="_Toc95751518"></ a><strong>1.1.3.    </strong>修复建议</h3>↵<p>鉴权、后端判断资源归属</p >
    """
    print(s.replace("↵",""))
    pass
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    print(host)
