Summary:	Simple DirectMedia Layer - ttf handling
Summary(pl):	Biblioteka obs³ugi fontów TTF
Name:		SDL_ttf
Version:	1.2.2
Release:	4
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.libsdl.org/projects/SDL_ttf/src/%{name}-%{version}.tar.gz
URL:		http://www.libsdl.org/projects/SDL_ttf/
BuildRequires:	XFree86-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype1-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is a sample library which allows you to use TrueType fonts in
your SDL applications. It comes with an example program "showfont"
which displays an example string for a given TrueType font file.

%description -l pl
Przyk³adowa biblioteka do obs³ugi fontów TrueType w aplikacjach SDL.

%package devel
Summary:	Header files and more to develop SDL_ttf applications
Summary(pl):	Pliki na³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_ttf
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_ttf applications.

%description -l pl devel
Pliki na³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_ttf.

%package static
Summary:	Static SDL_ttf libraries
Summary(pl):	Biblioteki statyczne SDL_ttf
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_ttf libraries.

%description -l pl static
Biblioteki statyczne SDL_ttf.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/showfont $RPM_BUILD_ROOT%{_bindir}/sdlfont

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
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
