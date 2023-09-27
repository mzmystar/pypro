"""
# -*- coding: UTF-8 -*-
from flup.server.fcgi import WSGIServer
from yourapplication import app

if __name__ == '__main__':
    WSGIServer(app).run()
    # nginx和旧版本的lighttpd需要显示传递套接字以与WSGI服务器通信
    WSGIServer(application,bindAddress = '/path/to/fcgi.sock').run()

    # 配置Lighttpd
    fastcgi.server = ("/yourapplication.fcgi"=> ((
                      "socket" => "/tmp/yourapplication-fcgi.sock",
                      "bin-path" => "/var/www/yourapplication/yourapplication.fcgi",
                      "check-local" => "disable",
                      "max-procs" => 1
                      )))
    alias.url = (
        "/static/" => "/path/to/your/static"
    )
    url.rewrite-once = (
        "^(/static($|/.*))$" => "$1",
        "^(/.*)$" => "/yourapplication.fcgi$1"
    )

"""
