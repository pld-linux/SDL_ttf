Summary:	Simple DirectMedia Layer - ttf handling
Summary(pl):	Biblioteka obs³ugi fontów TTF
Name:		SDL_ttf
Version:	2.0.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_ttf/release/%{name}-%{version}.tar.gz
URL:		http://www.libsdl.org/projects/SDL_ttf/
BuildRequires:	SDL-devel >= 1.2.3
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is a sample library which allows you to use TrueType fonts in
your SDL applications. It comes with an example program "sdlfont"
which displays an example string for a given TrueType font file.

%description -l pl
Przyk³adowa biblioteka do obs³ugi fontów TrueType w aplikacjach SDL.
Pakiet zawiera przyk³adowy program "sdlfont", wy¶wietlaj±cy
przyk³adowy ci±g znaków zadanym fontem TrueType.

%package devel
Summary:	Header files and more to develop SDL_ttf applications
Summary(pl):	Pliki na³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_ttf
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_ttf applications.

%description devel -l pl
Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_ttf.

%package static
Summary:	Static SDL_ttf libraries
Summary(pl):	Biblioteki statyczne SDL_ttf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static SDL_ttf libraries.

%description static -l pl
Biblioteki statyczne SDL_ttf.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
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
%doc {README,CHANGES}.gz
%{_includedir}/SDL/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
