%define	major 1
%define libname %mklibname dnet %{major}
%define develname %mklibname dnet -d

Summary:	Portable interface to several low-level networking routines
Name:		libdnet
Version:	1.12
Release:	12
License:	BSD
Group:		System/Libraries
URL:		http://code.google.com/p/libdnet/
Source0:	http://libdnet.googlecode.com/files/%{name}-%{version}.tgz
Patch0:		libdnet-shrext.patch
Patch4:		libdnet-1.10-nmap2.diff
BuildRequires:	autoconf automake libtool
BuildRequires:	python-devel
BuildRequires:	python-pyrex

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
Obsoletes:	%{name}-utils < %{version}-%{release}
Provides:	%{name}-utils = %{version}-%{release}

%description -n	%{libname}-utils
Provides a simple test program for the %{libname} library.

%package -n	%{develname}
Summary:	Static library and header files for the %{libname} library
Group:		Development/C
License: 	BSD
Provides:       dnet-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:	%{mklibname dnet 1 -d} = %{version}-%{release}
Obsoletes:	%{mklibname dnet 1 -d} < %{version}-%{release}
Requires:	%{libname} >= %{version}-%{release}

%description -n	%{develname}
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1
%patch4 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/dnet-config

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc README THANKS TODO
%{_libdir}/*.so.%{major}*

%files -n %{libname}-utils
%{_sbindir}/*
%{_mandir}/man8/*

%files -n %{develname}
%{multiarch_bindir}/dnet-config
%{_bindir}/dnet-config
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*
