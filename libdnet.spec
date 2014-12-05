%define major	1
%define libname	%mklibname dnet %{major}
%define devname	%mklibname dnet -d

Summary:	Portable interface to several low-level networking routines
Name:		libdnet
Version:	1.12
Release:	20
License:	BSD
Group:		System/Libraries
Url:		http://code.google.com/p/libdnet/
Source0:	http://libdnet.googlecode.com/files/%{name}-%{version}.tgz
Patch0:		libdnet-shrext.patch
Patch4:		libdnet-1.10-nmap2.diff
BuildRequires:	libtool
BuildRequires:	python-pyrex
BuildRequires:	pkgconfig(python2)

%description
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%package -n	dnet
Summary:	A simple test program for the %{libname} library
Group:		System/Libraries
Provides:	%{name}-utils = %{version}-%{release}
Obsoletes:	%{_lib}dnet1-utils < 1.12-14

%description -n	dnet
Provides a simple test program for the %{libname} library.

%package -n	%{libname}
Summary:	Portable interface to several low-level networking routines
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%package -n	%{devname}
Summary:	Development library and header files for the %{libname} library
Group:		Development/C
Provides:	dnet-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package contains the development files for %{name}.

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

%prep
%setup -q
%apply_patches

%build
export PYTHON=%{__python2}

%configure \
	--disable-static \
	--with-python
%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/dnet-config

%files -n dnet
%doc README THANKS TODO
%{_sbindir}/*
%{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/libdnet.so.%{major}*

%files -n %{devname}
%{multiarch_bindir}/dnet-config
%{_bindir}/dnet-config
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

%files -n python-dnet
%{py2_platsitedir}/*.egg-info
%{py2_platsitedir}/*.so

