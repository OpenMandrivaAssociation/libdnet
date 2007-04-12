%define	major 1
%define libname	%mklibname dnet %{major}

Summary:	Portable interface to several low-level networking routines
Name:		libdnet
Version:	1.11
Release:	%mkrel 3
License:	BSD
Group:		System/Libraries
URL:		http://libdnet.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libdnet/%{name}-%{version}.tar.bz2
Patch0:		libdnet-1.11-lib_version_fix.diff
Patch3:		libdnet-1.10-nmap1.diff
Patch4:		libdnet-1.10-nmap2.diff
BuildRequires:	autoconf2.5
BuildRequires:	python-devel
BuildRequires:	pyrex
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%package -n	python-dnet
Summary:	Python bindings for dnet
Group:		Development/Python
Requires:	python >= %{py_ver}

%description -n	python-dnet
This module provides a simplified interface to several low-level
networking routines, including network address manipulation, kernel
arp(4) cache and route(4) table lookup and manipulation, network
firewalling, network interface lookup and manipulation, and raw IP
packet and Ethernet frame transmission.

%package -n	%{libname}
Summary:	Portable interface to several low-level networking routines
Group:          System/Libraries
License:	BSD
Obsoletes:	%{name}
Provides:	%{name}

%description -n	%{libname}
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%package -n	%{libname}-utils
Summary:	A simple test program for the %{libname} library
Group:          System/Libraries
License:	BSD
Obsoletes:	%{name}-utils
Provides:	%{name}-utils

%description -n	%{libname}-utils
Provides a simple test program for the %{libname} library.

%package -n	%{libname}-devel
Summary:	Static library and header files for the %{libname} library
Group:		Development/C
License: 	BSD
Obsoletes:	%{name}-devel
Provides:	%{name}-devel
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%patch3 -p0
%patch4 -p0

%build
export WANT_AUTOCONF_2_5=1
libtoolize --copy --force
aclocal -I config
autoheader
autoconf
automake --foreign

%configure2_5x

%make

pushd python
    pyrexc dnet.pyx
    python setup.py build
popd

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

pushd python
    python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}
popd

%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/dnet-config
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n python-dnet
%defattr(-,root,root)
%{py_platsitedir}/dnet.so
%{py_platsitedir}/*.egg-info

%files -n %{libname}
%defattr(-,root,root)
%doc README THANKS TODO
%{_libdir}/*.so.*

%files -n %{libname}-utils
%defattr(-,root,root)
%{_sbindir}/*
%{_mandir}/man8/*

%files -n %{libname}-devel
%defattr(-,root,root)
%if %mdkversion >= 1020
%multiarch %{multiarch_bindir}/dnet-config
%endif
%{_bindir}/dnet-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_mandir}/man3/*


