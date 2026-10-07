Name:           oowget
Version:        0.1.0
Release:        1%{?dist}
Summary:        Resumable file downloader with hash verification and bandwidth limiting.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oowget
Source0:        oowget-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oowget is a sovereign, capability-bounded STREAM DOWNLOAD written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oowget
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oowget-uninstall

%files
/usr/bin/oowget
/usr/bin/oowget-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
