Summary:	A program to read and control device brightness
Name:		brightnessctl
Version:	0.5.1
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/Hummer12007/brightnessctl/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f65719e7e9070f212dd4e1162d5d6412
URL:		https://github.com/Hummer12007/brightnessctl
BuildRequires:	pkgconfig
BuildRequires:	systemd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
his program allows you read and control device brightness on Linux.
Devices, by default, include backlight and LEDs (searched for in
corresponding classes). If omitted, the first found device is
selected.

It can also preserve current brightness before applying the operation
(allowing for usecases like disabling backlight on lid close).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS='%{rpmcflags} %{rpmcppflags} -std=c99 -DVERSION=\"$(VERSION)\" -D_POSIX_C_SOURCE=200809L' \
	LDFLAGS="%{rpmldflags}" \
	ENABLE_SYSTEMD=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR="$RPM_BUILD_ROOT%{_bindir}" \
	MANDIR="$RPM_BUILD_ROOT%{_mandir}" \
	ENABLE_SYSTEMD=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/brightnessctl
%{_mandir}/man1/brightnessctl.1*
