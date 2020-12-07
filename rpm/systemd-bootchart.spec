Name:           systemd-bootchart
Version:        233
Release:        1
Summary:        Boot performance graphing tool
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/systemd/systemd-bootchart
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  systemd
BuildRequires:  pkgconfig(libsystemd) >= 221
%{?systemd_requires}

%description
This package provides a binary which can be started during boot early boot
to capture informations about processes and services launched during bootup.
Resource utilization and process information are collected during the boot
process and are later rendered in an SVG chart. The timings for each services
are displayed separately.

%package config
Summary:    Default configuration for systemd-bootchart
Requires:   %{name} = %{version}-%{release}

%description config
This package provides default configuration for systemd-bootchart

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%reconfigure --disable-silent-rules --disable-man
%make_build

%install
%make_install

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE.GPL2
%license LICENSE.LGPL2.1
%doc README
%{_unitdir}/systemd-bootchart.service
%{_unitdir}/../%{name}

%files config
%config %{_sysconfdir}/systemd/bootchart.conf
