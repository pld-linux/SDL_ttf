%define name SDL_ttf
%define version 1.0.1

Summary: Simple DirectMedia Layer - ttf handling
Name: %{name}
Version: %{version}
Release: 2mdk
Source0: %{name}-%{version}.tar.bz2
Copyright: LGPL
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.devolution.com/~slouken/SDL/projects/SDL_ttf/
Prefix: %{_prefix}
Requires: SDL >= 1.0

%description
This is a sample library which allows you to use TrueType fonts in your SDL
applications. It comes with an example program "showfont" which displays an
example string for a given TrueType font file.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%package devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C
Requires: %{name}
Requires: SDL-devel

%description devel
This is a sample library which allows you to use TrueType fonts in your SDL
applications. It comes with an example program "showfont" which displays an
example string for a given TrueType font file.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup
#%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING
%{prefix}/bin/showfont
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README COPYING CHANGES
%{prefix}/lib/*a
%{prefix}/include/SDL/
%{prefix}/lib/lib*.so

%changelog
* Tue Apr 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-2mdk
- added url
- fixed group
- some minor package build fixes
- built against stable SDL version, previous was using 1.1.x devel

* Fri Feb 11 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used specfile provided by Hakan Tandogan <hakan@iconsult.com>

* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file
