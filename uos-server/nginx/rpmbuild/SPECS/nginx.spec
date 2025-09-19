Name:              nginx
Epoch:             2
Version:           1.28.0
Release:           1%{?dist}

Summary:           A high performance web server and reverse proxy server
License:           BSD-2-Clause
URL:               https://nginx.org

Source0:           https://nginx.org/download/nginx-%{version}.tar.gz
Source1:           https://nginx.org/download/nginx-%{version}.tar.gz.asc
Source10:          nginx.service
Source11:          nginx.logrotate
Source12:          nginx.sysusers

BuildRequires:     make
BuildRequires:     gcc
BuildRequires:     openssl-devel
BuildRequires:     pcre2-devel
BuildRequires:     zlib-devel
BuildRequires:     systemd

%description
Nginx is a web server and a reverse proxy server for HTTP, SMTP, POP3 and
IMAP protocols, with a strong focus on high concurrency, performance and low
memory usage.


%prep
%setup -q

%build
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

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

install -p -D -m 0644 %{SOURCE10} \
    %{buildroot}%{_unitdir}/nginx.service

install -p -D -m 0644 %{SOURCE11} \
    %{buildroot}%{_sysconfdir}/logrotate.d/nginx

install -p -D -m 0644 %{SOURCE12} \
    %{buildroot}%{_sysusersdir}/nginx.conf

install -p -d -m 0755 %{buildroot}%{_sysconfdir}/nginx
install -p -d -m 0755 %{buildroot}%{_localstatedir}/log/nginx

%post
%systemd_post nginx.service
%sysusers_create_compat nginx.conf

%preun
%systemd_preun nginx.service

%postun
%systemd_postun nginx.service

%files
%{_sysusersdir}/nginx.conf
%license LICENSE
%{_sbindir}/nginx
%config(noreplace) %{_sysconfdir}/nginx/*
%config(noreplace) %{_sysconfdir}/logrotate.d/nginx
%{_unitdir}/nginx.service
%dir %{_sysconfdir}/nginx
%dir %{_localstatedir}/log/nginx
/usr/html/*

%changelog
* Thu Sep 19 2025 Suknna suknna@foxmail.com - 2:1.28.0-1
- Minimal nginx build with core modules only
- Removed all patches and unnecessary dependencies
- Kept only systemd service and logrotate configuration

