Summary:	Simple DirectMedia Layer - ttf handling
Name:		SDL_ttf
Version:	1.0.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.devolution.com/~slouken/SDL/projects/SDL_ttf/src/%{name}-%{version}.tar.gz
URL:		http://www.devolution.com/~slouken/SDL/projects/SDL_ttf/
BuildRequires:	freetype-devel
BuildRequires:	SDL-devel >= 1.0.1
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is a sample library which allows you to use TrueType fonts in
your SDL applications. It comes with an example program "showfont"
which displays an example string for a given TrueType font file.

%package devel
Summary:	Header files and more to develop SDL_ttf applications
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_ttf applications.

%package static
Summary:	Statis SDL_ttf libraries
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_ttf libraries.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS 
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/showfont
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_includedir}/SDL/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
