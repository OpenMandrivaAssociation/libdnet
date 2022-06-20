%define major	1
%define libname	%mklibname dnet %{major}
%define devname	%mklibname dnet -d

%define _disable_lto 1

Summary:	Portable interface to several low-level networking routines
Name:		libdnet
Version:	1.16.1
Release:	1
License:	BSD
Group:		System/Libraries
Url:		https://github.com/dugsong/libdnet
Source0:	http://libdnet.googlecode.com/files/%{name}-%{name}-%{version}.tar.gz
Patch0:		fix-python-build.patch

BuildRequires:	libtool
BuildRequires:	python-pyrex
BuildRequires:	python-cython
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(check)

%description
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%package -n dnet
Summary:	A simple test program for the %{libname} library
Group:		System/Libraries
Provides:	%{name}-utils = %{version}-%{release}
Obsoletes:	%{_lib}dnet1-utils < 1.12-14

%description -n dnet
Provides a simple test program for the %{libname} library.

%package -n %{libname}
Summary:	Portable interface to several low-level networking routines
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%package -n %{devname}
Summary:	Development library and header files for the %{libname} library
Group:		Development/C
Provides:	dnet-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%package -n python-dnet
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
%autosetup -n %{name}-%{name}-%{version} -p1

%build
export PYTHON=%{__python3}

%configure \
	--disable-static \
	--with-python="%{__python3}" \

# Hack to disable --no-udefined to allow build of python lib

sed -i s/"no-undefined"/"no-undefined -Wl,--warn-unresolved-symbols"/ python/Makefile

%make_build

%install
%make_install

%files -n dnet
%doc README.md THANKS TODO
%{_sbindir}/*
%doc %{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/libdnet.so.%{major}*

%files -n %{devname}
%{_bindir}/dnet-config
%{_includedir}/*
%{_libdir}/*.so
%doc %{_mandir}/man3/*

%files -n python-dnet
%{py3_platsitedir}/*.egg-info
%{py3_platsitedir}/*.so
