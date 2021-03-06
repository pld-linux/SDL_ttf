Summary:	Simple DirectMedia Layer - ttf handling
Summary(pl.UTF-8):	Biblioteka obsługi fontów TTF dla SDL
Summary(pt_BR.UTF-8):	Simple DirectMedia Layer - Biblioteca de fontes TrueType
Name:		SDL_ttf
Version:	2.0.11
Release:	2
License:	Zlib-like
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_ttf/release/%{name}-%{version}.tar.gz
# Source0-md5:	61e29bd9da8d245bc2471d1b2ce591aa
URL:		http://www.libsdl.org/projects/SDL_ttf/release-1.2.html
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.5-2
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	libtool >= 2:2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a sample library which allows you to use TrueType fonts in
your SDL applications. It comes with an example program "sdlfont"
which displays an example string for a given TrueType font file.

%description -l pl.UTF-8
Przykładowa biblioteka do obsługi fontów TrueType w aplikacjach SDL.
Pakiet zawiera przykładowy program "sdlfont", wyświetlający
przykładowy ciąg znaków zadanym fontem TrueType.

%description -l pt_BR.UTF-8
Esta é uma biblioteca que permite a utilização de fontes TrueType em
suas aplicações SDL. Ela vem com o programa exemplo "sdlfont" que
mostra uma string exemplo para uma fonte TrueType fornecida.

%package devel
Summary:	Header files and more to develop SDL_ttf applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL_ttf
Summary(pt_BR.UTF-8):	Cabeçalhos para desenvolver programas utilizando a SDL_ttf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.5-2
Requires:	freetype-devel >= 2.1.4

%description devel
Header files and more to develop SDL_ttf applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania aplikacji używających SDL_ttf.

%description devel -l pt_BR.UTF-8
Este pacote contém os cabeçalhos que programadores vão precisar para
desenvolver aplicações utilizando a SDL_ttf.

%package static
Summary:	Static SDL_ttf library
Summary(pl.UTF-8):	Biblioteka statyczna SDL_ttf
Summary(pt_BR.UTF-8):	Biblioteca estática para desenvolvimento utilizando a SDL_ttf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL_ttf library.

%description static -l pl.UTF-8
Biblioteka statyczna SDL_ttf.

%description static -l pt_BR.UTF-8
Este pacote contém a biblioteca estática que programadores vão
precisar para desenvolver aplicações linkados estaticamente com a
SDL_ttf.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} \
	libSDL_ttf_la_LIBADD="-lm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install .libs/showfont $RPM_BUILD_ROOT%{_bindir}/sdlfont

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) %{_bindir}/sdlfont
%attr(755,root,root) %{_libdir}/libSDL_ttf-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL_ttf-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_ttf.so
%{_libdir}/libSDL_ttf.la
%{_includedir}/SDL/SDL_ttf.h
%{_pkgconfigdir}/SDL_ttf.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL_ttf.a
