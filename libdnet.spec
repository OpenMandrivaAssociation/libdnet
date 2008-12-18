%define	major 1
%define libname %mklibname dnet %{major}
%define develname %mklibname dnet -d

Summary:	Portable interface to several low-level networking routines
Name:		libdnet
Version:	1.12
Release:	%mkrel 7
License:	BSD
Group:		System/Libraries
URL:		http://code.google.com/p/libdnet/
Source0:	http://libdnet.googlecode.com/files/%{name}-%{version}.tgz
Patch0:		libdnet-1.11-lib_version_fix.diff
Patch4:		libdnet-1.10-nmap2.diff
BuildRequires:	autoconf2.5
BuildRequires:	python-devel
BuildRequires:	python-pyrex
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0
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

#pushd python
#    pyrexc dnet.pyx
#    python setup.py build
#popd

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

#pushd python
#    python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}
#popd

%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/dnet-config
%endif

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

#%files -n python-dnet
#%defattr(-,root,root)
#%{py_platsitedir}/dnet.so
#%{py_platsitedir}/*.egg-info

%files -n %{libname}
%defattr(-,root,root)
%doc README THANKS TODO
%{_libdir}/*.so.*

%files -n %{libname}-utils
%defattr(-,root,root)
%{_sbindir}/*
%{_mandir}/man8/*

%files -n %{develname}
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
