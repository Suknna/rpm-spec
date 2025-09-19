# 介绍
nginx构建脚本以及成功构建的软件包，如果直接使用请确保目标机器环境为uos server 20。
# 模块包含
```bash
./configure \
    --prefix=%{_prefix} \
    --sbin-path=%{_sbindir}/nginx \
    --conf-path=%{_sysconfdir}/nginx/nginx.conf \
    --error-log-path=%{_localstatedir}/log/nginx/error.log \
    --http-log-path=%{_localstatedir}/log/nginx/access.log \
    --pid-path=/run/nginx.pid \
    --lock-path=/run/lock/subsys/nginx \
    --user=nginx \
    --group=nginx \
    --with-compat \
    --with-file-aio \
    --with-http_addition_module \
    --with-http_auth_request_module \
    --with-http_dav_module \
    --with-http_degradation_module \
    --with-http_flv_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_mp4_module \
    --with-http_random_index_module \
    --with-http_realip_module \
    --with-http_secure_link_module \
    --with-http_slice_module \
    --with-http_ssl_module \
    --with-http_stub_status_module \
    --with-http_sub_module \
    --with-http_v2_module \
    --with-http_v3_module \
    --with-pcre \
    --with-pcre-jit \
    --with-threads \
    --with-cc-opt="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fstack-protector-strong" \
    --with-ld-opt="-Wl,-z,relro -Wl,-z,now"
```
### HTTP 模块

- __http_addition_module__: 在响应前后添加文本内容
- __http_auth_request_module__: 基于子请求结果进行客户端认证
- __http_dav_module__: 支持 WebDAV (分布式创作和版本控制) 功能
- __http_degradation_module__: 在内存不足时允许降级服务
- __http_flv_module__: 支持 Flash Video (FLV) 文件伪流
- __http_gunzip_module__: 对不支持 gzip 的客户端解压响应
- __http_gzip_static_module__: 发送预压缩的 .gz 文件
- __http_mp4_module__: 支持 MP4 文件伪流
- __http_random_index_module__: 目录索引时随机显示文件
- __http_realip_module__: 从代理服务器获取真实客户端IP
- __http_secure_link_module__: 检查请求链接的合法性
- __http_slice_module__: 允许将大文件分割为多个小片段
- __http_ssl_module__: 支持 HTTPS 协议
- __http_stub_status_module__: 提供基本的状态信息
- __http_sub_module__: 响应内容替换
- __http_v2_module__: 支持 HTTP/2 协议
- __http_v3_module__: 支持 HTTP/3 协议

### 其他核心模块

- __compat__: 提供向后兼容性支持
- __file-aio__: 异步文件 I/O 支持
- __pcre__: Perl 兼容正则表达式库
- __pcre-jit__: PCRE 的即时编译支持
- __threads__: 线程支持

