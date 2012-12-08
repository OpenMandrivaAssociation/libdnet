%define major 1
%define libname %mklibname dnet %{major}
%define develname %mklibname dnet -d

Summary:	Portable interface to several low-level networking routines
Name:		libdnet
Version:	1.12
Release:	13
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
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%package -n	%{libname}-utils
Summary:	A simple test program for the %{libname} library
Group:		System/Libraries
Provides:	%{name}-utils = %{version}-%{release}

%description -n	%{libname}-utils
Provides a simple test program for the %{libname} library.

%package -n	%{develname}
Summary:	Static library and header files for the %{libname} library
Group:		Development/C
Provides:	dnet-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
libdnet provides a simplified, portable interface to several
low-level networking routines, including network address
manipulation, kernel arp(4) cache and route(4) table lookup and
manipulation, network firewalling, network interface lookup and
manipulation, and raw IP packet and Ethernet frame transmission.

%prep
%setup -q
%patch0 -p1
%patch4 -p0

%build
%configure2_5x --disable-static --with-python
%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/dnet-config

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

%files -n python-dnet
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/*.so

%changelog
* Thu Dec 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1.12-12
+ Revision: 738985
- drop the static lib and the libtool *.la file
- various fixes

* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 1.12-11
+ Revision: 660616
- really fix building
- fix multiarch usages

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 1.12-10mdv2011.0
+ Revision: 601041
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.12-9mdv2010.1
+ Revision: 519020
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.12-8mdv2010.0
+ Revision: 425530
- rebuild

* Thu Dec 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.12-7mdv2009.1
+ Revision: 315554
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.12-6mdv2009.0
+ Revision: 264776
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 30 2008 Oden Eriksson <oeriksson@mandriva.com> 1.12-5mdv2009.0
+ Revision: 213445
- fix spec/rpm borkiness (thanks _TPG and Anssi)
- disable the python stuff for now
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.12-4mdv2008.1
+ Revision: 150551
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.12-3mdv2008.0
+ Revision: 83871
- fix deps

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 1.12-2mdv2008.0
+ Revision: 81110
- bump release
- 1.12
- new url
- drop one upstream implemented patch

* Wed Sep 05 2007 David Walluck <walluck@mandriva.org> 1.11-5mdv2008.0
+ Revision: 79643
- Provides: dnet-devel = %%{version}-%%{release}
- version Obsoletes for rpmlint

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 1.11-4mdv2008.0
+ Revision: 74548
- fix deps
- conform to the new devel naming


* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.11-3mdv2007.0
+ Revision: 96086
- Fix File list
- Rebuild for new python

  + Oden Eriksson <oeriksson@mandriva.com>
    - Import libdnet

* Tue Jul 25 2006 Oden Eriksson <oeriksson@mandriva.com> 1.11-1mdv2007.0
- 1.11
- use python rpm macros
- rediffed patches; P0
- drop redundant patches; P1,P2
- drop upstream patches; P5

* Mon Dec 12 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.10-2mdk
- add BuildRequires: pyrex

* Sat Dec 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10-1mdk
- 1.10
- rediffed P0,P2
- added two patches from nmap (P3,P4)
- added P5 from cvs to make the python module compile

* Mon Jan 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.8-4mdk
- fix deps and conditional %%multiarch
- fix requires-on-release

* Tue Sep 21 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.8-3mdk
- use automake 1.4

* Wed May 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.8-2mdk
- make it compile on 9.2 too (libtool mess...)
- added P1 & P2 from PLD

* Mon May 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.8-1mdk
- 1.8
- fix libname (P0)
- added the python stuff
- misc spec file fixes

* Sat Feb 28 2004 Pascal Terjan <pterjan@mandrake.org> 1.7-3mdk
- dont obsolete current version and don't provide packagename = version

